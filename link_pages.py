# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '</nav>'
link_html = """    <a href="notes.html" class="ml-2 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-indigo-950/80 border border-indigo-700/60 text-indigo-300 hover:bg-indigo-900 transition flex items-center gap-1 shadow shrink-0" title="切換至無干擾純筆記閱讀手冊">
                    <span>📖 精華筆記手冊</span> →
                </a>
            </nav>"""

if target in html and 'notes.html' not in html:
    html = html.replace(target, link_html, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully added link to notes.html in index.html.")
else:
    print("Already linked or target not found.")
