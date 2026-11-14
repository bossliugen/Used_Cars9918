/**
 * 台灣中古車時價分析互動式 Canvas 圖表引擎（白底藍框簡約版）
 */

class MarketTrendChart {
  constructor(canvasId, tooltipId) {
    this.canvas = document.getElementById(canvasId);
    this.tooltip = document.getElementById(tooltipId);
    this.ctx = this.canvas.getContext("2d");
    this.timeline = [];
    this.mode = "price"; // 'price' | 'residual'
    this.selectedYear = null;
    this.hoverIndex = -1;
    this.pointsMeta = [];

    this._bindEvents();
  }

  setData(timeline, mode = "price", selectedYear = null) {
    this.timeline = timeline || [];
    this.mode = mode;
    this.selectedYear = selectedYear;
    this.hoverIndex = -1;
    this.render();
  }

  _bindEvents() {
    window.addEventListener("resize", () => this.render());

    this.canvas.addEventListener("mousemove", (e) => {
      if (!this.pointsMeta.length) return;
      const rect = this.canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;

      let closestIdx = -1;
      let minDist = Infinity;
      this.pointsMeta.forEach((pt, idx) => {
        const d = Math.abs(pt.x - mx);
        if (d < minDist) {
          minDist = d;
          closestIdx = idx;
        }
      });

      if (closestIdx !== -1 && minDist < 48) {
        if (this.hoverIndex !== closestIdx) {
          this.hoverIndex = closestIdx;
          this.render();
        }
        this._showTooltip(this.pointsMeta[closestIdx], e.clientX - rect.left, e.clientY - rect.top, rect.width);
      } else if (this.hoverIndex !== -1) {
        this.hoverIndex = -1;
        this.tooltip.style.display = "none";
        this.render();
      }
    });

    this.canvas.addEventListener("mouseleave", () => {
      this.hoverIndex = -1;
      this.tooltip.style.display = "none";
      this.render();
    });
  }

  _showTooltip(ptMeta, mouseX, mouseY, containerWidth) {
    const d = ptMeta.data;
    const majorTag = d.is_major_change
      ? `<span style="color:#1B4332;font-weight:700;"> ★ 大改款</span>`
      : "";
    const riskTag =
      d.alert_level === "high"
        ? `<div style="color:#991B1B;font-size:0.75rem;margin-top:4px;font-weight:600;">⚠ 高風險通病/殘值劇降區間</div>`
        : d.alert_level === "medium"
        ? `<div style="color:#B45309;font-size:0.75rem;margin-top:4px;font-weight:600;">● 需留意特定通病</div>`
        : "";

    this.tooltip.innerHTML = `
      <div style="font-weight:700;font-size:0.9rem;color:#1C1917;margin-bottom:2px;">
        ${d.year} 年式${majorTag}
      </div>
      <div style="color:#57534E;font-size:0.76rem;margin-bottom:7px;">${d.gen_name}</div>
      <div style="display:grid;grid-template-columns:1fr auto;gap:3px 14px;font-size:0.8rem;">
        <span style="color:#57534E;">當年新車 MSRP：</span><strong style="color:#1C1917;">${d.msrp.toFixed(1)} 萬</strong>
        <span style="color:#1B4332;">認證車商均價：</span><strong style="color:#143326;">${d.dealer.toFixed(1)} 萬 (${d.residual_dealer_pct}%)</strong>
        <span style="color:#40916C;">非第三方自售實價：</span><strong style="color:#2D6A4F;">${d.private.toFixed(1)} 萬 (${d.residual_private_pct}%)</strong>
        <span style="color:#B45309;">權威天書基準價：</span><strong style="color:#92400E;">${d.book.toFixed(1)} 萬 (${d.residual_book_pct}%)</strong>
        <span style="color:#57534E;">車商 / 自售價差：</span><span style="color:#1C1917;">+${d.dealer_private_spread_wan.toFixed(1)} 萬 (${d.dealer_private_spread_pct}%)</span>
      </div>
      ${riskTag}
    `;

    this.tooltip.style.display = "block";
    const tipW = this.tooltip.offsetWidth || 240;
    const left = mouseX + 16 + tipW > containerWidth ? mouseX - tipW - 14 : mouseX + 14;
    const top = Math.max(10, mouseY - 40);
    this.tooltip.style.left = `${left}px`;
    this.tooltip.style.top = `${top}px`;
  }

