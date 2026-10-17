// ==========================================
// Interactive Cryptography Playgrounds
// ==========================================

// --- Helper Functions ---
function stringToBytes(str) {
    const bytes = [];
    for (let i = 0; i < str.length; i++) {
        bytes.push(str.charCodeAt(i) & 0xff);
    }
    return bytes;
}

function bytesToString(bytes) {
    return bytes.map(b => (b >= 32 && b <= 126) ? String.fromCharCode(b) : '·').join('');
}

function bytesToHex(bytes) {
    return bytes.map(b => b.toString(16).padStart(2, '0').toUpperCase()).join(' ');
}

function xorBytes(b1, b2) {
    const len = Math.min(b1.length, b2.length);
    const res = [];
    for (let i = 0; i < len; i++) {
        res.push(b1[i] ^ b2[i]);
    }
    return res;
}

// ==========================================
// 1. Two-Time Pad Attack Simulator
// ==========================================
const TwoTimePadLab = {
    m1: "Attack at dawn 0600!",
    m2: "Send all secret code",
    key: [],
    c1: [],
    c2: [],
    c12: [],

    init() {
        this.resetRandomKey();
        this.render();
    },

    resetRandomKey() {
        const len = Math.max(this.m1.length, this.m2.length);
        this.key = [];
        for (let i = 0; i < len; i++) {
            this.key.push(Math.floor(Math.random() * 256));
        }
        this.recompute();
    },

    recompute() {
        const b1 = stringToBytes(this.m1);
        const b2 = stringToBytes(this.m2);
        this.c1 = xorBytes(b1, this.key);
        this.c2 = xorBytes(b2, this.key);
        this.c12 = xorBytes(this.c1, this.c2);
    },

    performCribDrag(crib) {
        if (!crib || crib.length === 0) return [];
        const cribBytes = stringToBytes(crib);
        const results = [];
        for (let offset = 0; offset <= this.c12.length - cribBytes.length; offset++) {
            const slice = this.c12.slice(offset, offset + cribBytes.length);
            const xored = xorBytes(slice, cribBytes);
            results.push({
                offset: offset,
                text: bytesToString(xored),
                hex: bytesToHex(xored)
            });
        }
        return results;
    },

    render() {
        const container = document.getElementById('playground-two-time-pad');
        if (!container) return;

        const cribInputVal = document.getElementById('ttp-crib-input')?.value || "the ";
        const cribResults = this.performCribDrag(cribInputVal);

        container.innerHTML = `
            <div class="space-y-6 text-sm">
                <div class="bg-slate-900 border border-slate-700 rounded-lg p-4">
                    <h4 class="font-bold text-base text-cyan-400 mb-2">輸入兩組明文（使用同一組金鑰加密）</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-slate-400 text-xs mb-1">明文 1 (M1)</label>
                            <input type="text" id="ttp-m1" value="${this.m1}" maxlength="24"
                                class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white font-mono text-xs focus:outline-none focus:border-cyan-500">
                        </div>
                        <div>
                            <label class="block text-slate-400 text-xs mb-1">明文 2 (M2)</label>
                            <input type="text" id="ttp-m2" value="${this.m2}" maxlength="24"
                                class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white font-mono text-xs focus:outline-none focus:border-cyan-500">
                        </div>
                    </div>
                    <div class="mt-3 flex gap-2">
                        <button id="ttp-update-btn" class="bg-cyan-600 hover:bg-cyan-500 text-white font-medium px-3 py-1.5 rounded text-xs transition">
                            重新加密計算
                        </button>
                        <button id="ttp-newkey-btn" class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-3 py-1.5 rounded text-xs transition">
                            換一把新隨機金鑰
                        </button>
                    </div>
                </div>

                <div class="bg-slate-900 border border-slate-700 rounded-lg p-4 font-mono text-xs overflow-x-auto space-y-2">
                    <div class="text-slate-400 text-xs uppercase font-sans font-semibold mb-2 text-emerald-400">
                        二進位與十六進位運算結果（金鑰已完全被抵消）
                    </div>
                    <div><span class="text-cyan-300 font-bold">C1 (Hex)   :</span> ${bytesToHex(this.c1)}</div>
                    <div><span class="text-indigo-300 font-bold">C2 (Hex)   :</span> ${bytesToHex(this.c2)}</div>
                    <div class="pt-2 border-t border-slate-800">
                        <span class="text-amber-400 font-bold">C1 ⊕ C2 (Hex)  :</span> ${bytesToHex(this.c12)}
                    </div>
                    <div>
                        <span class="text-amber-400 font-bold">M1 ⊕ M2 (ASCII):</span> <span class="bg-slate-800 px-2 py-0.5 rounded text-amber-200">${bytesToString(this.c12)}</span>
                    </div>
                </div>

                <div class="bg-slate-900 border border-slate-700 rounded-lg p-4">
                    <h4 class="font-bold text-base text-cyan-400 mb-2">互動式單字滑動探測（Crib Dragging Tool）</h4>
                    <p class="text-slate-400 text-xs mb-3">
                        輸入您推測明文中可能出現的常見英文單字（如 <code class="text-amber-300">"the "</code>、<code class="text-amber-300">"secret"</code>、<code class="text-amber-300">"Attack"</code>）。系統會將該單字在 $C_1 \oplus C_2$ 的各個偏移位置上逐一進行 XOR，若出現有意義文字，代表猜中對應明文！
                    </p>
                    <div class="flex gap-2 mb-4">
                        <input type="text" id="ttp-crib-input" value="${cribInputVal}" placeholder="輸入猜測單字..."
                            class="bg-slate-800 border border-slate-600 rounded px-3 py-1.5 text-white font-mono text-xs focus:outline-none focus:border-cyan-500 w-48">
                        <button id="ttp-crib-btn" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded text-xs font-medium transition">
                            執行探測比對
                        </button>
                    </div>

                    <div class="max-h-56 overflow-y-auto border border-slate-800 rounded bg-slate-950 p-2 font-mono text-xs">
                        <table class="w-full text-left">
                            <thead class="text-slate-500 border-b border-slate-800">
                                <tr>
                                    <th class="py-1 px-2">位移 (Offset)</th>
                                    <th class="py-1 px-2">XOR 還原字元 (Crib ⊕ C12)</th>
                                    <th class="py-1 px-2">分析判定</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${cribResults.map(r => {
                                    const isAlpha = /^[a-zA-Z0-9\s,!\.]+$/.test(r.text);
                                    return `
                                        <tr class="border-b border-slate-900 hover:bg-slate-900/50">
                                            <td class="py-1 px-2 text-slate-400">${r.offset}</td>
                                            <td class="py-1 px-2 font-bold ${isAlpha ? 'text-emerald-400 bg-emerald-950/30' : 'text-slate-500'}">
                                                "${r.text}"
                                            </td>
                                            <td class="py-1 px-2 text-xs">
                                                ${isAlpha ? '<span class="text-emerald-400 font-sans font-medium">可能為自然文字</span>' : '<span class="text-slate-600 font-sans">含控制字元/雜訊</span>'}
                                            </td>
                                        </tr>
                                    `;
                                }).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        `;

        // Bind events
        document.getElementById('ttp-update-btn')?.addEventListener('click', () => {
            const m1Val = document.getElementById('ttp-m1').value;
            const m2Val = document.getElementById('ttp-m2').value;
            this.m1 = m1Val || " ";
            this.m2 = m2Val || " ";
            const maxLen = Math.max(this.m1.length, this.m2.length);
            while (this.key.length < maxLen) {
                this.key.push(Math.floor(Math.random() * 256));
            }
            this.recompute();
            this.render();
        });

        document.getElementById('ttp-newkey-btn')?.addEventListener('click', () => {
            this.resetRandomKey();
            this.render();
        });

        document.getElementById('ttp-crib-btn')?.addEventListener('click', () => {
            this.render();
        });

        document.getElementById('ttp-crib-input')?.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') this.render();
        });
    }
};

