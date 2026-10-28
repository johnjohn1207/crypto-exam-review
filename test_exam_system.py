# -*- coding: utf-8 -*-
import os
import re

print("Starting validation of exam and homework review system...")

# 1. Check exam_data.js & hw_practice_data.js
data_path = os.path.join("js", "exam_data.js")
assert os.path.exists(data_path), "js/exam_data.js does not exist!"

with open(data_path, "r", encoding="utf-8") as f:
    data_content = f.read()

assert "const EXAM_FORMULAS = " in data_content
assert "const HW1_DATA = " in data_content
assert "const PRACTICE1_DATA = " in data_content
assert "const VARIATION_DATA = " in data_content
print("Check 1 passed: js/exam_data.js has all required data arrays.")

hw_data_path = os.path.join("js", "hw_practice_data.js")
assert os.path.exists(hw_data_path), "js/hw_practice_data.js does not exist!"

with open(hw_data_path, "r", encoding="utf-8") as f:
    hw_data_content = f.read()

assert "const HW_PRACTICE_DATA = " in hw_data_content
print("Check 2 passed: js/hw_practice_data.js verified.")

# 2. Check exam.html
assert os.path.exists("exam.html"), "exam.html does not exist!"
with open("exam.html", "r", encoding="utf-8") as f:
    exam_html = f.read()

for req_id in ["site-nav", "search-input", "cards-container", "filter-summary", "result-count"]:
    assert f'id="{req_id}"' in exam_html, f"Missing id: {req_id} in exam.html"

assert "katex.min.js" in exam_html
assert "exam_data.js" in exam_html
print("Check 3 passed: exam.html elements and script links verified.")

# 3. Check homework_practice.html
assert os.path.exists("homework_practice.html"), "homework_practice.html does not exist!"
with open("homework_practice.html", "r", encoding="utf-8") as f:
    hw_html = f.read()

for req_id in ["site-nav", "search-input", "cards-container", "filter-summary", "result-count", "proof-only-btn"]:
    assert f'id="{req_id}"' in hw_html, f"Missing id: {req_id} in homework_practice.html"

assert "katex.min.js" in hw_html
assert "hw_practice_data.js" in hw_html
print("Check 4 passed: homework_practice.html elements and script links verified.")

# 4. Check cross links
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()
assert 'href="notes.html"' in index_html
assert 'href="exam.html"' in index_html
assert 'href="homework_practice.html"' in index_html

with open("notes.html", "r", encoding="utf-8") as f:
    notes_html = f.read()
assert 'href="index.html"' in notes_html
assert 'href="exam.html"' in notes_html
assert 'href="homework_practice.html"' in notes_html

assert 'href="index.html"' in exam_html
assert 'href="notes.html"' in exam_html
assert 'href="homework_practice.html"' in exam_html

assert 'href="index.html"' in hw_html
assert 'href="notes.html"' in hw_html
assert 'href="exam.html"' in hw_html
assert 'href="homework_practice.html"' in hw_html

print("Check 5 passed: Quad-directional links verified across all 4 pages!")
print("All validation checks passed successfully!")
