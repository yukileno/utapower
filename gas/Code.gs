/**
 * うたパワー スプレッドシート連携
 *
 * 【設置手順】
 * 1. 新しい Google スプレッドシートを作る
 * 2. メニュー「拡張機能」→「Apps Script」を開き、このファイルの中身を全部貼り付けて保存
 * 3. 右上「デプロイ」→「新しいデプロイ」→ 種類「ウェブアプリ」
 *      実行ユーザー：自分
 *      アクセスできるユーザー：全員
 *    →「デプロイ」→ 表示された「ウェブアプリのURL」（…/exec で終わるもの）をコピー
 * 4. index.html の GAS_URL に貼り付け
 *
 * コードを書き換えたときは「デプロイを管理」→ 鉛筆マーク → バージョン「新バージョン」で更新すると URL が変わりません。
 */

const RECORD_SHEET = '記録';
const RANK_SHEET = 'ランキング';
const CLASSES = ['1組', '2組', '3組', '4組', '5組'];
const DEFAULT_RANGE = 30;
const HEAD = ['id', '日付', '時刻', 'クラス', '玉', '得点', '最大コンボ', '秒数', '歌っていた割合(%)', 'むずかしさ', '受信日時'];

// 端末から記録を受け取る（1件でも配列でもOK。同じidは二重登録しない）
function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const data = JSON.parse(e.postData.contents);
    if (data && data.action === 'saveSettings') return json_(saveSettings_(data));
    const list = Array.isArray(data) ? data : [data];
    const sh = recordSheet_();
    const last = sh.getLastRow();
    const ids = new Set(last > 1 ? sh.getRange(2, 1, last - 1, 1).getValues().map(r => String(r[0])) : []);
    const now = new Date();
    const rows = list
      .filter(r => r && r.id && !ids.has(String(r.id)))
      .map(r => [String(r.id), String(r.date), String(r.time), String(r.cls),
        Number(r.balls) || 0, Number(r.score) || 0, Number(r.maxCombo) || 0,
        Number(r.duration) || 0, Number(r.singRatio) || 0, String(r.diff || ''), now]);
    if (rows.length) sh.getRange(last + 1, 1, rows.length, HEAD.length).setValues(rows);
    writeRankingSheet_(ranking_());
    return json_({ ok: true, added: rows.length });
  } finally {
    lock.releaseLock();
  }
}

// ?action=records&cls=1組 … そのクラスの記録（新しい順・最大300件）
// それ以外 … ランキング
function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.action === 'records') return json_(records_(String(p.cls || '')));
  if (p.action === 'settings') return json_(settings_());
  return json_(ranking_());
}

// 設定（マイク感度。全クラス共通）はスクリプトプロパティに保存。プレイ中に変えると自動で送られてくる
function settings_() {
  const raw = PropertiesService.getScriptProperties().getProperty('SETTINGS');
  const s = raw ? JSON.parse(raw) : {};
  return { range: Number(s.range) || DEFAULT_RANGE };
}

function saveSettings_(data) {
  const cur = settings_();
  const v = Number((data.settings || {}).range);
  if (!(v >= 12 && v <= 50)) return { ok: false, error: 'range' };
  cur.range = v;
  PropertiesService.getScriptProperties().setProperty('SETTINGS', JSON.stringify(cur));
  return { ok: true, settings: cur };
}

function records_(cls) {
  const tz = Session.getScriptTimeZone();
  const sh = recordSheet_();
  const n = sh.getLastRow() - 1;
  const vals = n > 0 ? sh.getRange(2, 1, n, HEAD.length).getValues() : [];
  const list = vals
    .filter(r => !cls || String(r[3]) === cls)
    .map(r => ({
      id: String(r[0]),
      date: r[1] instanceof Date ? Utilities.formatDate(r[1], tz, 'yyyy-MM-dd') : String(r[1]),
      time: r[2] instanceof Date ? Utilities.formatDate(r[2], tz, 'HH:mm') : String(r[2]),
      cls: String(r[3]), balls: Number(r[4]) || 0, score: Number(r[5]) || 0, maxCombo: Number(r[6]) || 0,
      duration: Number(r[7]) || 0, singRatio: Number(r[8]) || 0, diff: String(r[9])
    }))
    .sort((a, b) => (b.date + b.time + b.id).localeCompare(a.date + a.time + a.id))
    .slice(0, 300);
  return { cls, records: list };
}

