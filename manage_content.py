# -*- coding: utf-8 -*-
"""
Content Management & Extension CLI for Modern Cryptography Learning Platform
Author: Antigravity Assistant
Purpose: Enables easy extension of course modules, quizzes, and glossary items
without touching front-end JavaScript code.
"""

import sys
import os
import glob
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_JS_PATH = os.path.join("js", "data.js")


def load_js_data():
    if not os.path.exists(DATA_JS_PATH):
        print(f"[Error] {DATA_JS_PATH} not found.")
        sys.exit(1)

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract MODULES_DATA, QUIZ_DATA, GLOSSARY_DATA
    m_modules = re.search(r"const\s+MODULES_DATA\s*=\s*(\[.*?\]);\s*const\s+QUIZ_DATA", content, re.DOTALL)
    m_quiz = re.search(r"const\s+QUIZ_DATA\s*=\s*(\[.*?\]);\s*const\s+GLOSSARY_DATA", content, re.DOTALL)
    m_glossary = re.search(r"const\s+GLOSSARY_DATA\s*=\s*(\[.*?\]);\s*$", content, re.DOTALL)

    if not m_modules or not m_quiz or not m_glossary:
        print("[Error] Failed to parse js/data.js. Format signature mismatch.")
        sys.exit(1)

    modules = json.loads(m_modules.group(1))
    quizzes = json.loads(m_quiz.group(1))
    glossary = json.loads(m_glossary.group(1))

    return modules, quizzes, glossary


def save_js_data(modules, quizzes, glossary):
    content = f"""// Cryptography Review & Learning Platform Data
// Auto-generated data source for modern & post-quantum cryptography review

const MODULES_DATA = {json.dumps(modules, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(quizzes, ensure_ascii=False, indent=2)};

const GLOSSARY_DATA = {json.dumps(glossary, ensure_ascii=False, indent=2)};
"""
    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[Success] Updated {DATA_JS_PATH} (Modules: {len(modules)}, Quizzes: {len(quizzes)}, Glossary: {len(glossary)})")


def cmd_validate():
    print("--- 執行資料完整性驗證 ---")
    modules, quizzes, glossary = load_js_data()

    errors = 0
    warnings = 0

    # 1. Validate Modules
    module_ids = set()
    for i, m in enumerate(modules):
        for field in ["id", "number", "title", "subtitle", "sections"]:
            if field not in m:
                print(f"[Error] Module[{i}] 缺少必要欄位: {field}")
                errors += 1
        if m.get("id") in module_ids:
            print(f"[Error] 重複的 Module ID: {m.get('id')}")
            errors += 1
        module_ids.add(m.get("id"))

    # 2. Validate Quizzes
    quiz_ids = set()
    for i, q in enumerate(quizzes):
        for field in ["id", "moduleId", "category", "question", "options", "answer", "explanation"]:
            if field not in q:
                print(f"[Error] Quiz[{i}] 缺少必要欄位: {field}")
                errors += 1
        if q.get("moduleId") not in module_ids:
            print(f"[Warning] Quiz[{i}] 的 moduleId '{q.get('moduleId')}' 未在任何已註冊模組中找到")
            warnings += 1
        ans = q.get("answer")
        opts = q.get("options", [])
        if not isinstance(ans, int) or ans < 0 or ans >= len(opts):
            print(f"[Error] Quiz[{i}] answer 索引 ({ans}) 超出選項範圍 [0, {len(opts)-1}]")
            errors += 1
        if q.get("id") in quiz_ids:
            print(f"[Error] 重複的 Quiz ID: {q.get('id')}")
            errors += 1
        quiz_ids.add(q.get("id"))

    # 3. Validate Glossary
    terms = set()
    for i, g in enumerate(glossary):
        for field in ["term", "chinese", "category", "definition"]:
            if field not in g:
                print(f"[Error] Glossary[{i}] 缺少必要欄位: {field}")
                errors += 1
        if g.get("term") in terms:
            print(f"[Warning] 重複的術語: {g.get('term')}")
            warnings += 1
        terms.add(g.get("term"))

    print(f"驗證完成：錯誤 {errors} 項，警告 {warnings} 項。")
    if errors == 0:
        print("[Pass] 全域資料結構完全合規，運作正常！")


