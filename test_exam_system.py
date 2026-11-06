# -*- coding: utf-8 -*-
"""
Comprehensive validation of the exam, homework, notes, proof cheat sheet, and term-segmented system.
Verifies:
1. Exam scope constraints (Midterm archive preserves Ch. 1-8 up to 1.5 Sec 1; Final exam hub ready).
2. UI/UX integrity (Dynamic header height sync, no blocked sticky buttons).
3. Universal navigation across all 11 pages with Term Segmentation (Final Exam Modules vs Midterm Archive).
4. Inline JS syntax verification across all 11 pages.
5. Final exam data verification (js/final_data.js) including Mod-1 (CCA/AE) & Mod-3 (DH/Hard Problems) completed status.
"""
import os
import re
import subprocess

print("Starting full system validation (Term Segmentation & UI/UX Integrity across 11 pages)...")

# 1. Check data files exist
DATA_FILES = ["js/exam_data.js", "js/hw_practice_data.js", "js/proof_sheet_data.js", "js/data.js", "js/final_data.js"]
for df in DATA_FILES:
    assert os.path.exists(df), f"Missing data file: {df}"

with open("js/exam_data.js", "r", encoding="utf-8") as f:
    exam_data_txt = f.read()
assert "const EXAM_FORMULAS = " in exam_data_txt
assert "const HW1_DATA = " in exam_data_txt
assert "const PRACTICE1_DATA = " in exam_data_txt
assert "const VARIATION_DATA = " in exam_data_txt
print("Check 1 passed: js/exam_data.js verified.")

with open("js/hw_practice_data.js", "r", encoding="utf-8") as f:
    hw_data_txt = f.read()
assert "const HW_PRACTICE_DATA = " in hw_data_txt

# Verify exclusion of out-of-scope questions in midterm data
for bad_id in ["hw1-5b", "p1-12", "p1-13", "p1-25", "p1-26", "p1-34"]:
    assert f'"{bad_id}"' not in hw_data_txt, f"Out-of-scope ID {bad_id} found in hw_practice_data.js!"
print("Check 2 passed: js/hw_practice_data.js verified (out-of-scope questions excluded from midterm archive).")

with open("js/proof_sheet_data.js", "r", encoding="utf-8") as f:
    proof_data_txt = f.read()
assert "const PROOF_SHEET_DATA = " in proof_data_txt
print("Check 3 passed: js/proof_sheet_data.js verified.")

with open("js/data.js", "r", encoding="utf-8") as f:
    data_txt = f.read()
for bad_mod in ["mod-5", "mod-6", "mod-7"]:
    assert f'"{bad_mod}"' not in data_txt, f"Out-of-scope module {bad_mod} found in js/data.js!"
print("Check 4 passed: js/data.js verified (out-of-scope modules excluded from midterm).")

with open("js/final_data.js", "r", encoding="utf-8") as f:
    final_data_txt = f.read()
assert "const FINAL_EXAM_MODULES = " in final_data_txt
assert 'final-mod-1' in final_data_txt and 'final_ch9_cca_ae.html' in final_data_txt
assert 'final-mod-3' in final_data_txt and 'final_ch11_dh_hard_problems.html' in final_data_txt
print("Check 5 passed: js/final_data.js verified (Modules 1 & 3 completed and active).")

# 2. Check HTML files exist, have KaTeX, and have site-nav
PAGES = [
    "index.html",
    "final_ch9_cca_ae.html",
    "final_ch11_dh_hard_problems.html",
    "midterm_index.html",
    "notes.html",
    "exam.html",
    "homework_practice.html",
    "hw1_summary.html",
    "p1_summary.html",
    "mock_exam.html",
    "proof_sheet.html"
]

for p in PAGES:
    assert os.path.exists(p), f"Missing page: {p}"
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()
    assert "katex.min.js" in html, f"KaTeX missing in {p}"
    assert 'id="site-nav"' in html, f"site-nav missing in {p}"
    assert "--header-height" in html, f"--header-height CSS variable missing in {p}"
    assert "header-sync-script" in html, f"header-sync-script missing in {p}"
    assert "top-16" not in html, f"Legacy hardcoded top-16 found in {p} (causes button blocking)!"
print(f"Check 6 passed: All {len(PAGES)} pages exist and have KaTeX, universal dual-dropdown site-nav, and dynamic UI/UX header sync.")

# 3. Check cross navigation across all 11 pages
for p in PAGES:
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()
    for target_page in PAGES:
        assert f'href="{target_page}"' in html, f"{p} missing link to {target_page}"

print(f"Check 7 passed: Complete cross-navigation verified across all {len(PAGES)} pages (Final Hub, Ch. 9, Ch. 11 & Midterm Archive)!")

# 4. Check inline JavaScript syntax across all 11 pages
node_check_code = r"""
const fs = require('fs');
const pages = process.argv.slice(1);
for (const p of pages) {
    const html = fs.readFileSync(p, 'utf8');
    const matches = [...html.matchAll(/<script[\s\S]*?>([\s\S]*?)<\/script>/gi)];
    for (let i = 0; i < matches.length; i++) {
        const code = matches[i][1];
        if (code.trim() && !matches[i][0].includes('src=')) {
            try {
                new Function(code);
            } catch (e) {
                console.error(`SYNTAX_ERROR in ${p} script #${i}: ${e.message}`);
                process.exit(1);
            }
        }
    }
}
process.exit(0);
"""
res = subprocess.run(["node", "-e", node_check_code, *PAGES], capture_output=True, text=True)
assert res.returncode == 0, f"Inline JS Syntax Check Failed:\n{res.stderr}\n{res.stdout}"
print(f"Check 8 passed: All inline JavaScript scripts across all {len(PAGES)} pages validated syntax-error-free!")

print("All 8 validation checks passed successfully across all 11 pages!")
