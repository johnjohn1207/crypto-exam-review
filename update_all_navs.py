# -*- coding: utf-8 -*-
"""
Sync navigation across all 5 pages:
- index.html
- notes.html
- exam.html
- homework_practice.html
- proof_sheet.html
"""
import re

GITHUB_REPO_URL = "https://github.com/johnjohn1207/crypto-exam-review"

PAGES = [
    {"file": "index.html", "id": "index"},
    {"file": "notes.html", "id": "notes"},
    {"file": "exam.html", "id": "exam"},
    {"file": "homework_practice.html", "id": "homework_practice"},
    {"file": "proof_sheet.html", "id": "proof_sheet"}
]

def make_nav(current_id):
    def get_btn(page_id, href, title, label, is_amber=False):
        is_active = (current_id == page_id)
        if is_active:
            if is_amber:
                border_bg = "border-amber-500/60 bg-amber-950/80 text-amber-200 font-semibold"
                dot = '<span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>'
            else:
                border_bg = "border-indigo-500/60 bg-indigo-950/80 text-indigo-200 font-semibold"
                dot = '<span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-pulse"></span>'
            return f'''<a href="{href}" class="px-2.5 py-1.5 rounded-lg border {border_bg} transition flex items-center gap-1 shadow-sm shrink-0" title="{title}">
                    {dot}
                    <span>{label}</span>
                </a>'''
        else:
            return f'''<a href="{href}" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="{title}">
                    <span>{label}</span>
                </a>'''

    btn_index = get_btn("index", "index.html", "切換至互動實驗室", "互動實驗室")
    btn_notes = get_btn("notes", "notes.html", "切換至講義筆記", "講義筆記")
    btn_exam = get_btn("exam", "exam.html", "切換至考點變化題", "考點與變化題")
    btn_hw = get_btn("homework_practice", "homework_practice.html", "切換至作業與練習全解", "作業練習全解")
    btn_proof = get_btn("proof_sheet", "proof_sheet.html", "切換至必考形式證明一覽表", "📐 證明一覽表", is_amber=True)

    github_svg = f'''<a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0 ml-1" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>'''

    return f'''<nav id="site-nav" class="flex items-center gap-1.5 text-xs overflow-x-auto no-scrollbar py-0.5">
                {btn_index}
                {btn_notes}
                {btn_exam}
                {btn_hw}
                {btn_proof}
                {github_svg}
            </nav>'''

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    idx_text = f.read()

# in index.html, the nav has tab buttons first, then the links
idx_nav_tail = f'''    <a href="notes.html" class="ml-2 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 border border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white transition flex items-center gap-1 shadow shrink-0" title="切換至講義筆記">
                    <span>📖 講義筆記</span>
                </a>
                <a href="exam.html" class="ml-1 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 border border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white transition flex items-center gap-1 shadow shrink-0" title="切換至考點變化題解析">
                    <span>🎯 考點變化題</span>
                </a>
                <a href="homework_practice.html" class="ml-1 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 border border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white transition flex items-center gap-1 shadow shrink-0" title="切換至作業與練習全解">
                    <span>📝 作業練習全解</span>
                </a>
                <a href="proof_sheet.html" class="ml-1 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-amber-950/80 border border-amber-700/60 text-amber-300 hover:bg-amber-900 transition flex items-center gap-1 shadow shrink-0" title="切換至必考形式證明一覽表">
                    <span>📐 證明一覽表</span>
                </a>
                <a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0 ml-1" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>
            </nav>'''

idx_text = re.sub(r'</button>\s*<a href="notes\.html".*?</nav>', '</button>\n' + idx_nav_tail, idx_text, flags=re.DOTALL)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_text)
print("Updated index.html nav.")

# 2. Update notes.html
with open("notes.html", "r", encoding="utf-8") as f:
    notes_text = f.read()

