# -*- coding: utf-8 -*-
import os
import re

print("Starting validation of exam review system...")

# 1. Check exam_data.js
data_path = os.path.join("js", "exam_data.js")
assert os.path.exists(data_path), "js/exam_data.js does not exist!"

with open(data_path, "r", encoding="utf-8") as f:
    data_content = f.read()

assert "const EXAM_FORMULAS = " in data_content
assert "const HW1_DATA = " in data_content
assert "const PRACTICE1_DATA = " in data_content
assert "const VARIATION_DATA = " in data_content

print("Check 1 passed: js/exam_data.js has all required data arrays.")

# 2. Check exam.html
assert os.path.exists("exam.html"), "exam.html does not exist!"
with open("exam.html", "r", encoding="utf-8") as f:
    exam_html = f.read()

for req_id in ["site-nav", "search-input", "cards-container", "filter-summary", "result-count"]:
    assert f'id="{req_id}"' in exam_html, f"Missing id: {req_id} in exam.html"

assert "katex.min.js" in exam_html
assert "exam_data.js" in exam_html
print("Check 2 passed: exam.html elements and script links verified.")

# 3. Check cross links
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()
assert 'href="notes.html"' in index_html, "index.html missing link to notes.html"
assert 'href="exam.html"' in index_html, "index.html missing link to exam.html"
print("Check 3 passed: index.html links to notes.html and exam.html.")

with open("notes.html", "r", encoding="utf-8") as f:
    notes_html = f.read()
assert 'href="index.html"' in notes_html, "notes.html missing link to index.html"
assert 'href="exam.html"' in notes_html, "notes.html missing link to exam.html"
print("Check 4 passed: notes.html links to index.html and exam.html.")

assert 'href="index.html"' in exam_html, "exam.html missing link to index.html"
assert 'href="notes.html"' in exam_html, "exam.html missing link to notes.html"
print("Check 5 passed: exam.html links to index.html and notes.html.")

print("All validation checks passed successfully!")
