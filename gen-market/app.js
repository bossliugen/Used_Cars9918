const LISTINGS = [
  {
    id: "gen-swift-sport-2022",
    brand: "Suzuki",
    model: "Swift Sport 1.4T",
    gen: "ZC33S 48V 輕油電",
    year: 2022,
    mileageKm: 28000,
    powerType: "渦輪 / 48V 輕油電",
    fuelFilter: "油電",
    transFilter: "手排",
    city: "台北",
    priceWan: 62.8,
    msrpWan: 82.0,
    verified: true,
    verifiedLabel: "已查驗",
    photoQuery: "Suzuki Swift Sport ZC33S",
    specs: {
      displacement: "1,373 cc",
      horsepower: "129.2 ps + 電推",
      torque: "23.9 kgm",
      transmission: "6 速純手排",
      drivetrain: "前輪驅動",
      fuelEconomy: "19.5 km/L",
      annualTax: "11,920 元",
      dimensions: "3,890 x 1,735 x 1,480 mm",
    },
    records: [
      { title: "原廠定期保養紀錄（4 次完整）", meta: "2022–2025 ・ 皆於內湖原廠施作", note: "每 5,000 公里更換全合成機油，無待修耗材，離合器咬合點正常。" },
      { title: "第三方車體與底盤查驗", meta: "查驗日期 2026 年 10 月", note: "全車原鈑件、無泡水、無調表紀錄，底盤無滲油與異音。" },
    ],
    features: {
      safety: ["6 具安全氣囊", "ACC 主動車距控制", "BSM 盲點偵測", "AEB 自動緊急煞車"],
      chassis: ["Monroe 專屬運動化避震", "雙出排氣尾管", "17 吋原廠雙色鋁圈"],
      interior: ["Sport 跑車化座椅", "Apple CarPlay / Android Auto", "恆溫空調"],
    },
  },
  {
    id: "gen-swift-glx-2021",
    brand: "Suzuki",
    model: "Swift 1.2 GLX",
    gen: "第 4 代輕油電",
    year: 2021,
    mileageKm: 41000,
    powerType: "1.2L 輕油電",
    fuelFilter: "油電",
    transFilter: "CVT",
    city: "新北",
    priceWan: 47.5,
    msrpWan: 72.0,
    verified: true,
    verifiedLabel: "透明車況",
    photoQuery: "Suzuki Swift ZC83S",
    specs: {
      displacement: "1,197 cc",
      horsepower: "83 ps",
      torque: "11.0 kgm",
      transmission: "CVT 無段變速",
      drivetrain: "前輪驅動",
      fuelEconomy: "22.3 km/L",
      annualTax: "8,640 元",
      dimensions: "3,845 x 1,735 x 1,480 mm",
    },
    records: [
      { title: "一手車主自售轉認證整理", meta: "2021–2025 ・ 里程實跑 4.1 萬", note: "剛更換四條全新輪胎與電瓶，都會代步極省油。" },
      { title: "安全配備查核", meta: "全車無重大事故", note: "右後葉子板曾有輕微擦傷烤漆，其餘均為原漆。" },
    ],
    features: {
      safety: ["6 具安全氣囊", "ACC 主動式安全車距巡航", "車道偏離警示"],
      chassis: ["HEARTECT 輕量化底盤", "16 吋鋁圈"],
      interior: ["Keyless 免鑰匙啟動", "恆溫空調", "多功能方向盤"],
    },
  },
  {
    id: "gen-focus-mk4-2022",
    brand: "Ford",
    model: "Focus 5D ST-Line Lommel",
    gen: "MK4 第四代",
    year: 2022,
    mileageKm: 36000,
    powerType: "1.5T 渦輪汽油",
    fuelFilter: "渦輪",
    transFilter: "自排",
    city: "台中",
    priceWan: 61.5,
    msrpWan: 92.9,
    verified: true,
    verifiedLabel: "已查驗",
    photoQuery: "Ford Focus MK4 hatchback",
    specs: {
      displacement: "1,497 cc",
      horsepower: "182 ps",
      torque: "24.5 kgm",
      transmission: "8 速手自排",
      drivetrain: "前輪驅動",
      fuelEconomy: "16.7 km/L",
      annualTax: "11,920 元",
      dimensions: "4,378 x 1,825 x 1,465 mm",
    },
    records: [
      { title: "原廠保養與變速箱油更換", meta: "3.5 萬公里已完成大保養", note: "已預防性更換水泵浦總成改良件，底盤紮實無異音。" },
      { title: "第三方機構查驗通過", meta: "原鈑件無結構損傷", note: "附完整監理站驗車與出險紀錄查詢報告。" },
    ],
    features: {
      safety: ["Co-Pilot360 Level 2", "6 具氣囊", "全速域車道置中"],
      chassis: ["Lommel 運動化獨立多連桿", "四輪碟煞加大碟盤", "18 吋鋁圈"],
      interior: ["B&O 環艙音響", "HUD 抬頭顯示器", "無線充電座"],
    },
  },
  {
    id: "gen-altis-hybrid-2021",
    brand: "Toyota",
    model: "Corolla Altis 1.8 Hybrid 尊爵",
    gen: "第 12 代 TNGA",
    year: 2021,
    mileageKm: 49000,
    powerType: "1.8L 油電複合",
    fuelFilter: "油電",
    transFilter: "CVT",
    city: "桃園",
    priceWan: 58.8,
    msrpWan: 84.5,
    verified: true,
    verifiedLabel: "已查驗",
    photoQuery: "Toyota Corolla Altis E210",
    specs: {
      displacement: "1,798 cc",
      horsepower: "綜效 122 ps",
      torque: "14.5 kgm + 馬達輔助",
      transmission: "E-CVT 電子無段變速",
      drivetrain: "前輪驅動",
      fuelEconomy: "25.8 km/L",
      annualTax: "11,920 元",
      dimensions: "4,630 x 1,780 x 1,435 mm",
    },
    records: [
      { title: "非營業用純家用車查核", meta: "確認無計程車／多元租賃歷史", note: "大電池健康度檢測達 94%，仍在原廠油電電池 8 年保固內。" },
      { title: "原廠半年定期檢查", meta: "完整工單可查", note: "冷氣濾網、煞車油剛於 4.5 萬公里更新。" },
    ],
    features: {
      safety: ["7 具安全氣囊", "TSS 駕駛輔助系統", "BSM 盲點警示"],
      chassis: ["TNGA 高剛性底盤", "後雙 A 臂獨立懸吊"],
      interior: ["7 吋數位儀表", "雙區恆溫空調", "後座冷氣出風口"],
    },
  },
  {
    id: "gen-golf-gti-2019",
    brand: "Volkswagen",
    model: "Golf 2.0 GTI Performance",
    gen: "MK7.5 第七代小改款",
    year: 2019,
    mileageKm: 54000,
    powerType: "2.0T 渦輪汽油",
    fuelFilter: "渦輪",
    transFilter: "雙離合",
    city: "台北",
    priceWan: 84.5,
    msrpWan: 154.8,
    verified: true,
    verifiedLabel: "透明車況",
    photoQuery: "Volkswagen Golf VII GTI",
    specs: {
      displacement: "1,984 cc",
      horsepower: "245 ps",
      torque: "37.7 kgm",
      transmission: "DQ381 7 速濕式雙離合器",
      drivetrain: "前驅 + VAQ 電子限滑差速器",
      fuelEconomy: "13.5 km/L",
      annualTax: "17,410 元",
      dimensions: "4,268 x 1,790 x 1,442 mm",
    },
    records: [
      { title: "EA888 冷卻系統預防性整備", meta: "5 萬公里已換新節溫器座與水泵", note: "無漏水滲油，濕式 DSG 變速箱油已按原廠規範更換。" },
      { title: "無改裝電腦與排氣管", meta: "全車維持原廠設定", note: "外觀僅前保桿下緣細微石擊痕跡。" },
    ],
    features: {
      safety: ["7 具安全氣囊", "ACC 主動定速", "二次碰撞預煞系統"],
      chassis: ["VAQ 前軸電子限滑差速器", "運動化懸吊", "紅色高性能卡鉗"],
      interior: ["經典格紋跑車座椅", "12.3 吋數位儀表", "Dynaudio 音響"],
    },
  },
  {
    id: "gen-cx5-20-2016",
    brand: "Mazda",
    model: "CX-5 2.0 Skyactiv-G 尊榮",
    gen: "第 1 代 KE 小改款",
    year: 2016,
    mileageKm: 88000,
    powerType: "2.0L 自然進氣",
    fuelFilter: "汽油",
    transFilter: "自排",
    city: "台南",
    priceWan: 38.8,
    msrpWan: 106.8,
    verified: true,
    verifiedLabel: "已查驗",
    photoQuery: "Mazda CX-5 KE",
    specs: {
      displacement: "1,998 cc",
      horsepower: "165 ps",
      torque: "21.4 kgm",
      transmission: "6 速手自排",
      drivetrain: "前輪驅動",
      fuelEconomy: "13.5 km/L",
      annualTax: "17,410 元",
      dimensions: "4,540 x 1,840 x 1,710 mm",
    },
    records: [
      { title: "穩定 2.0 汽油版本（非柴油）", meta: "引擎乾爽、水箱溫度正常", note: "已更換前後來令片與兩側收折後視鏡馬達總成。" },
      { title: "底盤橡膠耗材更新", meta: "8.2 萬公里更換三角架與李仔串", note: "行駛坑洞無鬆散感，冷氣壓縮機運作正常。" },
    ],
    features: {
      safety: ["6 具氣囊", "SCBS 都會煞車輔助", "BSM 盲點偵測"],
      chassis: ["前麥花臣 / 後獨立多連桿", "17 吋鋁圈"],
      interior: ["MZD Connect 多媒體旋鈕", "電子手煞車", "雙區恆溫"],
    },
  },
  {
    id: "gen-nx200-2020",
    brand: "Lexus",
    model: "NX 200 菁英 Plus",
    gen: "第 1 代 AZ10 小改款",
    year: 2020,
    mileageKm: 52000,
    powerType: "2.0L 自然進氣",
    fuelFilter: "汽油",
    transFilter: "CVT",
    city: "高雄",
    priceWan: 104.0,
    msrpWan: 167.0,
    verified: true,
    verifiedLabel: "已查驗",
    photoQuery: "Lexus NX AZ10",
    specs: {
      displacement: "1,987 cc",
      horsepower: "150 ps",
      torque: "19.3 kgm",
      transmission: "CVT 模擬 8 速",
      drivetrain: "前輪驅動",
      fuelEconomy: "13.6 km/L",
      annualTax: "17,410 元",
      dimensions: "4,640 x 1,845 x 1,645 mm",
    },
    records: [
      { title: "Lexus 原廠完整保養履歷", meta: "每萬公里準時回廠", note: "內裝皮革無龜裂磨損，車庫停放外觀極佳。" },
      { title: "認證無重大事故", meta: "原廠認證中古標準檢測", note: "輪胎剩餘胎紋約七成，短期內無須額外大整理。" },
    ],
    features: {
      safety: ["8 具安全氣囊", "LSS+ 2.0 智動駕駛輔助", "全速域車道維持"],
      chassis: ["高剛性 SUV 底盤", "18 吋原廠鋁圈"],
      interior: ["電動尾門", "雙前座電動加熱椅", "原廠導航與 CarPlay"],
    },
  },
  {
    id: "gen-crv-2019",
    brand: "Honda",
    model: "CR-V 1.5 VTi-S",
    gen: "第 5 代 RW",
    year: 2019,
    mileageKm: 63000,
    powerType: "1.5T 渦輪汽油",
    fuelFilter: "渦輪",
    transFilter: "CVT",
    city: "台中",
    priceWan: 63.5,
    msrpWan: 103.0,
    verified: false,
    verifiedLabel: "",
    photoQuery: "Honda CR-V fifth generation",
    specs: {
      displacement: "1,498 cc",
      horsepower: "193 ps",
      torque: "24.8 kgm",
      transmission: "CVT 無段變速",
      drivetrain: "前輪驅動",
      fuelEconomy: "14.6 km/L",
      annualTax: "11,920 元",
      dimensions: "4,570 x 1,855 x 1,665 mm",
    },
    records: [
      { title: "民間保修廠定期保養", meta: "留有近三年紙本工單", note: "1.5T 機油更換正常無乳化現象，稅金僅 1.5L 級距。" },
      { title: "外觀說明", meta: "車主自售", note: "前保險桿曾重新烤漆，其餘為原廠漆面。" },
    ],
    features: {
      safety: ["6 具安全氣囊", "Honda SENSING 智慧輔助", "LaneWatch 盲點監視"],
      chassis: ["前麥花臣 / 後多連桿", "18 吋鋁圈"],
      interior: ["後座大空間平坦果嶺", "定速巡航", "雙區恆溫空調"],
    },
  },
  {
    id: "gen-yaris-2017",
    brand: "Toyota",
    model: "Yaris 1.5 豪華",
    gen: "第 3 代 XP150",
    year: 2017,
    mileageKm: 74000,
    powerType: "1.5L 自然進氣",
    fuelFilter: "汽油",
    transFilter: "CVT",
    city: "新北",
    priceWan: 32.5,
    msrpWan: 61.9,
    verified: true,
    verifiedLabel: "透明車況",
    photoQuery: "Toyota Yaris XP150 Asia",
    specs: {
      displacement: "1,496 cc",
      horsepower: "107 ps",
      torque: "14.3 kgm",
      transmission: "Super CVT-i 模擬 7 速",
      drivetrain: "前輪驅動",
      fuelEconomy: "17.2 km/L",
      annualTax: "11,920 元",
      dimensions: "4,115 x 1,700 x 1,475 mm",
    },
    records: [
      { title: "都會通勤一手女用車", meta: "保養單純好照顧", note: "冷氣冷度充足、變速箱換檔平順，適合新手或代步買家。" },
    ],
    features: {
      safety: ["2 具氣囊", "ABS / EBD 煞車輔助", "倒車雷達與顯影"],
      chassis: ["小迴轉半徑 5.1m", "15 吋鋁圈"],
      interior: ["Push Start 免鑰匙", "恆溫空調", "6/4 分離傾倒後座"],
    },
  },
];