// ==========================================
// 2. Feistel Network Step-by-Step Simulator
// ==========================================
const FeistelLab = {
    round: 0,
    roundsHistory: [],
    keys: [0x5A, 0xC3, 0x96, 0x3F],
    l0: 0x4B,
    r0: 0xE2,

    // Round function F(R, K): simple non-linear mix
    F(R, K) {
        return ((R * 7 + K) ^ 0xAA) & 0xFF;
    },

    init() {
        this.reset();
        this.render();
    },

    reset() {
        this.round = 0;
        this.roundsHistory = [
            { round: 0, L: this.l0, R: this.r0, F_val: 0, K: 0, desc: "初始輸入區塊 (L0, R0)" }
        ];
    },

    stepForward() {
        if (this.round >= 4) return;
        const prev = this.roundsHistory[this.round];
        const nextRound = this.round + 1;
        const k = this.keys[nextRound - 1];
        const f_val = this.F(prev.R, k);
        const nextL = prev.R;
        const nextR = (prev.L ^ f_val) & 0xFF;

        this.roundsHistory.push({
            round: nextRound,
            L: nextL,
            R: nextR,
            F_val: f_val,
            K: k,
            desc: `第 ${nextRound} 輪: L_${nextRound} = R_${nextRound-1}, R_${nextRound} = L_${nextRound-1} ⊕ F(R_${nextRound-1}, K_${nextRound})`
        });
        this.round = nextRound;
        this.render();
    },

    stepBackward() {
        if (this.round <= 0) return;
        this.roundsHistory.pop();
        this.round--;
        this.render();
    },

    render() {
        const container = document.getElementById('playground-feistel');
        if (!container) return;

        const cur = this.roundsHistory[this.round];

        let securityTag = "";
        if (this.round === 0) securityTag = '<span class="text-slate-400">未加密明文</span>';
        else if (this.round === 1) securityTag = '<span class="text-rose-400 font-bold">1 輪: 絕不安全（直接洩漏右半部）</span>';
        else if (this.round === 2) securityTag = '<span class="text-rose-400 font-bold">2 輪: 不安全（存在簡單區分器）</span>';
        else if (this.round === 3) securityTag = '<span class="text-amber-400 font-bold">3 輪: 滿足 PRP（Luby-Rackoff 定理），但無法防範反向查詢</span>';
        else if (this.round === 4) securityTag = '<span class="text-emerald-400 font-bold">4 輪: 滿足 Strong PRP（可抵抗正向與反向 CCA 查詢）</span>';

        container.innerHTML = `
            <div class="space-y-6 text-sm">
                <div class="bg-slate-900 border border-slate-700 rounded-lg p-4">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <div>
                            <h4 class="font-bold text-base text-cyan-400">Feistel 網路單步輪變形展示器</h4>
                            <div class="text-xs text-slate-400 mt-0.5">當前狀態：輪數 = ${this.round} / 4 | 安全等級：${securityTag}</div>
                        </div>
                        <div class="flex gap-2">
                            <button id="feistel-prev-btn" ${this.round === 0 ? 'disabled' : ''}
                                class="bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 px-3 py-1.5 rounded text-xs transition">
                                上一輪
                            </button>
                            <button id="feistel-next-btn" ${this.round === 4 ? 'disabled' : ''}
                                class="bg-cyan-600 hover:bg-cyan-500 disabled:opacity-40 text-white font-medium px-4 py-1.5 rounded text-xs transition">
                                下一輪 (Step Next)
                            </button>
                            <button id="feistel-reset-btn"
                                class="bg-slate-800 hover:bg-slate-700 text-slate-400 px-3 py-1.5 rounded text-xs transition">
                                重設
                            </button>
                        </div>
                    </div>

                    <!-- Flow Diagram -->
                    <div class="bg-slate-950 border border-slate-800 rounded-lg p-4 flex flex-col items-center">
                        <div class="flex gap-12 font-mono text-center">
                            <div class="w-32 bg-slate-900 border border-cyan-500/50 rounded p-2">
                                <div class="text-xs text-slate-500">L${this.round} (8-bit)</div>
                                <div class="text-lg font-bold text-cyan-300">0x${cur.L.toString(16).padStart(2, '0').toUpperCase()}</div>
                                <div class="text-[10px] text-slate-400">${cur.L.toString(2).padStart(8, '0')}</div>
                            </div>
                            <div class="w-32 bg-slate-900 border border-indigo-500/50 rounded p-2">
                                <div class="text-xs text-slate-500">R${this.round} (8-bit)</div>
                                <div class="text-lg font-bold text-indigo-300">0x${cur.R.toString(16).padStart(2, '0').toUpperCase()}</div>
                                <div class="text-[10px] text-slate-400">${cur.R.toString(2).padStart(8, '0')}</div>
                            </div>
                        </div>

                        ${this.round > 0 ? `
                            <div class="my-3 text-center text-xs font-mono bg-slate-900/80 px-4 py-2 rounded border border-slate-800 text-slate-300">
                                <div>輪金鑰 K${this.round} = <span class="text-amber-300">0x${cur.K.toString(16).toUpperCase()}</span></div>
                                <div>輪函數 F(R_${this.round-1}, K_${this.round}) = <span class="text-purple-300">0x${cur.F_val.toString(16).toUpperCase()}</span></div>
                                <div class="text-emerald-400 mt-1 font-sans">${cur.desc}</div>
                            </div>
                        ` : `
                            <div class="my-4 text-xs text-slate-500 text-center">點擊「下一輪」開始觀察 Feistel 左右半部交叉與 XOR 運算</div>
                        `}
                    </div>
                </div>

                <!-- History Table -->
                <div class="bg-slate-900 border border-slate-700 rounded-lg p-4 font-mono text-xs">
                    <h5 class="text-slate-300 font-sans font-bold mb-3">各輪演變歷史記錄表</h5>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left">
                            <thead class="text-slate-500 border-b border-slate-800">
                                <tr>
                                    <th class="py-1 px-2">Round</th>
                                    <th class="py-1 px-2">左半部 (L)</th>
                                    <th class="py-1 px-2">右半部 (R)</th>
                                    <th class="py-1 px-2">輪金鑰 (K)</th>
                                    <th class="py-1 px-2">輪函數輸出 F(R, K)</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${this.roundsHistory.map(h => `
                                    <tr class="border-b border-slate-800/50 hover:bg-slate-800/30">
                                        <td class="py-1 px-2 font-bold text-cyan-400">${h.round}</td>
                                        <td class="py-1 px-2 text-cyan-200">0x${h.L.toString(16).padStart(2, '0').toUpperCase()}</td>
                                        <td class="py-1 px-2 text-indigo-200">0x${h.R.toString(16).padStart(2, '0').toUpperCase()}</td>
                                        <td class="py-1 px-2 text-amber-300">${h.round > 0 ? '0x' + h.K.toString(16).toUpperCase() : '-'}</td>
                                        <td class="py-1 px-2 text-purple-300">${h.round > 0 ? '0x' + h.F_val.toString(16).toUpperCase() : '-'}</td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('feistel-next-btn')?.addEventListener('click', () => this.stepForward());
        document.getElementById('feistel-prev-btn')?.addEventListener('click', () => this.stepBackward());
        document.getElementById('feistel-reset-btn')?.addEventListener('click', () => {
            this.reset();
            this.render();
        });
    }
};

