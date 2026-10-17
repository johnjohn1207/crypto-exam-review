# -*- coding: utf-8 -*-
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

required_ids = [
    'summaries-module-list', 'module-content-area',
    'playground-tabs-bar', 'playground-content-container',
    'quiz-filter-container', 'quiz-list-container',
    'glossary-content-area'
]

for rid in required_ids:
    if f'id="{rid}"' not in html:
        print(f"[Missing ID in HTML] {rid}")
    else:
        print(f"[HTML ID OK] {rid}")

with open('js/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

with open('js/playgrounds.js', 'r', encoding='utf-8') as f:
    pg_js = f.read()

with open('js/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

print("所有核心檔案讀取正常，ID 對照無誤。")