// きょう：各クラスのきょうのベスト（玉の数）
// こんしゅう：月曜からきょうまでの「1日ごとのベスト」の合計（毎日歌うほど伸びる）
function ranking_() {
  const tz = Session.getScriptTimeZone();
  const now = new Date();
  const today = Utilities.formatDate(now, tz, 'yyyy-MM-dd');
  const dow = (Number(Utilities.formatDate(now, tz, 'u')) + 6) % 7; // 月=0
  const monday = Utilities.formatDate(new Date(now.getTime() - dow * 86400000), tz, 'yyyy-MM-dd');

  const sh = recordSheet_();
  const n = sh.getLastRow() - 1;
  const vals = n > 0 ? sh.getRange(2, 1, n, HEAD.length).getValues() : [];

  // best[クラス][日付] = その日いちばん良かった回
  const best = {};
  const classes = CLASSES.slice();
  vals.forEach(r => {
    const date = r[1] instanceof Date ? Utilities.formatDate(r[1], tz, 'yyyy-MM-dd') : String(r[1]);
    const cls = String(r[3]);
    const rec = { balls: Number(r[4]) || 0, score: Number(r[5]) || 0 };
    if (classes.indexOf(cls) < 0) classes.push(cls);
    best[cls] = best[cls] || {};
    const b = best[cls][date];
    if (!b || rec.balls > b.balls || (rec.balls === b.balls && rec.score > b.score)) best[cls][date] = rec;
    best[cls][date].plays = ((b && b.plays) || 0) + 1;
  });

  const todayList = classes.map(cls => {
    const b = (best[cls] || {})[today];
    return { cls, balls: b ? b.balls : 0, score: b ? b.score : 0, plays: b ? b.plays : 0 };
  });
  const weekList = classes.map(cls => {
    const days = Object.keys(best[cls] || {}).filter(d => d >= monday && d <= today);
    return {
      cls,
      balls: days.reduce((s, d) => s + best[cls][d].balls, 0),
      score: days.reduce((s, d) => s + best[cls][d].score, 0),
      days: days.length
    };
  });
  const sorter = (a, b) => b.balls - a.balls || b.score - a.score;
  todayList.sort(sorter);
  weekList.sort(sorter);
  return { today: todayList, week: weekList, date: today, weekStart: monday, updated: Utilities.formatDate(now, tz, 'yyyy-MM-dd HH:mm') };
}

// 先生がスプレッドシートで見る用のランキングシート
function writeRankingSheet_(rk) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName(RANK_SHEET) || ss.insertSheet(RANK_SHEET);
  sh.clearContents();
  const rows = [['きょう（' + rk.date + '）', '', '', '', '', 'こんしゅう（' + rk.weekStart + '〜）', '', '', ''],
    ['順位', 'クラス', '玉', '得点', '', '順位', 'クラス', '玉（毎日のベスト合計）', '歌った日数']];
  const len = Math.max(rk.today.length, rk.week.length);
  for (let i = 0; i < len; i++) {
    const a = rk.today[i], b = rk.week[i];
    rows.push([a ? i + 1 : '', a ? a.cls : '', a ? a.balls : '', a ? a.score : '', '',
      b ? i + 1 : '', b ? b.cls : '', b ? b.balls : '', b ? b.days : '']);
  }
  rows.push(['', '', '', '', '', '', '', '', '']);
  rows.push(['更新: ' + rk.updated, '', '', '', '', '', '', '', '']);
  sh.getRange(1, 1, rows.length, 9).setValues(rows);
  sh.getRange('A1:I2').setFontWeight('bold');
}

function recordSheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(RECORD_SHEET);
  if (!sh) {
    sh = ss.insertSheet(RECORD_SHEET);
    sh.getRange('A:C').setNumberFormat('@'); // id・日付・時刻を文字のまま保存
    sh.getRange(1, 1, 1, HEAD.length).setValues([HEAD]).setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