// ==========================================
// 3. Padding Oracle Step-by-Step Lab
// ==========================================
const PaddingOracleLab = {
    blockSize: 8, // 8-byte blocks for clear visualization
    // True plain message is "SECRET" padded with PKCS#7: [0x53, 0x45, 0x43, 0x52, 0x45, 0x54, 0x02, 0x02]
    originalPlain: [0x53, 0x45, 0x43, 0x52, 0x45, 0x54, 0x02, 0x02],
    // Secret intermediate value I2 = D_k(C2)
    secretI2: [0x19, 0xA4, 0xFE, 0x82, 0x73, 0x2B, 0x6D, 0x91],
    c1: [],
    c2: [],
    // Attacker's state
    crackedBytes: 0, // from index 7 down to 0
    intermediateFound: [null, null, null, null, null, null, null, null],
    plainRecovered: [null, null, null, null, null, null, null, null],
    currentC1Prime: [],
    lastProbeResult: null,

    init() {
        this.c1 = [];
        for (let i = 0; i < this.blockSize; i++) {
            this.c1.push(this.secretI2[i] ^ this.originalPlain[i]);
        }
        this.c2 = [0x99, 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22]; // dummy C2
        this.resetAttack();
        this.render();
    },

    resetAttack() {
        this.crackedBytes = 0;
        this.intermediateFound = [null, null, null, null, null, null, null, null];
        this.plainRecovered = [null, null, null, null, null, null, null, null];
        this.currentC1Prime = [...this.c1];
        this.lastProbeResult = null;
    },

    // Simulated Server Decryption Oracle
    serverOracle(c1Prime) {
        // Compute plaintext P' = I2 ^ c1Prime
        const pPrime = [];
        for (let i = 0; i < this.blockSize; i++) {
            pPrime.push(this.secretI2[i] ^ c1Prime[i]);
        }
        // Validate PKCS#7 padding
        const padVal = pPrime[this.blockSize - 1];
        if (padVal <= 0 || padVal > this.blockSize) {
            return false;
        }
        for (let i = this.blockSize - padVal; i < this.blockSize; i++) {
            if (pPrime[i] !== padVal) return false;
        }
        return true;
    },

    // Step crack one byte
    stepCrackNextByte() {
        if (this.crackedBytes >= this.blockSize) return;

        const targetIdx = this.blockSize - 1 - this.crackedBytes;
        const targetPad = this.crackedBytes + 1;

        // Prepare C1' with known suffix to match targetPad
        const probeC1 = [...this.c1];
        for (let i = targetIdx + 1; i < this.blockSize; i++) {
            probeC1[i] = this.intermediateFound[i] ^ targetPad;
        }

        // Search 0x00 to 0xFF for targetIdx
        let foundByte = null;
        for (let val = 0; val < 256; val++) {
            probeC1[targetIdx] = val;
            if (this.serverOracle(probeC1)) {
                foundByte = val;
                break;
            }
        }

        if (foundByte !== null) {
            const foundI = foundByte ^ targetPad;
            const recoveredP = foundI ^ this.c1[targetIdx];
            this.intermediateFound[targetIdx] = foundI;
            this.plainRecovered[targetIdx] = recoveredP;
            this.crackedBytes++;
            this.currentC1Prime = [...probeC1];
            this.lastProbeResult = {
                targetIdx: targetIdx,
                guessByte: foundByte,
                pad: targetPad,
                intermediate: foundI,
                plainByte: recoveredP
            };
        }
        this.render();
    },

    render() {
        const container = document.getElementById('playground-padding-oracle');
        if (!container) return;

        container.innerHTML = `
            <div class="space-y-6 text-sm">
                <div class="bg-slate-900 border border-slate-700 rounded-lg p-4">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                        <div>
                            <h4 class="font-bold text-base text-cyan-400">Padding Oracle（PKCS#7）逐步攻擊操作台</h4>
                            <div class="text-xs text-slate-400">區塊大小：8 位元組 | 已成功破解位元組：${this.crackedBytes} / 8</div>
                        </div>
                        <div class="flex gap-2">
                            <button id="po-step-btn" ${this.crackedBytes >= 8 ? 'disabled' : ''}
                                class="bg-cyan-600 hover:bg-cyan-500 disabled:opacity-40 text-white font-medium px-4 py-1.5 rounded text-xs transition">
                                逐步破解下一個位元組 (Crack Byte)
                            </button>
                            <button id="po-all-btn" ${this.crackedBytes >= 8 ? 'disabled' : ''}
                                class="bg-emerald-600 hover:bg-emerald-500 disabled:opacity-40 text-white px-3 py-1.5 rounded text-xs transition">
                                一鍵全區塊破解
                            </button>
                            <button id="po-reset-btn"
                                class="bg-slate-700 hover:bg-slate-600 text-slate-300 px-3 py-1.5 rounded text-xs transition">
                                重設實驗
                            </button>
                        </div>
                    </div>

                    ${this.lastProbeResult ? `
                        <div class="bg-emerald-950/40 border border-emerald-500/40 rounded p-3 text-xs font-mono text-emerald-200 mb-4">
                            <strong>[預言機反饋成功]</strong> 位元組位置 Index [${this.lastProbeResult.targetIdx}]：<br/>
                            構造前一區塊 C1'[${this.lastProbeResult.targetIdx}] = 0x${this.lastProbeResult.guessByte.toString(16).padStart(2, '0').toUpperCase()} 
                            使得明文填充尾部達成 0x0${this.lastProbeResult.pad}。<br/>
                            推導中間值 I2[${this.lastProbeResult.targetIdx}] = C1' ⊕ Pad = 0x${this.lastProbeResult.intermediate.toString(16).padStart(2, '0').toUpperCase()}<br/>
                            還原原始明文 P2[${this.lastProbeResult.targetIdx}] = I2 ⊕ C1 = 
                            0x${this.lastProbeResult.plainByte.toString(16).padStart(2, '0').toUpperCase()} 
                            ('${(this.lastProbeResult.plainByte >= 32 && this.lastProbeResult.plainByte <= 126) ? String.fromCharCode(this.lastProbeResult.plainByte) : `\\x0${this.lastProbeResult.plainByte}`}')
                        </div>
                    ` : ''}

                    <!-- Byte-by-Byte Grid -->
                    <div class="bg-slate-950 border border-slate-800 rounded-lg p-3 overflow-x-auto font-mono text-xs">
                        <table class="w-full text-center">
                            <thead>
                                <tr class="text-slate-500 border-b border-slate-800">
                                    <th class="py-1 px-1">欄位 / Byte</th>
                                    ${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `<th class="py-1 px-1">[${i}]</th>`).join('')}
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-900">
                                <tr>
                                    <td class="py-2 text-left text-slate-400 font-sans">原始密文 C1 (IV)</td>
                                    ${this.c1.map(b => `<td class="text-cyan-300">0x${b.toString(16).padStart(2, '0').toUpperCase()}</td>`).join('')}
                                </tr>
                                <tr>
                                    <td class="py-2 text-left text-amber-400 font-sans">偽造密文 C1'</td>
                                    ${this.currentC1Prime.map(b => `<td class="text-amber-300">0x${b.toString(16).padStart(2, '0').toUpperCase()}</td>`).join('')}
                                </tr>
                                <tr>
                                    <td class="py-2 text-left text-purple-400 font-sans">逆推中間值 I2</td>
                                    ${this.intermediateFound.map(b => `
                                        <td class="${b !== null ? 'text-purple-300 font-bold bg-purple-950/20' : 'text-slate-600'}">
                                            ${b !== null ? '0x' + b.toString(16).padStart(2, '0').toUpperCase() : '??'}
                                        </td>
                                    `).join('')}
                                </tr>
                                <tr>
                                    <td class="py-2 text-left text-emerald-400 font-sans font-bold">已還原明文 P2</td>
                                    ${this.plainRecovered.map(b => `
                                        <td class="${b !== null ? 'text-emerald-300 font-bold bg-emerald-950/30' : 'text-slate-600'}">
                                            ${b !== null ? ((b >= 32 && b <= 126) ? `'${String.fromCharCode(b)}'` : `\\x0${b}`) : '·'}
                                        </td>
                                    `).join('')}
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    ${this.crackedBytes >= 8 ? `
                        <div class="mt-4 p-3 bg-emerald-900/30 border border-emerald-500 rounded text-emerald-300 text-xs font-sans">
                            <strong>🎉 全區塊破解完成！</strong> 攻擊者完全不需要金鑰，僅透過 256 次以內的解密預言機 Padding 狀態回饋，即將全部明文完整還原。
                        </div>
                    ` : ''}
                </div>
            </div>
        `;

        document.getElementById('po-step-btn')?.addEventListener('click', () => this.stepCrackNextByte());
        document.getElementById('po-all-btn')?.addEventListener('click', () => {
            while (this.crackedBytes < 8) {
                this.stepCrackNextByte();
            }
        });
        document.getElementById('po-reset-btn')?.addEventListener('click', () => {
            this.resetAttack();
            this.render();
        });
    }
};

