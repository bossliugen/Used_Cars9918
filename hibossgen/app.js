const PRINCIPLES = {
  clarity: {
    title: "讓資料流向一眼看懂",
    desc: "不堆砌過度抽象的框架，把頁面狀態、資料來源與計算邏輯拆成單純的模組，減少日後維護時的猜測成本。",
    points: [
      "每個元件只負責一件明確的事",
      "用平實的命名取代艱澀的縮寫",
      "發生錯誤時提供具體可讀的提示",
    ],
    svg: `
      <svg viewBox="0 0 240 92" fill="none" stroke="#1B4332" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="16" y="26" width="52" height="40" rx="8" fill="#E7EFEA" />
        <rect x="94" y="26" width="52" height="40" rx="8" fill="#FFFFFF" />
        <rect x="172" y="26" width="52" height="40" rx="8" fill="#FFFFFF" />
        <path d="M68 46h26M146 46h26" />
        <path d="M88 41l6 5-6 5M166 41l6 5-6 5" />
      </svg>
    `,
  },
  longevity: {
    title: "五年後依然好改好修",
    desc: "少用半年就過時的流行套件，優先依賴瀏覽器原生能力與穩定的資料結構，讓產品陪著團隊走得更遠。",
    points: [
      "盡量降低外部相依套件數量",
      "資料與介面分離，方便隨時替換",
      "保留完整的設計決策與交接筆記",
    ],
    svg: `
      <svg viewBox="0 0 240 92" fill="none" stroke="#1B4332" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="44" y="54" width="152" height="18" rx="6" fill="#E7EFEA" />
        <rect x="64" y="34" width="112" height="16" rx="6" fill="#FFFFFF" />
        <rect x="88" y="14" width="64" height="16" rx="6" fill="#FFFFFF" />
      </svg>
    `,
  },
  human: {
    title: "把時間還給真正使用的人",
    desc: "介面不該讓使用者猜測下一步在哪。透過適度的留白、清晰的字階與誠實的回饋，讓日常操作安靜而順暢。",
    points: [
      "文字對比清楚，長時間閱讀不吃力",
      "表單與篩選回饋即時且不干擾",
      "桌機與手機都能單手輕鬆瀏覽",
    ],
    svg: `
      <svg viewBox="0 0 240 92" fill="none" stroke="#1B4332" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="52" y="14" width="136" height="64" rx="10" fill="#FFFFFF" />
        <path d="M72 32h56" />
        <path d="M72 46h96M72 58h74" stroke="#57534E" />
        <circle cx="164" cy="32" r="6" fill="#E7EFEA" />
      </svg>
    `,
  },
};