notes_nav_tail = f'''<!-- Back to Playground Link -->
                <a href="index.html" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium px-2.5 py-1 rounded-lg text-xs transition flex items-center gap-1 shadow">
                    <span>⚙️ 互動平台</span>
                </a>

                <!-- Link to Exam Page -->
                <a href="exam.html" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium px-2.5 py-1 rounded-lg text-xs transition flex items-center gap-1 shadow">
                    <span>🎯 考點變化題</span>
                </a>

                <!-- Link to HW & Practice Page -->
                <a href="homework_practice.html" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium px-2.5 py-1 rounded-lg text-xs transition flex items-center gap-1 shadow">
                    <span>📝 作業練習全解</span>
                </a>

                <!-- Link to Proof Sheet Page -->
                <a href="proof_sheet.html" class="bg-amber-600 hover:bg-amber-500 text-white font-medium px-2.5 py-1 rounded-lg text-xs transition flex items-center gap-1 shadow">
                    <span>📐 證明一覽表</span>
                </a>

                <!-- GitHub Repo Link -->
                <a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>'''

notes_text = re.sub(r'<!-- Back to Playground Link -->.*?</a>\s*<!-- Link to Exam Page -->.*?</a>.*?(?:<!-- GitHub Repo Link -->.*?</a>)', notes_nav_tail, notes_text, flags=re.DOTALL)
with open("notes.html", "w", encoding="utf-8") as f:
    f.write(notes_text)
print("Updated notes.html nav.")

# 3. Update exam.html
with open("exam.html", "r", encoding="utf-8") as f:
    exam_text = f.read()

exam_nav = make_nav("exam")
exam_text = re.sub(r'<nav id="site-nav".*?</nav>', exam_nav, exam_text, flags=re.DOTALL)

# Also update counts in exam.html:
exam_text = re.sub(r'全部內容 <span id="count-all"[^>]*>\(\d+\)</span>', '全部內容 <span id="count-all" class="text-[10px] opacity-80">(51)</span>', exam_text)
exam_text = re.sub(r'核心公式 <span id="count-formulas"[^>]*>\(\d+\)</span>', '核心公式 <span id="count-formulas" class="text-[10px] opacity-80">(8)</span>', exam_text)
exam_text = re.sub(r'作業一詳解 <span id="count-hw1"[^>]*>\(\d+\)</span>', '作業一詳解 <span id="count-hw1" class="text-[10px] opacity-80">(9)</span>', exam_text)
exam_text = re.sub(r'練習一詳解 <span id="count-practice1"[^>]*>\(\d+\)</span>', '練習一詳解 <span id="count-practice1" class="text-[10px] opacity-80">(29)</span>', exam_text)
exam_text = re.sub(r'變化題演練 <span id="count-variations"[^>]*>\(\d+\)</span>', '變化題演練 <span id="count-variations" class="text-[10px] opacity-80">(5)</span>', exam_text)
# Category button replace ch8-9 with ch8
exam_text = re.sub(r'Ch 8-9 CPA/CCA 攻擊模式', 'Ch 8 選擇明文安全 CPA', exam_text)

with open("exam.html", "w", encoding="utf-8") as f:
    f.write(exam_text)
print("Updated exam.html nav and counts.")

# 4. Update homework_practice.html
with open("homework_practice.html", "r", encoding="utf-8") as f:
    hw_text = f.read()

hw_nav = make_nav("homework_practice")
hw_text = re.sub(r'<nav id="site-nav".*?</nav>', hw_nav, hw_text, flags=re.DOTALL)
with open("homework_practice.html", "w", encoding="utf-8") as f:
    f.write(hw_text)
print("Updated homework_practice.html nav.")

# 5. Update proof_sheet.html
with open("proof_sheet.html", "r", encoding="utf-8") as f:
    proof_text = f.read()

proof_nav = make_nav("proof_sheet")
proof_text = re.sub(r'<nav id="site-nav".*?</nav>', proof_nav, proof_text, flags=re.DOTALL)
with open("proof_sheet.html", "w", encoding="utf-8") as f:
    f.write(proof_text)
print("Updated proof_sheet.html nav.")

print("All 5 navigation bars synchronized successfully!")