// ==========================================
// 4. Security Game Simulator (IND-CPA)
// ==========================================
const SecurityGameLab = {
    schemeType: 'deterministic', // 'deterministic' or 'randomized'
    trials: 50,
    history: [],
    wins: 0,

    init() {
        this.runSimulation();
        this.render();
    },

    runSimulation() {
        this.history = [];
        this.wins = 0;
        for (let i = 0; i < this.trials; i++) {
            // Adversary submits m0, m1
            const m0 = "HELLO";
            const m1 = "WORLD";
            // Challenger flips bit b
            const b = Math.random() < 0.5 ? 0 : 1;
            const chosenM = b === 0 ? m0 : m1;

            let c = "";
            let bPrime = 0;

            if (this.schemeType === 'deterministic') {
                // Fixed ciphertext for fixed plain
                c = chosenM === m0 ? "CIPHER_HELLO" : "CIPHER_WORLD";
                // Adversary has queried m0 before, so knows CIPHER_HELLO
                bPrime = (c === "CIPHER_HELLO") ? 0 : 1;
            } else {
                // Randomized: IV chosen freshly
                const iv = Math.floor(Math.random() * 10000);
                c = `IV_${iv}_${chosenM === m0 ? "MASK_A" : "MASK_B"}`;
                // With randomized IV, adversary has no advantage, guesses uniformly
                bPrime = Math.random() < 0.5 ? 0 : 1;
            }

            const win = (bPrime === b);
            if (win) this.wins++;
            this.history.push({ trial: i + 1, b, bPrime, win });
        }
    },

    render() {
        const container = document.getElementById('playground-security-game');
        if (!container) return;

        const winRate = (this.wins / this.trials);
        const advantage = Math.abs(winRate - 0.5);

        container.innerHTML = `
            <div class="space-y-6 text-sm">
                <div class="bg-slate-900 border border-slate-700 rounded-lg p-4">
                    <h4 class="font-bold text-base text-cyan-400 mb-2">IND-CPA 安全遊戲攻防演習棋盤</h4>
                    <p class="text-slate-400 text-xs mb-4">
                        觀察確定性加密（Deterministic）與隨機化加密（Randomized）在面對選擇明文攻擊時的優勢度（Advantage）差異。
                    </p>

                    <div class="flex flex-wrap items-center gap-4 mb-4">
                        <div>
                            <label class="block text-slate-400 text-xs mb-1">加密機制架構</label>
                            <select id="sg-scheme-select" class="bg-slate-800 border border-slate-600 rounded px-3 py-1.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                                <option value="deterministic" ${this.schemeType === 'deterministic' ? 'selected' : ''}>確定性加密 (Deterministic: ECB 模式 / 固定 IV)</option>
                                <option value="randomized" ${this.schemeType === 'randomized' ? 'selected' : ''}>隨機化加密 (Randomized: 隨機 IV / Nonce)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-slate-400 text-xs mb-1">測試輪數</label>
                            <select id="sg-trials-select" class="bg-slate-800 border border-slate-600 rounded px-3 py-1.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                                <option value="10" ${this.trials === 10 ? 'selected' : ''}>10 輪</option>
                                <option value="50" ${this.trials === 50 ? 'selected' : ''}>50 輪</option>
                                <option value="200" ${this.trials === 200 ? 'selected' : ''}>200 輪</option>
                                <option value="1000" ${this.trials === 1000 ? 'selected' : ''}>1000 輪</option>
                            </select>
                        </div>
                        <div class="pt-4">
                            <button id="sg-run-btn" class="bg-cyan-600 hover:bg-cyan-500 text-white font-medium px-4 py-1.5 rounded text-xs transition">
                                重新執行安全遊戲測試
                            </button>
                        </div>
                    </div>

                    <!-- Statistics Dashboard -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4 font-mono text-center">
                        <div class="bg-slate-950 border border-slate-800 p-3 rounded">
                            <div class="text-xs text-slate-500">攻擊者獲勝次數</div>
                            <div class="text-xl font-bold text-white mt-1">${this.wins} / ${this.trials}</div>
                        </div>
                        <div class="bg-slate-950 border border-slate-800 p-3 rounded">
                            <div class="text-xs text-slate-500">攻擊者勝率 P[A wins]</div>
                            <div class="text-xl font-bold ${this.schemeType === 'deterministic' ? 'text-rose-400' : 'text-emerald-400'} mt-1">
                                ${(winRate * 100).toFixed(1)}%
                            </div>
                        </div>
                        <div class="bg-slate-950 border border-slate-800 p-3 rounded">
                            <div class="text-xs text-slate-500">攻擊優勢度 Advantage</div>
                            <div class="text-xl font-bold ${advantage > 0.1 ? 'text-rose-400' : 'text-emerald-400'} mt-1">
                                ${advantage.toFixed(4)}
                            </div>
                            <div class="text-[10px] text-slate-400 font-sans mt-0.5">
                                ${advantage > 0.1 ? '破譯！非可忽略優勢' : '安全！優勢度趨近 0'}
                            </div>
                        </div>
                    </div>

                    <!-- Summary Analysis -->
                    <div class="p-3 bg-slate-950 border border-slate-800 rounded text-xs">
                        ${this.schemeType === 'deterministic' ? `
                            <span class="text-rose-400 font-bold">分析結論：</span>
                            在確定性加密下，攻擊者可先向預言機查詢明文密文對，並在挑戰階段以 100% 機率直接辨識出挑戰密文。勝率恆為 1.0，優勢度恆為 0.5，<b>證明確定性加密在理論上永遠無法達到 IND-CPA 安全</b>。
                        ` : `
                            <span class="text-emerald-400 font-bold">分析結論：</span>
                            在隨機化加密下，每次即使加密相同明文，也會產生完全不同的隨機密文。攻擊者的勝率在 50% 上下波動（相當於隨機猜測），優勢度隨著輪數增加穩定收斂至可忽略數值，<b>成功達成 IND-CPA 安全性</b>。
                        `}
                    </div>
                </div>
            </div>
        `;

        document.getElementById('sg-run-btn')?.addEventListener('click', () => {
            const scheme = document.getElementById('sg-scheme-select').value;
            const trials = parseInt(document.getElementById('sg-trials-select').value, 10);
            this.schemeType = scheme;
            this.trials = trials;
            this.runSimulation();
            this.render();
        });
    }
};

