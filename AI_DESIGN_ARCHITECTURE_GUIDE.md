# 台灣中古車實價趨勢與世代資料庫 — AI 網站設計架構指引說明書

> **派發來源**：`E:\GoogleAntigravityCoding\品牌風格設計\DESIGN_SYSTEM.md`（經 Gemini 品牌設計對話彙總確立）  
> **目標專案**：`E:\GoogleAntigravityCoding\中古車網站時價分析及資料庫分析網站`（線上入口：`https://bossliugen.github.io/Used_Cars9918/`）  
> **技術架構**：Python 資料管線（`scripts/analyze_market.py` → `data/cars_db.json`）+ 原生 HTML/CSS/JS（`index.html`、`css/style.css`、`js/app.js`、`js/chart.js`）  
> **專案角色**：**03 / AUTO ARCHIVE — 冷靜購車研究圖鑑（專屬低飽和點綴色：`#7D8B82` 鼠尾草冷灰）**

---

## 1. 給本專案 AI 的核心任務定義

本專案目標是將台灣中古車市場（8891、認證車行、民間自售等）原本雜亂的資訊收斂為**高信任、冷靜、理性的購車研究與查價工具**。畫面必須像一本編輯嚴謹的汽車年鑑，讓買家在查價與比較世代差異時不被推銷感干擾。

---

## 2. 必須鎖死的 80% 品牌共享規範

1. **色票與表面系統（對齊 `css/style.css`）**：
   - 畫布 `#F6F3EC`、數據卡片 `#FFFFFF`、細線邊框 `1px solid #DFD9CE`（圓角 `16px`，禁止厚重陰影）。
   - 主文字 `#1C1917`、次要文字 `#57534E`、品牌主色 `#1B4332`（搭配 `#E7EFEA` 柔和鼠尾草綠底）、風險提醒 `#B45309` / `#991B1B`。
   - 領域專屬點綴色：`#7D8B82`（鼠尾草冷灰），全畫面佔比維持 `<= 5%`，僅用於車市趨勢次級標註或輔助線條。
2. **字型防呆與數字對齊**：
   - Top Bar 的 `GEN.` 字標使用 `Instrument Serif`（句點 `.` 為 `#1B4332`）。
   - 所有中文車名、世代標題與篩選膠囊**嚴禁套用 `serif`**，強制使用 `"Inter", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif`。
   - 所有價格（萬）、年份、里程（km）、折舊率與估算區間**必須使用等寬數字 `font-variant-numeric: tabular-nums`**（推薦搭配 `IBM Plex Mono`）。
3. **無留白橫向 2D SVG 圖示**：
   - 維持頂部單筆畫車頂弧線（roofline）＋ 3 節點世代時間軸 SVG（`viewBox="0 0 180 36"`，無背景方框）。

---

## 3. 本專案專屬 20% 架構與跨站整合指引

### A. 統一 Top Bar 與 Cross-Site Switcher（`index.html`）
- 確保頂部保持單行 `64px` 黏性導覽列：
  - 左側：`GEN.`（超連結回 `https://bossliugen.github.io/GENWeb/`）＋ 2D 車頂弧線 SVG ＋ 網站標題。
  - 右側：加入精簡的 **Cross-Site Switcher** 膠囊（`總門戶` / `中古車庫 [Active]` / `鏈上監測` / `F1 遙測`），當前頁以 `#1C1917` 或 `#1B4332` 實心標示，其餘為 `1px #DFD9CE` 邊框。

### B. 資訊架構與互動密度收斂
1. **單行 Sticky 篩選列**：保留搜尋框 + 4 個核心膠囊（品牌 / 預算 / 車齡 / 地區）+ 「更多篩選」收合抽屜，避免雙排、三排過載表單。
2. **4:3 實車卡片極簡原則**：
   - 僅保留：去背／實車照片、中文標題、**最多 1 個 `#1B4332` 實價徽章**、3 項核心數據（年份 / 里程 / 動力規格）與實價區間。
   - 嚴禁在卡片上堆滿 5–6 個彩色促銷標籤。
3. **右側側滑詳情抽屜（Slide-Over Drawer）**：
   - 點擊車款後展開：實價折舊趨勢圖（`js/chart.js`）、大改款世代沿革時間軸（例如 Focus MK3 vs MK3.5 vs MK4）、8891 等級規格表、通病與養車重點（用 `#B45309` / `#FEF3C7` 克制標示）。
   - **影音漏斗整合**：在抽屜底部與頁尾可預留連結至 YouTube `LOG 03 // 車市實價檔案` 播放清單（`https://www.youtube.com/channel/UC9vw9-i6Sgr1xZv1-2PwgDQ`），讓查價用戶延伸觀看該世代的影音實測與折舊分析。

### C. 統一精簡頁尾
- `1px solid #DFD9CE` 上邊線，左側 `© 2026 HIBOSS GEN. · 台灣`，右側純文字連結：`總門戶` · `YouTube` · `Instagram`。