const state = {
  search: "",
  brand: "all",
  budget: "all",
  year: "all",
  city: "all",
  fuel: "all",
  trans: "all",
  sort: "default",
  verifiedOnly: false,
  activeListingId: null,
  activeDetailTab: "specs",
  compareIds: [],
};

const photoCache = {};

const FALLBACK_CAR_SVG = `
  <svg class="card-photo-fallback" viewBox="0 0 180 96" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M22 64h136" stroke="#DFD9CE" />
    <path d="M28 58l14-22c3-5 8-8 14-8h48c7 0 13 3 17 9l15 21H28z" fill="#FFFFFF" />
    <circle cx="54" cy="60" r="11" fill="#F6F3EC" />
    <circle cx="128" cy="60" r="11" fill="#F6F3EC" />
    <path d="M56 36h44l10 12H48l8-12z" fill="#E7EFEA" />
  </svg>
`;

async function loadWikimediaPhoto(query, imgEl) {
  if (!query || !imgEl) return;
  if (photoCache[query]) {
    imgEl.src = photoCache[query];
    return;
  }
  const cacheKey = `gen_wiki_v1_${query}`;
  const local = localStorage.getItem(cacheKey);
  if (local) {
    photoCache[query] = local;
    imgEl.src = local;
    return;
  }

  try {
    const api = `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch=${encodeURIComponent(
      query
    )}&gsrlimit=4&prop=imageinfo&iiprop=url&iiurlwidth=520&format=json&origin=*`;
    const resp = await fetch(api);
    const data = await resp.json();
    const pages = data?.query?.pages ? Object.values(data.query.pages) : [];
    const match = pages.find((p) => {
      const t = (p.title || "").toLowerCase();
      return (t.endsWith(".jpg") || t.endsWith(".jpeg") || t.endsWith(".png")) && p.imageinfo?.[0]?.thumburl;
    });
    if (match) {
      const url = match.imageinfo[0].thumburl;
      photoCache[query] = url;
      localStorage.setItem(cacheKey, url);
      imgEl.src = url;
    }
  } catch (e) {
    // 靜默維持線條佔位圖
  }
}