  render() {
    const parent = this.canvas.parentElement;
    if (!parent) return;

    const width = parent.clientWidth;
    const height = parent.clientHeight;
    const dpr = window.devicePixelRatio || 1;

    this.canvas.width = width * dpr;
    this.canvas.height = height * dpr;
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    const ctx = this.ctx;
    ctx.clearRect(0, 0, width, height);

    if (!this.timeline.length) return;

    const pad = { top: 34, right: 26, bottom: 40, left: 54 };
    const plotW = width - pad.left - pad.right;
    const plotH = height - pad.top - pad.bottom;

    let maxVal = 0;
    if (this.mode === "price") {
      this.timeline.forEach((d) => {
        maxVal = Math.max(maxVal, d.msrp, d.dealer, d.private, d.book);
      });
      maxVal = Math.ceil(maxVal / 20) * 20;
    } else {
      maxVal = 100;
    }
    const minVal = 0;

    const xAt = (i) => {
      if (this.timeline.length === 1) return pad.left + plotW / 2;
      return pad.left + (i / (this.timeline.length - 1)) * plotW;
    };
    const yAt = (v) => pad.top + plotH - ((v - minVal) / (maxVal - minVal)) * plotH;

    // 1. 高風險區間淡紅背景著色
    this.timeline.forEach((d, i) => {
      if (d.alert_level === "high") {
        const x = xAt(i);
        const step = this.timeline.length > 1 ? plotW / (this.timeline.length - 1) : plotW;
        const leftX = Math.max(pad.left, x - step / 2);
        const rightX = Math.min(pad.left + plotW, x + step / 2);
        ctx.fillStyle = "rgba(239, 68, 68, 0.08)";
        ctx.fillRect(leftX, pad.top, rightX - leftX, plotH);
      }
    });

    // 2. 水平格線與 Y 軸刻度
    const ticks = 5;
    ctx.font = "11px sans-serif";
    ctx.textAlign = "right";
    ctx.textBaseline = "middle";
    for (let t = 0; t <= ticks; t++) {
      const val = minVal + ((maxVal - minVal) * t) / ticks;
      const y = yAt(val);
      ctx.strokeStyle = "#e2e8f0";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(pad.left, y);
      ctx.lineTo(pad.left + plotW, y);
      ctx.stroke();

      ctx.fillStyle = "#64748b";
      const label = this.mode === "price" ? `${Math.round(val)}萬` : `${Math.round(val)}%`;
      ctx.fillText(label, pad.left - 8, y);
    }

    // 3. 大改款年份垂直虛線與標籤
    this.timeline.forEach((d, i) => {
      if (d.is_major_change) {
        const x = xAt(i);
        ctx.save();
        ctx.strokeStyle = "rgba(27, 67, 50, 0.4)";
        ctx.setLineDash([4, 4]);
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(x, pad.top);
        ctx.lineTo(x, pad.top + plotH);
        ctx.stroke();
        ctx.restore();

        ctx.fillStyle = "#1B4332";
        ctx.font = "600 11px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(`★ 大改款 ${d.year}`, x, pad.top - 14);
      }
    });

    // 4. 目前選擇年份高亮指示線
    this.timeline.forEach((d, i) => {
      if (this.selectedYear && d.year === this.selectedYear) {
        const x = xAt(i);
        ctx.save();
        ctx.strokeStyle = "rgba(27, 67, 50, 0.18)";
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(x, pad.top);
        ctx.lineTo(x, pad.top + plotH);
        ctx.stroke();
        ctx.restore();
      }
    });

    // 5. X 軸年份標籤
    ctx.font = "11px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "top";
    this.timeline.forEach((d, i) => {
      const x = xAt(i);
      const isSelected = this.selectedYear && d.year === this.selectedYear;
      ctx.fillStyle = isSelected ? "#1B4332" : "#57534E";
      ctx.font = isSelected ? "bold 12px sans-serif" : "11px sans-serif";
      if (this.timeline.length <= 14 || i % 2 === 0 || d.is_major_change || isSelected || i === this.timeline.length - 1) {
        ctx.fillText(String(d.year), x, pad.top + plotH + 10);
      }
    });

    // 6. 繪製折線與半透明填色
    const drawLine = (key, color, dashed = false, lineWidth = 2.8, fillArea = false) => {
      if (fillArea) {
        ctx.save();
        ctx.beginPath();
        this.timeline.forEach((d, i) => {
          const x = xAt(i);
          const y = yAt(d[key]);
          if (i === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        });
        ctx.lineTo(xAt(this.timeline.length - 1), pad.top + plotH);
        ctx.lineTo(xAt(0), pad.top + plotH);
        ctx.closePath();
        const grad = ctx.createLinearGradient(0, pad.top, 0, pad.top + plotH);
        grad.addColorStop(0, "rgba(27, 67, 50, 0.10)");
        grad.addColorStop(1, "rgba(27, 67, 50, 0.01)");
        ctx.fillStyle = grad;
        ctx.fill();
        ctx.restore();
      }

      ctx.save();
      ctx.strokeStyle = color;
      ctx.lineWidth = lineWidth;
      if (dashed) ctx.setLineDash([6, 4]);
      ctx.beginPath();
      this.timeline.forEach((d, i) => {
        const x = xAt(i);
        const y = yAt(d[key]);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      });
      ctx.stroke();
      ctx.restore();

      this.timeline.forEach((d, i) => {
        const x = xAt(i);
        const y = yAt(d[key]);
        const isSel = this.selectedYear && d.year === this.selectedYear;
        const r = this.hoverIndex === i || isSel ? 5.2 : 3.4;
        ctx.beginPath();
        ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff";
        ctx.fill();
        ctx.lineWidth = 2.2;
        ctx.strokeStyle = color;
        ctx.stroke();
      });
    };

    if (this.mode === "price") {
      drawLine("msrp", "#A8A29E", true, 1.8, false);
      drawLine("book", "#B45309", true, 2.2, false);
      drawLine("private", "#40916C", false, 2.6, false);
      drawLine("dealer", "#1B4332", false, 3.0, true);
    } else {
      drawLine("residual_book_pct", "#B45309", true, 2.2, false);
      drawLine("residual_private_pct", "#40916C", false, 2.6, false);
      drawLine("residual_dealer_pct", "#1B4332", false, 3.0, true);
    }

    if (this.hoverIndex >= 0 && this.hoverIndex < this.timeline.length) {
      const hx = xAt(this.hoverIndex);
      ctx.save();
      ctx.strokeStyle = "rgba(37, 99, 235, 0.35)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(hx, pad.top);
      ctx.lineTo(hx, pad.top + plotH);
      ctx.stroke();
      ctx.restore();
    }

    this.pointsMeta = this.timeline.map((d, i) => ({
      x: xAt(i),
      data: d,
    }));
  }
}
