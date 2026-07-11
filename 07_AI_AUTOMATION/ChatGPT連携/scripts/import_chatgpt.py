#!/usr/bin/env python3
"""
ChatGPT の会話エクスポート(conversations.json)を読み込み、
事業領域(01〜09)ごとにMarkdownファイルへ振り分けて保存する。

使い方:
    python3 import_chatgpt.py [conversations.jsonのパス]

  パスを省略した場合は inbox/conversations.json を読む。

分類はキーワードマッチによる簡易推定のため、必ず import_log.md で
振り分け結果を確認し、誤分類があれば手動で移動すること。
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # .../ChatGPT連携
INBOX_DIR = BASE_DIR / "inbox"
IMPORTED_DIR = BASE_DIR / "imported"
MANIFEST_PATH = IMPORTED_DIR / "imported_ids.json"
LOG_PATH = IMPORTED_DIR / "import_log.md"

# 事業領域ごとの判定キーワード(タイトル・本文に含まれる語で簡易マッチング)
CATEGORIES = {
    "01_VIVANI": ["VIVANI", "ヴィヴァーニ", "チョコレート", "チョコ", "ドイツ", "通関", "輸入"],
    "02_HEMP": ["ヘンプ", "麻", "アパレル", "下着", "寝具", "エプロン", "スウェット", "OEM", "生地", "Hemp"],
    "03_FURNITURE": ["家具", "Furniture", "木材", "職人", "工房"],
    "04_HISSAN": ["HISSAN", "陶器", "窯元", "焼き物", "陶芸"],
    "05_FOOD": ["食品", "食材", "食品表示", "原材料", "レシピ", "賞味期限"],
    "07_AI_AUTOMATION": ["AI", "自動化", "Claude", "ChatGPT", "プロンプト", "ワークフロー", "スクリプト", "自動連携"],
    "08_BUSINESS": ["freee", "経理", "契約", "見積", "請求書", "在庫", "顧客", "仕入先", "財務", "経営", "予算"],
    "09_COMPANY_MANUAL": ["マニュアル", "SOP", "社内規程", "ルール", "手順書", "ガイドライン"],
}
FALLBACK_CATEGORY = "06_OTHERS"

ROLE_LABEL = {"user": "User", "assistant": "ChatGPT", "system": "System", "tool": "Tool"}


def load_manifest() -> set:
    if MANIFEST_PATH.exists():
        return set(json.loads(MANIFEST_PATH.read_text(encoding="utf-8")))
    return set()


def save_manifest(ids: set) -> None:
    IMPORTED_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(sorted(ids), ensure_ascii=False, indent=2), encoding="utf-8")


def extract_transcript(conversation: dict) -> str:
    mapping = conversation.get("mapping", {})
    entries = []
    for node in mapping.values():
        message = node.get("message")
        if not message:
            continue
        author = message.get("author", {}).get("role")
        content = message.get("content", {})
        if content.get("content_type") != "text":
            continue
        parts = [p for p in content.get("parts", []) if isinstance(p, str) and p.strip()]
        if not parts or author not in ("user", "assistant"):
            continue
        create_time = message.get("create_time") or 0
        entries.append((create_time, author, "\n".join(parts)))

    entries.sort(key=lambda e: e[0])
    lines = []
    for _, author, text in entries:
        lines.append(f"### {ROLE_LABEL.get(author, author)}\n\n{text}\n")
    return "\n".join(lines)


def classify(title: str, transcript: str) -> str:
    haystack = f"{title}\n{transcript}"
    scores = {}
    for category, keywords in CATEGORIES.items():
        score = sum(haystack.count(kw) for kw in keywords)
        if score:
            scores[category] = score
    if not scores:
        return FALLBACK_CATEGORY
    return max(scores, key=scores.get)


def slugify(title: str) -> str:
    title = title.strip() or "無題の会話"
    title = re.sub(r"[\\/:*?\"<>|]", "_", title)
    title = re.sub(r"\s+", "_", title)
    return title[:60]


def format_date(epoch: float | None) -> str:
    if not epoch:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%d")


def write_markdown(category: str, date_str: str, title: str, transcript: str) -> Path:
    out_dir = IMPORTED_DIR / category
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(title)
    base_name = f"{date_str}_{slug}.md"
    out_path = out_dir / base_name
    counter = 2
    while out_path.exists():
        out_path = out_dir / f"{date_str}_{slug}_{counter}.md"
        counter += 1

    body = f"""# {title or "無題の会話"}

- 取り込み日: {datetime.now().strftime('%Y-%m-%d')}
- 出典: ChatGPT エクスポート ({date_str})
- 対象事業領域: {category}（自動分類・要確認）

## 要点

（未記入。内容を確認して要約を追記してください）

## 本文 / 成果物

{transcript if transcript.strip() else "（本文を抽出できませんでした）"}
"""
    out_path.write_text(body, encoding="utf-8")
    return out_path


def main() -> None:
    src_path = Path(sys.argv[1]) if len(sys.argv) > 1 else INBOX_DIR / "conversations.json"
    if not src_path.exists():
        print(f"エクスポートファイルが見つかりません: {src_path}")
        print(f"ChatGPTの「設定 → データ管理 → データのエクスポート」で取得したconversations.jsonを")
        print(f"{INBOX_DIR} に置くか、パスを引数で指定してください。")
        sys.exit(1)

    conversations = json.loads(src_path.read_text(encoding="utf-8"))
    imported_ids = load_manifest()

    results = []
    for conversation in conversations:
        conv_id = conversation.get("id") or conversation.get("conversation_id")
        if not conv_id or conv_id in imported_ids:
            continue

        title = conversation.get("title") or "無題の会話"
        transcript = extract_transcript(conversation)
        category = classify(title, transcript)
        date_str = format_date(conversation.get("create_time"))
        out_path = write_markdown(category, date_str, title, transcript)

        imported_ids.add(conv_id)
        results.append((title, category, out_path.relative_to(BASE_DIR)))

    save_manifest(imported_ids)

    if not results:
        print("新規に取り込む会話はありませんでした（すべて取り込み済み、または対象ファイルが空です）。")
        return

    IMPORTED_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as log:
        log.write(f"\n## 取り込み実行: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        log.write("| タイトル | 分類先 | ファイル |\n|---|---|---|\n")
        for title, category, path in results:
            log.write(f"| {title} | {category} | `{path}` |\n")

    print(f"{len(results)} 件の会話を取り込みました。振り分け結果は {LOG_PATH} を確認してください。")


if __name__ == "__main__":
    main()