def cmd_scan_pdfs():
    print("--- 掃描目錄下的 PDF 檔案 ---")
    pdf_files = sorted(glob.glob("*.pdf"))
    if not pdf_files:
        print("目錄中無任何 PDF 檔案。")
        return

    modules, _, _ = load_js_data()
    known_titles = [m.get("title", "").lower() for m in modules]
    known_sources = [m.get("source", "").lower() for m in modules]

    new_candidates = []
    try:
        import fitz
    except ImportError:
        print("[Notice] 未安裝 PyMuPDF (fitz)，僅檢測檔案名稱。")
        fitz = None

    for pdf in pdf_files:
        # Check if already mentioned
        matched = False
        pdf_name_lower = pdf.lower()
        for src in known_sources:
            if pdf_name_lower in src or src in pdf_name_lower:
                matched = True
                break

        page_count = "?"
        toc = []
        if fitz:
            try:
                doc = fitz.open(pdf)
                page_count = len(doc)
                toc = doc.get_toc()
            except Exception:
                pass

        status = "已納入教材" if matched else "待擴充之新教材"
        print(f"檔案: {pdf} ({page_count} 頁) -> {status}")
        if not matched:
            new_candidates.append({
                "file": pdf,
                "pages": page_count,
                "toc": toc[:10]
            })

    if new_candidates:
        draft_file = "new_module_draft.json"
        sample_draft = []
        for i, cand in enumerate(new_candidates):
            mod_num = f"{len(modules) + i:02d}"
            sections = []
            if cand.get("toc"):
                for t in cand["toc"]:
                    sections.append({
                        "title": t[1],
                        "content": [
                            f"**{t[1]}**：請填寫本節核心定理與定義。",
                            "- 重點條列一",
                            "- 重點條列二"
                        ]
                    })
            else:
                sections.append({
                    "title": "章節概述與核心理論",
                    "content": ["請填寫此處重點說明。"]
                })

            sample_draft.append({
                "id": f"mod-{len(modules) + i}",
                "number": mod_num,
                "title": f"新章節：{os.path.splitext(cand['file'])[0]}",
                "subtitle": "Chapter Subtitle",
                "source": cand["file"],
                "summary": "請填寫本章教學目標與摘要。",
                "sections": sections
            })

        with open(draft_file, "w", encoding="utf-8") as f:
            json.dump(sample_draft, f, ensure_ascii=False, indent=2)
        print(f"\n[Generated] 已自動為新教材生成擴充草稿範本：{draft_file}")
        print(f"填妥內容後，執行 `python manage_content.py add-module {draft_file}` 即可自動匯入！")


def cmd_add_module(json_path):
    if not os.path.exists(json_path):
        print(f"[Error] 找不到指定的 JSON 檔案: {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        new_data = json.load(f)

    if isinstance(new_data, dict):
        new_data = [new_data]

    modules, quizzes, glossary = load_js_data()
    existing_ids = {m["id"] for m in modules}

    added = 0
    for item in new_data:
        if item.get("id") in existing_ids:
            print(f"[Notice] 模組 ID '{item.get('id')}' 已存在，進行覆蓋更新。")
            for idx, old in enumerate(modules):
                if old["id"] == item["id"]:
                    modules[idx] = item
                    added += 1
                    break
        else:
            modules.append(item)
            existing_ids.add(item["id"])
            added += 1

    save_js_data(modules, quizzes, glossary)
    print(f"成功匯入/更新 {added} 個章節模組！")


def cmd_add_quiz(json_path):
    if not os.path.exists(json_path):
        print(f"[Error] 找不到指定的 JSON 檔案: {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        new_quizzes = json.load(f)

    if isinstance(new_quizzes, dict):
        new_quizzes = [new_quizzes]

    modules, quizzes, glossary = load_js_data()
    existing_ids = {q["id"] for q in quizzes}

    added = 0
    for q in new_quizzes:
        if q.get("id") in existing_ids:
            print(f"[Notice] 題目 ID '{q.get('id')}' 已存在，進行覆蓋更新。")
            for idx, old in enumerate(quizzes):
                if old["id"] == q["id"]:
                    quizzes[idx] = q
                    added += 1
                    break
        else:
            quizzes.append(q)
            existing_ids.add(q["id"])
            added += 1

    save_js_data(modules, quizzes, glossary)
    print(f"成功匯入/更新 {added} 道測驗題目！")


def cmd_export_json():
    os.makedirs("data", exist_ok=True)
    modules, quizzes, glossary = load_js_data()
    with open("data/modules.json", "w", encoding="utf-8") as f:
        json.dump(modules, f, ensure_ascii=False, indent=2)
    with open("data/quizzes.json", "w", encoding="utf-8") as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)
    with open("data/glossary.json", "w", encoding="utf-8") as f:
        json.dump(glossary, f, ensure_ascii=False, indent=2)
    print("[Success] 已將全部資料結構導出至 data/ 目錄下的三個 JSON 檔案。")


def print_help():
    print("""
======================================================
密碼學學習平台 內容管理與擴充工具 (Content Manager)
======================================================
指令用法：
  python manage_content.py validate
      驗證目前資料完整性、欄位正確性與 ID 衝突。

  python manage_content.py scan-pdfs
      自動掃描目錄中的 PDF 教材，並為未收錄之教材生成草稿 new_module_draft.json。

  python manage_content.py add-module <file.json>
      將 JSON 格式的章節模組資料自動注入到 js/data.js。

  python manage_content.py add-quiz <file.json>
      將 JSON 格式的題目資料追加到題庫中。

  python manage_content.py export-json
      將全站資料匯出為 data/modules.json, quizzes.json, glossary.json。
======================================================
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    action = sys.argv[1].lower()
    if action == "validate":
        cmd_validate()
    elif action == "scan-pdfs":
        cmd_scan_pdfs()
    elif action == "add-module" and len(sys.argv) >= 3:
        cmd_add_module(sys.argv[2])
    elif action == "add-quiz" and len(sys.argv) >= 3:
        cmd_add_quiz(sys.argv[2])
    elif action == "export-json":
        cmd_export_json()
    else:
        print_help()
