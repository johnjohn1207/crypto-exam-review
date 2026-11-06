# 現代與後量子密碼學導論：複習暨互動學習平台

> Introduction to Modern and Post-quantum Cryptography Review Portal

本專案為針對現代與後量子密碼學課程所設計的全方位整合複習平台。平台已全面升級為**「學期雙軌分流架構（Term-Segmented Dual-Engine Architecture）」**，明確區隔「**期末考核心工作區（進行中）**」與「**期中考歷史歸檔庫（已結算・折疊收合）**」，兼顧歷史資料完整保存與期末新教材的高效推進。

---

## 學期階段分流架構（Term Segmentation）

### 1. ⚡ 期末考核心工作區（Final Exam Workspace - 進行中・全站焦點）
- **主要入口**：首頁 `index.html`（預設選中）
- **課程進度**：接續投影片 1-5 Section 2 之後至期末考終點。
- **6 大核心模組規劃架構**：
  1. **Ch. 9**：選擇密文攻擊 (IND-CCA1 / IND-CCA2)、Padding Oracle 攻擊與認證加密 (AE / Encrypt-then-MAC / GCM)
  2. **Ch. 10**：密碼雜湊函數 (Hash)、Merkle-Damgård 結構抗碰撞性證明、長度擴展攻擊與 HMAC 雙重雜湊
  3. **Ch. 11**：數論基礎、模反元素、歐拉函數、中國剩餘定理 (CRT)、離散對數問題 (DLP / CDH / DDH)
  4. **Ch. 12**：公鑰加密體系 (PKE)、Diffie-Hellman 金鑰交換、ElGamal 語意安全、RSA-OAEP 填充標準
  5. **Ch. 13**：數位簽章 (Signatures)、EUF-CMA 安全模型、Hash-and-Sign 範式、Schnorr、ECDSA
  6. **Ch. 14**：後量子密碼學前瞻 (PQC)、Shor 量子威脅、晶格幾何 (Lattice)、容錯學習 (LWE)、NIST 標準 (ML-KEM, ML-DSA)
- **教材注入機制**：隨時提供期末投影片、作業二或練習題目，系統將自動解析推導並結構化注入生成題解與形式證明。

### 2. 📦 期中考歷史歸檔專區（Midterm Archive - 唯讀封存・可折疊隱藏）
- **收納方式**：全站所有頁面頂部導覽列均配置「`📦 期中考歷史歸檔 (8 大模組 ▾)`」折疊下拉選單，平常自動收合不佔據視線，點擊即可展開存取。
- **涵蓋 8 大完備模組**：
  1. **期中互動總覽 (`midterm_index.html`)**：Ch. 1-8 六大互動實驗室（OTP、PRG、DES/AES S-box、Feistel、CTR 等）與名詞庫。
  2. **期中講義筆記 (`notes.html`)**：Ch. 1-8 精華閱讀講義手冊，支援深色/紙張/明亮主題切換。
  3. **期中考點變化題 (`exam.html`)**：10 大核心考點、20 道考卷常考衍生題與題型變體剖析。
  4. **作業與練習全解 (`homework_practice.html`)**：作業一（9 題）+ 練習一（29 題）雙軌直觀思維與嚴謹題解。
  5. **作業一攻略 (`hw1_summary.html`)**：作業一 7 大密碼學核心思維、數學本質與 4 大萬用證明藍圖。
  6. **練習一攻略 (`p1_summary.html`)**：練習一 6 大核心考點精華與 5 大秒殺極簡證明範本。
  7. **期中全真模擬試卷 (`mock_exam.html`)**：滿分 100 分期中考全真模擬試卷，單選、簡答與計算證明完整解析。
  8. **期中必考證明表 (`proof_sheet.html`)**：27 題形式證明直觀大腦模型、速記公式膠囊與分步推導。

---

## 本地快速啟動

若要在本機離線瀏覽任一頁面，可直接執行對應批次檔：
- `start_website.bat`：啟動期末考專區主入口 (`index.html`)。
- `start_notes.bat`：啟動期中精華講義閱讀頁面 (`notes.html`)。
- `start_exam.bat`：啟動期中考點與題型變化分析平台 (`exam.html`)。
- `start_hw_practice.bat`：啟動作業與練習全解專頁 (`homework_practice.html`)。
- `start_proof_sheet.bat`：啟動期中必考形式證明一覽表 (`proof_sheet.html`)。

---

## 資料結構維護與自動化建置腳本

本專案具備完整資料管道，各模組可獨立建置、同步與驗證：

```powershell
# 1. 同步全站 9 大頁面之學期階段導覽列（期末專區 + 折疊期中歸檔）
python update_all_navs.py

# 2. 執行全站完整性與代碼語法測試（驗證範圍、導覽交叉連結、V8 JS 語法零錯誤）
python test_exam_system.py
```