const WORKS = [
  {
    id: "market-ledger",
    category: "data",
    categoryLabel: "資料工具",
    year: "2026",
    title: "台灣中古車實價與養車成本分析平台",
    summary: "整合跨世代折舊曲線、通病維修預估與稅金試算，讓不懂車的買家也能安心比較不同年份與版本。",
    background: "許多買家在看二手車時，只看得到開價卻看不到背後的世代通病與養車成本。我們將散落於論壇與實價紀錄的資料結構化，整理成單一靜態網頁工具。",
    approach: [
      "以品牌、車款、年份與版本四層篩選，避免混淆一般版與性能版行情",
      "純前端繪製互動式折舊走勢圖，免後端伺服器也能流暢運作",
      "將排氣量稅金、油耗與車齡耗材整合成清楚的年度預估清單",
    ],
    outcome: "上線後能直接部署於靜態空間，零維護成本，並讓使用者在三分鐘內掌握特定年份車款的合理入手價與整備預算。",
    svg: `
      <svg viewBox="0 0 220 84" fill="none" stroke="#1B4332" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M24 64h172" stroke="#DFD9CE" />
        <path d="M32 54l38-20 42 10 40-26 36 8" />
        <circle cx="70" cy="34" r="4" fill="#E7EFEA" />
        <circle cx="152" cy="18" r="4" fill="#1B4332" />
      </svg>
    `,
  },
  {
    id: "clinic-booking",
    category: "product",
    categoryLabel: "數位產品",
    year: "2025",
    title: "社區診所看診進度與預約整理系統",
    summary: "替在地中醫診所重整掛號流程，拿掉繁瑣的註冊步驟，讓長輩與上班族都能用手機直接確認叫號。",
    background: "診所原本的預約網頁步驟過多，櫃檯每天仍需接聽大量詢問看診進度的電話。我們重新設計了輕量化的看診看板與簡易預約表。",
    approach: [
      "免下載軟體，手機掃描門診單即可查看即時燈號",
      "放大字體與按鈕間距，確保中高齡患者也能輕鬆操作",
      "後台僅保留櫃檯最常用的三項排班調整功能",
    ],
    outcome: "上線兩個月內，櫃檯詢問看診進度的電話減少約四成，現場候診空間也更從容。",
    svg: `
      <svg viewBox="0 0 220 84" fill="none" stroke="#1B4332" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="44" y="12" width="132" height="60" rx="10" fill="#FFFFFF" />
        <rect x="60" y="26" width="38" height="32" rx="6" fill="#E7EFEA" />
        <path d="M112 34h48M112 48h34" stroke="#57534E" />
      </svg>
    `,
  },
  {
    id: "inventory-sync",
    category: "system",
    categoryLabel: "系統架構",
    year: "2025",
    title: "小型選物店多通路庫存同步工具",
    summary: "把門市收銀、官網與市集擺攤的庫存收斂在同一份簡單帳本裡，避免超賣與人工對帳錯誤。",
    background: "三人規模的生活選物店每逢週末市集後，都需要花整個週一晚上手動核對各平台庫存。我們為他們建立了一套輕量的庫存中介服務。",
    approach: [
      "以單一主資料庫作為庫存唯一真實來源",
      "設計離線暫存機制，市集現場訊號不佳也能先記帳後同步",
      "每日自動寄送簡潔的補貨提醒清單給店長",
    ],
    outcome: "盤點與對帳時間從每週四小時縮短至十五分鐘，且未再發生熱門商品超賣。",
    svg: `
      <svg viewBox="0 0 220 84" fill="none" stroke="#1B4332" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="110" cy="42" r="18" fill="#E7EFEA" />
        <circle cx="42" cy="24" r="10" fill="#FFFFFF" />
        <circle cx="42" cy="60" r="10" fill="#FFFFFF" />
        <circle cx="178" cy="42" r="10" fill="#FFFFFF" />
        <path d="M52 27l42 11M52 57l42-11M128 42h40" stroke="#57534E" />
      </svg>
    `,
  },
  {
    id: "editorial-archive",
    category: "product",
    categoryLabel: "數位產品",
    year: "2024",
    title: "獨立出版刊物數位典藏與檢索網站",
    summary: "為地方文化季刊建立長久保存的線上閱讀空間，重視排版呼吸感與跨期數的關鍵字檢索。",
    background: "刊物累積十年後，許多珍貴的地方訪談僅存在紙本與零散檔案中。編輯團隊希望有一個像紙本一樣耐讀、又方便研究人員查詢的網站。",
    approach: [
      "採用襯線體標題搭配寬裕行距，還原雜誌閱讀節奏",
      "建立輕量靜態全文索引，無需資料庫伺服器即可秒速搜尋",
      "每篇文章皆提供乾淨的列印與引用格式",
    ],
    outcome: "成功彙整超過兩百篇地方紀錄，成為在地文史工作者與學生最常引用的線上入口。",
    svg: `
      <svg viewBox="0 0 220 84" fill="none" stroke="#1B4332" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="46" y="14" width="60" height="56" rx="4" fill="#E7EFEA" />
        <rect x="114" y="14" width="60" height="56" rx="4" fill="#FFFFFF" />
        <path d="M58 28h34M58 40h28M126 28h34M126 40h30M126 52h22" stroke="#57534E" />
      </svg>
    `,
  },
];

const NOTES = [
  {
    id: "why-less-abstraction",
    date: "2026 年 10 月",
    tag: "架構筆記",
    title: "為什麼我們越來越少使用複雜的前端狀態庫",
    excerpt: "多數中小型產品真正需要的不是龐大的工具鏈，而是清楚的資料流向。",
    paragraphs: [
      "過去幾年我們接手過不少維護困難的專案，問題往往不是業務邏輯太複雜，而是為了應付「未來可能用得到」的彈性，提前引入了過多層次的抽象。",
      "當一個按鈕的點擊要經過五個檔案才能追蹤到資料變化時，團隊修改介面的意願就會大幅下降。我們現在更傾向把狀態收斂在單一清楚的物件裡，搭配明確的重新繪製函式。",
      "少一點魔術，多一點直白。這讓一年後回來看自己寫的程式時，依然能在一分鐘內看懂當初的決定。",
    ],
  },
  {
    id: "honest-loading-states",
    date: "2026 年 08 月",
    tag: "介面觀察",
    title: "誠實的介面，從不假裝自己永遠不會出錯",
    excerpt: "與其用華麗的動畫掩蓋等待，不如好好告訴使用者現在發生了什麼事。",
    paragraphs: [
      "很多網站喜歡用過度樂觀的提示或閃爍的骨架畫面來製造流暢的錯覺，但當網路真的慢下來或資料缺漏時，使用者反而會感到困惑。",
      "我們在設計表單與資料查詢介面時，會把「查無資料」、「載入失敗」與「等待確認」當成和正常畫面一樣重要的一等公民來排版。",
      "一句清楚、有禮貌、告訴你下一步可以怎麼做的中文提示，往往比任何特效都更能建立信任感。",
    ],
  },
  {
    id: "warm-typography-for-tools",
    date: "2026 年 05 月",
    tag: "排版隨筆",
    title: "工具型網站也可以有雜誌般的閱讀節奏",
    excerpt: "把冰冷的深灰科技感換成暖奶油底色與襯線標題，專注度反而更高。",
    paragraphs: [
      "工程團隊習慣把工具網站做成深色背景或高對比藍紫配色，看久了眼睛其實容易疲勞。",
      "在嘗試為數據分析與知識庫導入暖奶油白底色、1px 暖灰細線與襯線標題後，我們發現使用者停留在頁面上細讀說明的時間明顯變長了。",
      "舒服的視覺節奏不是裝飾，而是讓重要資訊更容易被看進心裡的基礎工程。",
    ],
  },
];