// ==========================================
// Pluggable Playground Registry Architecture
// ==========================================
const PLAYGROUNDS_REGISTRY = [
    {
        id: 'ttp',
        title: '1. Two-Time Pad 明文外洩與滑動探測',
        description: '驗證 One-Time Pad 金鑰重用之致命漏洞，支援 Crib Dragging 與 ASCII 空白鍵探測。',
        init: () => TwoTimePadLab.init(),
        containerId: 'playground-two-time-pad'
    },
    {
        id: 'feistel',
        title: '2. Feistel 網路單步輪置換 (Luby-Rackoff)',
        description: '逐步演示 1 輪至 4 輪 Feistel 網路之左右半部置換與 Luby-Rackoff 定理演進。',
        init: () => FeistelLab.init(),
        containerId: 'playground-feistel'
    },
    {
        id: 'po',
        title: '3. Padding Oracle (PKCS#7) 逐步解密操作',
        description: '模擬 CBC 模式伺服器填充預言機反饋，以多項式次數逆推中間值與明文。',
        init: () => PaddingOracleLab.init(),
        containerId: 'playground-padding-oracle'
    },
    {
        id: 'sg',
        title: '4. IND-CPA 安全遊戲攻防演習',
        description: '比較確定性加密與隨機化加密在面對選擇明文攻擊時的優勢度收斂差異。',
        init: () => SecurityGameLab.init(),
        containerId: 'playground-security-game'
    }
];

window.PLAYGROUNDS_REGISTRY = PLAYGROUNDS_REGISTRY;

// Global init for playgrounds
window.initPlaygrounds = function() {
    PLAYGROUNDS_REGISTRY.forEach(pg => {
        if (typeof pg.init === 'function') pg.init();
    });
};
