# -*- coding: utf-8 -*-
"""
Sync navigation across index.html, notes.html, exam.html, and homework_practice.html
"""
import re

GITHUB_REPO_URL = "https://github.com/johnjohn1207/crypto-exam-review"

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

nav_tail_index = f'''    <a href="notes.html" class="ml-2 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 border border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white transition flex items-center gap-1 shadow shrink-0" title="切換至講義筆記">
                    <span>📖 講義筆記</span>
                </a>
                <a href="exam.html" class="ml-1 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 border border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white transition flex items-center gap-1 shadow shrink-0" title="切換至考點變化題解析">
                    <span>🎯 考點變化題</span>
                </a>
                <a href="homework_practice.html" class="ml-1 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-indigo-950/80 border border-indigo-700/60 text-indigo-300 hover:bg-indigo-900 transition flex items-center gap-1 shadow shrink-0" title="切換至作業與練習全解">
                    <span>📝 作業練習全解</span>
                </a>
                <a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0 ml-1" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>
            </nav>'''

index_html = re.sub(r'</button>\s*<a href="notes\.html".*?</nav>', '</button>\n' + nav_tail_index, index_html, flags=re.DOTALL)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated index.html nav.")

# 2. Update notes.html
with open("notes.html", "r", encoding="utf-8") as f:
    notes_html = f.read()

notes_nav_tail = f'''<!-- Back to Playground Link -->
                <a href="index.html" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium px-2.5 py-1 rounded-lg text-xs transition flex items-center gap-1 shadow">
                    <span>⚙️ 互動平台</span>
                </a>

                <!-- Link to Exam Page -->
                <a href="exam.html" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium px-2.5 py-1 rounded-lg text-xs transition flex items-center gap-1 shadow">
                    <span>🎯 考點變化題</span>
                </a>

                <!-- Link to HW & Practice Page -->
                <a href="homework_practice.html" class="bg-indigo-600 hover:bg-indigo-500 text-white font-medium px-2.5 py-1 rounded-lg text-xs transition flex items-center gap-1 shadow">
                    <span>📝 作業練習全解</span>
                </a>

                <!-- GitHub Repo Link -->
                <a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>'''

notes_html = re.sub(r'<!-- Back to Playground Link -->.*?</a>\s*<!-- Link to Exam Page -->.*?</a>.*?(?:<!-- GitHub Repo Link -->.*?</a>)', notes_nav_tail, notes_html, flags=re.DOTALL)
with open("notes.html", "w", encoding="utf-8") as f:
    f.write(notes_html)
print("Updated notes.html nav.")

# 3. Update exam.html
with open("exam.html", "r", encoding="utf-8") as f:
    exam_html = f.read()

exam_nav_tail = f'''<nav id="site-nav" class="flex items-center gap-1.5 text-xs overflow-x-auto no-scrollbar py-0.5">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="切換至互動實驗室">
                    <span>互動實驗室</span>
                </a>
                <a href="notes.html" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="切換至講義筆記">
                    <span>講義筆記</span>
                </a>
                <a href="exam.html" class="px-2.5 py-1.5 rounded-lg border border-indigo-500/60 bg-indigo-950/80 text-indigo-200 font-semibold transition flex items-center gap-1 shadow-sm shrink-0" title="當前頁面：考點與變化題">
                    <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-pulse"></span>
                    <span>考點與變化題</span>
                </a>
                <a href="homework_practice.html" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="切換至作業與練習全解">
                    <span>作業練習全解</span>
                </a>
                <a href="{GITHUB_REPO_URL}" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0 ml-1" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>
            </nav>'''

exam_html = re.sub(r'<nav id="site-nav".*?</nav>', exam_nav_tail, exam_html, flags=re.DOTALL)
with open("exam.html", "w", encoding="utf-8") as f:
    f.write(exam_html)
print("Updated exam.html nav.")

print("All navigations successfully synchronized!")
