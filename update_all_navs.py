# -*- coding: utf-8 -*-
"""
Sync navigation across all 9 pages using the Term-Segmented (Final Exam vs Midterm Archive) architecture.
Pages:
- Final Exam Hub: index.html
- Midterm Archive: midterm_index.html, notes.html, exam.html, homework_practice.html, hw1_summary.html, p1_summary.html, mock_exam.html, proof_sheet.html
"""
import re

GITHUB_REPO_URL = "https://github.com/johnjohn1207/crypto-exam-review"

PAGES = [
    {"file": "index.html", "id": "final_hub", "name": "期末考專區"},
    {"file": "midterm_index.html", "id": "midterm_index", "name": "期中互動總覽"},
    {"file": "notes.html", "id": "notes", "name": "期中講義筆記"},
    {"file": "exam.html", "id": "exam", "name": "期中考點變化題"},
    {"file": "homework_practice.html", "id": "homework_practice", "name": "作業與練習全解"},
    {"file": "hw1_summary.html", "id": "hw1_summary", "name": "作業一攻略"},
    {"file": "p1_summary.html", "id": "p1_summary", "name": "練習一攻略"},
    {"file": "mock_exam.html", "id": "mock_exam", "name": "期中模擬試卷"},
    {"file": "proof_sheet.html", "id": "proof_sheet", "name": "期中必考證明表"}
]

MIDTERM_PAGES = [
    {"file": "midterm_index.html", "id": "midterm_index", "label": "期中互動總覽", "desc": "Ch. 1-8 互動實驗室與名詞庫"},
    {"file": "notes.html", "id": "notes", "label": "期中講義筆記", "desc": "Ch. 1-8 精華閱讀講義"},
    {"file": "exam.html", "id": "exam", "label": "期中考點變化題", "desc": "10 大考點衍生變化題"},
    {"file": "homework_practice.html", "id": "homework_practice", "label": "作業練習全解", "desc": "作業一與練習一 38 題解析"},
    {"file": "hw1_summary.html", "id": "hw1_summary", "label": "作業一攻略", "desc": "作業一 7 大思維與證明藍圖"},
    {"file": "p1_summary.html", "id": "p1_summary", "label": "練習一攻略", "desc": "練習一 6 大考點與 5 大極簡證明"},
    {"file": "mock_exam.html", "id": "mock_exam", "label": "期中模擬試卷", "desc": "100 分全真模擬試卷與詳解"},
    {"file": "proof_sheet.html", "id": "proof_sheet", "label": "期中必考證明表", "desc": "27 題形式證明直觀速記表"}
]

def make_nav(current_id):
    is_final = (current_id == "final_hub")
    is_in_midterm = not is_final

    # Final Exam Button (Primary Spotlight)
    if is_final:
        btn_final = '''<a href="index.html" class="px-3 py-1.5 rounded-lg border border-emerald-500/80 bg-emerald-950/90 text-emerald-200 font-semibold shadow-sm transition flex items-center gap-1.5 shrink-0 whitespace-nowrap" title="前往期末考核心複習與教材工作區">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></span>
                    <span>⚡ 期末考專區 (進行中)</span>
                </a>'''
    else:
        btn_final = '''<a href="index.html" class="px-3 py-1.5 rounded-lg border border-slate-700/80 bg-slate-800/80 hover:bg-slate-700/90 hover:border-slate-600 text-slate-300 hover:text-white transition flex items-center gap-1.5 shrink-0 whitespace-nowrap" title="前往期末考核心複習與教材工作區">
                    <span>⚡ 期末考專區</span>
                </a>'''

    # Midterm Archive Dropdown / Drawer Button (Collapsible)
    midterm_btn_classes = "border-amber-500/80 bg-amber-950/90 text-amber-200 font-semibold shadow-sm" if is_in_midterm else "border-slate-700/80 bg-slate-800/80 hover:bg-slate-700/90 hover:border-slate-600 text-slate-300 hover:text-white"
    
    midterm_menu_items = ""
    for item in MIDTERM_PAGES:
        item_active = (current_id == item["id"])
        item_style = "bg-amber-950/70 text-amber-200 font-semibold border-l-2 border-amber-400" if item_active else "text-slate-300 hover:bg-slate-800 hover:text-white"
        midterm_menu_items += f'''<a href="{item['file']}" class="px-3 py-2 text-xs transition flex items-center justify-between gap-3 {item_style}">
                        <div>
                            <div class="font-medium">{item['label']}</div>
                            <div class="text-[10px] text-slate-500 font-mono">{item['desc']}</div>
                        </div>
                        { '<span class="text-[10px] text-amber-400 font-mono shrink-0">目前頁面</span>' if item_active else '' }
                    </a>\n'''

    dropdown_html = f'''<div class="relative group" id="midterm-archive-wrapper">
                    <button type="button" onclick="toggleMidtermMenu(event)" id="midterm-archive-btn" class="px-3 py-1.5 rounded-lg border {midterm_btn_classes} transition flex items-center gap-1.5 shrink-0 whitespace-nowrap text-xs">
                        <span>📦 期中考歷史歸檔 (8 大模組)</span>
                        <svg class="w-3.5 h-3.5 text-slate-400 transition-transform duration-200 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <!-- Floating Dropdown Drawer -->
                    <div id="midterm-dropdown-menu" class="hidden group-hover:block absolute right-0 sm:right-auto sm:left-0 mt-1 w-64 rounded-xl bg-slate-900 border border-slate-700/90 shadow-2xl py-1.5 z-50 divide-y divide-slate-800/80 backdrop-blur-md">
                        <div class="px-3 py-1.5 text-[10px] font-mono text-slate-400 bg-slate-950/60 flex items-center justify-between">
                            <span>期中考精華存檔庫（已結算）</span>
                            <span class="text-amber-400">Ch. 1-8 完備</span>
                        </div>
                        <div class="py-1">
                            {midterm_menu_items}
                        </div>
                    </div>
                </div>'''

    github_svg = f'''<a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700/80 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0 ml-1" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>'''

    return f'''<nav id="site-nav" class="flex items-center gap-2 text-xs py-0.5">
                {btn_final}
                {dropdown_html}
                {github_svg}
            </nav>'''

CLICK_SCRIPT = """
<script id="nav-dropdown-script">
function toggleMidtermMenu(e) {
    if (e) e.stopPropagation();
    const menu = document.getElementById('midterm-dropdown-menu');
    if (menu) {
        menu.classList.toggle('hidden');
    }
}
document.addEventListener('click', (e) => {
    const wrapper = document.getElementById('midterm-archive-wrapper');
    const menu = document.getElementById('midterm-dropdown-menu');
    if (menu && wrapper && !wrapper.contains(e.target)) {
        menu.classList.add('hidden');
    }
});
</script>
"""

def update_all_pages():
    for page in PAGES:
        with open(page["file"], "r", encoding="utf-8") as f:
            html = f.read()

        new_nav = make_nav(page["id"])
        # Replace nav#site-nav
        html = re.sub(r'<nav id="site-nav".*?</nav>', new_nav, html, flags=re.DOTALL)

        # Inject or update CLICK_SCRIPT before </body>
        if "nav-dropdown-script" in html:
            html = re.sub(r'<script id="nav-dropdown-script">.*?</script>', CLICK_SCRIPT.strip(), html, flags=re.DOTALL)
        else:
            html = html.replace("</body>", f"{CLICK_SCRIPT}\n</body>")

        with open(page["file"], "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Synchronized term-aware nav in {page['file']}")

if __name__ == "__main__":
    update_all_pages()
    print("All 9 navigation bars successfully synchronized with Midterm/Final segmentation!")
