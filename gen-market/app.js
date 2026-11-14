const CITIES = ["台北", "新北", "桃園", "台中", "台南", "高雄"];

const state = {
  listings: [],
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
  activeDetailTab: "trend",
  compareIds: [],
};

function classifyFuel(trim) {
  const txt = `${trim.trim_name} ${trim.engine_code}`.toLowerCase();
  if (txt.includes("hybrid") || txt.includes("e:hev") || txt.includes("油電")) return "油電";
  if (txt.includes("柴油") || txt.includes("tdci") || txt.includes("skyactiv-d")) return "柴油";
  if (txt.includes("渦輪") || txt.includes("tsi") || txt.includes("ecoboost") || txt.includes("1.4t") || txt.includes("1.5t") || txt.includes("2.0t")) return "渦輪";
  return "汽油";
}

function classifyTrans(transStr) {
  const t = String(transStr || "");
  if (t.includes("純手排") || t.includes("6MT")) return "手排";
  if (t.includes("雙離合") || t.includes("DSG") || t.includes("PowerShift")) return "雙離合";
  if (t.includes("CVT")) return "CVT";
  return "自排";
}

function buildListingsFromDb(db) {
  const items = [];
  let cityIdx = 0;

  db.cars.forEach((car) => {
    car.generations.forEach((gen) => {
      const baseMsrp = gen.trims?.[0]?.msrp_wan || 1;
      const pts = gen.year_points || [];
      if (!pts.length) return;

      // 每個世代挑選代表年式（最新與中段），每個版本各自獨立一筆
      const pickPts = pts.length > 3 ? [pts[Math.floor(pts.length / 2)], pts[pts.length - 1]] : [pts[pts.length - 1]];

      (gen.trims || []).forEach((trim, trimIdx) => {
        const ratio = trim.msrp_wan ? trim.msrp_wan / baseMsrp : 1.0;
        pickPts.forEach((pt) => {
          const priceWan = +(pt.dealer * ratio).toFixed(1);
          const mileageKm = Math.round(pt.age_years * 11500);
          const city = CITIES[cityIdx % CITIES.length];
          cityIdx += 1;

          const verified = gen.depreciation_alert.level === "low";
          const verifiedLabel = verified ? "已查驗" : gen.depreciation_alert.level === "medium" ? "實價趨勢" : "";

          items.push({
            id: `${car.id}-${gen.gen_id}-${pt.year}-${trimIdx}`,
            carId: car.id,
            brand: car.brand,
            model: car.model,
            category: car.category,
            summary: car.summary,
            genId: gen.gen_id,
            genName: gen.gen_name,
            year: pt.year,
            mileageKm,
            trimName: trim.trim_name,
            powerType: classifyFuel(trim),
            transType: classifyTrans(trim.transmission),
            city,
            priceWan,
            msrpWan: +(pt.msrp * ratio).toFixed(1),
            residualPct: pt.residual_dealer_pct,
            verified,
            verifiedLabel,
            photoUrl: `../assets/cars/${gen.gen_id}.jpg`,
            trim,
            gen,
            car,
            ratio,
          });
        });
      });
    });
  });

  return items;
}

