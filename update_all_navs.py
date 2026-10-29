# -*- coding: utf-8 -*-
"""
Sync navigation across all 7 pages using the refined UI/UX navigation architecture.
"""
import re

GITHUB_REPO_URL = "https://github.com/johnjohn1207/crypto-exam-review"

PAGES = [
    {"file": "index.html", "id": "index"},
    {"file": "notes.html", "id": "notes"},
    {"file": "exam.html", "id": "exam"},
    {"file": "homework_practice.html", "id": "homework_practice"},
    {"file": "hw1_summary.html", "id": "hw1_summary"},
    {"file": "p1_summary.html", "id": "p1_summary"},
    {"file": "proof_sheet.html", "id": "proof_sheet"}
]

def make_nav(current_id):
    def get_btn(page_id, href, title, label, is_amber=False, is_cyan=False, is_emerald=False):
        is_active = (current_id == page_id)
        if is_active:
            if is_amber:
                border_bg = "border-amber-500/70 bg-amber-950/90 text-amber-200 font-semibold shadow-sm"
                dot = '<span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse shrink-0"></span>'
            elif is_cyan:
                border_bg = "border-cyan-500/70 bg-cyan-950/90 text-cyan-200 font-semibold shadow-sm"
                dot = '<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse shrink-0"></span>'
            elif is_emerald:
                border_bg = "border-emerald-500/70 bg-emerald-950/90 text-emerald-200 font-semibold shadow-sm"
                dot = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse shrink-0"></span>'
            else:
                border_bg = "border-indigo-500/70 bg-indigo-950/90 text-indigo-200 font-semibold shadow-sm"
                dot = '<span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-pulse shrink-0"></span>'
            return f'''<a href="{href}" class="px-2.5 py-1.5 rounded-lg border {border_bg} transition flex items-center gap-1.5 shrink-0 whitespace-nowrap" title="{title}">
                    {dot}
                    <span>{label}</span>
                </a>'''
        else:
            return f'''<a href="{href}" class="px-2.5 py-1.5 rounded-lg border border-slate-700/80 bg-slate-800/80 hover:bg-slate-700/90 hover:border-slate-600 text-slate-300 hover:text-white transition flex items-center gap-1.5 shrink-0 whitespace-nowrap" title="{title}">
                    <span>{label}</span>
                </a>'''

    btn_index = get_btn("index", "index.html", "切換至互動實驗室與核心教材總覽", "互動總覽")
    btn_notes = get_btn("notes", "notes.html", "切換至精華講義閱讀手冊", "講義筆記")
    btn_exam = get_btn("exam", "exam.html", "切換至考點變化題解析", "考點變化題")
    btn_hw = get_btn("homework_practice", "homework_practice.html", "切換至作業與練習全解", "作業練習全解")
    btn_hw1_summary = get_btn("hw1_summary", "hw1_summary.html", "切換至作業一核心概念與萬用證明攻略", "作業一攻略", is_cyan=True)
    btn_p1_summary = get_btn("p1_summary", "p1_summary.html", "切換至練習一核心考點精華與極簡證明攻略", "練習一攻略", is_emerald=True)
    btn_proof = get_btn("proof_sheet", "proof_sheet.html", "切換至必考形式證明一覽表", "證明一覽表", is_amber=True)

    github_svg = f'''<a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700/80 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0 ml-1" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>'''

    return f'''<nav id="site-nav" class="flex items-center gap-1 sm:gap-1.5 text-xs overflow-x-auto no-scrollbar py-0.5">
                {btn_index}
                {btn_notes}
                {btn_exam}
                {btn_hw}
                {btn_hw1_summary}
                {btn_p1_summary}
                {btn_proof}
                {github_svg}
            </nav>'''

for page in PAGES:
    with open(page["file"], "r", encoding="utf-8") as f:
        html = f.read()
    new_nav = make_nav(page["id"])
    html = re.sub(r'<nav id="site-nav".*?</nav>', new_nav, html, flags=re.DOTALL)
    with open(page["file"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Synchronized nav in {page['file']}")

print("All 7 navigation bars synchronized successfully!")
