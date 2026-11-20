// Final Exam Comprehensive Multiple Choice Question Bank
// Generated from Slides 1.5 Section 2 (P.15-85), Slides 1.7 (P.1-49), and Slides 1.8 (P.1-61)
// Total: 105 high-yield exam questions

const FINAL_MCQ_DATA = [
  {
    "id": "q1",
    "topic": "CCA 安全性與解密預言機",
    "difficulty": "基礎",
    "question": "在選擇密文攻擊（CCA）的安全性博弈中，攻擊者相較於選擇明文攻擊（CPA）被額外賦予了何種預言機權限？",
    "options": [
      "A. 能夠直接讀取對稱密鑰 $K$ 的前 32 位元",
      "B. 能夠提交除「挑戰密文 $C^*$」以外的任意密文要求解密預言機回傳其解密明文",
      "C. 能夠無限制地解密包含挑戰密文 $C^*$ 在內的任何密文",
      "D. 能夠要求伺服器更換新的隨機主密鑰"
    ],
    "answer": 1,
    "explanation": "依據投影片 1.5 P.18-19 與 P.39，CCA 安全性允許攻擊者自由存取解密預言機（cca.dec），可解密任意攻擊者選定的密文，但嚴格禁止直接提交挑戰密文 $C^*$ 本身（否則解密出明文即平凡攻破）。",
    "trap": "若允許解密挑戰密文 $C^*$，任何加密體系在數學定義上都無法達成安全性。"
  },
  {
    "id": "q2",
    "topic": "CCA 安全性與解密預言機",
    "difficulty": "中等",
    "question": "在投影片 1.5 P.39 的 CCA 安全性形式化庫定義中，理想隨機庫 $\\mathcal{L}_{\\Sigma}^{\\text{cca-rand}}$ 在收到攻擊者調用 `cca.dec(C)` 時，其處理邏輯為何？",
    "options": [
      "A. 一律直接回傳錯誤代碼 `err`",
      "B. 若 $C$ 存在於字典 $\\mathcal{D}$ 中則回傳 $\\mathcal{D}[C]$；若不存在則回落至真實解密 $\\Sigma.\\text{Dec}(K, C)$",
      "C. 若 $C$ 不在字典中則生成均勻隨機字串加入字典並回傳",
      "D. 重新計算該密文的 SHA-256 雜湊值並比對"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.39 明確定義：在 $\\mathcal{L}^{\\text{cca-rand}}$ 中，若 $\\mathcal{D}[C]$ defined 則 return $\\mathcal{D}[C]$；否則回落執行 $\\Sigma.\\text{Dec}(K, C)$。這使得攻擊者篡改密文所造成的明文洩漏在真實庫與隨機庫之間產生可被檢驗的行為差異。",
    "trap": "注意勿與 Authenticated Encryption (AE) 的理想庫混淆，AE 隨機庫在密文不在字典時一律回傳 `err`，而 CCA 隨機庫是回落至真實解密。"
  },
  {
    "id": "q3",
    "topic": "延展性 (Malleability)",
    "difficulty": "基礎",
    "question": "密碼學中對「延展性（Malleability）」的精確定義為何？",
    "options": [
      "A. 密鑰長度可以隨著明文長度動態拉伸",
      "B. 給定未知明文 $M$ 的密文 $C$，攻擊者能在不知道密鑰的情況下構造出新密文 $C' \\neq C$，使得其解密明文 $M'$ 與 $M$ 存在已知或可預測的數學關係",
      "C. 加密演算法可以平行化在多核心處理器上執行",
      "D. 密文在傳輸過程中若遺失部分位元組仍可藉由 Reed-Solomon 碼自動糾錯"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.24 定義：Malleability 指的是給定 $C = \\text{Enc}(K, M)$，能產生 $C' \\neq C$ 使得 $M' = \\text{Dec}(K, C')$ 與 $M$ 存在可預測關係（例如 $M' = M \\oplus \\Delta$）。",
    "trap": "延展性並非彈性或擴充性，而是安全漏洞，代表密文缺乏完整性防護。"
  },
  {
    "id": "q4",
    "topic": "延展性 (Malleability)",
    "difficulty": "基礎",
    "question": "下列哪一種對稱加密工作模式在未搭配認證標籤（MAC）時，具備延展性（Malleable）？",
    "options": [
      "A. 僅 CTR 模式",
      "B. 僅 CBC 模式",
      "C. 僅 One-Time Pad (OTP)",
      "D. CTR 模式、CBC 模式與 One-Time Pad 全都具備延展性"
    ],
    "answer": 3,
    "explanation": "投影片 1.5 P.17 與 P.24-26 闡明：所有未認證的經典對稱加密模式（CTR、CBC、OTP、CFB、OFB）皆具備延展性。CTR 與 OTP 可任意進行 Bit-flipping；CBC 翻轉前一密文區塊可精準控制後一明文區塊的 XOR 差值。",
    "trap": "別以為 CBC 模式因為有鏈結機制就沒有延展性，CBC 模式對前一個區塊的修改同樣會以 bit-flipping 的形式影響下一區塊。"
  },
  {
    "id": "q5",
    "topic": "延展性 (Malleability)",
    "difficulty": "中等",
    "question": "延展性（Malleability）與選擇密文安全性（CCA Security）之間的根本關係為何？",
    "options": [
      "A. 具備延展性的加密方案絕對不是 CCA 安全的",
      "B. 具備延展性的加密方案必定是 CCA 安全的",
      "C. 延展性僅影響 CPA 安全性，與 CCA 安全性無關",
      "D. 只要密鑰長度達到 256 位元，具備延展性的方案就能保證 CCA 安全"
    ],
    "answer": 0,
    "explanation": "投影片 1.5 P.40 定義：任何具備延展性的方案皆可輕易攻破 CCA 安全性。攻擊者只需加密測試訊息 $M$，對密文進行已知篡改（如 $S \\oplus \\Delta$），再送交解密預言機驗證解密結果是否滿足預期關係即可區分真實庫與隨機庫。",
    "trap": "金鑰長度無法彌補架構上的可篡改性缺陷。"
  },
  {
    "id": "q6",
    "topic": "形式化證明 (1-bit Malleability)",
    "difficulty": "進階",
    "question": "針對方案 $\\text{Enc}(K, M): R \\leftarrow \\{0,1\\}^\\lambda, S := F(K, R) \\oplus M$，攻擊者構造區分器：加密 $M$ 得到 $R \\parallel S$，向解密預言機查詢 $R \\parallel (S \\oplus \\Delta)$ 得到 $M'$，並回傳 $M' \\stackrel{?}{=} M \\oplus \\Delta$。在隨機庫 $\\mathcal{L}_{\\Sigma}^{\\text{cca-rand}}$ 中，該等式成立的機率為何？",
    "options": [
      "A. $1$",
      "B. $1/2$",
      "C. 約 $1/2^\\lambda$（極小可忽略值）",
      "D. $0$"
    ],
    "answer": 2,
    "explanation": "投影片 1.5 P.41 推導：在隨機庫中，$R \\parallel (S \\oplus \\Delta)$ 因 $\\Delta \\neq 0$ 未記錄在字典 $\\mathcal{D}$，回落至真實解密。但隨機庫中 $S$ 是獨立均勻隨機選取的字串，因此解密出的明文 $M' = F(K, R) \\oplus S \\oplus \\Delta$ 與原始 $M$ 完全獨立，剛好等於 $M \\oplus \\Delta$ 的機率僅為 $2^{-\\lambda}$。",
    "trap": "注意隨機庫中的 $S$ 是純隨機字串，不是 $F(K, R) \\oplus M$。"
  },
  {
    "id": "q7",
    "topic": "Frankenstein 拼湊攻擊",
    "difficulty": "進階",
    "question": "投影片 1.5 P.42-43 提出的「科學怪人拼湊攻擊（Frankenstein Trick）」針對方案 $S = F(K, R) \\oplus F(K, M)$，攻擊者加密同一個 $M$ 兩次得到 $R_1 \\parallel S_1$ 與 $R_2 \\parallel S_2$。若攻擊者交叉提交解密 $C_A = R_1 \\parallel S_2$ 與 $C_B = R_2 \\parallel S_1$，其解密結果 $M_1^*$ 與 $M_2^*$ 在真實庫中為何必然相等？",
    "options": [
      "A. 因為 $R_1 = R_2$",
      "B. 因為 PRP 函數具有同態加法性",
      "C. 因為解密前之輸入皆為 $F(K, R_1) \\oplus F(K, R_2) \\oplus F(K, M)$，因 XOR 滿足交換律而完全相同",
      "D. 因為解密預言機會快取相同的查詢"
    ],
    "answer": 2,
    "explanation": "投影片 1.5 P.43 數學推導：$S_1 = F(K, R_1) \\oplus F(K, M)$ 且 $S_2 = F(K, R_2) \\oplus F(K, M)$。解密 $R_1 \\parallel S_2$ 時求逆前之值為 $F(K, R_1) \\oplus S_2 = F(K, R_1) \\oplus F(K, R_2) \\oplus F(K, M)$；解密 $R_2 \\parallel S_1$ 時求逆前之值為 $F(K, R_2) \\oplus S_1 = F(K, R_2) \\oplus F(K, R_1) \\oplus F(K, M)$。兩者數學上嚴格恆等，故解密結果必相等。",
    "trap": "此方案即使 $M$ 經過非線性 PRP 處理防止了單 bit 翻轉，仍會被跨密文塊的拼湊偽造攻破。"
  },
  {
    "id": "q8",
    "topic": "CCA1 vs CCA2",
    "difficulty": "中等",
    "question": "非適應性選擇密文攻擊（IND-CCA1 / Lunchtime Attack）與適應性選擇密文攻擊（IND-CCA2）的主要差異為何？",
    "options": [
      "A. CCA1 只能解密長度小於 64 位元組的密文",
      "B. CCA1 僅允許攻擊者在「收到挑戰密文之前」存取解密預言機；CCA2 則在「收到挑戰密文之後」仍可繼續查詢解密預言機（唯獨不能查詢挑戰密文本身）",
      "C. CCA1 是針對公開金鑰密碼，CCA2 僅針對對稱金鑰密碼",
      "D. CCA1 不允許攻擊者選取明文，只能選取密文"
    ],
    "answer": 1,
    "explanation": "依據密碼學標準定義（投影片 1.5 講義脈絡）：CCA1（午餐時間攻擊）的解密預言機存取權限在挑戰階段開始前終止；而 CCA2（適應性選擇密文攻擊）允許攻擊者在獲得挑戰密文 $C^*$ 之後，繼續根據 $C^*$ 構造相關密文向預言機發起解密查詢。",
    "trap": "「適應性（Adaptive）」意味著後續查詢能夠根據先前獲得的挑戰密文動態調整。"
  },
  {
    "id": "q9",
    "topic": "CTR 模式位元翻轉攻擊",
    "difficulty": "基礎",
    "question": "在 CTR 模式中，假設密文區塊為 $C_i = F(K, C_0 + i - 1) \\oplus M_i$。若攻擊者將密文第 $i$ 區塊翻轉一個差異值 $\\Delta$（即 $C_i' = C_i \\oplus \\Delta$），解密後的明文區塊 $M_i'$ 將會變成什麼？",
    "options": [
      "A. 整個區塊變成不可預測的隨機垃圾資料",
      "B. $M_i' = M_i \\oplus \\Delta$，其餘區塊完全不受影響",
      "C. 解密演算法直接拋出語法錯誤崩潰",
      "D. 僅翻轉 $M_i$ 的最高有效位元"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.24-26 說明：CTR 模式下解密為 $\\text{Keystream} \\oplus C_i' = \\text{Keystream} \\oplus (C_i \\oplus \\Delta) = (\\text{Keystream} \\oplus C_i) \\oplus \\Delta = M_i \\oplus \\Delta$。攻擊者可精準篡改明文數值（例如將匯款金額從 $100 改為 $900）。",
    "trap": "CBC 模式翻轉密文會導致當前區塊解密變垃圾且下一區塊被精確翻轉；而 CTR 模式翻轉密文只會精確翻轉對應明文，完全不擴散到其他字元。"
  },
  {
    "id": "q10",
    "topic": "CCA 安全性的防禦解法",
    "difficulty": "基礎",
    "question": "投影片 1.5 P.44 與 P.54 指出，防禦延展性攻擊並達成 CCA 安全性的根本性核心修復哲學為何？",
    "options": [
      "A. 增加 AES 的輪數（Round）從 10 輪增加至 20 輪",
      "B. 限制解密預言機的查詢頻率（Rate Limiting）",
      "C. 拒絕解密任何不是由合法持有金鑰者自身創造的密文（Reject any ciphertext we didn't create ourselves）",
      "D. 改用更長的密碼字串作為金鑰"
    ],
    "answer": 2,
    "explanation": "投影片 1.5 P.44 明確總結：The fix is to 'Reject any ciphertext we didn’t create ourselves. That is exactly what authenticated encryption gives us.' 任何未經合法認證的密文在解密前必須被無條件拒絕。",
    "trap": "頻率限制（Rate-limiting）只能拖延攻擊時間，無法從數學上修復漏洞。"
  },
  {
    "id": "q11",
    "topic": "Null-Oracle 盲解攻擊",
    "difficulty": "中等",
    "question": "在投影片 1.5 P.27-31 的 Null-Oracle 攻擊中，伺服器僅洩漏解密結果「是否含有空字元（`0x00`）」的 1-bit 訊息。若要完全還原一個長度為 $n$ 位元組的 CTR 明文，攻擊者最壞情況下只需向預言機發起幾次查詢？",
    "options": [
      "A. $256^n$ 次",
      "B. 不超過 $255 \\times n$ 次",
      "C. $n^2$ 次",
      "D. $16 \\times 2^{16}$ 次"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.29-31 明確給出演算法複雜度：每個位元組最多猜測 255 種非零異或值即可精準判定該位元組（若皆否則原值必為 0x00），故 $n$ 個位元組總查詢數不超過 $255 \\times n$ 次（線性級複雜度）。",
    "trap": "不要誤選指數級的 $256^n$（那是沒有 Oracle 時的盲目暴力窮舉）。"
  },
  {
    "id": "q12",
    "topic": "PKCS#7 填充標準",
    "difficulty": "基礎",
    "question": "在 16 位元組（128-bit）區塊大小的對稱加密中，採用 PKCS#7 規範填充。若明文最後一個區塊剛好已填滿 16 位元組，系統將如何處理填充？",
    "options": [
      "A. 不做任何填充，直接進行加密",
      "B. 額外補上一整塊全新的 16 位元組，每個位元組的值皆為 `0x10`（十進位 16）",
      "C. 在末端補上一個字節的 `0x00`",
      "D. 回報錯誤並拒絕加密"
    ],
    "answer": 1,
    "explanation": "PKCS#7 規定：若明文恰好是區塊大小的整數倍，為了避免解密時無法區分原始資料與填充，必須額外追加一個完整區塊，其 16 個位元組的值全為 `0x10`（16）。若差 1 字節則補 `0x01`，差 2 字節補 `0x02 0x02`。",
    "trap": "許多人常誤以為剛好整除時不需要填充，這是導致解密歧義的嚴重錯誤。"
  },
  {
    "id": "q13",
    "topic": "PKCS#7 Padding Oracle 攻擊",
    "difficulty": "進階",
    "question": "在針對 CBC 模式的 PKCS#7 Padding Oracle 攻擊中，CBC 解密公式為 $P_k = \\text{Dec}_K(C_k) \\oplus C_{k-1}$，令中間值 $I_k = \\text{Dec}_K(C_k)$。若攻擊者篡改 $C_{k-1}$ 的末字節為猜測值 $r$，且伺服器回報 Padding Valid（有效填充為 `0x01`），則中間值末字節 $I_k[16]$ 的計算公式為何？",
    "options": [
      "A. $I_k[16] = r \\oplus 0x00$",
      "B. $I_k[16] = r \\oplus 0x01$",
      "C. $I_k[16] = C_{k-1}[16] \\oplus 0x01$",
      "D. $I_k[16] = r \\oplus C_k[16]$"
    ],
    "answer": 1,
    "explanation": "依據投影片 1.5 P.34 與 Padding Oracle 原理：當填充有效為 `0x01` 時，解密明文末字節滿足 $P_k'[16] = I_k[16] \\oplus r = 0x01$。移項異或即得 $\\mathbf{I_k[16] = r \\oplus 0x01}$。求出中間值後，再與原始密文 $C_{k-1}[16]$ 異或即可得真實明文 $P_k[16] = I_k[16] \\oplus C_{k-1}[16]$。",
    "trap": "計算中間值使用的是攻擊者當前猜測的 $r$，而非原始密文。"
  },
  {
    "id": "q14",
    "topic": "真實世界 Format Oracle 案例",
    "difficulty": "基礎",
    "question": "2014 年針對 SSL 3.0 協議造成數百萬網站受害的 POODLE 攻擊，其底層核心漏洞機制為何？",
    "options": [
      "A. RSA 密鑰過短被量子電腦分解",
      "B. CBC 模式在 SSL 3.0 實作中的 PKCS#7 Padding Oracle 漏洞",
      "C. Diffie-Hellman 參數使用了弱質數",
      "D. SHA-1 產生了雜湊碰撞"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.34 明確提及：CBC 模式在 SSL 3.0 中的填充檢查缺陷導致了著名的 POODLE 攻擊，攻擊者藉由 Padding Oracle 逐字節解密 HTTPS Cookie 等敏感資料。",
    "trap": "POODLE 攻擊是 CBC 模式的 Padding Oracle 漏洞，非雜湊碰撞亦非離散對數問題。"
  },
  {
    "id": "q15",
    "topic": "時序側信道 (Timing Side-Channels)",
    "difficulty": "中等",
    "question": "投影片 1.5 P.35 介紹的「Lucky Thirteen」攻擊破壞了舊版 TLS，它是利用何種現象構成解密預言機的？",
    "options": [
      "A. 伺服器回傳的 HTTP 狀態碼是 200 還是 500",
      "B. 伺服器解密後因不同的 Padding 長度導致計算 HMAC 的時間產生微秒級差異（Timing Differences）",
      "C. 伺服器發送封包的大小長度變化",
      "D. 電腦 CPU 散熱風扇轉速聲音頻率"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.35 指出：Lucky Thirteen 利用伺服器解密檢驗 Padding 與後續計算 MAC 時產生的微小執行時間差（Microsecond differences）作為側信道，間接洩露明文內容。",
    "trap": "側信道攻擊不一定需要伺服器拋出顯式報錯訊息，時間微差即可致命。"
  },
  {
    "id": "q16",
    "topic": "格式預言機 (Format Oracles)",
    "difficulty": "中等",
    "question": "投影片 1.5 P.36 描述的舊版 Apple iMessage 漏洞中，攻擊者是如何建立解密預言機的？",
    "options": [
      "A. 系統在解密出合法的 gzip 壓縮檔與損壞的 gzip 檔案時會產生不同行為與報錯",
      "B. 利用 Siri 語音朗讀出錯誤的明文",
      "C. 藉由 iCloud 照片同步的時間戳記",
      "D. 透過推播通知音效長短"
    ],
    "answer": 0,
    "explanation": "投影片 1.5 P.36 記錄：Apple iMessage 使用 gzip 壓縮明文。伺服器解密後若為有效 gzip 則正常處理，若非有效 gzip 則報錯。攻擊者利用 gzip 格式規範構造特定密文，達成完全靜默解密私密訊息。",
    "trap": "格式預言機不限於密碼學 Padding，任何高層應用協定解碼器（gzip、XML、JSON）皆可能成為預言機。"
  },
  {
    "id": "q17",
    "topic": "格式預言機本質",
    "difficulty": "基礎",
    "question": "依據投影片 1.5 P.33，構成一個「格式預言機攻擊（Format-Oracle Attack）」必須具備哪些必要條件？",
    "options": [
      "A. 系統存在記憶體溢位（Buffer Overflow）錯誤",
      "B. 系統接收未受信任的密文、進行解密、並依解密結果產生攻擊者可觀測的行為差異（如報錯、崩潰或時間差）",
      "C. 系統必須使用超過 10 年未更新的舊版硬體",
      "D. 攻擊者必須持有部分金鑰資訊"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.33 總結四要件：1. 接收不可信密文；2. 執行解密；3. 根據解密結果產生不同行為；4. 行為差異可被攻擊者觀測。即使程式碼完全沒有實作 Bug，正常的邏輯分支也可能構成預言機。",
    "trap": "格式預言機攻擊是密碼協定設計缺陷，不需要程式碼具有記憶體安全漏洞。"
  },
  {
    "id": "q18",
    "topic": "Rate Limiting 的局限性",
    "difficulty": "基礎",
    "question": "為什麼在伺服器端單純實施「請求速率限制（Rate-Limiting）」無法徹底解決 Padding Oracle 攻擊？",
    "options": [
      "A. 因為速率限制演算法本身存在數學漏洞",
      "B. 速率限制只增加攻擊耗時，並未修復可延展性與 Oracle 洩漏的根本缺陷，且攻擊者可多帳號或耐心發送，合法用戶亦受波及",
      "C. 因為速率限制只能針對 IPv4，無法限制 IPv6",
      "D. 因為攻擊者可以直接修改伺服器的限制設定檔"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.32 闡釋：Rate-limiting 僅能拉長攻擊時間，無法消除根本脆弱性；攻擊者可保持耐心或分散 IP 查詢。根本解法必須採用密碼學方案（如認證加密 AE）從源頭拒絕未認證密文。",
    "trap": "防護資安問題不能只依賴維運防禦（WAF/限速），核心加密架構必須證明安全。"
  },
  {
    "id": "q19",
    "topic": "MAC 與 Hash 的本質差異",
    "difficulty": "基礎",
    "question": "訊息鑑別碼（MAC）與無金鑰密碼雜湊函數（如 SHA-256）最根本的區別為何？",
    "options": [
      "A. MAC 的輸出長度永遠比雜湊函數長",
      "B. MAC 必須使用通訊雙方共享的「秘密金鑰」進行運算，因此具備驗證訊息來源真實性與不可偽造性；而普通雜湊無金鑰，無法防範主動攻擊者同時竄改資料與雜湊值",
      "C. 雜湊函數具備抗碰撞性，而 MAC 完全不具備抗碰撞性",
      "D. MAC 只能用於加密短文字，雜湊函數只能用於檔案下載"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.46-51 說明：一般雜湊（如驗證 Linux ISO）無金鑰，只能捕捉意外位元損壞，無法防範惡意鏡像同時替換 ISO 與 SHA-256；MAC 需要持有秘密金鑰才能產生與驗證 Tag，提供真實性與不可偽造性。",
    "trap": "無金鑰雜湊無法防範中間人攻擊，因為攻擊者竄改內容後可以自行重算雜湊值。"
  },
  {
    "id": "q20",
    "topic": "PRF 作為 MAC",
    "difficulty": "中等",
    "question": "依據投影片 1.5 P.53，直接將偽隨機函數（PRF）$F$ 作為 MAC 使用（即標籤 $T = F(K, M)$），其安全性前提為何？",
    "options": [
      "A. 訊息 $M$ 必須長度小於 8 位元組",
      "B. 若 $F$ 是一個安全的 PRF，則該 MAC 在 EUF-CMA 模型下是不可偽造的",
      "C. 必須搭配非對稱公鑰才能保證安全",
      "D. 必須使用至少兩組獨立金鑰進行交替加密"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.53 指出：A pseudorandom function (PRF) can be used directly as a MAC! 若攻擊者能偽造未知訊息的 $F(K, M)$，則該攻擊者當場可作為區分 $F$ 與真隨機函數的 Distinguisher，違反 PRF 安全性假設。",
    "trap": "安全 PRF 的輸出對未查詢過的輸入具有不可預測性，天生即為不可偽造的 MAC。"
  },
  {
    "id": "q21",
    "topic": "三大組合範式對比",
    "difficulty": "基礎",
    "question": "在結合對稱加密方案（$\\text{Enc}$）與訊息鑑別碼（$\\text{MAC}$）的三大範式中，哪一種方式能夠「保證在任意 CPA 安全加密方案與安全 MAC 下通用達成 CCA 安全」？",
    "options": [
      "A. Encrypt-then-MAC (EtM)",
      "B. Encrypt-and-MAC (E&M)",
      "C. MAC-then-Encrypt (MtE)",
      "D. 三種方式在數學上皆具備相同的 CCA 安全性"
    ],
    "answer": 0,
    "explanation": "投影片 1.5 P.57-61 權威總結：只有 Encrypt-then-MAC (EtM) 是普適（Generic）達到 CCA 安全性的範式；Encrypt-and-MAC 連 CPA 都不安全；MAC-then-Encrypt 則高度依賴特定實作，通常易破。",
    "trap": "必須牢記只有 Encrypt-then-MAC 是唯一被證明通用的安全範式。"
  },
  {
    "id": "q22",
    "topic": "Encrypt-then-MAC 流程",
    "difficulty": "基礎",
    "question": "Encrypt-then-MAC (EtM) 的解密與驗證流程中，最關鍵的「黃金實作法則」為何？",
    "options": [
      "A. 先解密密文，再驗證明文的雜湊值",
      "B. 必須在執行任何解密運算之前先驗證 MAC 標籤，若驗證失敗立即回傳 `err` 終止，絕不進入解密演算法",
      "C. 將 MAC 標籤與密文同時平行解密",
      "D. 若 MAC 驗證失敗，先嘗試修復填充再解密"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.55 與 P.67 明確強調：Verify before decrypt! 任何被篡改的密文因缺乏 MAC 金鑰無法偽造合法標籤，在 MAC 驗證階段即被直接拋棄，解密模組完全不被觸碰，從根源消滅 Padding Oracle。",
    "trap": "若先解密後驗證，解密過程中的報錯或時間差依然會形成 Oracle 洩漏！"
  },
  {
    "id": "q23",
    "topic": "Encrypt-and-MAC 缺陷",
    "difficulty": "中等",
    "question": "為什麼 Encrypt-and-MAC 範式（密文為 $C \\parallel T$，其中 $C = \\text{Enc}(K_e, M), T = \\text{MAC}(K_m, M)$）「連最基礎的 CPA 安全性都無法滿足」？",
    "options": [
      "A. 因為它使用了兩組金鑰導致計算負擔過重",
      "B. 因為 MAC 直接計算在明文 $M$ 上，且標準 MAC 多為確定性函數，相同明文必產生相同標籤，直接洩漏明文相等性（$M_1 = M_2 \\implies T_1 = T_2$）",
      "C. 因為 MAC 會逆向推導出加密金鑰 $K_e$",
      "D. 因為解密端無法區分密文與標籤的分界點"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.59 指出：Encrypt-and-MAC is not even CPA-secure! MAC is computed on the plaintext. 攻擊者只要比對標籤是否相同，就能輕易區分挑戰密文加密了哪一個明文，破壞密文不可區分性。",
    "trap": "SSH 協定早期採用了 Encrypt-and-MAC，是密碼學歷史上的著名設計失誤。"
  },
  {
    "id": "q24",
    "topic": "MAC-then-Encrypt 缺陷",
    "difficulty": "中等",
    "question": "MAC-then-Encrypt (MtE) 範式（先算明文標籤 $T = \\text{MAC}(K_m, M)$，再加密整合成 $C = \\text{Enc}(K_e, M \\parallel T)$）在實務上最大的安全風險為何？",
    "options": [
      "A. 密文體積會膨脹超過十倍",
      "B. 標籤被包在密文內部，接收者必須先執行解密才能看到標籤，解密過程中的 Padding 錯誤或時序差異極易遭受 Padding Oracle 攻擊（如 POODLE 與 Lucky 13）",
      "C. 只能使用在非同步網路",
      "D. 無法支援多個使用者通訊"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.60 說明：Tag is hidden inside the ciphertext. 接收端解密時若 Padding 錯誤往往在檢驗 MAC 之前就報錯，使攻擊者獲得解密預言機，這正是舊版 TLS 屢遭重創的主因。",
    "trap": "MtE 在某些理論條件下可安全，但工程上極難實現安全，因此不是通用安全範式。"
  },
  {
    "id": "q25",
    "topic": "三大組合範式矩陣速記",
    "difficulty": "基礎",
    "question": "依據投影片 1.5 P.61 的安全對比矩陣，下列關於三大範式的 CPA 與 CCA 安全性評價何者完全正確？",
    "options": [
      "A. EtM: CPA 是 / CCA 是；E&M: CPA 否 / CCA 否；MtE: CPA 是 / CCA 視情況 (Maybe)",
      "B. EtM: CPA 否 / CCA 是；E&M: CPA 是 / CCA 是；MtE: CPA 否 / CCA 否",
      "C. EtM: CPA 是 / CCA 否；E&M: CPA 否 / CCA 是；MtE: CPA 是 / CCA 是",
      "D. 三者皆為 CPA 是 / CCA 是"
    ],
    "answer": 0,
    "explanation": "投影片 1.5 P.61 經典表格：\nEncrypt-then-MAC: CPA-secure? Yes, CCA-secure? Yes.\nEncrypt-and-MAC: CPA-secure? No, CCA-secure? No.\nMAC-then-encrypt: CPA-secure? Yes, CCA-secure? Maybe.",
    "trap": "考場必背矩陣：EtM 雙 Yes，E&M 雙 No，MtE 一 Yes 一 Maybe。"
  },
  {
    "id": "q26",
    "topic": "Encrypt-then-MAC 金鑰獨立性",
    "difficulty": "進階",
    "question": "在實作 Encrypt-then-MAC 時，加密金鑰 $K_e$ 與認證金鑰 $K_m$ 必須滿足什麼關係？",
    "options": [
      "A. 兩者必須相等（$K_e = K_m$）以節省記憶體",
      "B. 兩者必須是相互獨立的隨機金鑰（$K_e \\neq K_m$），絕不可混用同一把金鑰",
      "C. $K_m$ 必須是 $K_e$ 的反元素",
      "D. $K_m$ 必須是 $K_e$ 的 SHA-256 雜湊前 8 位元組"
    ],
    "answer": 1,
    "explanation": "密碼學基本安全原則（投影片 1.5 P.52 與 P.55）：Key separation！若將同一金鑰同時用於加密與 MAC，兩演算法內部的代數交互作用可能導致金鑰洩漏或破壞安全性證明。必須使用獨立金鑰。",
    "trap": "切記不同密碼原語絕對不可共用同一金鑰（Never reuse keys across different algorithms）。"
  },
  {
    "id": "q27",
    "topic": "CBC-MAC 局限性",
    "difficulty": "中等",
    "question": "針對可變長度訊息（Variable-length messages），標準的 CBC-MAC 存在何種著名脆弱性？",
    "options": [
      "A. 容易被量子電腦在一微秒內攻破",
      "B. 容易遭受長度擴展與訊息拼接偽造攻擊（若攻擊者獲得 $T_1 = \\text{MAC}(M_1)$，可偽造拼接訊息 $M_1 \\parallel (M_2 \\oplus T_1)$ 的標籤）",
      "C. 只能支援英文 ASCII 字元",
      "D. 標籤長度會隨著訊息長度線性增加"
    ],
    "answer": 1,
    "explanation": "密碼學經典考點：基本 CBC-MAC 僅對固定區塊長度安全；若訊息長度可變，攻擊者可透過異或前一標籤進行訊息拼接偽造。現代標準因此引入 CMAC（使用子金鑰 $K_1, K_2$ 修正末區塊）來防禦此漏洞。",
    "trap": "CBC-MAC 必須搭配長度預處理或改用 CMAC 才能安全處理任意長度訊息。"
  },
  {
    "id": "q28",
    "topic": "HMAC 雙重結構",
    "difficulty": "基礎",
    "question": "HMAC（Hash-based Message Authentication Code）採用雙重雜湊架構 $\\text{HMAC}(K, M) = H((K \\oplus \\text{opad}) \\parallel H((K \\oplus \\text{ipad}) \\parallel M))$，其核心設計初衷為何？",
    "options": [
      "A. 為了讓雜湊速度加快一倍",
      "B. 為了防範 Merkle-Damgård 結構雜湊函數固有的「長度擴展攻擊（Length Extension Attack）」",
      "C. 為了壓縮密鑰長度至 16 位元組",
      "D. 為了將非對稱密鑰轉為對稱密鑰"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.46-52 脈絡：若直接使用單層雜湊 $H(K \\parallel M)$ 作為 MAC，攻擊者可利用 MD 結構的內部狀態直接在末端追加數據，造成偽造。HMAC 藉由內外兩層密鑰加鹽填充（ipad/opad）徹底杜絕長度擴展攻擊。",
    "trap": "純 $H(K \\parallel M)$ 絕不是安全的 MAC，只有 HMAC 才是經過形式證明的結構。"
  },
  {
    "id": "q29",
    "topic": "認證加密 (AE) vs CCA 安全性",
    "difficulty": "中等",
    "question": "依據投影片 1.5 P.63-65，認證加密（Authenticated Encryption, AE）與選擇密文安全性（CCA Security）之間的最關鍵差異為何？",
    "options": [
      "A. AE 是非對稱加密，CCA 針對對稱加密",
      "B. 在 AE 的理想隨機庫中，任何非該庫自身產生的密文解密「一律回傳錯誤代碼 `err`」；而在 CCA 隨機庫中，未記錄密文仍會回落執行真實解密",
      "C. CCA 安全性比 AE 安全性更強大",
      "D. AE 只能保證完整性，不保證機密性"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.64-65 詳細對比：AE 要求除了金鑰持有者生成的密文外，所有攻擊者構造的密文解密結果必須嚴格為 `err`。定理指出：$\\text{AE} \\implies \\text{CCA}$，AE 是比 CCA 更高階的黃金標準。",
    "trap": "注意蘊含方向：AE 蘊含 CCA，但 CCA 不保證解密結果皆為 err，故 CCA 不蘊含 AE。"
  },
  {
    "id": "q30",
    "topic": "AES-GCM 架構組成",
    "difficulty": "基礎",
    "question": "目前網際網路最廣泛使用的認證加密模式 AES-GCM（Galois/Counter Mode），是由哪兩個密碼學組件結合而成的？",
    "options": [
      "A. AES in CBC 模式 ＋ HMAC-SHA256",
      "B. AES in CTR 模式（提供機密性） ＋ GMAC / GHASH（提供真實性與完整性）",
      "C. ChaCha20 ＋ Poly1305",
      "D. RSA ＋ SHA-1"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.68 指出：AES-GCM combines AES in CTR mode (for encryption) with GMAC/GHASH (for authentication).",
    "trap": "ChaCha20-Poly1305 是另一種主流 AEAD，切勿與 AES-GCM 的組件混淆。"
  },
  {
    "id": "q31",
    "topic": "GHASH 特性與優勢",
    "difficulty": "中等",
    "question": "依據投影片 1.5 P.70-71，AES-GCM 採用 GHASH 而非 HMAC-SHA256 作為認證標籤演算法的主要優勢為何？",
    "options": [
      "A. GHASH 在沒有金鑰的情況下也是抗碰撞的",
      "B. GHASH 基於伽羅瓦有限體 $GF(2^{128})$ 多項式乘法，完全可平行化處理，且具備 Intel PCLMULQDQ 硬體指令加速，速度可比 HMAC 快 15 倍",
      "C. GHASH 可以取代非對稱數位簽章",
      "D. GHASH 不需要輸入任何 Nonce"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.71 比較：HMAC-SHA256 本質是循序的且需兩次雜湊；GHASH 每個區塊僅需一次有限體乘法，高度平行化且硬體支援，在 1KB 訊息處理上快達 15 倍。",
    "trap": "GHASH 是帶金鑰函數（Keyed），無金鑰時無抗碰撞性，其優勢在於極致的平行運算與硬體加速效能。"
  },
  {
    "id": "q32",
    "topic": "GHASH 局限性",
    "difficulty": "中等",
    "question": "依據投影片 1.5 P.72，為什麼 GHASH 絕對不能直接取代 SHA-256 或 SHA-3 用於公開憑證簽章或比特幣工作量證明？",
    "options": [
      "A. 因為 GHASH 輸出長度超過 512 位元",
      "B. 因為 GHASH 是帶金鑰函數（Keyed function），且具備代數線性結構；若無秘密金鑰，任何人都能輕易尋找碰撞",
      "C. 因為 GHASH 受到專利保護",
      "D. 因為 GHASH 只能在 Linux 作業系統運行"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.72 強調：GHASH has a linear structure $\\text{GHASH}_H(A \\oplus B) = \\text{GHASH}_H(A) \\oplus \\text{GHASH}_H(B)$，沒有金鑰保護時不具備抗碰撞性。公開可驗證場合必須使用 SHA-2/3。",
    "trap": "不同工具用於不同場景：GHASH 是專用對稱 MAC，SHA 是公開無金鑰雜湊。"
  },
  {
    "id": "q33",
    "topic": "AES-GCM Nonce 重用致命災難",
    "difficulty": "進階",
    "question": "在 AES-GCM 實作中，若在相同金鑰 $K$ 下重複使用了相同的 Nonce，會導致什麼毀滅性後果？",
    "options": [
      "A. 僅導致當前單一訊息解密失敗",
      "B. CTR 模式金鑰流重複導致明文 XOR 洩漏，且攻擊者可藉由多項式方程直接求解出認證金鑰 $H$，往後可任意偽造所有密文的合法 Tag",
      "C. 伺服器 CPU 會發生硬體損毀",
      "D. 系統會自動切換為 CBC 模式"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.73 警告：Never reuse a nonce with the same key! Nonce 重用會破壞 CTR 的機密性，更嚴重的是兩個具相同 Nonce 的 Tag 相減可列出有限體多項式方程，直接解出雜湊密鑰 $H = \\text{AES}(K, 0^{128})$，使認證性全盤崩潰。",
    "trap": "GCM 對 Nonce 重用的脆弱性極高，這也是 TLS 1.3 嚴格管理 Nonce 計數器的原因。"
  },
  {
    "id": "q34",
    "topic": "金鑰承諾 (Key Commitment)",
    "difficulty": "進階",
    "question": "投影片 1.5 P.74 探討的「金鑰承諾缺陷（Lack of Key Commitment）」對 AEAD 體系有何影響？",
    "options": [
      "A. 密鑰會在傳輸過程中被中間人掉包",
      "B. 大多數 AEAD（包含 AES-GCM）未承諾金鑰：攻擊者可精心構造單一合法密文 $C$，使其在金鑰 $K_1$ 下解密為無害明文，而在金鑰 $K_2$ 下解密出惡意攻擊內容且皆通過驗證",
      "C. 伺服器必須承諾定期更換金鑰",
      "D. 使用者必須簽署法律合約保證不外洩金鑰"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.74 詳細剖析：Key commitment 指的是密文只能在單一合法金鑰下解密。若無此性質，攻擊者可進行內容走私（Content smuggling）或偽造不可抵賴性，在多收件者情境下造成安全漏洞。",
    "trap": "這是一個近年密碼學前沿漏洞，顯示單純滿足 AE 定義仍可能在多金鑰情境下出問題。"
  },
  {
    "id": "q35",
    "topic": "ChaCha20-Poly1305 特性",
    "difficulty": "基礎",
    "question": "相較於 AES-GCM，ChaCha20-Poly1305（由 Daniel J. Bernstein 設計）在何種運行環境下具有最顯著的優勢？",
    "options": [
      "A. 具備 Intel AES-NI 硬體加速的大型伺服器",
      "B. 缺乏專用 AES 硬體加速指令集的行動裝置、物聯網（IoT）設備，且具備優異的抗時序側信道能力（無查表操作）",
      "C. 只能處理少於 128 位元的短封包",
      "D. 量子電腦運算環境"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.75-76 比較：ChaCha20 採用 ARX（加法、旋轉、異或）運算，無查表（No table lookups），天然免疫快取時序側信道攻擊，且在無 AES 硬體加速的晶片上效能遠高於軟體 AES。",
    "trap": "有 AES 硬體指令時 AES-GCM 稍快；但無硬體指令時 ChaCha20-Poly1305 具壓倒性優勢且更安全。"
  },
  {
    "id": "q36",
    "topic": "重放攻擊 (Replay Attack)",
    "difficulty": "中等",
    "question": "投影片 1.5 P.77-79 展示的情境中，Alice 曾發送過合法的認證加密密文 $C = \\text{Enc}(K, \\text{\"family-recipes.txt\"})$。為什麼即使使用完全安全的認證加密（AE），Bob 仍可能被攻擊者重放該密文而將重要檔案刪除？",
    "options": [
      "A. 因為金鑰 $K$ 被攻擊者逆推破解",
      "B. 因為 AE 只能保證密文內容未被竄改，但無法防範合法舊密文在不同上下文語境（如從「顯示檔案」變成「刪除檔案」）下被原封不動重新發送",
      "C. 因為 AES 演算法存在已知的碰撞",
      "D. 因為 Bob 的電腦中毒"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.79 總結：Authenticated encryption didn't save us — context matters! 密文本身完全有效且通過 MAC 檢驗，但環境語意由「DISPLAY」切換為「DELETE」，密文缺乏與上下文的強制綁定。",
    "trap": "單純的加密和標籤防不了重放，必須將「語境/上下文」引入保護範圍。"
  },
  {
    "id": "q37",
    "topic": "AEAD 關聯資料 (Associated Data)",
    "difficulty": "基礎",
    "question": "AEAD 中的「關聯資料（Associated Data, AD）」在加密與解密過程中扮演何種角色？",
    "options": [
      "A. 它是與明文一起被加密隱藏的秘密資訊",
      "B. 它是參與完整性與真實性標籤計算、但「保持明文不加密」的上下文資訊（如協定版本、封包序號、指令語意），解密時必須傳入相同 AD 否則判定驗證失敗",
      "C. 它是解密時用來還原金鑰的輔助參數",
      "D. 它是用來填充密文使其達到 16 位元組倍數的假資料"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.80-83 定義：Associated Data (AD) 是雙方已知的上下文（如封包頭、`ACTION: DISPLAY`），它不佔用密文加密負載，但強烈綁定於認證標籤中。解密時若上下文不符（如嘗試在 DELETE 語境解密），立即回傳 `err`。",
    "trap": "記住 AD 是「被認證（Authenticated）」但「不被加密（Not Encrypted）」的資料。"
  },
  {
    "id": "q38",
    "topic": "Fujisaki-Okamoto Transform",
    "difficulty": "進階",
    "question": "投影片 1.5 P.84 介紹的 Fujisaki-Okamoto (FO) 轉換，在現代密碼學（包括後量子標準 ML-KEM / Kyber）中的主要功用為何？",
    "options": [
      "A. 將對稱加密轉為非對稱加密",
      "B. 在隨機預言機模型（ROM）下，將僅具備 CPA 安全性的公鑰加密方案轉換為具備強大 CCA2 安全性的公鑰加密機制",
      "C. 將 SHA-256 提速為 GHASH",
      "D. 解決離散對數問題"
    ],
    "answer": 1,
    "explanation": "投影片 1.5 P.84 說明：The Fujisaki-Okamoto Transform converts CPA-secure PKE to CCA-secure PKE. 核心做法是將加密所需的隨機數改由訊息雜湊 $R = H(M)$ 決定，解密時重新加密比對密文一致性，杜絕惡意密文篡改。",
    "trap": "FO 轉換是公鑰密碼從被動安全（CPA）躍升為主動安全（CCA）的關鍵經典橋樑。"
  },
  {
    "id": "q39",
    "topic": "非對稱原語本質",
    "difficulty": "基礎",
    "question": "依據投影片 1.7 P.5-6，公鑰/非對稱密碼原語（如 Diffie-Hellman、RSA、ML-KEM）與對稱原語最大的結構性差異為何？",
    "options": [
      "A. 非對稱原語的運算速度快上千倍",
      "B. 非對稱原語基於代數結構，其安全性嚴格依賴於特定數學難題的單向計算困難度假設",
      "C. 非對稱原語不需要使用任何亂數",
      "D. 非對稱原語已經完全不受量子電腦威脅"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.6 闡述：Asymmetric Primitives are algebraic, assuming the hardness of mathematical problems. 對稱原語依靠工程混淆擴散，非對稱原語依賴代數結構難題。",
    "trap": "非對稱加密因為涉及大數模運算，速度通常比對稱加密慢數百至數千倍。"
  },
  {
    "id": "q40",
    "topic": "P 類問題與快速模冪",
    "difficulty": "基礎",
    "question": "在模 $p$ 乘法群中計算 $g^x \\pmod p$，已知最佳演算法（如平方乘算法 Square-and-Multiply）的時間複雜度為何？",
    "options": [
      "A. $\\mathcal{O}(x)$（與指數數值成正比）",
      "B. $\\mathcal{O}(\\log x)$（與指數的位元長度成多項式關係，屬於 P 類容易問題）",
      "C. $\\mathcal{O}(2^x)$",
      "D. 無法在多項式時間內完成"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.12 說明：Computing $g^x \\bmod p$ takes about $\\log_2 x$ multiplications (square-and-multiply). 正向計算指數屬於多項式時間容易問題（Easy Problem）。",
    "trap": "計算 $g^x \\pmod p$ 極快，只有逆向給定 $h = g^x$ 求解 $x$（離散對數）才是難題。"
  },
  {
    "id": "q41",
    "topic": "數學群公理",
    "difficulty": "基礎",
    "question": "對於密碼學常用的模 $p$ 乘法群 $\\mathbb{Z}_p^* = \\{1, 2, \\dots, p-1\\}$（$p$ 為質數），下列哪一項群公理陳述是錯誤的？",
    "options": [
      "A. 封閉性：群內任意兩元素相乘取模 $p$，結果仍在群內",
      "B. 單位元素：群內唯一的乘法單位元素是 $1$",
      "C. 反元素：群內每個元素 $a$ 皆存在唯一的模逆元 $a^{-1}$ 使得 $a \\cdot a^{-1} \\equiv 1 \\pmod p$",
      "D. 零元素：群內必須包含元素 $0$ 且滿足 $0 \\cdot a \\equiv 0 \\pmod p$"
    ],
    "answer": 3,
    "explanation": "投影片 1.7 P.13-14 定義：乘法群 $\\mathbb{Z}_p^*$ 僅包含非零整數 $\\{1, 2, \\dots, p-1\\}$，**絕對不包含 $0$**（因為 $0$ 沒有乘法逆元，若包含 $0$ 則無法滿足反元素公理）。",
    "trap": "加法群 $\\mathbb{Z}_p$ 包含 $0$；但乘法群 $\\mathbb{Z}_p^*$ 排除 $0$。"
  },
  {
    "id": "q42",
    "topic": "生成元 (Generator)",
    "difficulty": "中等",
    "question": "在乘法群 $\\mathbb{Z}_7^*$（元素為 $\\{1, 2, 3, 4, 5, 6\\}$）中，判斷元素 $g = 3$ 是否為該群的生成元（Generator）？",
    "options": [
      "A. 是，因為其次方產生的集合剛好包含全體 6 個元素 $\\{3, 2, 6, 4, 5, 1\\}$",
      "B. 否，因為 $3^2 \\equiv 2 \\pmod 7$",
      "C. 否，因為 $3$ 是質數不能作為生成元",
      "D. 否，因為其階數只有 3"
    ],
    "answer": 0,
    "explanation": "驗證 $g = 3$ 的次方模 7：\n$3^1 \\equiv 3$, $3^2 \\equiv 9 \\equiv 2$, $3^3 \\equiv 6$, $3^4 \\equiv 18 \\equiv 4$, $3^5 \\equiv 12 \\equiv 5$, $3^6 \\equiv 15 \\equiv 1$。\n生成的集合恰好為 $\\{3, 2, 6, 4, 5, 1\\}$，包含全體 $p-1=6$ 個非零元素，故 $g = 3$ 確為生成元。",
    "trap": "必須能產生群內「所有」元素才稱為生成元。"
  },
  {
    "id": "q43",
    "topic": "離散對數問題 (DLP)",
    "difficulty": "基礎",
    "question": "離散對數問題（Discrete Logarithm Problem, DLP）的標準數學形式為：給定 $p, g, h$，尋找整數 $x$ 使得 $g^x \\equiv h \\pmod p$。已知 $p = 17, g = 3, h = 10$，則秘密指數 $x$ 為何？",
    "options": [
      "A. $x = 2$",
      "B. $x = 3$",
      "C. $x = 5$",
      "D. $x = 7$"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.16 原題範例：\n$3^1 \\equiv 3$, $3^2 \\equiv 9$, $3^3 = 27 = 17 + 10 \\equiv 10 \\pmod{17}$。\n故 $x = 3$。",
    "trap": "小數值可手算驗證，但在 2048 位元的大質數下目前無任何經典捷徑。"
  },
  {
    "id": "q44",
    "topic": "DLP 攻擊演算法比較",
    "difficulty": "中等",
    "question": "針對任意群中的離散對數問題，Baby-Step Giant-Step (BSGS) 演算法相較於簡單暴力窮舉 $\\mathcal{O}(p)$，將時間複雜度降到了多少？代價是什麼？",
    "options": [
      "A. 降至 $\\mathcal{O}(\\log p)$，代價是必須知道私鑰",
      "B. 降至 $\\mathcal{O}(\\sqrt{p})$，代價是需要消耗 $\\mathcal{O}(\\sqrt{p})$ 的記憶體空間來儲存查表（空間換時間）",
      "C. 降至多項式時間，無任何代價",
      "D. 複雜度完全沒變"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.18 說明：Baby-step giant-step 與 Pollard's rho 皆可將時間降至 $\\mathcal{O}(\\sqrt{p})$。BSGS 需要建立大小為 $\\lceil\\sqrt{p}\\rceil$ 的雜湊表，空間換時間；Pollard's rho 則近乎無額外空間需求。",
    "trap": "即使降至 $\\mathcal{O}(\\sqrt{p})$，對於 2048 位元質數，$\\sqrt{2^{2048}} = 2^{1024}$ 依然無法在實務中破解。"
  },
  {
    "id": "q45",
    "topic": "DLP vs. 大整數質因數分解 (Factoring)",
    "difficulty": "中等",
    "question": "依據投影片 1.7 P.17，離散對數問題（DLP）與大整數質因數分解問題（Factoring）之間的對比何者正確？",
    "options": [
      "A. 兩者都已經被證明是 NP-complete 問題",
      "B. DLP 用於 Diffie-Hellman（1976），Factoring 用於 RSA（1977）；在相同位元長度下兩者經典難度相近，且皆會被量子 Shor 演算法在多項式時間內攻破",
      "C. 量子電腦只能破解 RSA，無法破解 Diffie-Hellman",
      "D. Factoring 存在已知的經典多項式時間演算法"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.17 明確闡述：Security equivalence: n-bit factoring $\\approx$ n-bit discrete logarithm. Both are vulnerable to Shor’s quantum algorithm. Both are not known to be NP-hard.",
    "trap": "Shor 演算法能同時攻破 RSA（質因數分解）與 ECC / DH（離散對數問題）。"
  },
  {
    "id": "q46",
    "topic": "通用群與數體篩法",
    "difficulty": "進階",
    "question": "為什麼相同的 128 位元安全強度下，工作在一般有限體模乘法群 $\\mathbb{Z}_p^*$ 上的 Diffie-Hellman 需要至少 2048 位元的質數 $p$，而工作在橢圓曲線群（ECDH）上只需約 256 位元的密鑰？",
    "options": [
      "A. 因為橢圓曲線完全不受 Shor 演算法影響",
      "B. 因為 $\\mathbb{Z}_p^*$ 受到次指數時間演算法（數體篩法 Index Calculus / GNFS）攻擊；而良好設計的橢圓曲線不存在指數運算微細結構，已知最佳經典攻擊只有 $\\mathcal{O}(\\sqrt{q})$ 的 Pollard's rho",
      "C. 因為 256 位元的質數在 $\\mathbb{Z}_p^*$ 中不存在生成元",
      "D. 因為美國政府強制規定"
    ],
    "answer": 1,
    "explanation": "密碼學核心原理：$\\mathbb{Z}_p^*$ 具有整數乘法與質數因數分解特性，Index Calculus 能達到次指數時間破解；但橢圓曲線群沒有此類光滑數結構，只能依賴 $\\mathcal{O}(\\sqrt{q})$ 演算法，故 256-bit ECC 等效於 3072-bit $\\mathbb{Z}_p^*$。",
    "trap": "橢圓曲線金鑰短是因為經典演算法對它只能用平方根暴力法，而非量子免疫。"
  },
  {
    "id": "q47",
    "topic": "Diffie-Hellman 協定流程",
    "difficulty": "基礎",
    "question": "在標準 Diffie-Hellman 金鑰交換中，Alice 與 Bob 協商公開參數 $p, g$ 後，雙方在公開通道上互相交換的資訊是什麼？",
    "options": [
      "A. Alice 的私鑰 $a$ 與 Bob 的私鑰 $b$",
      "B. Alice 的公鑰 $A = g^a \\bmod p$ 與 Bob 的公鑰 $B = g^b \\bmod p$",
      "C. 最終的共享金鑰 $S = g^{ab} \\bmod p$",
      "D. 雙方各自的密碼明文"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.19：Alice 送出 $A = g^a \\bmod p$，Bob 送出 $B = g^b \\bmod p$。私鑰 $a, b$ 與共享秘密 $S$ 絕不在網路上傳輸。",
    "trap": "共享秘密 $S$ 是雙方各自在本地端計算出來的，絕不可公開傳輸。"
  },
  {
    "id": "q48",
    "topic": "手算實戰題 (p=13, g=2)",
    "difficulty": "基礎",
    "question": "投影片 1.7 P.20 數值範例：公開參數 $p = 13, g = 2$。Alice 挑選私鑰 $a = 5$，Bob 挑選私鑰 $b = 7$。試問 Alice 發送的公鑰 $A$ 為何？",
    "options": [
      "A. $A = 5$",
      "B. $A = 6$",
      "C. $A = 7$",
      "D. $A = 11$"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.20 計算：$A = g^a \\bmod p = 2^5 \\bmod 13 = 32 \\bmod 13 = 2 \\times 13 + 6 = 6$。",
    "trap": "$32 = 26 + 6$，餘數為 6。"
  },
  {
    "id": "q49",
    "topic": "手算實戰題 (p=13, g=2)",
    "difficulty": "基礎",
    "question": "承上題（$p = 13, g = 2, a = 5, b = 7$），已知 Alice 的公鑰 $A = 6$，Bob 的公鑰 $B = 11$。試問雙方計算出的共享秘密 $S$ 為何？",
    "options": [
      "A. $S = 6$",
      "B. $S = 7$",
      "C. $S = 11$",
      "D. $S = 1$"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.20 計算：\nAlice 計算：$S = B^a \\bmod p = 11^5 \\equiv (-2)^5 = -32 \\equiv 7 \\pmod{13}$。\nBob 計算：$S = A^b \\bmod p = 6^7 \\bmod 13 = 7$。\n共享秘密 $S = 7$。",
    "trap": "利用負數取模 $(-2)^5 = -32 \\equiv 7 \\pmod{13}$ 可以大幅加速手算。"
  },
  {
    "id": "q50",
    "topic": "課堂必考手算 (p=23, g=5)",
    "difficulty": "中等",
    "question": "投影片 1.7 P.21 課堂原題：公開參數 $p = 23, g = 5$。Alice 挑選私鑰 $a = 6$。試問 Alice 發送給 Bob 的公鑰 $A = 5^6 \\bmod 23$ 之值為何？",
    "options": [
      "A. $A = 2$",
      "B. $A = 8$",
      "C. $A = 13$",
      "D. $A = 19$"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.21 答案：\n$5^2 = 25 \\equiv 2 \\pmod{23}$。\n因此 $A = 5^6 = (5^2)^3 \\equiv 2^3 = \\mathbf{8} \\pmod{23}$。",
    "trap": "先將 $5^2$ 化簡為 2，再算 $2^3 = 8$，只需 1 秒鐘即可解出。"
  },
  {
    "id": "q51",
    "topic": "課堂必考手算 (p=23, g=5)",
    "difficulty": "中等",
    "question": "承上題（$p = 23, g = 5$），Bob 挑選私鑰 $b = 15$。試問 Bob 發送給 Alice 的公鑰 $B = 5^{15} \\bmod 23$ 之值為何？",
    "options": [
      "A. $B = 8$",
      "B. $B = 11$",
      "C. $B = 19$",
      "D. $B = 22$"
    ],
    "answer": 2,
    "explanation": "投影片 1.7 P.21 答案：\n$5^2 \\equiv 2$, $5^4 \\equiv 4$, $5^8 \\equiv 16 \\equiv -7 \\pmod{23}$。\n$5^{14} = 5^8 \\cdot 5^4 \\cdot 5^2 \\equiv (-7) \\cdot 4 \\cdot 2 = -56 \\equiv 13 \\pmod{23}$。\n$5^{15} = 5^{14} \\cdot 5 \\equiv 13 \\cdot 5 = 65 \\equiv \\mathbf{19} \\pmod{23}$（或 $65 - 3 \\times 23 = -4 \\equiv 19$）。",
    "trap": "$65 = 2 \times 23 + 19$，計算時小心進位減法。"
  },
  {
    "id": "q52",
    "topic": "課堂必考手算 (p=23, g=5)",
    "difficulty": "進階",
    "question": "承前兩題（$p = 23, g = 5, a = 6, b = 15$），雙方最終計算出的共享秘密 $S = g^{ab} \\pmod{23}$ 為何？",
    "options": [
      "A. $S = 2$",
      "B. $S = 8$",
      "C. $S = 16$",
      "D. $S = 19$"
    ],
    "answer": 0,
    "explanation": "投影片 1.7 P.21 答案：\n理論值 $S = 5^{6 \\times 15} = 5^{90} \\pmod{23}$。\n根據費馬小定理，$\\phi(23) = 22$，$5^{22} \\equiv 1 \\pmod{23}$。\n指數取模：$90 \\equiv 90 - 4 \\times 22 = 2 \\pmod{22}$。\n故 $S \\equiv 5^2 = 25 \\equiv \\mathbf{2} \\pmod{23}$！\n驗證 Alice：$S = B^a = 19^6 \\equiv (-4)^6 = 4096 \\equiv 2 \\pmod{23}$。\n驗證 Bob：$S = A^b = 8^{15} = (2^3)^{15} = 2^{45} \\equiv (2^{22})^2 \\cdot 2^1 \\equiv 1 \\cdot 2 = 2 \\pmod{23}$。",
    "trap": "牢記費馬小定理：指數部分是模 $p-1$（22），底數運算才是模 $p$（23）！"
  },
  {
    "id": "q53",
    "topic": "歷史先驅貢獻",
    "difficulty": "基礎",
    "question": "依據投影片 1.7 P.11，Martin Hellman 本人主張 Diffie-Hellman 金鑰交換協定應被稱作「Diffie-Hellman-Merkle」，原因為何？",
    "options": [
      "A. 因為 Merkle 發明了計算機網路",
      "B. 因為 Ralph Merkle 是歷史上最早提出公開金鑰分發（Public-key distribution / Merkle's Puzzles）概念的先驅",
      "C. 因為 Merkle 證明了該協定的數學安全性",
      "D. 因為 Merkle 贊助了史丹佛大學的研究經費"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.11 記錄：Hellman himself says it should be called Diffie-Hellman-Merkle: Ralph Merkle had the idea of public-key distribution first (Merkle's Puzzles, 1974).",
    "trap": "Merkle 的貢獻是公開金鑰分配構想，GCHQ 的 Malcolm Williamson 則是在機密環境下平行發現。"
  },
  {
    "id": "q54",
    "topic": "Eve 竊聽者的資訊視野",
    "difficulty": "基礎",
    "question": "在被動竊聽（Passive Eavesdropping）模型下，竊聽者 Eve 攔截通訊封包後，究竟掌握了哪些數值？",
    "options": [
      "A. 僅能看到密鑰交換成功的通知",
      "B. 掌握公開參數 $(p, g)$ 以及雙方交換的公鑰 $(A = g^a, B = g^b)$，但不知道私鑰 $(a, b)$ 與共享秘密 $S$",
      "C. 能直接看到 $a$ 與 $b$",
      "D. 掌握所有的金鑰與明文"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.20 總結：Eavesdropper sees only: $p, g, A, B$。Eve 的任務是從 $(g^a, g^b)$ 推導出 $g^{ab}$，這正是 CDH 問題。",
    "trap": "被動竊聽者能看到所有傳輸的公鑰，但無法看到私鑰與共享秘密。"
  },
  {
    "id": "q55",
    "topic": "計算型 DH (CDH) 問題",
    "difficulty": "基礎",
    "question": "計算型 Diffie-Hellman 問題（Computational Diffie-Hellman Problem, CDH）的目標為何？",
    "options": [
      "A. 給定 $g$ 與 $g^x$，求解 $x$",
      "B. 給定 $g^a \\bmod p$ 與 $g^b \\bmod p$，在不知道私鑰 $a, b$ 的情況下計算出共享秘密 $g^{ab} \\bmod p$",
      "C. 給定質數 $p$，尋找所有的生成元",
      "D. 判定兩個密文是否加密相同明文"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.22 定義：CDH 指的是已知 $g^a, g^b$，求解 $g^{ab}$。這正是被動竊聽者欲攻破 DH 共享秘密所面臨的直接數學難題。",
    "trap": "CDH 要求的是算出 $g^{ab}$，不要求解出 $a$ 或 $b$。"
  },
  {
    "id": "q56",
    "topic": "CDH 與 DLP 的歸約關係",
    "difficulty": "中等",
    "question": "投影片 1.7 P.23 闡明：「DLP is at least as hard as CDH」（$\\text{CDH} \\le \\text{DLP}$），其嚴格推導理由為何？",
    "options": [
      "A. 因為解出 CDH 就能自動解出 DLP",
      "B. 若存在一演算法能解 DLP，則給定 $g^a, g^b$，可先用 DLP 解出私鑰 $a$，再直接計算 $(g^b)^a = g^{ab}$ 破解 CDH",
      "C. 因為 CDH 的金鑰長度比 DLP 長",
      "D. 這是未經證明的經驗假設"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.23 證明：If you can solve DLP, then you can solve CDH. 給定 $(g^a, g^b)$，先對 $g^a$ 調用 DLP 求解器得出 $a$，再進行一次模冪 $(g^b)^a = g^{ab}$ 即解出 CDH。故 CDH 不會比 DLP 難。",
    "trap": "反過來「能否由 CDH 求解器解出 DLP」目前仍是密碼學未解的公開難題（Open Question）。"
  },
  {
    "id": "q57",
    "topic": "判定型 DH (DDH) 問題",
    "difficulty": "基礎",
    "question": "判定型 Diffie-Hellman 問題（Decisional Diffie-Hellman Problem, DDH）的目標為何？",
    "options": [
      "A. 計算出 $g^{ab}$ 的精確數值",
      "B. 給定 $g^a, g^b$ 以及候選值 $X$，判定 $X$ 究竟是真正的共享秘密 $g^{ab}$，還是獨立隨機選取的群元素 $g^c$",
      "C. 判定質數 $p$ 是否為安全質數",
      "D. 計算生成元 $g$ 的階數"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.24 定義：DDH 是一個區分（Distinguishing）問題，要求區分真正的 DH 秘密與隨機群元素。這是公鑰加密語意不可區分性證明（如 ElGamal）不可或缺的前提假設。",
    "trap": "DDH 是「判定題（Yes/No）」，CDH 是「計算題（求出數值）」。"
  },
  {
    "id": "q58",
    "topic": "難度層級歸約鏈",
    "difficulty": "基礎",
    "question": "依據投影片 1.7 P.25，DLP、CDH、DDH 三大問題的計算難度層級（Hardness Hierarchy）排序為何？",
    "options": [
      "A. $\\text{DLP} \\le \\text{CDH} \\le \\text{DDH}$",
      "B. $\\text{DDH} \\le \\text{CDH} \\le \\text{DLP}$（DDH 不會比 CDH 難，CDH 不會比 DLP 難）",
      "C. $\\text{CDH} \\le \\text{DLP} \\le \\text{DDH}$",
      "D. 三者難度完全等價"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.25 權威結論：Hardness hierarchy: $\\mathbf{\\text{DDH} \\le \\text{CDH} \\le \\text{DLP}}$。能解 DLP 必能解 CDH；能解 CDH 必能解 DDH。",
    "trap": "符號 $\\le$ 代表難度「不高於」。DDH 最容易解，DLP 最難解。"
  },
  {
    "id": "q59",
    "topic": "安全性假設強弱比較",
    "difficulty": "中等",
    "question": "在形式化安全證明中，若將方案安全性建立在「DDH 假設是成立的」，相較於建立在「DLP 假設是成立的」，兩者的假設強度關係為何？",
    "options": [
      "A. DDH 假設更弱，因為 DDH 更難被攻破",
      "B. DDH 假設更強（Stronger Assumption），因為 DDH 是三者中最容易被攻破的假設，其成立的前提更嚴苛",
      "C. 兩者假設強度完全相同",
      "D. DLP 是最強的假設"
    ],
    "answer": 1,
    "explanation": "密碼學經典邏輯：假設某問題是困難的，該問題越容易被攻破，這個「困難假設」就越強（越脆弱）。因為 $\\text{DDH} \\le \\text{CDH} \\le \\text{DLP}$，若 DLP 被破解則全毀；但某些群中 DDH 已經被攻破了 CDH 和 DLP 依然完好，因此 DDH 是最強、最脆弱的假設。",
    "trap": "「問題較容易」代表「假設其困難是較強的假設（較冒險）」。"
  },
  {
    "id": "q60",
    "topic": "勒讓德符號攻破 DDH",
    "difficulty": "進階",
    "question": "投影片 1.7 P.25 指出，在全模群 $\\mathbb{Z}_p^*$ 中，為什麼 DDH 假設「不成立」（即攻擊者能輕易區分 $g^{ab}$ 與隨機 $g^c$）？",
    "options": [
      "A. 因為生成元 $g$ 必定是偶數",
      "B. 藉由勒讓德符號（二次剩餘性）：$g^{ab}$ 為平方數（二次剩餘）當且僅當 $g^a$ 或 $g^b$ 至少有一個是平方數；但隨機元素 $g^c$ 為平方數的機率僅嚴格為 $1/2$",
      "C. 因為 $g^{ab}$ 永遠大於 $g^c$",
      "D. 因為 $\\mathbb{Z}_p^*$ 中的所有元素都是完全平方數"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.25 原文說明：In $\\mathbb{Z}_p^*$, DDH can be broken using the Legendre symbol (quadratic residuosity): $g^{ab}$ is a square exactly when $g^a$ or $g^b$ is, while a random $g^c$ is a square only half the time. 攻擊者藉此獲得顯著的區分優勢（Advantage = 1/2）。",
    "trap": "勒讓德符號在多項式時間內可由尤拉準則 $a^{(p-1)/2} \\pmod p$ 算出，不需要求解離散對數！"
  },
  {
    "id": "q61",
    "topic": "質數階子群解決 DDH",
    "difficulty": "進階",
    "question": "承上題，為了在工程實作中消除勒讓德符號漏洞，使 DDH 困難假設得以成立，現代密碼學採取的標準解決方案為何？",
    "options": [
      "A. 改用更長的 4096 位元質數",
      "B. 將運算限制在「大質數階子群（Subgroup of Prime Order $q$）」中（例如安全質數 $p = 2q+1$ 的階 $q$ 子群，或質數階橢圓曲線）",
      "C. 對公鑰先進行 MD5 雜湊",
      "D. 禁止 Bob 選取奇數作為私鑰"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.25 結論：Work in a group of large prime order $q$, where this leak disappears: the order-$q$ subgroup of $\\mathbb{Z}_p^*$ for $p = 2q + 1$ (Schnorr group), or a prime-order elliptic curve. 在質數階群中所有非單位元素皆為生成元，二次剩餘洩漏徹底消除。",
    "trap": "不是加大質數，而是選取特定質數階子群結構。"
  },
  {
    "id": "q62",
    "topic": "DDH 在密碼協定中的必要性",
    "difficulty": "中等",
    "question": "為什麼公鑰加密方案（如 ElGamal）的安全性證明必須依賴 DDH 假設，而不能僅依賴 CDH 假設？",
    "options": [
      "A. 因為 CDH 演算法計算太快",
      "B. 因為若只滿足 CDH，攻擊者雖然無法算出完整的 $g^{ab}$，但可能能夠有效推測出 $g^{ab}$ 的部分位元（例如前 32 位元），這已足以破壞語意不可區分性（IND-CPA）",
      "C. 因為 DDH 才能產生對稱金鑰",
      "D. 這是 NIST 為了增加推導複雜度的要求"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.24 強調：What if an attacker can compute the first 32 bits of $g^{ab}$? CDH isn't broken, but the attacker learns something! DDH 保證整個秘密在統計上不可區分於真隨機，才能確保加密方案的語意安全性。",
    "trap": "CDH 只保證「無法完全求出」，DDH 才能保證「連 1 bit 的資訊都未洩漏」。"
  },
  {
    "id": "q63",
    "topic": "KDF 白化法則",
    "difficulty": "基礎",
    "question": "投影片 1.7 P.29 提出了工程上的重要經驗法則（Rule of thumb）：「Never feed a shared secret straight into a cipher; always pass it through a KDF first。」其原因為何？",
    "options": [
      "A. 避免密鑰被壓縮得太短",
      "B. 共享秘密 $S = g^{ab} \\bmod p$ 是具備特定代數分佈偏誤的群元素，且位元組長度會浮動（前導零造成時序洩漏），必須經由 KDF「白化」才能產出均勻偽隨機的對稱金鑰",
      "C. KDF 可以自動抵抗量子電腦 Shor 演算法",
      "D. 因為 AES 演算法不支援質數作為輸入"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.29-31 說明：$S$ 不是均勻隨機位元串，直接拿來當 AES 金鑰會讓攻擊者佔有先機；且前導零位元組處理時差曾導致 2020 年著名的 Raccoon 攻擊。KDF（如 HKDF）負責提取偏誤並展開為標準金鑰。",
    "trap": "Raccoon 攻擊是直接使用 $g^{ab}$ 導致時序側信道的經典歷史教訓。"
  },
  {
    "id": "q64",
    "topic": "HKDF 兩階段運作",
    "difficulty": "中等",
    "question": "在現代標準 HKDF（RFC 5869）中，Extract 階段與 Expand 階段的功能劃分何者正確？",
    "options": [
      "A. Extract 負責解密；Expand 負責加密",
      "B. Extract 利用 HMAC(salt, $S$) 提取出固定長度的偽隨機主金鑰 PRK；Expand 則根據情境標籤（info）將 PRK 擴展衍生為多把獨立的通訊金鑰（$K_{\\text{enc}}, K_{\\text{mac}}, IV$）",
      "C. Extract 負責產生公鑰；Expand 負責產生私鑰",
      "D. Extract 用於非對稱密碼；Expand 用於對稱密碼"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.31 圖解：\n1. Extract: PRK = HMAC(salt, $S$)\n2. Expand: (info, length) $\\to K_{\\text{enc}}, K_{\\text{mac}}, IV$。使單一共享秘密能安全派生多把獨立金鑰。",
    "trap": "Extract 消除偏誤固定長度，Expand 依情境拉伸產生多把金鑰。"
  },
  {
    "id": "q65",
    "topic": "未認證 DH 的中間人攻擊 (MITM)",
    "difficulty": "基礎",
    "question": "在未具備身分認證機制的 Diffie-Hellman 協定中，中間人 Mallory 發動 MITM 攻擊後，通訊各方最終持有的金鑰狀態為何？",
    "options": [
      "A. Alice、Bob 與 Mallory 三方共享同一把金鑰 $g^{abm}$",
      "B. Alice 與 Mallory 共享 $g^{am}$；Bob 與 Mallory 共享 $g^{bm}$；Alice 與 Bob 之間根本沒有共享任何秘密金鑰",
      "C. Alice 與 Bob 仍正常建立 $g^{ab}$，Mallory 只能旁觀",
      "D. 雙方通訊立即中斷並拋出憑證無效警告"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.36 攻擊步驟：Mallory 分別攔截雙方公鑰並換上自己的公鑰 $g^m$。結果 Alice 協商出 $g^{am}$，Bob 協商出 $g^{bm}$。Mallory 充當雙向代理人，解密讀取篡改後再重新加密轉發，通訊雙方渾然不知。",
    "trap": "基礎 DH 只能抵禦被動竊聽（Passive Eavesdropping），對主動中間人（Active MITM）毫無還手之力。"
  },
  {
    "id": "q66",
    "topic": "MITM 成功的根本原因",
    "difficulty": "基礎",
    "question": "為什麼未經認證的 Diffie-Hellman 容易受到中間人攻擊？其最本質的缺陷是什麼？",
    "options": [
      "A. 公開參數 $p$ 太小容易被因數分解",
      "B. DH 公鑰 $g^a$ 在數學上看似均勻隨機的群元素，協定本身缺乏「身分綁定（Identity Verification）」機制，接收方無法確認公鑰究竟來自合法對象還是攻擊者",
      "C. 網際網路路由器不支援 Diffie-Hellman 封包",
      "D. 攻擊者破解了離散對數問題"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.37 總結：Public values look random. No identity verification! Like agreeing on a secret handshake with someone wearing a mask. 協定只證明建立了秘密，沒證明與誰建立。",
    "trap": "密碼學名言：與戴著面具的人握手，即使握手動作再秘密，你也無法確認對方是誰。"
  },
  {
    "id": "q67",
    "topic": "認證金鑰交換 (AKE) 防禦機制",
    "difficulty": "中等",
    "question": "在 HTTPS / TLS 協定中，伺服器如何防止中間人發動 Diffie-Hellman 的 MITM 攻擊？",
    "options": [
      "A. 要求客戶端輸入伺服器的管理員密碼",
      "B. 伺服器在發送 DH 公鑰參數 $g^b$ 時，附帶由權威憑證機構（CA）簽署的數位憑證，並使用伺服器的私鑰對該 DH 參數進行數位簽章",
      "C. 強制使用有線網路通訊",
      "D. 使用長度超過 10000 位的質數"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.39 流程：Server sends its certificate and a signature on $g^b$。CA 憑證將伺服器私鑰綁定至網域名稱（如 gmail.com），私鑰簽章將該次會話的 $g^b$ 綁定至該金鑰，中間人無法偽造合法簽名。",
    "trap": "憑證保證了身分歸屬，數位簽章保證了當次 DH 公鑰的防篡改。"
  },
  {
    "id": "q68",
    "topic": "Signal 與 WhatsApp 認證機制",
    "difficulty": "中等",
    "question": "針對點對點即時通訊中缺乏集中式 CA 憑證的問題，Signal 與 WhatsApp 分別採用了何種機制來防禦 MITM 攻擊？",
    "options": [
      "A. Signal 使用 60 位數字安全碼指紋進行帶外手動比對；WhatsApp（2023）引入了「金鑰透明度（Key Transparency）」透過可審計公鑰目錄自動驗證",
      "B. 兩者都強制使用者必須親自到門市核驗身分證件",
      "C. 兩者完全不防範中間人攻擊",
      "D. 使用明文發送金鑰以確保透明"
    ],
    "answer": 0,
    "explanation": "投影片 1.7 P.40-41 介紹：Signal 使用 Safety Numbers（兩方長期身分金鑰雜湊出的 60 位數指紋）；WhatsApp 在 2023 年引入基於可審計追加字典（AKD）的 Key Transparency，避免百人群組需做 4,950 次手動比對的拓展難題。",
    "trap": "金鑰透明度（Key Transparency）是近年解決大規模公開金鑰身分驗證的革命性技術。"
  },
  {
    "id": "q69",
    "topic": "SSH 首次信任模型 (TOFU)",
    "difficulty": "基礎",
    "question": "SSH 協定採用「首次使用信任（Trust On First Use, TOFU）」模型防範伺服器假冒，其主要安全脆弱點為何？",
    "options": [
      "A. 一旦連線成功後金鑰就會失效",
      "B. 在「第一次連線」到該伺服器時，若攻擊者在此時發動中間人攻擊，客戶端無法檢驗真偽，極易將攻擊者的公鑰當作合法主機金鑰寫入 `known_hosts`",
      "C. 它不支援使用密碼登入",
      "D. 只能在 Unix 系統運行"
    ],
    "answer": 1,
    "explanation": "投影片 1.7 P.42 指出：Weakness: TOFU is vulnerable on the very first connection! 首次連線時使用者通常直接略過 SHA-256 指紋驗證按下 Yes，使中間人有機可乘。",
    "trap": "TOFU 只有在第二次及後續連線才能檢測出金鑰變動，初次建立連線是其防線空窗期。"
  },
  {
    "id": "q70",
    "topic": "RSA 歷史先鋒與退役原因",
    "difficulty": "中等",
    "question": "投影片 1.7 P.44-48 總結了 RSA 演算法的核心機制與現代密碼學界（如 Trail of Bits 2019 年呼籲「Seriously, stop using RSA」）主張淘汰 RSA 的原因。下列敘述何者錯誤？",
    "options": [
      "A. RSA 基於大質數分解問題，是歷史上第一個同時具備加密與數位簽章雙重功能的演算法",
      "B. 4096 位元的 RSA 簽章耗時約 10 毫秒，而現代 Ed25519 簽章僅需約 0.1 毫秒（快 100 倍）",
      "C. 教科書 RSA 具延展性且為確定性，其 PKCS#1 v1.5 填充極易遭受 Bleichenbacher Oracle 攻擊（如 2018 年 ROBOT 漏洞）",
      "D. RSA 可以直接無縫遷移到橢圓曲線群上以縮小金鑰尺寸，因此未來仍將是後量子密碼的主流標準"
    ],
    "answer": 3,
    "explanation": "投影片 1.7 P.48 明確指出：Its math doesn't travel — DH moves to elliptic curves unchanged; RSA's trapdoor is tied to factoring, where the number field sieve keeps pushing key sizes up. RSA 的陷門單向函數牢牢綁定於質因數分解，根本無法移植到橢圓曲線！且在量子電腦 Shor 演算法下將被徹底破解，絕非後量子標準。故 D 選項敘述錯誤。",
    "trap": "Diffie-Hellman 可自然過渡為 ECDH，但 RSA 根本無法移到橢圓曲線。"
  },
  {
    "id": "q71",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "基礎",
    "question": "在相同的 128 位元安全強度（128-bit security）下，橢圓曲線密碼學（ECC）與傳統 RSA / 有限體 Diffie-Hellman 的金鑰長度比較，下列何者正確？",
    "options": [
      "A. 256-bit ECC 金鑰約等同於 3,072-bit RSA 金鑰或 3,072-bit 有限體 DH 金鑰",
      "B. 256-bit ECC 金鑰僅等同於 256-bit RSA 金鑰",
      "C. ECC 金鑰長度必須是安全強度的 10 倍，因此 128-bit 安全需要 1,280-bit ECC 金鑰",
      "D. 隨著安全等級從 128-bit 提升到 256-bit，ECC 金鑰長度會暴增 5 倍，而 RSA 只增加 2 倍"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.3-4 指出：256-bit ECC 金鑰約等同於 3,072-bit RSA 與 3,072-bit 有限體 DH。橢圓曲線金鑰長度只需安全等級的 2 倍（128-bit 安全需 256-bit；256-bit 安全需 512-bit），而 RSA 從 128-bit 升到 256-bit 安全需從 3,072-bit 暴增 5 倍至 15,360-bit。",
    "trap": "記住黃金比例：ECC 金鑰長度 ≈ 2 × 安全位元數（例如 256-bit ECC 提供 128-bit 安全）。"
  },
  {
    "id": "q72",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "中等",
    "question": "為什麼傳統有限體 Diffie-Hellman（在 $\\mathbb{Z}_p^*$ 上）需要 2,048 到 3,072 位元的大質數，而橢圓曲線 ECDH 只需要 256 位元就能達到同等安全？",
    "options": [
      "A. 因為橢圓曲線上的點加法完全無法用電腦計算，所以攻擊者無法進行任何嘗試",
      "B. 因為 $\\mathbb{Z}_p^*$ 的元素是整數，可分解成小質數而遭受次指數級的「指標微積分（Index Calculus）」攻擊；但橢圓曲線上的點沒有「小質數點」的分解結構，目前對良好曲線只存在 $\\mathcal{O}(\\sqrt{n})$ 的通用攻擊",
      "C. 因為橢圓曲線可以免疫量子電腦的 Shor 演算法",
      "D. 因為 Pollard's rho 演算法無法在橢圓曲線群上執行"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.6 說明：Baby-step giant-step 與 Pollard's rho 屬於通用群攻擊，複雜度為 $\\mathcal{O}(\\sqrt{n})$，對兩者都適用。但 $\\mathbb{Z}_p^*$ 額外受到次指數級的 Index Calculus（指標微積分）威脅，因為整數可分解為小質數。橢圓曲線上的點無法做質因數分解，沒有 Index Calculus，因此 256-bit 曲線就能提供 $\\sqrt{2^{256}} = 2^{128}$ 的安全強度。",
    "trap": "Pollard's rho 在 ECC 上依然有效（所以 256-bit 只有 128-bit 安全）；真正被擋掉的是 Index Calculus，且 ECC 依然會被量子 Shor 演算法破解。"
  },
  {
    "id": "q73",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "基礎",
    "question": "密碼學中常用的 Weierstrass 標準型橢圓曲線方程式為 $y^2 = x^3 + ax + b$，為何必須加上附加條件 $4a^3 + 27b^2 \\neq 0$？",
    "options": [
      "A. 為了讓曲線變成一個標準的幾何橢圓形",
      "B. 為了排除曲線出現尖點（cusps）或自相交（self-intersections）等奇異點，確保切線與點加法定義良好",
      "C. 為了保證 $a$ 和 $b$ 都是質數",
      "D. 為了防止曲線在有限體 $\\mathbb{F}_p$ 上有任何點"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.9 指出：條件 $4a^3 + 27b^2 \\neq 0$（判別式非零）用於排除尖點（cusps）與自相交（self-intersections），讓曲線光滑無奇異點，才能定義合法的群加法結構。此外，橢圓曲線並不是橢圓形，名稱源於歷史上計算橢圓弧長的問題。",
    "trap": "別被名字騙了：Elliptic Curves（橢圓曲線）並不是幾何上的橢圓（Ellipses）。"
  },
  {
    "id": "q74",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "基礎",
    "question": "在實數平面上，如何以幾何方式計算橢圓曲線上兩個相異點 $P$ 與 $Q$ 的相加結果 $P + Q$？",
    "options": [
      "A. 直接將兩點的座標相加，即 $(x_P + x_Q, y_P + y_Q)$",
      "B. 畫一條通過 $P$ 與 $Q$ 的直線，找到它與曲線的第三個交點，再將該交點沿著 $x$ 軸鏡射（翻轉 $y$ 座標正負號）即得 $P + Q$",
      "C. 畫一條通過 $P$ 與 $Q$ 的直線，該直線與曲線的第三個交點就是 $P + Q$，不需翻轉",
      "D. 以 $P$ 與 $Q$ 的中點作為 $P + Q$"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.11 說明：畫過 $P$ 與 $Q$ 的割線，找到與曲線的第三個交點後，必須「沿 $x$ 軸鏡射（Reflect across the $x$-axis）」。這個鏡射步驟讓「同一直線上的三個曲線點相加為零」成立，進而使橢圓曲線滿足群的公理。",
    "trap": "初學者最容易忘記最後一步「沿 $x$ 軸鏡射」！沒有鏡射就不滿足結合律與反元素定義。"
  },
  {
    "id": "q75",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "基礎",
    "question": "在橢圓曲線上計算「倍點（Point Doubling）」$2P = P + P$ 時，因為只有單一點 $P$ 無法畫兩點割線，幾何上應如何操作？",
    "options": [
      "A. 改畫一條通過 $P$ 點且與曲線「相切」的切線，找到它與曲線的另一個交點，再沿 $x$ 軸鏡射",
      "B. 畫一條垂直於 $x$ 軸的直線通過 $P$ 點",
      "C. 直接將 $P$ 點的座標乘以 2",
      "D. 無法計算 $P + P$，結果一律定義為無窮遠點 $\\mathcal{O}$"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.12 說明：計算 $2P$ 時，畫出曲線在 $P$ 點的切線（tangent line），找出該切線與曲線的另一個交點，最後再沿 $x$ 軸鏡射即為 $2P$。在代數公式中（P.13），其斜率由隱函數微分得出 $\\lambda = (3x_P^2 + a)/(2y_P)$。",
    "trap": "只有在 $y_P = 0$（切線為鉛直線）時，$2P$ 才會是無窮遠點 $\\mathcal{O}$。"
  },
  {
    "id": "q76",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "中等",
    "question": "觀察投影片 1.8 P.13 在有限體 $\\mathbb{F}_p$ 上的 Weierstrass 點加法與倍點公式，下列哪一個曲線參數「完全沒有出現在公式中」，並因此在實務上成為「無效曲線攻擊（Invalid Curve Attack）」的破口？",
    "options": [
      "A. 質數模數 $p$",
      "B. 一次項係數 $a$",
      "C. 常數項係數 $b$",
      "D. 點的座標 $x_P$ 與 $y_P$"
    ],
    "answer": 2,
    "explanation": "投影片 1.8 P.13 特別提醒：加法公式 $\\lambda = (y_Q-y_P)/(x_Q-x_P)$ 與倍點公式 $\\lambda = (3x_P^2+a)/(2y_P)$ 中，出現了 $a$，但「完全沒有出現 $b$」！因此如果程式沒檢查收到的點是否真的滿足原本的 $b$，同樣的程式碼會在任意其他曲線 $y^2 = x^3 + ax + b'$ 上照常運作。",
    "trap": "倍點公式有 $a$ 但沒有 $b$；加法公式連 $a$ 和 $b$ 都沒有。這是後面無效曲線攻擊的根本原因！"
  },
  {
    "id": "q77",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "基礎",
    "question": "在橢圓曲線密碼學中，若私鑰 $k$ 為 256 位元的整數，如何快速計算純量乘法（Scalar Multiplication）$k \\cdot G$？以 $k = 13 = (1101)_2$ 為例，演算法會如何運作？",
    "options": [
      "A. 將 $G$ 連續相加 $k$ 次，對 256-bit 的 $k$ 約需 $2^{256}$ 次加法",
      "B. 使用「倍增與加法（Double-and-Add）」演算法，將 $k$ 寫成二進位，對 256-bit 的 $k$ 最多只需約 255 次倍點與 255 次加法",
      "C. 直接將 $k$ 乘以 $G$ 的 $x$ 座標再取模 $p$",
      "D. 使用快速傅立葉轉換（FFT）"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.14 展示：若直接連加 $k$ 次會需要約 $2^{256}$ 次運算完全不可行。使用 Double-and-Add，把 $k=13=1101_2$ 拆解為 $G \\xrightarrow{\\text{double}} 2G \\xrightarrow{+G} 3G \\xrightarrow{\\text{double}} 6G \\xrightarrow{\\text{double}} 12G \\xrightarrow{+G} 13G$。對 256-bit 的 $k$ 只需數百次點運算（微秒等級），這就是正向容易、逆向困難的計算非對稱性。",
    "trap": "Double-and-Add 的核心概念跟傳統 DH 的 Square-and-Multiply（快速冪）完全一樣，只是乘法變加法、平方變倍點。"
  },
  {
    "id": "q78",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "基礎",
    "question": "在橢圓曲線的群結構（Group Structure）中，單位元素（Identity Element）與點 $P = (x_P, y_P)$ 的反元素（Inverse）分別為何？",
    "options": [
      "A. 單位元素為原點 $(0, 0)$；反元素為 $(-x_P, -y_P)$",
      "B. 單位元素為 $(1, 1)$；反元素為 $(1/x_P, 1/y_P)$",
      "C. 單位元素為「無窮遠點 $\\mathcal{O}$」（滿足 $P + \\mathcal{O} = P$）；反元素為 $-P = (x_P, -y_P)$（滿足 $P + (-P) = \\mathcal{O}$）",
      "D. 橢圓曲線沒有單位元素與反元素"
    ],
    "answer": 2,
    "explanation": "投影片 1.8 P.16 定義：單位元素是無窮遠點 $\\mathcal{O}$（Point at infinity），任何點加上 $\\mathcal{O}$ 維持不變；點 $P=(x_P, y_P)$ 的反元素是它沿 $x$ 軸對稱的點 $-P=(x_P, -y_P)$，兩者連線為鉛直線，不會再與曲線交於第三點，因此定義 $P + (-P) = \\mathcal{O}$。",
    "trap": "注意反元素是 $(x_P, -y_P)$（只翻轉 $y$ 座標），不是 $(-x_P, -y_P)$！且 $(0,0)$ 不一定是單位元素。"
  },
  {
    "id": "q79",
    "topic": "橢圓曲線基礎與 ECDLP",
    "difficulty": "基礎",
    "question": "關於「橢圓曲線離散對數問題（ECDLP）」的定義，下列敘述何者正確？",
    "options": [
      "A. 給定曲線參數 $a, b$ 與質數 $p$，將 $p$ 分解成兩個質數的乘積",
      "B. 給定橢圓曲線、基點 $G$ 以及曲線上另一點 $H = k \\cdot G$，找出整數純量 $k$",
      "C. 給定整數 $k$ 與基點 $G$，計算出 $H = k \\cdot G$",
      "D. 給定兩個點 $P$ 與 $Q$，計算 $P + Q$"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.18 明確對照：傳統 DLP 是給定 $g, h$ 找 $x$ 滿足 $g^x \\equiv h \\pmod p$；ECDLP 則是給定曲線、基點 $G$ 與目標點 $H$，找出整數 $k$ 滿足 $k \\cdot G = H$。正向算 $k \\cdot G$ 只需幾百次點運算，逆向從 $H$ 找 $k$ 在 256-bit 曲線上最佳古典演算法（Pollard's rho）需約 $2^{128}$ 步。",
    "trap": "別把正向計算（給 $k, G$ 算 $k \\cdot G$，很簡單）與逆向問題（給 $G, H$ 找 $k$，極困難）搞反。"
  },
  {
    "id": "q80",
    "topic": "ECDLP 手算與 ECDH",
    "difficulty": "進階",
    "question": "【課堂手算原題】在投影片 1.8 P.19 的玩具橢圓曲線 $E: y^2 = x^3 + 2x + 2$ over $\\mathbb{F}_{17}$ 上，已知基點 $G = (5, 1)$。利用倍點公式計算 $2G$ 時，第一步的斜率 $\\lambda$ 與最終點 $2G$ 分別為何？（提示：$2^{-1} \\equiv 9 \\pmod{17}$）",
    "options": [
      "A. $\\lambda \\equiv 13 \\pmod{17}$，$2G = (6, 3)$",
      "B. $\\lambda \\equiv 9 \\pmod{17}$，$2G = (10, 6)$",
      "C. $\\lambda \\equiv 4 \\pmod{17}$，$2G = (5, 16)$",
      "D. $\\lambda \\equiv 13 \\pmod{17}$，$2G = (6, 14)$"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.19 完整手算過程：這裡 $a=2, p=17, x_P=5, y_P=1$。斜率 $\\lambda = (3x_P^2 + a)/(2y_P) = (3 \\cdot 25 + 2)/2 = 77/2 \\equiv 9/2 \\equiv 9 \\cdot 9 = 81 \\equiv 13 \\pmod{17}$。接著 $x_R = \\lambda^2 - 2x_P = 169 - 10 = 159 \\equiv 6 \\pmod{17}$；$y_R = \\lambda(x_P - x_R) - y_P = 13(5 - 6) - 1 = -14 \\equiv 3 \\pmod{17}$。故 $2G = (6, 3)$。",
    "trap": "驗算技巧：把 $(6, 3)$ 代回方程式左邊 $3^2 = 9$，右邊 $6^3 + 2(6) + 2 = 230 = 17 \\times 13 + 9 \\equiv 9 \\pmod{17}$，左右相等即可秒確認沒算錯！"
  },
  {
    "id": "q81",
    "topic": "ECDLP 手算與 ECDH",
    "difficulty": "中等",
    "question": "在橢圓曲線領域參數（Domain Parameters）$(p, a, b, G, n, h)$ 中，Hasse 定理（Hasse's Theorem）與輔因子（Cofactor）$h$ 的意義分別為何？",
    "options": [
      "A. 曲線上總點數 $\\#E$ 必定嚴格等於 $p$，而 $h = p - n$",
      "B. Hasse 定理指出曲線上總點數滿足 $\\#E = p + 1 \\pm 2\\sqrt{p}$（接近 $p$），而輔因子 $h = \\#E / n$（總點數除以基點 $G$ 的階數 $n$）",
      "C. 曲線上總點數為 $p^2$，而 $h$ 是私鑰長度",
      "D. Hasse 定理用來計算雙線性配對，與點數無關"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.19 與 P.51 指出：Hasse's theorem 保證有限體 $\\mathbb{F}_p$ 上的曲線點數 $\\#E$ 落在 $p + 1 \\pm 2\\sqrt{p}$ 範圍內（例如 $p=17$ 時 $18 \\pm 8.2$，實際為 $19$ 個點）。領域參數 $(p, a, b, G, n, h)$ 分別代表質數、係數 $a, b$、基點 $G$、基點階數 $n$、以及輔因子 $h = \\#E / n$。",
    "trap": "記住輔因子公式 $h = \\#E / n$：當曲線總點數本身就是質數時（如 NIST P-256），$h = 1$；而 Curve25519 的 $h = 8$。"
  },
  {
    "id": "q82",
    "topic": "ECDLP 手算與 ECDH",
    "difficulty": "基礎",
    "question": "在橢圓曲線 Diffie-Hellman（ECDH）金鑰交換協定中，Alice 選取私密整數 $a$，Bob 選取私密整數 $b$，雙方公開傳輸的數值與最終算出的共享秘密分別為何？",
    "options": [
      "A. Alice 傳送 $g^a \\bmod p$，Bob 傳送 $g^b \\bmod p$，共享秘密為 $g^{ab} \\bmod p$",
      "B. Alice 傳送曲線點 $A = a \\cdot G$，Bob 傳送曲線點 $B = b \\cdot G$，雙方各自計算 $a \\cdot B = b \\cdot A = ab \\cdot G$",
      "C. Alice 傳送私鑰 $a$，Bob 傳送私鑰 $b$，雙方相加得 $a + b$",
      "D. Alice 傳送 $a + G$，Bob 傳送 $b + G$，共享秘密為 $(a+b) + G$"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.20-21 展示 ECDH 對應關係：傳統 DH 的指數運算 $g^x$ 對應到純量乘法 $x \\cdot G$；生成元 $g$ 對應到基點 $G$。Alice 算 $A = a \\cdot G$、Bob 算 $B = b \\cdot G$ 並互換後，Alice 算 $a \\cdot B = ab \\cdot G$，Bob 算 $b \\cdot A = ab \\cdot G$，得到相同共享點 $K = ab \\cdot G$。",
    "trap": "竊聽者 Eve 看到 $G, A, B$，想從 $A = a \\cdot G$ 反推 $a$ 就是面對 ECDLP。"
  },
  {
    "id": "q83",
    "topic": "ECDLP 手算與 ECDH",
    "difficulty": "基礎",
    "question": "當 Alice 與 Bob 完成 ECDH 並共同計算出共享秘密曲線點 $K = ab \\cdot G$ 後，實務上為何「不可以」直接拿點 $K$ 的座標當作 AES 對稱加密金鑰使用？",
    "options": [
      "A. 因為曲線點 $K$ 的資料太短，不足 128 位元",
      "B. 因為 $K$ 是橢圓曲線上的點（其座標帶有代數結構、並非均勻隨機位元串），必須如同傳統 DH 一樣，將 $K$ 透過雜湊或金鑰衍生函數（如 HKDF）轉化為均勻隨機的對稱金鑰",
      "C. 因為 AES 無法加密曲線座標",
      "D. 因為點 $K$ 在網路上已經被明文廣播"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.21 明確提醒：$K$ is a curve point, not a key: as with classical DH, hash it (e.g. with HKDF) to derive symmetric keys. 橢圓曲線點的座標必須滿足曲線方程式，其位元分布不均勻，直接當對稱金鑰違反均勻隨機前提，必須經由 HKDF 白化。",
    "trap": "這跟投影片 1.7 的原則一脈相承：無論是 $g^{ab}$ 還是 $ab \\cdot G$，都不能直接當 AES 金鑰，一定要過 KDF（如 HKDF）。"
  },
  {
    "id": "q84",
    "topic": "ECDLP 手算與 ECDH",
    "difficulty": "基礎",
    "question": "現代網路協定中，ECDH（特別是 X25519）已經廣泛取代傳統有限體 DH。下列哪一項「不是」ECDH 相較於有限體 DH 的主要優勢？",
    "options": [
      "A. 在相同安全強度下，運算速度比有限體 DH 快 10 到 40 倍",
      "B. 金鑰、憑證與握手封包體積大幅縮小，更適合手機與嵌入式裝置",
      "C. 隨著安全需求拉高（如升到 256-bit 安全），效能與金鑰長度優勢差距會進一步擴大",
      "D. 能夠完全抵禦大型量子電腦的 Shor 演算法攻擊"
    ],
    "answer": 3,
    "explanation": "投影片 1.8 P.3-5 列出 ECDH 的三大優勢（效率快 10-40 倍、更小的金鑰與憑證、高安全等級下擴展性更佳），現為 TLS 1.3、SSH、Signal、WireGuard 預設。但 P.18 與 P.59 明確指出，Shor 演算法可完全破解 ECDLP，因此 ECC 無法抵抗大型量子電腦。",
    "trap": "「橢圓曲線很現代、很安全」不等於「能抗量子」！抗量子需要後量子密碼（如 ML-KEM）。"
  },
  {
    "id": "q85",
    "topic": "數位簽章與 ECDSA",
    "difficulty": "基礎",
    "question": "數位簽章（Digital Signatures）可視為公鑰版本的 MAC，但相較於對稱式的 MAC，數位簽章額外提供了一項關鍵安全屬性，請問是哪一項？原因為何？",
    "options": [
      "A. 機密性（Confidentiality），因為數位簽章會把訊息加密成亂碼",
      "B. 不可否認性（Non-repudiation），因為只有簽章者握有私鑰，第三方也能用公鑰驗證；而 MAC 雙方共用同一把對稱金鑰，無法向第三方證明是誰產生的標籤",
      "C. 運算速度比 MAC 快 1000 倍",
      "D. 簽章可以從 A 文件複製貼上到 B 文件重複使用"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.23 指出：合法數位簽章提供三大保證：真實性（Authenticity）、完整性（Integrity）、不可否認性（Non-repudiation）。MAC 無法提供不可否認性，因為通訊雙方握有相同金鑰，接收方也能自己偽造一份 MAC 標籤，因此無法向法官（第三方）舉證是對方發的。此外，數位簽章不提供機密性，且嚴格綁定單一訊息。",
    "trap": "考試極愛考「MAC vs 數位簽章的差別」：答案就是「不可否認性（Non-repudiation）」與「公鑰公開驗證」。"
  },
  {
    "id": "q86",
    "topic": "數位簽章與 ECDSA",
    "difficulty": "基礎",
    "question": "數位簽章的標準安全性目標稱為「EUF-CMA（選擇訊息攻擊下的存在性不可偽造）」，其直白意義為何？",
    "options": [
      "A. 攻擊者即使可以自由指定任意訊息並取得合法簽章，依然無法針對「任何一個未曾被簽過的新訊息」偽造出合法簽章",
      "B. 攻擊者無法看懂被簽章的訊息內容",
      "C. 同一個訊息每次簽章都必須產生完全相同的位元串",
      "D. 只要攻擊者沒拿到公鑰，就無法偽造簽章"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.24 定義：EUF-CMA（Existential Unforgeability under Chosen-Message Attack）指攻擊者即使能向簽章預言機請求對任意自選訊息簽章，仍無法對任何一個「新訊息（new message）」產出通過驗證的簽章。",
    "trap": "注意攻擊者本來就擁有公鑰！而且 EUF-CMA 甚至允許攻擊者自由挑選要簽哪些訊息來觀察（Chosen-Message）。"
  },
  {
    "id": "q87",
    "topic": "數位簽章與 ECDSA",
    "difficulty": "中等",
    "question": "在 ECDSA 簽章產生過程中（私鑰 $d$、公鑰 $P = d \\cdot G$、基點階數 $n$、訊息雜湊 $h = \\text{hash}(M)$），簽章者選出隨機數 $k \\in [1, n-1]$ 並算出 $k \\cdot G = (x, y)$ 後，簽章 $(r, s)$ 的計算公式為何？",
    "options": [
      "A. $r = x \\bmod n$，$s = \\frac{h + rd}{k} \\bmod n$",
      "B. $r = y \\bmod n$，$s = k(h + rd) \\bmod n$",
      "C. $r = x \\bmod n$，$s = r + \\text{hash}(R \\parallel A \\parallel M) \\cdot d \\bmod n$",
      "D. $r = d \\cdot h \\bmod n$，$s = k \\cdot G$"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.27 列出 ECDSA 簽章步驟：$k \\cdot G = (x, y)$，令 $r = x \\bmod n$，再計算 $s = k^{-1}(h + rd) \\bmod n = \\frac{h+rd}{k} \\bmod n$，輸出 $(r, s)$（若 $r=0$ 或 $s=0$ 需重選 $k$）。選項 C 則是 EdDSA 的公式。",
    "trap": "注意 ECDSA 需要做「模反元素 $k^{-1} \\bmod n$（除法）」，這正是它比 EdDSA 慢且實作複雜的原因之一。"
  },
  {
    "id": "q88",
    "topic": "數位簽章與 ECDSA",
    "difficulty": "中等",
    "question": "在 ECDSA 驗章過程中（收到訊息 $M$、簽章 $(r, s)$ 與公鑰 $P = d \\cdot G$），驗證者計算 $w = s^{-1} \\bmod n$、$u = h \\cdot w \\bmod n$、$v = r \\cdot w \\bmod n$，並算出驗證點 $Q = u \\cdot G + v \\cdot P$。為何最後檢查 $Q_x \\bmod n \\stackrel{?}{=} r$ 能驗證簽章真偽？",
    "options": [
      "A. 因為 $Q = uG + vP = (u + vd)G = w(h + rd)G = \\frac{h+rd}{s}G = k \\cdot G$，所以 $Q$ 的 $x$ 座標必然還原出 $r$",
      "B. 因為 $Q$ 會直接等於私鑰 $d$",
      "C. 因為 $u + v$ 永遠等於 1",
      "D. 因為 $Q$ 的 $x$ 座標會等於訊息雜湊值 $h$"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.28 推導：把 $P = d \\cdot G$ 代入得 $Q = (u + vd)G$。又因合法簽章滿足 $s = (h + rd)/k$，故 $u + vd = w(h + rd) = (h+rd)/s = k$，因此 $Q = k \\cdot G$，其 $x$ 座標模 $n$ 必然等於 $r$。驗章第一步也要先檢查 $r, s \\in [1, n-1]$。",
    "trap": "推導關鍵一步就是把 $s = (h+rd)/k$ 移項成 $(h+rd)/s = k$，立刻就能看懂為何 $Q = k \\cdot G$。"
  },
  {
    "id": "q89",
    "topic": "數位簽章與 ECDSA",
    "difficulty": "進階",
    "question": "在 ECDSA 中，若簽章者不小心對兩個不同訊息（雜湊值 $h_1 \\neq h_2$）重複使用了「同一個隨機數 $k$」，產出兩份簽章 $(r, s_1)$ 與 $(r, s_2)$（擁有相同的 $r$）。攻擊者可以如何直接算出簽章者的私鑰 $d$？",
    "options": [
      "A. 攻擊者仍然無法算出私鑰，只能偽造這兩個訊息的簽章",
      "B. 先由兩式相減解出 $k = \\frac{h_1 - h_2}{s_1 - s_2} \\bmod n$，再代回任一簽章公式解出私鑰 $d = \\frac{s_1 k - h_1}{r} \\bmod n$",
      "C. 直接把兩個簽章相加 $d = s_1 + s_2$",
      "D. 攻擊者必須暴力破解 $2^{128}$ 次才能解出 $k$"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.27 與 P.47 完整推導：相同 $r$ 代表使用了相同 $k$。因為 $s_1 = (h_1+rd)/k$ 且 $s_2 = (h_2+rd)/k$，兩式相減消去 $rd$ 得 $s_1 - s_2 = (h_1 - h_2)/k$，移項即得 $k = (h_1 - h_2)/(s_1 - s_2) \\bmod n$。拿到 $k$ 後代入 $s_1 k = h_1 + rd$，立刻解出私鑰 $d = (s_1 k - h_1)/r \\bmod n$。",
    "trap": "必考公式！只要兩張 ECDSA 簽章出現相同 $r$，國中代數解二元一次聯立方程式就能瞬間盜走私鑰！"
  },
  {
    "id": "q90",
    "topic": "數位簽章與 ECDSA",
    "difficulty": "中等",
    "question": "關於 ECDSA 的設計弱點與補救方式，下列敘述何者正確？",
    "options": [
      "A. ECDSA 簽章具備延展性（Malleability）：若 $(r, s)$ 是合法簽章，則 $(r, n - s)$ 同樣能通過驗證",
      "B. 為了避免爛隨機數產生器（RNG）毀掉 ECDSA，RFC 6979（現已納入 FIPS 186-5）提出將 $k$ 由「私鑰與訊息」決定性地推導出來",
      "C. 即使隨機數 $k$ 沒有完全重複，只要存在輕微偏差（bias，洩漏幾個位元），經過多次簽章後仍可被晶格攻擊（如 Minerva、LadderLeak）還原私鑰",
      "D. 以上皆正確"
    ],
    "answer": 3,
    "explanation": "投影片 1.8 P.32 與 P.47 完整涵蓋這三點：(1) ECDSA 具有延展性，$(r, n-s)$ 同樣有效；(2) 即使只是 $k$ 有微小偏差，Minerva (2019) 與 LadderLeak (2020) 都能用晶格攻擊還原私鑰；(3) 防範方式是用強 RNG，或依 RFC 6979（FIPS 186-5）改用決定性推導 $k$。",
    "trap": "不要以為「只要 $k$ 不重複就安全」——只要 $k$ 有偏差（例如前幾個 bit 總是 0），晶格攻擊照樣能偷出私鑰！"
  },
  {
    "id": "q91",
    "topic": "EdDSA 與 Ed25519",
    "difficulty": "基礎",
    "question": "EdDSA（代表實例為 Ed25519）是現代最受推薦的數位簽章演算法。它是基於哪一種早期簽章架構設計的？為何直到 2011 年才由 Bernstein 等人推出並普及？",
    "options": [
      "A. 基於 RSA 架構，因大質數演算法到 2011 年才發明",
      "B. 基於 1989 年的 Schnorr 簽章架構；因 Schnorr 專利直到 2008 年才過期，過期後才得以自由採用與改良",
      "C. 基於 AES-GCM 架構",
      "D. 基於 Dual_EC_DRBG 架構"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.29 說明：EdDSA 建立在 1989 年的 Schnorr 簽章之上。當年因為 Schnorr 申請了專利，迫使標準組織（NIST）轉向設計較複雜的 DSA / ECDSA。直到 2008 年專利到期，Bernstein 等人於 2011 年推出 EdDSA（Ed25519），連比特幣也在 2021 年 Taproot 升級中採用了 Schnorr 簽章。",
    "trap": "歷史冷知識常考：ECDSA 其實是當年為了繞過 Schnorr 專利的產物，專利過期後大家才回歸更簡潔安全的 Schnorr / EdDSA。"
  },
  {
    "id": "q92",
    "topic": "EdDSA 與 Ed25519",
    "difficulty": "基礎",
    "question": "EdDSA（Ed25519）如何從根本上解決 ECDSA「簽章時若隨機數產生器（RNG）故障就會洩漏私鑰」的致命問題？",
    "options": [
      "A. 要求使用者每次簽章時手動晃動滑鼠收集亂數",
      "B. 採用「決定性（Deterministic）Nonce」：先將私鑰雜湊展開成 $a \\parallel \\text{prefix}$，再以 $r = \\text{hash}(\\text{prefix} \\parallel M) \\bmod \\ell$ 決定性地算出 nonce，簽章過程完全不需要呼叫 RNG",
      "C. 規定每把私鑰一生只能簽署一次訊息",
      "D. 直接省略 nonce，讓 $r = 1$"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.30 展示 EdDSA 簽章流程：把 32-byte 私鑰 $k$ 用 SHA-512 展開為簽章純量 $a$ 與秘密前綴 $\\text{prefix}$，接著用 $r = \\text{hash}(\\text{prefix} \\parallel M) \\bmod \\ell$ 算出 nonce。因此同訊息永遠產生同簽章、不需 RNG、壞掉的 RNG 也不會洩漏私鑰。",
    "trap": "注意 EdDSA 在「產生私鑰 $k$ 時」仍需要安全亂數，是在「簽章（Signing）當下」不需要 RNG！"
  },
  {
    "id": "q93",
    "topic": "EdDSA 與 Ed25519",
    "difficulty": "中等",
    "question": "EdDSA 的簽章為 $(R, S)$（其中 $R = r \\cdot B$，$S = r + \\text{hash}(R \\parallel A \\parallel M) \\cdot a \\bmod \\ell$，公鑰 $A = a \\cdot B$）。驗證者檢查的標準方程式為何？相較於 ECDSA 有何效能優勢？",
    "options": [
      "A. 檢查 $S \\cdot B \\stackrel{?}{=} R + \\text{hash}(R \\parallel A \\parallel M) \\cdot A$；完全不需要計算昂貴的「模反元素（modular inverse）」，且支援批次驗證（batch verification）",
      "B. 檢查 $S^{-1} \\cdot B \\stackrel{?}{=} R$；需要計算兩次模反元素",
      "C. 檢查 $R \\cdot S \\stackrel{?}{=} A \\cdot B$；速度比 ECDSA 慢但更省記憶體",
      "D. 檢查 $\\text{hash}(S) \\stackrel{?}{=} \\text{hash}(M)$"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.31 推導：將 $S = r + \\text{hash}(R \\parallel A \\parallel M) \\cdot a$ 兩邊乘上基點 $B$，得 $S \\cdot B = r \\cdot B + \\text{hash}(R \\parallel A \\parallel M) \\cdot (a \\cdot B) = R + \\text{hash}(R \\parallel A \\parallel M) \\cdot A$。因為公式中沒有除法（無模反元素），速度更快且天然支援批次驗章。",
    "trap": "記住 EdDSA 驗章口訣：「無除法、無模反、可批次」。"
  },
  {
    "id": "q94",
    "topic": "EdDSA 與 Ed25519",
    "difficulty": "基礎",
    "question": "關於 Curve25519、X25519 與 Ed25519 這三個極易混淆的名稱，下列對應關係何者完全正確？",
    "options": [
      "A. 三者是三條完全不同的橢圓曲線，彼此在數學上毫無關聯",
      "B. Curve25519 是底層的 Montgomery 形式曲線，X25519 是跑在它上面的金鑰交換協定（ECDH）；edwards25519 是與它雙有理等價（同一條曲線換座標變數）的 Edwards 形式，Ed25519 是跑在上面的數位簽章協定（EdDSA）",
      "C. X25519 用於數位簽章，Ed25519 用於金鑰交換",
      "D. Curve25519 是 NIST 於 2000 年發明的曲線"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.43 畫出清楚的關係圖：Curve25519（Montgomery 形式，$y^2 = x^3 + 486662x^2 + x$）與 edwards25519（Edwards 形式，$-x^2 + y^2 = 1 + dx^2y^2$）透過變數代換雙有理等價（同一條曲線、兩種表示法）。Montgomery 適合只算 $x$ 座標的高速常數時間金鑰交換（X25519）；Edwards 擁有完整加法公式（無特例）適合安全簽章（Ed25519）。",
    "trap": "超好記口訣：X25519 的 X = Key e**X**change（金鑰交換）；Ed25519 的 Ed = **Ed**DSA（數位簽章）。"
  },
  {
    "id": "q95",
    "topic": "EdDSA 與 Ed25519",
    "difficulty": "中等",
    "question": "根據投影片 1.8 P.32 的比較，在規劃一個「全新軟體專案」且沒有特定法規或既有區塊鏈限制時，應如何選擇 ECDSA 與 Ed25519？又 Ed25519 有哪一項需要注意的弱點？",
    "options": [
      "A. 優先使用 Ed25519；需注意若在決定性簽章過程中遭遇硬體錯誤注入（fault attack），可能洩漏私鑰，且 RFC 8032 驗證規則曾有歧義",
      "B. 優先使用 ECDSA，因為 Ed25519 的簽章體積比 ECDSA 大 10 倍",
      "C. 優先使用 RSA-1024，因為最穩定",
      "D. Ed25519 已經可以直接取代比特幣的 secp256k1 交易簽章"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.32 建議：Use Ed25519 for new projects unless ECDSA is specifically required（例如比特幣、以太坊或強制要求 P-256 的 Web PKI）。Ed25519 的已知缺點包含較年輕、RFC 8032 留給驗證者選項導致歧義、以及決定性簽章若在運算時被故障注入（fault）改變結果會洩漏私鑰。",
    "trap": "別以為 Ed25519 完全沒缺點：「決定性簽章遇到 Fault Attack 會漏私鑰」以及「RFC 8032 驗證歧義」是投影片明講的兩大缺點。"
  },
  {
    "id": "q96",
    "topic": "安全曲線標準與爭議",
    "difficulty": "中等",
    "question": "投影片 1.8 P.35（參考 SafeCurves）列出「安全橢圓曲線」的四大準則，下列哪一項「不在」四大準則之內？",
    "options": [
      "A. 群階（Group Order）必須包含極大的質因數（避免 Pohlig-Hellman 攻擊）",
      "B. 完整加法公式（Complete Addition Formulas，避免 $P=Q, P=-Q, \\mathcal{O}$ 等分支特例藏匿 bug 與時序側通道）",
      "C. 扭曲安全性（Twist Security，確保無效 $x$ 座標落入的扭曲曲線也很強）與剛性（Rigidity，常數來源透明可驗證）",
      "D. 參數必須由情報機構秘密產生以確保「透過隱藏達成安全（Security through obscurity）」"
    ],
    "answer": 3,
    "explanation": "投影片 1.8 P.35 明確列出安全曲線四大標準：Group order（大質因數）、Complete addition formulas（完整加法公式）、Twist security（扭曲安全）、Rigidity（剛性，即「Nothing up my sleeve」透明可驗證的常數來源）。秘密常數正好違反 Rigidity！",
    "trap": "密碼學最忌諱秘密常數（Trust us constants）——「Nothing up my sleeve（袖子裡沒藏東西）」才是 Rigidity 的精神。"
  },
  {
    "id": "q97",
    "topic": "安全曲線標準與爭議",
    "difficulty": "中等",
    "question": "關於著名的「Dual_EC_DRBG（雙橢圓曲線偽隨機數產生器）」NSA 後門醜聞，下列敘述何者正確？",
    "options": [
      "A. 它是 NIST P-256 曲線本身被埋了數學後門，導致所有使用 P-256 的網站都被破解",
      "B. 它的後門藏在兩個未解釋來源的曲線點 $P$ 與 $Q$ 的秘密關係 $Q = d \\cdot P$ 中；握有陷門 $d$ 的人只要觀察 32 位元組輸出，猜測被截斷的 16 位元（僅 $2^{16}$ 次嘗試），就能反推內部狀態並預測所有未來亂數",
      "C. 沒有 $d$ 的人也能一眼看出 $P$ 和 $Q$ 之間存在後門",
      "D. 它比其他亂數產生器快 1,000 倍，因此才被 RSA BSAFE 設為預設"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.38-39 詳細拆解：Dual_EC_DRBG 其實比替代方案慢 1,000 倍（NSA 付了 RSA 一千萬美元設為預設）。關鍵在於「它是被動手腳的亂數產生器，而不是被動手腳的 P-256 曲線」！只要知道 $Q = d \\cdot P$，從輸出 $r_i$ 補猜前 16 bits 得 $s_i \\cdot Q$，再乘以 $d^{-1}$ 就得到 $s_i \\cdot P$ 進而算出下一狀態 $s_{i+1}$。而外人想從 $(P, Q)$ 驗證是否有 $d$ 等同於解 ECDLP，讓 NSA 擁有完美的可否認性（Plausible deniability）。",
    "trap": "高頻考點：Dual_EC_DRBG 是「後門產生器（backdoored generator）」，不是「後門曲線（backdoored curve）」！NIST P-256 本身目前無已知弱點。"
  },
  {
    "id": "q98",
    "topic": "安全曲線標準與爭議",
    "difficulty": "中等",
    "question": "投影片 1.8 P.40 提到 2026 年最新研究（Anthropic 研究人員使用 Claude）解開了困擾密碼學界 26 年的 NIST P-256 神秘種子（seed）來源之謎。研究發現該種子實際上從何而來？並帶出什麼結論？",
    "options": [
      "A. 來自 SHA-1 雜湊一句英文笑話「Give Bob and Jerry a raise」",
      "B. 其實根本不是雜湊值，而是用 Unix 時間戳作為種子跑 C 語言 `lrand48` 產生的原始輸出（透過晶格縮減 Lattice Reduction 還原）；這顯示 P-256 不太可能藏後門，但「可解釋（Explained）不等於剛性（Rigid）」，因為何選第 1842 號候選而非第 876 號仍未知",
      "C. 證明了 P-256 確實藏有 NSA 後門，必須立刻全面停用",
      "D. 來自圓周率 $\\pi$ 的小數點後前 256 位"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.40 更新了 2026 年的重大突破：過去傳說種子是雜湊一句話，但 Anthropic 團隊利用 `lrand48` 洩漏高位元狀態的特性，以 Lattice Reduction 還原出 P-256 種子源於 1997 年 8 月 16 日時間戳跑出的第 1842 號候選值。雖然排除了暗藏陷門的疑慮，但投影片強調「Explained is not the same as rigid」——像 Curve25519 這樣挑選最小合法係數（486662）的剛性曲線完全不留任何挑選空間。",
    "trap": "這題是老師 2026 年剛放進投影片的最新時事考點，極可能出題！記住關鍵字：`lrand48`、Lattice Reduction、Explained ≠ Rigid。"
  },
  {
    "id": "q99",
    "topic": "安全曲線標準與爭議",
    "difficulty": "基礎",
    "question": "根據投影片 1.8 P.44-45 的實務曲線選擇指南，下列配對或建議何者「錯誤」？",
    "options": [
      "A. 新專案首選：Curve25519（X25519 做金鑰交換、Ed25519 做簽章），透明高效且已於 2023 年獲 NIST SP 800-186 正式核准",
      "B. 政府合規與傳統憑證生態：NIST P-256 仍廣受接受且有大量經過嚴格稽核的實作",
      "C. 區塊鏈主力：secp256k1（$y^2 = x^3 + 7$）由比特幣與以太坊採用，幾乎沒有任意常數",
      "D. 應優先選用二元曲線（Binary Curves）與法國 ANSSI 曲線，因為它們最透明且具備完整加法公式"
    ],
    "answer": 3,
    "explanation": "投影片 1.8 P.45 明確列出「應避免（Avoid）」清單：ANSSI 曲線（未解釋常數、無統一加法公式）、Brainpool 曲線（雖用 $e$ 與 $\\pi$ 很透明但太慢且無完整公式）、二元曲線（Binary curves）以及任何低於 256-bit 的曲線。故 D 為錯誤敘述。",
    "trap": "注意 Brainpool 曲線雖然常數透明（來自 $e$ 和 $\\pi$），但因為運算慢且缺乏完整加法公式，仍被列在建議避免名單中。"
  },
  {
    "id": "q100",
    "topic": "ECC 實作攻擊與後量子混合",
    "difficulty": "基礎",
    "question": "2010 年震撼資安界的 Sony PlayStation 3（PS3）主機破解事件（由 fail0verflow 團隊揭露），其根本的密碼學實作錯誤為何？",
    "options": [
      "A. Sony 使用了只有 64 位元的橢圓曲線",
      "B. Sony 在對遊戲與韌體做 ECDSA 數位簽章時，每一次簽章都使用「同一個固定常數 $k$」，導致所有不同檔案的簽章都有相同 $r$，讓駭客直接反推出 Sony 根私鑰",
      "C. Sony 直接把私鑰印在主機外殼上",
      "D. Sony 沒有使用 HTTPS 傳輸韌體"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.48 案例：Sony 的 PS3 程式碼簽章對每份檔案都用了相同的 $k$（被 fail0verflow 用 xkcd 漫畫 `return 4; // chosen by fair dice roll` 嘲諷）。不同檔案簽章共享相同 $r$，讓駭客瞬間算出根私鑰，任何人都能簽出 PS3 認可的程式，且燒錄在硬體啟動鏈裡的公鑰無法輕易更換。",
    "trap": "PS3 事件是「ECDSA 重用隨機數 $k$」最經典的真實世界災難。"
  },
  {
    "id": "q101",
    "topic": "ECC 實作攻擊與後量子混合",
    "difficulty": "進階",
    "question": "關於「無效曲線攻擊（Invalid Curve Attack）」的原理與防禦，下列敘述何者正確？",
    "options": [
      "A. 攻擊者傳送一個「不在原本曲線 $E$ 上」、而是位於另一條同 $a$ 不同 $b'$ 且群階平滑（含許多小質因數）的曲線 $E'$ 上的點 $P$；受害者因未檢查曲線方程式而算出 $b \\cdot P$，讓攻擊者逐一洩漏 $b \\bmod m_i$，最後用中國剩餘定理（CRT）拼出完整私鑰 $b$",
      "B. 防禦方式是在使用收到的點 $P=(x, y)$ 前，檢查座標範圍並驗證 $y^2 \\equiv x^3 + ax + b \\pmod p$（帶入正確的 $b$），或改用只算 $x$ 座標且具扭曲安全性的 X25519",
      "C. 2015 年研究人員曾用此攻擊攻破使用 Bouncy Castle 與 Oracle Java 的 TLS-ECDH 伺服器",
      "D. 以上皆正確"
    ],
    "answer": 3,
    "explanation": "投影片 1.8 P.49-50 完整說明：因為點加法與倍點公式都沒用到 $b$，攻擊者可以自己挑一條有小階數 $m$ 的別條曲線 $E'$，相當於主動幫受害者製造 Pohlig-Hellman 攻擊環境，再用 CRT 拼出完整長期私鑰 $b$。解方極便宜：收到點先代入正確的 $b$ 驗算方程式，或直接採用 X25519。",
    "trap": "這題串聯了 1.7 的 Pohlig-Hellman 與中國剩餘定理（CRT），以及 1.8 P.13「公式不含 $b$」的伏筆！"
  },
  {
    "id": "q102",
    "topic": "ECC 實作攻擊與後量子混合",
    "difficulty": "中等",
    "question": "如何用「一句話」精準區分「無效曲線攻擊（Invalid Curve Attack）」與「小子群攻擊（Small Subgroup Attack）」的差異？",
    "options": [
      "A. 無效曲線攻擊＝點不在正確的方程式上（wrong equation）；小子群攻擊＝點在正確的曲線上，但階數太小（wrong order，例如落在輔因子 8 的子群中）",
      "B. 無效曲線攻擊只發生在 RSA；小子群攻擊只發生在 AES",
      "C. 兩者完全相同，只是不同論文取的名字不同",
      "D. 無效曲線攻擊是用來攻擊簽章；小子群攻擊是用來攻擊雜湊"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.53 給出考場滿分金句：「One line: invalid curve = wrong equation; small subgroup = wrong order.」小子群攻擊發生在輔因子 $h > 1$（如 Curve25519 的 $h=8$）的曲線上，攻擊者送出一個確實滿足方程式但階數只有 8 的點 $P$，讓受害者算出的 $s \\cdot P$ 只有 8 種可能（同時洩漏 $s \\bmod 8$）。X25519 透過將私鑰 clamping（鉗制）為 8 的倍數並拒絕全零輸出（RFC 7748）來防禦。",
    "trap": "考場看到「wrong equation」選 Invalid Curve；看到「wrong order / cofactor 8 / 只有 8 種可能」選 Small Subgroup！"
  },
  {
    "id": "q103",
    "topic": "ECC 實作攻擊與後量子混合",
    "difficulty": "中等",
    "question": "為什麼 Ed25519 實作之間會出現「同一份簽章在 A 函式庫驗過、在 B 函式庫卻被拒絕」的驗證不一致問題？在區塊鏈共識系統中這會造成什麼後果？又 Ristretto 技術解決了什麼問題？",
    "options": [
      "A. 因為 RFC 8032 同時允許無輔因子驗章（$S \\cdot B = R + hA$）與乘以輔因子 8 驗章（$8S \\cdot B = 8R + 8hA$），且未強制規範非標準編碼與小階數公鑰；在區塊鏈中會導致節點意見分歧而「分叉（Chain Fork）」（ZIP-215 透過統一規則修復）；Ristretto 則透過特殊編碼把 Curve25519 包裝成乾淨的質數階群，從底層消滅輔因子問題",
      "B. 因為不同電腦的 CPU 浮點數誤差不同",
      "C. 因為 Ed25519 沒有公開標準文件",
      "D. Ristretto 是用來把 RSA 轉換成橢圓曲線的編譯器"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.54-56 說明：RFC 8032 留給實作者選擇權（是否乘以 8、是否接受 $y \\ge p$ 或小階數公鑰），導致各函式庫在邊界案例上意見不同，對需要全網一致的區塊鏈會造成分叉（故 Zcash 制定 ZIP-215 統一規則）。而 Monero (2017) 曾因漏掉子群檢查讓同一筆錢可被花 8 次，Ristretto 透過把相差小階數點的點編碼成相同位元組，讓上層協定直接享受純質數階群 $\\ell$ 與 Curve25519 的極速。",
    "trap": "記住兩大解法：解決 Ed25519 驗章歧義＝ZIP-215；從底層消滅 Curve25519 輔因子 8 問題＝Ristretto。"
  },
  {
    "id": "q104",
    "topic": "ECC 實作攻擊與後量子混合",
    "difficulty": "中等",
    "question": "為什麼教科書寫的 `if bit == 1: R = R + G`（Double-and-Add）在實務上會導致私鑰洩漏（如 2019 年 Minerva 攻擊）？標準的防禦演算法是什麼？",
    "options": [
      "A. 因為 `if` 分支讓電腦只在私鑰位元為 1 時才做點加法，執行時間、耗電量或快取特徵會直接洩漏私鑰的每一個 bit；標準防禦是「Montgomery Ladder（蒙哥馬利階梯）」，無論位元是 0 或 1 都固定執行一次加法與一次倍點，並用常數時間算術交換取代分支",
      "B. 因為 `if` 語句在 C 語言中無法編譯",
      "C. 只要在程式最後加上隨機延遲 `sleep()` 就能徹底根治所有時序攻擊",
      "D. 改用 Python 實作即可自動達成常數時間"
    ],
    "answer": 0,
    "explanation": "投影片 1.8 P.57 詳解：教科書 Double-and-Add 只有在 bit=1 時做加法，形成明顯的時序／功耗側通道（Side Channel）。Montgomery Ladder 維護 $(R_0, R_1)$（恆滿足 $R_1 = R_0 + G$），每個 bit 不管是 0 或 1 都固定算一次加、一次倍，並用無分支的常數時間交換（constant-time swap）選取結果。實務上應使用經過稽核且通過 Project Wycheproof 邊界測試的成熟函式庫（如 libsodium、curve25519-dalek、Go `crypto/ecdh`），絕不自己手刻 ECC（P.58）。",
    "trap": "注意即使改用 Montgomery Ladder，只要 swap 沒寫成常數時間依然會漏（例如 2020 年 LadderLeak 攻破 OpenSSL）！"
  },
  {
    "id": "q105",
    "topic": "ECC 實作攻擊與後量子混合",
    "difficulty": "基礎",
    "question": "面對未來量子電腦（Shor 演算法）對所有橢圓曲線的威脅，目前主流瀏覽器已在 TLS 預設部署「後量子混合金鑰交換（X25519 + ML-KEM）」。為什麼實務界優先遷移「金鑰交換」，而不是先全面遷移「數位簽章」？",
    "options": [
      "A. 因為量子電腦只能破解金鑰交換，無法破解數位簽章",
      "B. 因為「先截獲、後解密（Harvest Now, Decrypt Later）」威脅：攻擊者今天就能錄下加密流量，等未來量子電腦問世後再解密；而數位簽章只需要在「驗證當下」無法偽造即可，事後才造出量子電腦無法回頭竄改過去已驗證的通訊",
      "C. 因為 NIST 尚未制定任何後量子數位簽章標準",
      "D. 因為混合加密會讓連線速度變快 10 倍"
    ],
    "answer": 1,
    "explanation": "投影片 1.8 P.59 精闢說明：NIST 已於 2024 年 8 月完成首波後量子標準化（FIPS 203-205：ML-KEM 金鑰交換、ML-DSA 與 SLH-DSA 數位簽章）。實務上優先部署 X25519 + ML-KEM 混合金鑰交換（只要兩半其中之一沒被攻破，會話金鑰就安全），正是為了防範「Harvest now, decrypt later（現在側錄、未來解密）」；而簽章只需在當下防偽造，急迫性低於機密性保護。",
    "trap": "期末必考大趨勢：記住三大關鍵詞——「X25519 + ML-KEM（兩半其一安全即安全）」、「Harvest now, decrypt later」、「FIPS 203-205（2024 年 8 月）」。"
  }
];