function renderPrinciple(key) {
  const item = PRINCIPLES[key];
  if (!item) return;

  document.querySelectorAll(".tab-pill").forEach((btn) => {
    const isActive = btn.dataset.principle === key;
    btn.classList.toggle("active", isActive);
    btn.setAttribute("aria-selected", String(isActive));
  });

  document.getElementById("principleContent").innerHTML = `
    <div class="principle-svg-box">${item.svg}</div>
    <h3>${item.title}</h3>
    <p>${item.desc}</p>
    <ul class="principle-points">
      ${item.points.map((pt) => `<li>${pt}</li>`).join("")}
    </ul>
  `;
}

function renderWorks(filter = "all") {
  const grid = document.getElementById("worksGrid");
  const list = filter === "all" ? WORKS : WORKS.filter((w) => w.category === filter);

  grid.innerHTML = list
    .map(
      (w) => `
      <button type="button" class="work-card" data-work-id="${w.id}">
        <div class="work-thumb" aria-hidden="true">${w.svg}</div>
        <div class="work-meta">
          <span class="tag-sage">${w.categoryLabel}</span>
          <span class="work-year">${w.year}</span>
        </div>
        <h3 class="card-serif-title">${w.title}</h3>
        <p>${w.summary}</p>
        <span class="work-more">閱讀實作細節 →</span>
      </button>
    `
    )
    .join("");

  grid.querySelectorAll(".work-card").forEach((card) => {
    card.addEventListener("click", () => openWorkModal(card.dataset.workId));
  });
}

function renderNotes() {
  const list = document.getElementById("notesList");
  list.innerHTML = NOTES.map(
    (n) => `
    <button type="button" class="note-row" data-note-id="${n.id}">
      <span class="note-date">${n.date}</span>
      <div>
        <div class="note-title">${n.title}</div>
        <div class="note-excerpt">${n.excerpt}</div>
      </div>
      <span class="note-action">閱讀全文 →</span>
    </button>
  `
  ).join("");

  list.querySelectorAll(".note-row").forEach((row) => {
    row.addEventListener("click", () => openNoteModal(row.dataset.noteId));
  });
}

function openModal(tag, title, bodyHtml) {
  document.getElementById("modalTag").textContent = tag;
  document.getElementById("modalTitle").textContent = title;
  document.getElementById("modalBody").innerHTML = bodyHtml;

  const backdrop = document.getElementById("modalBackdrop");
  backdrop.classList.add("open");
  backdrop.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
}

function closeModal() {
  const backdrop = document.getElementById("modalBackdrop");
  backdrop.classList.remove("open");
  backdrop.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
}

function openWorkModal(workId) {
  const w = WORKS.find((item) => item.id === workId);
  if (!w) return;

  openModal(
    `${w.categoryLabel} ・ ${w.year}`,
    w.title,
    `
      <div class="principle-svg-box" style="margin-bottom:4px;">${w.svg}</div>
      <h4>專案背景</h4>
      <p>${w.background}</p>
      <h4>技術與設計做法</h4>
      <ul class="modal-list">
        ${w.approach.map((step) => `<li>・ ${step}</li>`).join("")}
      </ul>
      <h4>實際成果</h4>
      <p>${w.outcome}</p>
    `
  );
}

function openNoteModal(noteId) {
  const n = NOTES.find((item) => item.id === noteId);
  if (!n) return;

  openModal(
    `${n.tag} ・ ${n.date}`,
    n.title,
    n.paragraphs.map((p) => `<p>${p}</p>`).join("")
  );
}

function initPage() {
  renderPrinciple("clarity");
  renderWorks("all");
  renderNotes();

  document.querySelectorAll(".tab-pill").forEach((btn) => {
    btn.addEventListener("click", () => renderPrinciple(btn.dataset.principle));
  });

  document.querySelectorAll(".filter-pill").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".filter-pill").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderWorks(btn.dataset.filter);
    });
  });

  document.getElementById("modalCloseBtn").addEventListener("click", closeModal);
  document.getElementById("modalBackdrop").addEventListener("click", (e) => {
    if (e.target.id === "modalBackdrop") closeModal();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });

  document.getElementById("contactForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("cName").value.trim();
    const email = document.getElementById("cEmail").value.trim();
    const msg = document.getElementById("cMsg").value.trim();
    const feedback = document.getElementById("formFeedback");

    if (!name || !email || !msg) {
      feedback.style.color = "#991B1B";
      feedback.textContent = "請填寫稱呼、信箱與簡短說明後再送出。";
      return;
    }

    feedback.style.color = "#1B4332";
    feedback.textContent = `謝謝 ${name}，已收到你的來信，我們會在兩個工作天內回覆至 ${email}。`;
    e.target.reset();
  });
}

document.addEventListener("DOMContentLoaded", initPage);