function getFilteredListings() {
  let list = state.listings.filter((item) => {
    if (state.search) {
      const q = state.search.toLowerCase();
      const hay = `${item.brand} ${item.model} ${item.genName} ${item.trimName} ${item.city} ${item.powerType}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    if (state.brand !== "all" && item.brand !== state.brand) return false;
    if (state.city !== "all" && item.city !== state.city) return false;
    if (state.verifiedOnly && !item.verified) return false;
    if (state.fuel !== "all" && item.powerType !== state.fuel) return false;
    if (state.trans !== "all" && item.transType !== state.trans) return false;

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

  document.getElementById("resultCount").textContent = `共 ${list.length} 筆車源`;

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
    .slice(0, 60)
    .map(
      (item) => `
      <button type="button" class="listing-card" data-id="${item.id}">
        <div class="card-photo-wrap">
          <img src="${item.photoUrl}" alt="${item.brand} ${item.model}" loading="lazy" />
        </div>
        <div class="card-body">
          <div class="card-title-row">
            <h2 class="card-title">${item.brand} ${item.model} ${item.trimName}</h2>
            ${item.verifiedLabel ? `<span class="trust-pill">${item.verifiedLabel}</span>` : ""}
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

  grid.querySelectorAll(".listing-card").forEach((card) => {
    card.addEventListener("click", () => openDetailDrawer(card.dataset.id));
  });
}

function openDetailDrawer(id) {
  const item = state.listings.find((x) => x.id === id);
  if (!item) return;
  state.activeListingId = id;
  state.activeDetailTab = "trend";

  document.getElementById("detailHeaderMeta").innerHTML = `
    ${item.verifiedLabel ? `<span class="trust-pill">${item.verifiedLabel}</span>` : ""}
    <span style="font-size:0.86rem;color:var(--text-stone);">${item.city}市 ・ 殘值率 ${item.residualPct}%</span>
  `;

  document.getElementById("detailTitle").textContent = `${item.brand} ${item.model}`;
  document.getElementById("detailSubtitle").textContent = `${item.genName} ・ ${item.trimName}`;
  document.getElementById("detailPrice").textContent = `${item.priceWan.toFixed(1)} 萬`;
  document.getElementById("detailMsrp").textContent = `當年新車參考價 ${item.msrpWan.toFixed(1)} 萬`;
  document.getElementById("detailKeyStrip").textContent =
    `${item.year} 年 ・ ${(item.mileageKm / 10000).toFixed(1)} 萬公里 ・ ${item.powerType}`;

  const photoEl = document.getElementById("detailPhoto");
  photoEl.src = item.photoUrl;
  photoEl.alt = `${item.brand} ${item.model}`;

  updateCompareButtonText();
  renderDetailTab();

  const backdrop = document.getElementById("detailDrawerBackdrop");
  backdrop.classList.add("open");
  backdrop.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
}

function drawMiniTrendChart(canvas, item) {
  if (!canvas) return;
  const rect = canvas.parentElement.getBoundingClientRect();
  const width = Math.max(300, rect.width - 24);
  const height = 210;
  const dpr = window.devicePixelRatio || 1;
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, width, height);

  const timeline = item.car.timeline.map((pt) => {
    const r = pt.gen_id === item.genId ? item.ratio : 1.0;
    return {
      year: pt.year,
      dealer: +(pt.dealer * r).toFixed(1),
      private: +(pt.private * r).toFixed(1),
      msrp: +(pt.msrp * r).toFixed(1),
    };
  });
  if (!timeline.length) return;

  const pad = { top: 20, right: 16, bottom: 28, left: 46 };
  const plotW = width - pad.left - pad.right;
  const plotH = height - pad.top - pad.bottom;
  const maxVal = Math.ceil(Math.max(...timeline.map((d) => Math.max(d.msrp, d.dealer))) / 20) * 20;

  const xAt = (i) => (timeline.length === 1 ? pad.left + plotW / 2 : pad.left + (i / (timeline.length - 1)) * plotW);
  const yAt = (v) => pad.top + plotH - (v / maxVal) * plotH;

  ctx.font = "11px sans-serif";
  ctx.textAlign = "right";
  ctx.textBaseline = "middle";
  for (let t = 0; t <= 4; t++) {
    const val = (maxVal * t) / 4;
    const y = yAt(val);
    ctx.strokeStyle = "#DFD9CE";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(pad.left, y);
    ctx.lineTo(pad.left + plotW, y);
    ctx.stroke();
    ctx.fillStyle = "#57534E";
    ctx.fillText(`${Math.round(val)}萬`, pad.left - 6, y);
  }

  ctx.textAlign = "center";
  ctx.textBaseline = "top";
  timeline.forEach((d, i) => {
    if (timeline.length <= 10 || i % 2 === 0 || d.year === item.year || i === timeline.length - 1) {
      ctx.fillStyle = d.year === item.year ? "#1B4332" : "#78716C";
      ctx.fillText(String(d.year), xAt(i), pad.top + plotH + 8);
    }
  });

  const drawLine = (key, color, dashed = false) => {
    ctx.save();
    ctx.strokeStyle = color;
    ctx.lineWidth = dashed ? 1.5 : 2.5;
    if (dashed) ctx.setLineDash([5, 4]);
    ctx.beginPath();
    timeline.forEach((d, i) => {
      if (i === 0) ctx.moveTo(xAt(i), yAt(d[key]));
      else ctx.lineTo(xAt(i), yAt(d[key]));
    });
    ctx.stroke();
    ctx.restore();
  };

  drawLine("msrp", "#A8A29E", true);
  drawLine("private", "#40916C", false);
  drawLine("dealer", "#1B4332", false);
}

function renderDetailTab() {
  const item = state.listings.find((x) => x.id === state.activeListingId);
  if (!item) return;

  document.querySelectorAll(".drawer-tab").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.tab === state.activeDetailTab);
  });

  const body = document.getElementById("detailTabBody");

  if (state.activeDetailTab === "trend") {
    body.innerHTML = `
      <div class="drawer-chart-legend">
        <span><strong style="color:#1B4332;">—</strong> 認證車商均價</span>
        <span><strong style="color:#40916C;">—</strong> 民間自售實價</span>
        <span><strong style="color:#A8A29E;">--</strong> 當年新車 MSRP</span>
      </div>
      <div class="drawer-chart-box">
        <canvas id="drawerTrendCanvas"></canvas>
      </div>
      <div class="record-card">
        <div class="record-head">
          <span>${item.genName} 行情摘要</span>
          <span style="color:var(--green-forest);">殘值率 ${item.residualPct}%</span>
        </div>
        <p class="record-note">${item.gen.depreciation_alert.title} — ${item.gen.depreciation_alert.reason}</p>
      </div>
    `;
    requestAnimationFrame(() => drawMiniTrendChart(document.getElementById("drawerTrendCanvas"), item));
  } else if (state.activeDetailTab === "generations") {
    body.innerHTML = `
      <div class="record-list">
        ${item.car.generations
          .map((g) => {
            const yr = `${g.years[0]}–${g.years[g.years.length - 1]}`;
            const isCur = g.gen_id === item.genId;
            return `
            <div class="record-card ${isCur ? "active-gen" : ""}">
              <div class="record-head">
                <span>${g.gen_name}</span>
                <span style="color:var(--green-forest);">${yr}</span>
              </div>
              <p class="record-note">${g.major_change_note}</p>
            </div>`;
          })
          .join("")}
      </div>
    `;
  } else if (state.activeDetailTab === "specs") {
    const t = item.trim;
    const rows = [
      ["動力版本", t.trim_name],
      ["引擎形式", t.engine_code],
      ["排氣量", `${t.displacement_cc} cc`],
      ["最大馬力", t.horsepower],
      ["最大扭力", t.torque],
      ["變速箱", t.transmission],
      ["驅動方式", t.drivetrain],
      ["平均油耗", t.fuel_economy],
      ["年度稅金 (牌照+燃料)", `${t.annual_tax_ntd.toLocaleString()} 元`],
      ["車身尺碼", t.dimensions],
      ["安全配備", t.safety],
      ["產地 / 平台", `${item.gen.origin} / ${item.gen.platform}`],
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
  } else if (state.activeDetailTab === "maintenance") {
    const issues = item.gen.common_issues || [];
    body.innerHTML = `
      <div class="record-list">
        ${issues
          .map(
            (iss) => `
          <div class="record-card">
            <div class="record-head">
              <span>${iss.part}</span>
              <span style="color:var(--green-forest);">${iss.severity} ・ ${iss.mileage_range}</span>
            </div>
            <p class="record-note"><strong>症狀：</strong>${iss.symptom}</p>
            <p class="record-note" style="margin-top:4px;"><strong>預估維修：</strong>${iss.repair_cost_ntd}</p>
            <p class="record-note" style="margin-top:4px;"><strong>建議：</strong>${iss.advice}</p>
          </div>`
          )
          .join("")}
      </div>
    `;
  }
}

