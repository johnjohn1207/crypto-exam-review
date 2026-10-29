# -*- coding: utf-8 -*-
"""
Generate mock_exam.html: 現代密碼學期中模擬試卷（難度中等偏下，嚴格限縮至 1-5 Section 1）.
"""
import os

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="zh-TW" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>現代密碼學期中模擬試卷（難度中等偏下）| 範圍至 1-5 Section 1</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            500: '#6366f1',
                            600: '#4f46e5',
                            700: '#4338ca',
                            900: '#312e81',
                        }
                    },
                    fontFamily: {
                        mono: ['"JetBrains Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
                        sans: ['"Inter"', 'system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', '"Noto Sans TC"', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- KaTeX CSS & JS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

    <style>
        :root { --header-height: 64px; }
        .katex { font-size: 1.05em; }
        .katex-display { margin: 0.8em 0; overflow-x: auto; overflow-y: hidden; padding-bottom: 4px; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #0f172a; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-purple-500 selection:text-slate-950">

    <!-- 全域頂部導覽列 (Dynamic CSS variable: --header-height) -->
    <header id="site-header" class="bg-slate-900/95 backdrop-blur-md border-b border-slate-800 sticky top-0 z-50 transition-all duration-200">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <a href="index.html" class="flex items-center gap-2 hover:opacity-90 transition group">
                    <span class="w-2.5 h-2.5 rounded-full bg-purple-400 group-hover:scale-125 transition-transform shadow-sm shadow-purple-400/50"></span>
                    <span class="font-bold text-white tracking-wide text-sm sm:text-base">現代密碼學期中考複習平台</span>
                </a>
                <span class="hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-mono font-medium bg-purple-500/10 text-purple-300 border border-purple-500/30">
                    模擬考測驗卷
                </span>
            </div>
            
            <nav id="site-nav" class="flex items-center gap-1 sm:gap-1.5 text-xs overflow-x-auto no-scrollbar py-0.5">
                <!-- Nav dynamically synced by update_all_navs.py -->
            </nav>
        </div>
    </header>

    <!-- 專題 Hero 橫幅 -->
    <section class="bg-gradient-to-b from-purple-950/30 via-slate-900 to-slate-950 border-b border-slate-800/80 px-4 py-8">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div class="space-y-3">
                <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-purple-500/10 border border-purple-500/30 text-purple-300 text-xs font-mono">
                    <span>期中考全真模擬題本</span>
                    <span class="text-slate-600">|</span>
                    <span>難度：中等偏下（基礎送分與核心證明）</span>
                    <span class="text-slate-600">|</span>
                    <span class="text-emerald-400 font-bold">限縮至 1-5 Section 1</span>
                </div>
                <h1 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                    現代密碼學期中全真模擬試卷（中偏易）
                </h1>
                <p class="text-slate-400 text-sm max-w-3xl leading-relaxed">
                    本試卷嚴格依據<strong>作業一與練習一之題目性質</strong>命題，總分 100 分，建議作答時間 60 分鐘。難度設定為「中等偏下」，重點檢驗基礎定義直觀理解、常見反例構造、經典 birthday 計算與 3 至 4 行極簡形式證明默寫。完全剔除超出範圍之 Ch. 9（CCA、Padding Oracle、AE）。
                </p>
                <div class="flex flex-wrap items-center gap-3 pt-1">
                    <button onclick="toggleAllSolutions()" id="toggle-all-btn" class="px-3.5 py-1.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-mono text-xs transition shadow-sm">
                        展開 / 摺疊全部詳解與評分標準
                    </button>
                    <span class="text-xs text-slate-500 font-mono">作答心法：先遮住詳解自行思考，再點擊核對得分點</span>
                </div>
            </div>

            <!-- 考試基本規格 -->
            <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-2 lg:grid-cols-4 gap-2.5 shrink-0 text-center font-mono">
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">試卷滿分</div>
                    <div class="text-xl font-bold text-purple-400">100 分</div>
                </div>
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">單選觀念題</div>
                    <div class="text-xl font-bold text-cyan-400">6 題 / 30分</div>
                </div>
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">簡答分析題</div>
                    <div class="text-xl font-bold text-amber-400">3 題 / 30分</div>
                </div>
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">計算證明題</div>
                    <div class="text-xl font-bold text-emerald-400">3 題 / 40分</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 主試卷內容 -->
    <main class="max-w-7xl mx-auto px-4 py-8 space-y-12 flex-grow">

        <!-- 第一部分：單選觀念題 -->
        <section class="space-y-6">
            <div class="border-b border-slate-800 pb-3 flex items-center justify-between">
                <div>
                    <h2 class="text-xl font-bold text-white flex items-center gap-2">
                        <span>第一部分：單選基礎觀念題（共 6 題，每題 5 分，共 30 分）</span>
                    </h2>
                    <p class="text-slate-400 text-xs mt-1 font-mono">每題僅有一個最正確的選項，測驗基礎定義與核心直觀邊界</p>
                </div>
            </div>

            <div class="space-y-4">

                <!-- Q1 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">第 1 題 (5 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一第 1 題 / Ch. 1</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        在資訊理論安全中，One-Time Pad（OTP）能夠達成可證明完善保密性（Perfect Secrecy）的本質原因為何？
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-sans">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">A. 金鑰字串長度達到 256 位元以上，現代電腦難以暴力窮舉</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">B. 無論發送哪一份明文，密文在機率分佈上皆恆為獨立均勻分佈</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">C. 位元 XOR 運算具有極高的硬體執行效率與抗量子特性</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">D. 解密演算法使用了高強度的非線性置換盒（S-Box）</div>
                    </div>
                    <button onclick="toggleSolution('sol-1')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-1" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">標準答案：B</div>
                        <p class="text-slate-300 leading-relaxed">
                            <strong>解析</strong>：夏農完善保密性的定義為 $\Pr[C = c \mid M = m] = \Pr[C = c] = 2^{-n}$。密文分佈與明文內容徹底獨立。選項 A 與 C 混淆了計算複雜度與硬體速度，選項 D 為區塊密碼概念，皆非完善保密本質。
                        </p>
                    </div>
                </div>

                <!-- Q2 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">第 2 題 (5 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一第 4 題 / Ch. 4</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        在計算密碼學中，稱函數 $\mu(\lambda)$ 為「可忽略函數（Negligible Function）」的嚴格數學意涵為何？
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-sans">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">A. 該函數在多項式時間內無法被有效計算</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">B. 對於某個特定多項式 $p(\lambda)$，函數值恆小於 $1/p(\lambda)$</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">C. 當 $\lambda$ 趨近於無窮大時，函數值衰減的速度快於任何多項式的倒數</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">D. 函數在輸入為 0 時的輸出必定等於 0</div>
                    </div>
                    <button onclick="toggleSolution('sol-2')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-2" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">標準答案：C</div>
                        <p class="text-slate-300 leading-relaxed">
                            <strong>解析</strong>：定義要求對任意正整數 $c > 0$，皆存在門檻值 $N_0$，當 $\lambda > N_0$ 時恆有 $\mu(\lambda) < 1/\lambda^c$。代表其收斂至零的速度超越任何多項式倒數（典型如 $2^{-\lambda}$）。
                        </p>
                    </div>
                </div>

                <!-- Q3 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">第 3 題 (5 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一第 5, 21 題 / Ch. 4</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        根據生日悖論（Birthday Paradox），若密碼系統要求具備 128 位元的抗碰撞安全性（即攻擊者尋找碰撞需約 $2^{128}$ 次雜湊操作），則雜湊函數的輸出位元長度至少應為多少？
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-sans">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">A. 128 位元</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">B. 256 位元</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">C. 512 位元</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">D. 64 位元</div>
                    </div>
                    <button onclick="toggleSolution('sol-3')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-3" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">標準答案：B</div>
                        <p class="text-slate-300 leading-relaxed">
                            <strong>解析</strong>：在輸出為 $n$ 位元的空間中，碰撞取樣複雜度為 $q \approx 2^{n/2}$。若要求安全性達到 $2^{128}$ 次運算，則需滿足 $n/2 = 128 \implies n = 256$ 位元（這也是為何現代安全標準採用 SHA-256 而非 128 位元的 MD5）。
                        </p>
                    </div>
                </div>

                <!-- Q4 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">第 4 題 (5 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一第 8 題 / Ch. 7</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        Feistel 網路結構被廣泛應用於區塊密碼設計中，其保證「整體加解密架構恆為可逆置換（Permutation）」的根本幾何原因為何？
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-sans">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">A. 內部使用的每一輪輪函數 $F$ 本身皆必須是嚴格雙射且可逆的函數</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">B. 每輪透過交叉反饋與 XOR 自反性抵消，解密時完全無需將輪函數 $F$ 逆向計算</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">C. 迭代輪數必須嚴格達到 16 輪以上才能產生雙射置換</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">D. 金鑰排程演算法必須使用不可逆的單向雜湊函數生成子金鑰</div>
                    </div>
                    <button onclick="toggleSolution('sol-4')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-4" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">標準答案：B</div>
                        <p class="text-slate-300 leading-relaxed">
                            <strong>解析</strong>：Feistel 單輪結構為 $(L_{i+1}, R_{i+1}) = (R_i, L_i \oplus F(K_i, R_i))$。逆向運算時，由 $R_i = L_{i+1}$ 直接送入 $F$，計算 $L_i = R_{i+1} \oplus F(K_i, L_{i+1})$。利用 XOR 自反性（$A \oplus B \oplus B = A$）還原，輪函數 $F$ 本身即便完全不可逆（例如常數函數），整體結構依然為置換。
                        </p>
                    </div>
                </div>

                <!-- Q5 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">第 5 題 (5 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一第 10 題 / Ch. 6, 8</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        在現代密碼學中，所謂「PRF 黃金法則（Golden Rule of PRFs）」的核心原則為何？
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-sans">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">A. 金鑰長度必須隨查詢次數以線性比例增加</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">B. 在同一個金鑰下，絕不可傳入重複的輸入值給 PRF</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">C. 偽隨機函數的輸出長度必須嚴格大於輸入長度</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">D. 必須使用專用硬體加速器以防止旁路計時攻擊</div>
                    </div>
                    <button onclick="toggleSolution('sol-5')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-5" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">標準答案：B</div>
                        <p class="text-slate-300 leading-relaxed">
                            <strong>解析</strong>：PRF 安全性承諾的前提是「每次查詢的輸入點皆互不相同（Distinct Inputs）」。一旦輸入重複，由於函數確定性必吐出相同輸出，偽隨機性立即失效（如 CTR 模式 Nonce 重用災難）。
                        </p>
                    </div>
                </div>

                <!-- Q6 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">第 6 題 (5 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一第 11 題 / Ch. 8</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        在標準選擇明文安全模型（IND-CPA Security）中，下列何項資訊是密碼學方案「允許且不可避免洩漏」的？
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-sans">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">A. 明文的第一個位元組內容</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">B. 加密時所使用的內部秘密金鑰</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">C. 明文字串的長度 $|M|$</div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">D. 兩筆明文在同位置是否具有相同字元</div>
                    </div>
                    <button onclick="toggleSolution('sol-6')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-6" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">標準答案：C</div>
                        <p class="text-slate-300 leading-relaxed">
                            <strong>解析</strong>：在 CPA 博弈規則中，攻擊者提交的兩筆挑戰明文被強制規定長度必須相等（$|M_0| = |M_1|$），此設定直接體現了加密系統允許密文洩漏明文的長度。
                        </p>
                    </div>
                </div>

            </div>
        </section>

        <!-- 第二部分：簡答與分析題 -->
        <section class="space-y-6">
            <div class="border-b border-slate-800 pb-3 flex items-center justify-between">
                <div>
                    <h2 class="text-xl font-bold text-white flex items-center gap-2">
                        <span>第二部分：核心概念判讀與分析題（共 3 題，每題 10 分，共 30 分）</span>
                    </h2>
                    <p class="text-slate-400 text-xs mt-1 font-mono">回答須切中密碼學本質，點出因果關係與具體反例</p>
                </div>
            </div>

            <div class="space-y-4">

                <!-- Q7 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-amber-500/10 text-amber-300 border border-amber-500/30">第 7 題 (10 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：作業一 1(a) 變形題</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        考慮將 OTP 的位元 XOR 運算改為布林 OR（$\vee$）運算：$\text{Enc}(K, M) = K \vee M$，金鑰 $K$ 均勻隨機取自 $\{0, 1\}$。<br>
                        (1) 請問此方案是否具備解密正確性？若否請給出反例說明原因。（5 分）<br>
                        (2) 請問此方案是否具備完善保密性？請給出機率式證明其成立或破裂。（5 分）
                    </div>
                    <button onclick="toggleSolution('sol-7')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-7" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-3 font-sans">
                        <div>
                            <div class="font-bold text-emerald-400 font-mono text-sm">(1) 不具備解密正確性（5 分）</div>
                            <p class="text-slate-300 leading-relaxed mt-1">
                                正確性要求 $\text{Dec}(K, \text{Enc}(K, M)) = M$。反例：當金鑰 $K = 1$ 時，$\text{Enc}(1, 0) = 1 \vee 0 = 1$ 且 $\text{Enc}(1, 1) = 1 \vee 1 = 1$。給定金鑰 1 與密文 1，解密演算法無法判定明文原為 0 或 1。加密映射非單射（Injective），逆函數不存在。<br>
                                <span class="text-amber-400 font-mono">得分點：寫出 K=1 時兩不同明文產生相同密文 1（非單射）。</span>
                            </p>
                        </div>
                        <div>
                            <div class="font-bold text-emerald-400 font-mono text-sm">(2) 不提供完善保密性（5 分）</div>
                            <p class="text-slate-300 leading-relaxed mt-1">
                                取明文 $M_0 = 0, M_1 = 1$，檢驗密文 $C=0$ 的條件機率：<br>
                                當 $M = 0$ 時，$\Pr[C = 0 \mid M = 0] = \Pr[K \vee 0 = 0] = \Pr[K = 0] = \frac{1}{2}$。<br>
                                當 $M = 1$ 時，$\Pr[C = 0 \mid M = 1] = \Pr[K \vee 1 = 0] = 0$。<br>
                                由於 $\Pr[C = 0 \mid M = 0] \neq \Pr[C = 0 \mid M = 1]$，密文分佈與明文相關，完善保密性破裂。<br>
                                <span class="text-amber-400 font-mono">得分點：列出 C=0 時兩明文之條件機率分別為 1/2 與 0（不等式）。</span>
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Q8 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-amber-500/10 text-amber-300 border border-amber-500/30">第 8 題 (10 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：作業一 1(c) / 練習一 14</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        某加密系統因金鑰長度不足，使用同一把 $n$ 位元隨機金鑰 $K$ 同時加密兩筆長度各為 $n$ 的明文 $M_1, M_2$，產出密文對 $(C_1, C_2) = (K \oplus M_1, K \oplus M_2)$。<br>
                        (1) 請寫出攻擊者消除金鑰的差分運算式。（4 分）<br>
                        (2) 請條列說明攻擊者透過此缺陷可具體萃取出的至少三種機密資訊或攻擊手段。（6 分）
                    </div>
                    <button onclick="toggleSolution('sol-8')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-8" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-3 font-sans">
                        <div>
                            <div class="font-bold text-emerald-400 font-mono text-sm">(1) 差分消除算式（4 分）</div>
                            <div class="bg-slate-900 p-2.5 rounded font-mono text-cyan-200 mt-1">
                                $$C_1 \oplus C_2 = (K \oplus M_1) \oplus (K \oplus M_2) = (K \oplus K) \oplus (M_1 \oplus M_2) = M_1 \oplus M_2$$
                            </div>
                            <p class="text-slate-300 leading-relaxed mt-1">金鑰 $K$ 完全抵消，露出明文差分。</p>
                        </div>
                        <div>
                            <div class="font-bold text-emerald-400 font-mono text-sm">(2) 可萃取之資訊與攻擊（6 分，每項 2 分）</div>
                            <ul class="list-decimal pl-5 space-y-1 text-slate-300 mt-1">
                                <li><strong>位元差分樣式</strong>：直接得知兩份明文在哪些位元上完全相同、哪些位元上相異。</li>
                                <li><strong>明文重複性檢測</strong>：若 $M_1 = M_2$，則密文差分必為全零字串 $C_1 \oplus C_2 = 0^n$，暴露重複內容。</li>
                                <li><strong>已知前綴破譯（Crib Dragging）</strong>：若已知 $M_1$（如通訊協定開頭固定標頭），可直接算出另一份明文 $M_2 = (C_1 \oplus C_2) \oplus M_1$。</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Q9 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-amber-500/10 text-amber-300 border border-amber-500/30">第 9 題 (10 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一 17 / 作業一 2(a)</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        考慮下列兩個函式庫（Library）$\mathcal{L}_A$ 與 $\mathcal{L}_B$：<br>
                        - $\mathcal{L}_A$ 提供副程式 <code>query(x)</code>：取樣 $K \leftarrow \{0, 1\}^n$，回傳 $K \oplus x$。<br>
                        - $\mathcal{L}_B$ 提供副程式 <code>query(x)</code>：取樣 $R_1 \leftarrow \{0, 1\}^n$ 與 $R_2 \leftarrow \{0, 1\}^n$，若 $x = 0^n$ 回傳 $R_1$，否則回傳 $R_1 \oplus R_2$。<br>
                        請問 $\mathcal{L}_A$ 與 $\mathcal{L}_B$ 是否在計算上不可區分（$\mathcal{L}_A \equiv \mathcal{L}_B$）？請給出明確結論並簡要說明判定邏輯。（10 分）
                    </div>
                    <button onclick="toggleSolution('sol-9')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-9" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-rose-400 font-mono text-sm">結論：兩函式庫「可區分」（$\mathcal{L}_A \not\equiv \mathcal{L}_B$）（3 分）</div>
                        <p class="text-slate-300 leading-relaxed">
                            <strong>判定邏輯（7 分）</strong>：<br>
                            在 $\mathcal{L}_A$ 中，兩次查詢之輸出差分與輸入差分嚴格綁定：若查詢 $x_1 = 0^n$ 得 $y_1 = K$，查詢 $x_2 = 1^n$ 得 $y_2 = K \oplus 1^n$，則兩次輸出之 XOR 差分必恆為 $y_1 \oplus y_2 = 1^n$（機率 1）。<br>
                            但在 $\mathcal{L}_B$ 中，查詢 $x_1 = 0^n$ 得 $y_1 = R_1$，查詢 $x_2 = 1^n$ 得 $y_2 = R_1 \oplus R_2$，其差分為 $y_1 \oplus y_2 = R_1 \oplus (R_1 \oplus R_2) = R_2$。因為 $R_2$ 為獨立均勻隨機字串，等於 $1^n$ 的機率僅為 $2^{-n}$。<br>
                            區分器演算法：查詢 $0^n$ 與 $1^n$，檢驗 $y_1 \oplus y_2 \stackrel{?}{=} 1^n$，區分優勢達 $\mathbf{Adv} = 1 - 2^{-n} \approx 1$。
                        </p>
                    </div>
                </div>

            </div>
        </section>

        <!-- 第三部分：計算與極簡形式證明題 -->
        <section class="space-y-6">
            <div class="border-b border-slate-800 pb-3 flex items-center justify-between">
                <div>
                    <h2 class="text-xl font-bold text-white flex items-center gap-2">
                        <span>第三部分：計算與極簡形式證明題（共 3 題，共 40 分）</span>
                    </h2>
                    <p class="text-slate-400 text-xs mt-1 font-mono">須列出核心算式與分步推導步驟，格式簡明、邏輯閉環</p>
                </div>
            </div>

            <div class="space-y-4">

                <!-- Q10 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-emerald-500/10 text-emerald-300 border border-emerald-500/30">第 10 題 (12 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一第 21 題 / Ch. 4 生日界限計算</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        考慮一個輸出長度為 32 位元（$n = 32$）的簡化雜湊函數 $H: \{0, 1\}^* \to \{0, 1\}^{32}$。<br>
                        (1) 請寫出生日悖論碰撞近似公式 $q \approx \sqrt{2 \ln 2 \cdot 2^n}$。（4 分）<br>
                        (2) 請精確計算出：大約需要隨機取樣多少筆輸入，即可達到 50% 的機率找到至少一組碰撞？（8 分）
                    </div>
                    <button onclick="toggleSolution('sol-10')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-10" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">(1) 生日界限近似公式（4 分）</div>
                        <p class="text-slate-300 font-mono">
                            $$q \approx \sqrt{2 \ln 2 \cdot N} \approx 1.1774 \times \sqrt{2^n} = 1.1774 \times 2^{n/2}$$
                        </p>
                        <div class="font-bold text-emerald-400 font-mono text-sm pt-1">(2) 代入數值計算（8 分）</div>
                        <p class="text-slate-300 leading-relaxed font-mono">
                            代入 $n = 32$，得 $n/2 = 16$：<br>
                            $$q \approx 1.1774 \times 2^{16} = 1.1774 \times 65536 \approx 77162$$
                            <strong>結論</strong>：大約僅需取樣約 77,162 次（或回答約 $2^{16} = 65,536$ 次），即可達到 50% 碰撞機率。<br>
                            <span class="text-amber-400">得分點：寫出 $2^{16}$ 或計算出約 7.7 萬次皆可給滿分。</span>
                        </p>
                    </div>
                </div>

                <!-- Q11 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-emerald-500/10 text-emerald-300 border border-emerald-500/30">第 11 題 (14 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一 29 / 課本 Ex 2.14 / 夏農定理</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        請使用<strong>反證法</strong>與<strong>抽屜原理（鴿籠原理）</strong>，證明夏農金鑰長度下界定理：<br>
                        「任何具備解密正確性且達成完善保密性（Perfect Secrecy）的加密方案，其金鑰空間大小必須大於等於明文空間大小，即 $|\mathcal{K}| \ge |\mathcal{M}|$。」（14 分）
                    </div>
                    <button onclick="toggleSolution('sol-11')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-11" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">考場標準極簡 4 步推導（14 分）</div>
                        <div class="bg-slate-900 p-3 rounded-lg font-mono text-slate-200 space-y-2 leading-relaxed">
                            <div><strong>步驟 1（反向假設，3 分）</strong>：設方案具備解密正確性與完善保密性，但金鑰數嚴格小於明文數：$|\mathcal{K}| < |\mathcal{M}|$。</div>
                            <div><strong>步驟 2（解密集合大小受限，4 分）</strong>：固定任意出現機率大於零的合法密文 $c$（$\Pr[C=c] > 0$）。定義密文 $c$ 能解出的所有明文集合為 $S(c) = \{\text{Dec}(k, c) \mid k \in \mathcal{K}\}$。因解密演算法為確定性函數（同一把金鑰解同一密文只產出一種結果），故：
                            $$|S(c)| \le |\mathcal{K}|$$</div>
                            <div><strong>步驟 3（抽屜原理抓出零機率明文，4 分）</strong>：由反設 $|S(c)| \le |\mathcal{K}| < |\mathcal{M}|$，明文空間內必存在至少一筆明文 $m^* \notin S(c)$。由正確性，$m^*$ 加密絕不可能產出 $c$（否則拿該金鑰解密必定解出 $m^*$ 產生矛盾），故：
                            $$\Pr[C = c \mid M = m^*] = 0$$</div>
                            <div><strong>步驟 4（撞牆產生矛盾，3 分）</strong>：完善保密性要求對所有明文產生密文 $c$ 的機率皆嚴格等於無條件機率 $\Pr[C=c \mid M=m^*] = \Pr[C=c] > 0$。此與步驟 3 之數值 0 當場矛盾！反設不成立，故必有 $|\mathcal{K}| \ge |\mathcal{M}|$。</div>
                        </div>
                    </div>
                </div>

                <!-- Q12 -->
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-emerald-500/10 text-emerald-300 border border-emerald-500/30">第 12 題 (14 分)</span>
                        <span class="text-xs text-slate-500 font-mono">對應：練習一 31 / 課本 Ex 6.9 / PRF 破譯</span>
                    </div>
                    <div class="text-sm text-slate-200 font-medium leading-relaxed">
                        設 $F: \{0, 1\}^n \times \{0, 1\}^n \to \{0, 1\}^m$ 為安全偽隨機函數（PRF）。構造新函數 $H(K, X) = F(K, X) \oplus F(K, 0^n)$。<br>
                        請證明 $H$ 絕非安全 PRF：<br>
                        (1) 指出其結構上的致命自變數抵消破綻。（4 分）<br>
                        (2) 構造一個有效率的多項式時間區分者演算法 $D$。（6 分）<br>
                        (3) 精確推導其區分優勢 $\mathbf{Adv}_D$。（4 分）
                    </div>
                    <button onclick="toggleSolution('sol-12')" class="text-xs font-mono text-purple-400 hover:text-purple-300 flex items-center gap-1 pt-1">
                        <span>[點擊切換詳解與評分]</span>
                    </button>
                    <div id="sol-12" class="hidden p-4 rounded-xl bg-slate-950 border border-purple-500/30 text-xs space-y-2 font-sans">
                        <div class="font-bold text-emerald-400 font-mono text-sm">(1) 致命自變數抵消破綻（4 分）</div>
                        <p class="text-slate-300 leading-relaxed font-mono">
                            代入特殊輸入 $X = 0^n$：
                            $$H(K, 0^n) = F(K, 0^n) \oplus F(K, 0^n) = 0^m$$
                            無論金鑰 $K$ 為何，在全零輸入下輸出恆為全零字串 $0^m$。
                        </p>
                        <div class="font-bold text-emerald-400 font-mono text-sm pt-1">(2) 區分者演算法 $D$（6 分）</div>
                        <div class="bg-slate-900 p-2.5 rounded font-mono text-cyan-200 text-xs space-y-1">
                            <div>演算法 $D^{\mathcal{O}}$：</div>
                            <div>1. 查詢 Oracle $\mathcal{O}$ 輸入 $X = 0^n$，取得輸出字串 $Y \leftarrow \mathcal{O}(0^n)$。</div>
                            <div>2. 比對：若 $Y == 0^m$ 輸出 1（判定為真實函數 $H$）；否則輸出 0（判定為真隨機函數）。</div>
                        </div>
                        <div class="font-bold text-emerald-400 font-mono text-sm pt-1">(3) 優勢推導（4 分）</div>
                        <p class="text-slate-300 leading-relaxed font-mono">
                            - 在真實世界（$\mathcal{O} = H$）中：$Y = 0^m$ 恆成立，$\Pr[D^H = 1] = 1$。<br>
                            - 在隨機世界（$\mathcal{O} = f_{\text{Rand}}$）中：真隨機函數獨立取樣，命中 $0^m$ 機率為 $\Pr[D^{\text{Rand}} = 1] = 2^{-m}$。<br>
                            - 區分優勢：
                            $$\mathbf{Adv}_D = |\Pr[D^H = 1] - \Pr[D^{\text{Rand}} = 1]| = |1 - 2^{-m}| = 1 - 2^{-m} \approx 1$$
                            優勢不可忽略（接近 1），故 $H$ 絕非安全 PRF。證明完畢。
                        </p>
                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- 頁尾 -->
    <footer class="bg-slate-900 border-t border-slate-800 py-6 text-center text-xs text-slate-500 font-mono">
        <div class="max-w-7xl mx-auto px-4 space-y-2">
            <p>現代與後量子密碼學導論・期中全真模擬試卷（範圍嚴格至 1-5 Section 1）</p>
            <p class="text-[11px] text-slate-600">Introduction to Modern Cryptography by Katz & Lindell | The Joy of Cryptography by Mike Rosulek</p>
        </div>
    </footer>

    <!-- 浮動置頂按鈕 -->
    <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" id="back-to-top" class="fixed bottom-6 right-6 p-3 rounded-full bg-slate-800/90 hover:bg-purple-600 text-slate-300 hover:text-white border border-slate-700 shadow-xl transition-all opacity-0 pointer-events-none z-50">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
    </button>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const btn = document.getElementById('back-to-top');
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    btn.classList.remove('opacity-0', 'pointer-events-none');
                } else {
                    btn.classList.add('opacity-0', 'pointer-events-none');
                }
            });

            // 觸發 KaTeX
            if (window.renderMathInElement) {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ],
                    throwOnError: false
                });
            }
        });

        function toggleSolution(id) {
            const el = document.getElementById(id);
            if (el) {
                el.classList.toggle('hidden');
            }
        }

        let allOpen = false;
        function toggleAllSolutions() {
            allOpen = !allOpen;
            for (let i = 1; i <= 12; i++) {
                const el = document.getElementById(`sol-${i}`);
                if (el) {
                    if (allOpen) {
                        el.classList.remove('hidden');
                    } else {
                        el.classList.add('hidden');
                    }
                }
            }
            document.getElementById('toggle-all-btn').textContent = allOpen ? '摺疊全部詳解與評分標準' : '展開全部詳解與評分標準';
        }
    </script>
    <script id="header-sync-script">
    function syncHeaderHeight() {
        const header = document.getElementById('site-header') || document.querySelector('header');
        if (header) {
            const h = Math.ceil(header.getBoundingClientRect().height);
            document.documentElement.style.setProperty('--header-height', `${h}px`);
        }
    }
    window.addEventListener('resize', syncHeaderHeight);
    window.addEventListener('orientationchange', syncHeaderHeight);
    document.addEventListener('DOMContentLoaded', syncHeaderHeight);
    setTimeout(syncHeaderHeight, 50);
    setTimeout(syncHeaderHeight, 200);
    setTimeout(syncHeaderHeight, 600);
    </script>
</body>
</html>
"""

with open("mock_exam.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Successfully created mock_exam.html!")
