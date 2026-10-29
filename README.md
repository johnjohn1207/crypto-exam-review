# 現代與後量子密碼學導論：複習暨互動學習平台

> Introduction to Modern and Post-quantum Cryptography Review Portal

本專案為針對現代與後量子密碼學課程所設計的五合一整合複習平台，收錄課程教材（Katz & Lindell、Mike Rosulek《The Joy of Cryptography》及投影片教材），嚴格限定於期中考試範圍，並整合「作業一」與「練習一」建立全面題庫與嚴謹形式證明庫。

---

## 考試範圍界限說明（重要規範）

本平台所有內容嚴格限縮於授課考試範圍：
- **考試範圍內（In-Scope）**：
  - 投影片範圍：1.1 至 1.5 Section 1（對應教材內容）。
  - 教材章節：《The Joy of Cryptography》Ch. 0、1、2、4、5、6、7、8。
  - 涵蓋主題：完美保密性（Shannon 完美安全性、One-Time Pad）、計算安全性（優勢 Advantage、可忽略函數 Negligible Function、生日界限 Birthday Bound）、偽隨機產生器（PRG）、偽隨機函數（PRF）、區塊密碼與置換（PRP、Feistel 網絡）、選擇明文攻擊安全（IND-CPA、CBC 模式、CTR 模式）。
- **非考試範圍（Out-of-Scope，已全面剔除）**：
  - 投影片 1.5 Section 2 之後內容（選擇密文攻擊 CCA / IND-CCA2、格式預言機 Format Oracle、CTR 可鍛造性）。
  - 認證加密（AE / AEAD）、訊息鑑別碼（MAC 組合、Encrypt-then-MAC 等）、填充預言機攻擊（Padding Oracle 破譯）。
  - 補充資料與尚未教授之題目已從本站全數移除，避免誤導備考方向。

---

## 五大整合核心入口

所有頁面均配置全域頂部導覽列，支援即時互通切換：

1. **核心互動學習平台 (`index.html`)**：
   - 考綱 5 大主題章節重點整理與名詞檢索（Ch. 1 至 Ch. 8）。
   - 3 大互動展示實驗室（Two-Time Pad 攻擊實驗、Feistel 網絡可逆結構視覺化、IND-CPA 遊戲預言機安全模擬）。
   - 20 題標準自我評測系統。

2. **精華筆記手冊 (`notes.html`)**：
   - 專注閱讀模式，收錄 8 大核心章節精華內容。
   - 包含深度 Callout 知識點標註（概念定義、重要定理、考試防錯）。
   - 支援深色（Dark）、紙張暖色（Sepia）與明亮白（Light）主題切換。

3. **考點精華與變化題分析平台 (`exam.html`)**：
   - 8 大考綱核心公式與定理深度剖析。
   - 5 大高頻進階變化題型演練（合數階模乘、雙區塊重複、BEAST 攻擊原型等）。
   - 支援雙軌對照模式與刷題自測檢驗。

4. **作業一與練習一 獨立題目詳解與證明全觀念專頁 (`homework_practice.html`)**：
   - **38 題精確收錄**：作業一（9 題）+ 練習一（29 題），已自動剔除 6 題超出範圍之題目（hw1-5b、p1-12、p1-13、p1-25、p1-26、p1-34）。
   - **24 題形式證明題**：完整推導區分者演算法（Distinguisher）、優勢計算（Advantage）與歸約論證（Reduction）。
   - **四層式架構解析**：包含題目原意、核心觀念與定義定理、白話直觀思維、形式化嚴謹證明與考試防錯陷阱。

5. **考綱必考證明一覽表 (`proof_sheet.html`)**：
   - **27 題形式化證明彙編**：嚴選涵蓋反證法、鴿籠原理、區分者歸約、差分不變量、混淆論證之核心定理與練習題證明。
   - **雙重視角切換**：提供「矩陣一覽表（Matrix View）」橫向對照證明結構，以及「詳細推導卡片（Cards View）」展開逐步數學推導。
   - **強大檢索功能**：支援章節篩選、證明策略手法篩選、即時關鍵字過濾、一鍵複製證明與 KaTeX 數學渲染。

---

## 本地快速啟動

若要在本機離線瀏覽任一頁面，可直接執行對應批次檔：
- `start_website.bat`：啟動互動複習平台主頁 (`index.html`)。
- `start_notes.bat`：啟動精華講義閱讀頁面 (`notes.html`)。
- `start_exam.bat`：啟動考點與題型變化分析平台 (`exam.html`)。
- `start_hw_practice.bat`：啟動作業與練習全解專頁 (`homework_practice.html`)。
- `start_proof_sheet.bat`：啟動考綱必考證明一覽表 (`proof_sheet.html`)。

---

## 資料結構維護與自動化建置腳本

本專案具備完整資料管道，各模組可獨立建置與驗證：

```powershell
# 建置考點變化題資料
python build_exam_data.py

# 建置作業一與練習一題目資料
python build_hw_practice_page.py
python generate_hw_practice_page.py

# 建置考綱證明一覽表資料與獨立頁面
python build_proof_sheet_data.py
python generate_proof_sheet_html.py

# 同步五頁全域頂部導覽列
python update_all_navs.py

# 執行全系統驗證測試（自動核對範圍、排版與導覽）
python test_exam_system.py
```