function updateCompareButtonText() {
  const btn = document.getElementById("btnToggleCompare");
  const inList = state.compareIds.includes(state.activeListingId);
  btn.textContent = inList ? "移出比較清單" : "加入比較清單";
}

function renderCompareDrawer() {
  const body = document.getElementById("compareBody");
  const items = state.listings.filter((x) => state.compareIds.includes(x.id));

  if (!items.length) {
    body.innerHTML = `<p style="color:var(--text-stone);">尚未加入比較車款。點擊任一車輛詳情頁下方的「加入比較清單」，最多可同時比較 3 輛。</p>`;
    return;
  }

  const rows = [
    ["售價", (x) => `${x.priceWan.toFixed(1)} 萬`],
    ["年份", (x) => `${x.year} 年`],
    ["里程", (x) => `${(x.mileageKm / 10000).toFixed(1)} 萬 km`],
    ["動力", (x) => x.powerType],
    ["排氣量", (x) => `${x.trim.displacement_cc} cc`],
    ["變速箱", (x) => x.trim.transmission],
    ["油耗", (x) => x.trim.fuel_economy],
    ["年稅金", (x) => `${x.trim.annual_tax_ntd.toLocaleString()} 元`],
  ];

  body.innerHTML = `
    <div style="overflow-x:auto;">
      <table class="compare-table tabular">
        <thead>
          <tr>
            <th>項目</th>
            ${items.map((x) => `<td><strong>${x.brand} ${x.model}</strong><br><small style="color:var(--text-stone);">${x.trimName}</small></td>`).join("")}
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

async function initApp() {
  try {
    const resp = await fetch("../data/cars_db.json");
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const db = await resp.json();
    state.listings = buildListingsFromDb(db);
  } catch (err) {
    document.getElementById("resultCount").textContent = "無法載入資料庫";
    return;
  }

  const brands = [...new Set(state.listings.map((x) => x.brand))];
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