function getFilteredListings() {
  let list = LISTINGS.filter((item) => {
    if (state.search) {
      const q = state.search.toLowerCase();
      const hay = `${item.brand} ${item.model} ${item.gen} ${item.city} ${item.powerType}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    if (state.brand !== "all" && item.brand !== state.brand) return false;
    if (state.city !== "all" && item.city !== state.city) return false;
    if (state.verifiedOnly && !item.verified) return false;
    if (state.fuel !== "all" && item.fuelFilter !== state.fuel) return false;
    if (state.trans !== "all" && item.transFilter !== state.trans) return false;

    if (state.budget !== "all") {
      const [minP, maxP] = state.budget.split("-").map(Number);
      if (item.priceWan < minP || item.priceWan > maxP) return false;
    }
    if (state.year !== "all") {
      const [minY, maxY] = state.year.split("-").map(Number);
      if (item.year < minY || item.year > maxY) return false;
    }
    return true;
  });

  if (state.sort === "price-asc") list.sort((a, b) => a.priceWan - b.priceWan);
  else if (state.sort === "price-desc") list.sort((a, b) => b.priceWan - a.priceWan);
  else if (state.sort === "year-desc") list.sort((a, b) => b.year - a.year);
  else if (state.sort === "mileage-asc") list.sort((a, b) => a.mileageKm - b.mileageKm);

  return list;
}

function renderListings() {
  const list = getFilteredListings();
  const grid = document.getElementById("listingGrid");
  const empty = document.getElementById("emptyState");

  document.getElementById("resultCount").textContent = `共 ${list.length} 輛符合條件`;

  const moreBtn = document.getElementById("btnMoreFilters");
  const hasMoreActive = state.fuel !== "all" || state.trans !== "all" || state.sort !== "default" || state.verifiedOnly;
  moreBtn.classList.toggle("active", hasMoreActive);

  if (!list.length) {
    grid.innerHTML = "";
    empty.classList.remove("hidden");
    return;
  }

  empty.classList.add("hidden");
  grid.innerHTML = list
    .map(
      (item) => `
      <button type="button" class="listing-card" data-id="${item.id}">
        <div class="card-photo-wrap">
          <img id="card-img-${item.id}" alt="${item.brand} ${item.model}" onerror="this.style.display='none'" />
          ${FALLBACK_CAR_SVG}
        </div>
        <div class="card-body">
          <div class="card-title-row">
            <h2 class="card-title">${item.brand} ${item.model}</h2>
            ${item.verified ? `<span class="trust-pill">${item.verifiedLabel}</span>` : ""}
          </div>
          <div class="card-metrics-row">
            <span>${item.year} 年</span>
            <span class="metric-sep">・</span>
            <span>${(item.mileageKm / 10000).toFixed(1)} 萬 km</span>
            <span class="metric-sep">・</span>
            <span>${item.powerType}</span>
          </div>
          <div class="card-price-row">
            <span class="card-price">${item.priceWan.toFixed(1)}<span class="card-price-unit">萬</span></span>
          </div>
        </div>
      </button>
    `
    )
    .join("");

  list.forEach((item) => {
    const imgEl = document.getElementById(`card-img-${item.id}`);
    if (imgEl) {
      imgEl.addEventListener("load", () => {
        const svg = imgEl.parentElement.querySelector(".card-photo-fallback");
        if (svg) svg.style.display = "none";
      });
      loadWikimediaPhoto(item.photoQuery, imgEl);
    }
  });

  grid.querySelectorAll(".listing-card").forEach((card) => {
    card.addEventListener("click", () => openDetailDrawer(card.dataset.id));
  });
}

function openDetailDrawer(id) {
  const item = LISTINGS.find((x) => x.id === id);
  if (!item) return;
  state.activeListingId = id;
  state.activeDetailTab = "specs";

  document.getElementById("detailHeaderMeta").innerHTML = `
    ${item.verified ? `<span class="trust-pill">${item.verifiedLabel}</span>` : ""}
    <span style="font-size:0.86rem;color:var(--text-stone);">${item.city}市在售</span>
  `;

  document.getElementById("detailTitle").textContent = `${item.brand} ${item.model}`;
  document.getElementById("detailSubtitle").textContent = `${item.gen} ・ ${item.year} 年出廠`;
  document.getElementById("detailPrice").textContent = `${item.priceWan.toFixed(1)} 萬`;
  document.getElementById("detailMsrp").textContent = `當年新車參考價 ${item.msrpWan.toFixed(1)} 萬`;
  document.getElementById("detailKeyStrip").textContent =
    `${item.year} 年 ・ ${(item.mileageKm / 10000).toFixed(1)} 萬公里 ・ ${item.powerType}`;

  const photoEl = document.getElementById("detailPhoto");
  photoEl.removeAttribute("src");
  photoEl.alt = `${item.brand} ${item.model}`;
  loadWikimediaPhoto(item.photoQuery, photoEl);

  updateCompareButtonText();
  renderDetailTab();

  const backdrop = document.getElementById("detailDrawerBackdrop");
  backdrop.classList.add("open");
  backdrop.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
}

function renderDetailTab() {
  const item = LISTINGS.find((x) => x.id === state.activeListingId);
  if (!item) return;

  document.querySelectorAll(".drawer-tab").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.tab === state.activeDetailTab);
  });

  const body = document.getElementById("detailTabBody");

  if (state.activeDetailTab === "specs") {
    const s = item.specs;
    const rows = [
      ["排氣量", s.displacement],
      ["最大馬力", s.horsepower],
      ["最大扭力", s.torque],
      ["變速箱", s.transmission],
      ["驅動方式", s.drivetrain],
      ["平均油耗", s.fuelEconomy],
      ["年度稅金 (牌照+燃料)", s.annualTax],
      ["車身尺碼", s.dimensions],
    ];
    body.innerHTML = `
      <div class="spec-table">
        ${rows
          .map(
            ([k, v]) => `
          <div class="spec-item">
            <div class="spec-k">${k}</div>
            <div class="spec-v">${v}</div>
          </div>`
          )
          .join("")}
      </div>
    `;
  } else if (state.activeDetailTab === "records") {
    body.innerHTML = `
      <div class="record-list">
        ${item.records
          .map(
            (r) => `
          <div class="record-card">
            <div class="record-head">
              <span>${r.title}</span>
              <span style="color:var(--green-forest);font-size:0.82rem;">${r.meta}</span>
            </div>
            <p class="record-note">${r.note}</p>
          </div>`
          )
          .join("")}
      </div>
    `;
  } else if (state.activeDetailTab === "features") {
    const f = item.features;
    const groups = [
      ["安全與輔助科技", f.safety],
      ["底盤與外觀配備", f.chassis],
      ["座艙與便利機能", f.interior],
    ];
    body.innerHTML = groups
      .map(
        ([label, items]) => `
        <div class="feature-group">
          <h4>${label}</h4>
          <div class="feature-pills">
            ${items.map((x) => `<span class="feature-pill">${x}</span>`).join("")}
          </div>
        </div>`
      )
      .join("");
  }
}

function updateCompareButtonText() {
  const btn = document.getElementById("btnToggleCompare");
  const inList = state.compareIds.includes(state.activeListingId);
  btn.textContent = inList ? "移出比較清單" : "加入比較清單";
}

function renderCompareDrawer() {
  const body = document.getElementById("compareBody");
  const items = LISTINGS.filter((x) => state.compareIds.includes(x.id));

  if (!items.length) {
    body.innerHTML = `<p style="color:var(--text-stone);">尚未加入比較車款。點擊任一車輛詳情頁下方的「加入比較清單」，最多可同時比較 3 輛。</p>`;
    return;
  }

  const rows = [
    ["售價", (x) => `${x.priceWan.toFixed(1)} 萬`],
    ["年份", (x) => `${x.year} 年`],
    ["里程", (x) => `${(x.mileageKm / 10000).toFixed(1)} 萬 km`],
    ["動力", (x) => x.powerType],
    ["排氣量", (x) => x.specs.displacement],
    ["變速箱", (x) => x.specs.transmission],
    ["油耗", (x) => x.specs.fuelEconomy],
    ["年稅金", (x) => x.specs.annualTax],
  ];

  body.innerHTML = `
    <div style="overflow-x:auto;">
      <table class="compare-table tabular">
        <thead>
          <tr>
            <th>項目</th>
            ${items.map((x) => `<td><strong style="font-family:var(--font-serif);">${x.brand} ${x.model}</strong></td>`).join("")}
          </tr>
        </thead>
        <tbody>
          ${rows
            .map(
              ([label, fn]) => `
            <tr>
              <th>${label}</th>
              ${items.map((x) => `<td>${fn(x)}</td>`).join("")}
            </tr>`
            )
            .join("")}
        </tbody>
      </table>
    </div>
  `;
}

function closeAllDrawers() {
  document.querySelectorAll(".drawer-backdrop").forEach((d) => {
    d.classList.remove("open");
    d.setAttribute("aria-hidden", "true");
  });
  document.body.style.overflow = "";
}

function resetFilters() {
  state.search = "";
  state.brand = "all";
  state.budget = "all";
  state.year = "all";
  state.city = "all";
  state.fuel = "all";
  state.trans = "all";
  state.sort = "default";
  state.verifiedOnly = false;

  document.getElementById("filterSearch").value = "";
  document.getElementById("filterBrand").value = "all";
  document.getElementById("filterBudget").value = "all";
  document.getElementById("filterYear").value = "all";
  document.getElementById("filterCity").value = "all";
  document.getElementById("filterFuel").value = "all";
  document.getElementById("filterTrans").value = "all";
  document.getElementById("filterSort").value = "default";
  document.getElementById("filterVerifiedOnly").checked = false;

  renderListings();
}

function initApp() {
  const brands = [...new Set(LISTINGS.map((x) => x.brand))];
  const brandSel = document.getElementById("filterBrand");
  brands.forEach((b) => {
    const opt = document.createElement("option");
    opt.value = b;
    opt.textContent = b;
    brandSel.appendChild(opt);
  });

  document.getElementById("filterSearch").addEventListener("input", (e) => {
    state.search = e.target.value.trim();
    renderListings();
  });

  [
    ["filterBrand", "brand"],
    ["filterBudget", "budget"],
    ["filterYear", "year"],
    ["filterCity", "city"],
  ].forEach(([elId, key]) => {
    document.getElementById(elId).addEventListener("change", (e) => {
      state[key] = e.target.value;
      renderListings();
    });
  });

  // 更多篩選抽屜
  document.getElementById("btnMoreFilters").addEventListener("click", () => {
    const d = document.getElementById("filterDrawerBackdrop");
    d.classList.add("open");
    d.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  });

  document.getElementById("btnApplyFilterDrawer").addEventListener("click", () => {
    state.fuel = document.getElementById("filterFuel").value;
    state.trans = document.getElementById("filterTrans").value;
    state.sort = document.getElementById("filterSort").value;
    state.verifiedOnly = document.getElementById("filterVerifiedOnly").checked;
    closeAllDrawers();
    renderListings();
  });

  document.getElementById("btnResetInDrawer").addEventListener("click", () => {
    resetFilters();
    closeAllDrawers();
  });
  document.getElementById("btnResetFilters").addEventListener("click", resetFilters);

  // 詳情抽屜頁籤
  document.querySelectorAll(".drawer-tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.activeDetailTab = btn.dataset.tab;
      renderDetailTab();
    });
  });

  document.getElementById("btnToggleCompare").addEventListener("click", () => {
    const id = state.activeListingId;
    if (!id) return;
    if (state.compareIds.includes(id)) {
      state.compareIds = state.compareIds.filter((x) => x !== id);
    } else if (state.compareIds.length < 3) {
      state.compareIds.push(id);
    } else {
      state.compareIds = [...state.compareIds.slice(1), id];
    }
    document.getElementById("compareCount").textContent = String(state.compareIds.length);
    updateCompareButtonText();
  });

  document.getElementById("btnReserveView").addEventListener("click", () => {
    const item = LISTINGS.find((x) => x.id === state.activeListingId);
    if (!item) return;
    const btn = document.getElementById("btnReserveView");
    btn.textContent = "已登記預約通知";
    setTimeout(() => {
      btn.textContent = "預約現場看車";
    }, 2200);
  });

  document.getElementById("btnCompareOpen").addEventListener("click", () => {
    renderCompareDrawer();
    const d = document.getElementById("compareDrawerBackdrop");
    d.classList.add("open");
    d.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  });

  ["btnCloseFilterDrawer", "btnCloseDetailDrawer", "btnCloseCompareDrawer"].forEach((id) => {
    document.getElementById(id).addEventListener("click", closeAllDrawers);
  });

  document.querySelectorAll(".drawer-backdrop").forEach((bd) => {
    bd.addEventListener("click", (e) => {
      if (e.target === bd) closeAllDrawers();
    });
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeAllDrawers();
  });

  renderListings();
}

document.addEventListener("DOMContentLoaded", initApp);
