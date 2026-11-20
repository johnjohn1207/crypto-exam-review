# -*- coding: utf-8 -*-
"""
Synchronize the clean white editorial navigation bar and light theme across all pages.
"""
import re

FINAL_PAGES = [
    {"file": "index.html", "id": "final_hub", "legacy_dark": False},
    {"file": "final_ch9_cca_ae.html", "id": "final_ch9", "legacy_dark": True},
    {"file": "final_ch11_dh_hard_problems.html", "id": "final_ch11", "legacy_dark": True},
    {"file": "final_1_8_ecc_signatures.html", "id": "final_1_8", "legacy_dark": False},
    {"file": "final_quiz.html", "id": "final_quiz", "legacy_dark": False},
]

MIDTERM_PAGES = [
    "midterm_index.html", "notes.html", "exam.html", "homework_practice.html",
    "hw1_summary.html", "p1_summary.html", "mock_exam.html", "proof_sheet.html",
]

NAV_ITEMS = [
    {"file": "index.html", "id": "final_hub", "label": "首頁"},
    {"file": "final_ch9_cca_ae.html", "id": "final_ch9", "label": "1.5 CCA 與 AE"},
    {"file": "final_ch11_dh_hard_problems.html", "id": "final_ch11", "label": "1.7 DH 與 RSA"},
    {"file": "final_1_8_ecc_signatures.html", "id": "final_1_8", "label": "1.8 橢圓曲線與簽章"},
    {"file": "final_quiz.html", "id": "final_quiz", "label": "選擇題練習", "cta": True},
    {"file": "midterm_index.html", "id": "midterm", "label": "期中歸檔", "muted": True},
]

def make_light_nav(current_id):
    links = []
    for item in NAV_ITEMS:
        is_active = (current_id == item["id"])
        if item.get("cta"):
            cls = "px-3.5 py-1.5 rounded-lg bg-neutral-900 text-white font-medium transition ml-1" if is_active else "px-3.5 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-medium transition ml-1"
        elif item.get("muted"):
            cls = "px-2.5 py-1.5 rounded-lg bg-neutral-900 text-white font-medium transition ml-1" if is_active else "px-2.5 py-1.5 rounded-lg text-neutral-400 hover:text-neutral-700 transition ml-1"
        else:
            cls = "px-3 py-1.5 rounded-lg bg-neutral-900 text-white font-medium transition" if is_active else "px-3 py-1.5 rounded-lg text-neutral-600 hover:text-neutral-900 hover:bg-neutral-100 transition"
        links.append(f'<a href="{item["file"]}" class="{cls}">{item["label"]}</a>')
    joined = "\n                ".join(links)
    return f'''<nav id="site-nav" class="flex flex-wrap items-center gap-1 text-xs sm:text-[13px]">
                {joined}
            </nav>'''

def make_light_header(current_id):
    nav = make_light_nav(current_id)
    return f'''<header id="site-header" class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-neutral-200">
        <div class="max-w-5xl mx-auto px-5 py-3.5 flex flex-wrap items-center justify-between gap-3">
            <a href="index.html" class="font-bold text-neutral-900 text-sm sm:text-base tracking-tight hover:text-blue-600 transition">
                密碼學期末複習
            </a>
            {nav}
        </div>
    </header>'''

def update_all():
    for page in FINAL_PAGES:
        fn = page["file"]
        with open(fn, "r", encoding="utf-8") as f:
            html = f.read()

        if page["legacy_dark"]:
            html = html.replace('<html lang="zh-TW" class="dark">', '<html lang="zh-TW">')
            if 'css/light_theme.css' not in html:
                html = html.replace('</head>', '    <link rel="stylesheet" href="css/light_theme.css">\n</head>', 1)
            if 'light-override' not in html:
                html = re.sub(r'<body\s+class="([^"]*)"', r'<body class="\1 light-override"', html, count=1)

        # Replace entire site-header with clean white header
        html = re.sub(r'<header id="site-header".*?</header>', make_light_header(page["id"]), html, count=1, flags=re.DOTALL)
        html = re.sub(r'\s*<script id="nav-dropdown-script">.*?</script>', '', html, flags=re.DOTALL)

        with open(fn, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated final page -> {fn}")

    for fn in MIDTERM_PAGES:
        with open(fn, "r", encoding="utf-8") as f:
            html = f.read()
        html = re.sub(r'<nav id="site-nav".*?</nav>', make_light_nav("midterm"), html, flags=re.DOTALL)
        with open(fn, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Synced nav -> {fn}")

if __name__ == "__main__":
    update_all()
    print("All pages updated to clean white editorial UI.")
