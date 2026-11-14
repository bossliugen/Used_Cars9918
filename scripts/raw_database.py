# -*- coding: utf-8 -*-
"""
台灣市售中古車資料庫核心定義檔 (涵蓋 2000 年至今歷代車型)
資料參考架構：
- 權威車訊（天書）：台灣中古車商、銀行車貸、保險理賠基準殘值
- 8891 中古車實價/估價大數據：市場流通刊登與成交價格區間、8891等級詳細規格
- SUM 賞車網 / HOT 大聯盟 / ABC 好車網：認證中古車商實車實價基準
- 非第三方交易紀錄：PTT CarShop、FB 車友社團、個人自售實際過戶行情
"""

DATA_SOURCES = [
    {
        "id": "8891",
        "name": "8891 中古車大數據",
        "type": "第三方交易平台",
        "credibility": "極高（全台最大流通車源與估價資料庫）",
        "description": "涵蓋全台車商與個人刊登之實價區間與線上估價模型，反映市場真實供需。"
    },
    {
        "id": "authority_book",
        "name": "權威車訊（天書）",
        "type": "業界公信力鑑價基準",
        "credibility": "極高（銀行車貸、保險理賠、車商收購標準）",
        "description": "台灣中古車界傳統基準，提供各年式與等級之標準收購與殘值參考價。"
    },
    {
        "id": "cpo_alliance",
        "name": "ABC好車網 / SUM / HOT認證",
        "type": "認證車商聯盟",
        "credibility": "高（含車況履歷、無重大事故泡水保證與保固）",
        "description": "具備第三方查定與四大保固之車商成交價，通常高於自售行情約 8%~14%。"
    },
    {
        "id": "private_direct",
        "name": "非第三方民間自售紀錄",
        "type": "個人自售 / 車友會 / PTT CarShop",
        "credibility": "中高（無車商管銷與保固加成之裸車過戶價）",
        "description": "反映車主直接過戶給買家的實際成交水位，介於天書收購價與車商售價之間。"
    }
]

CARS_DATABASE = [
    {
        "id": "ford-focus",
        "brand": "Ford",
        "model": "Focus",
        "model_zh": "福特 Focus",
        "category": "中型房車 / 五門掀背 / 旅行車",
        "summary": "台灣歐系操控代表車款。MK1/MK2 為傳統 4AT 時期但受老車漏水與環保線組影響殘值；MK3 (2012-2015) 因乾式雙離合器 PowerShift 災情導致殘值暴跌；MK3.5 改回 6AT 止穩，MK4 全面換裝 C2 平台與 8AT。",
        "generations": [
            {
                "gen_id": "focus-mk1",
                "gen_name": "MK1 第一代 (進口時期)",
                "years": [2001, 2002, 2003, 2004],
                "is_major_change": True,
                "major_change_year": 2001,
                "major_change_note": "2001年福特六和以歐洲進口導入第一代 Focus，採用 New Edge 銳利造型與後獨立多連桿底盤。",
                "platform": "Ford C170 歐系底盤",
                "origin": "德國原裝進口",
                "photo_query": "Ford Focus Mk1 hatchback front",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "早期進口老車 + 環保線組與冷卻老化，殘值已達報廢邊緣",
                    "reason": "車齡逾 22 年且歐洲進口料件取得不易，僅存代步殘值，購買前需確認冷卻系統與變速箱狀態。"
                },
                "trims": [
                    {
                        "trim_name": "1.6 / 2.0 Ghia (4AT)",
                        "msrp_wan": 68.9,
                        "engine_code": "Zetec-SE 1.6L / Zetec-E 2.0L 自然進氣",
                        "displacement_cc": 1989,
                        "horsepower": "130 ps / 5,500 rpm",
                        "torque": "18.1 kgm / 4,000 rpm",
                        "transmission": "4F27E 4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "12.5 km/L",
                        "dimensions": "4152 x 1699 x 1430 mm (軸距 2615 mm)",
                        "safety": "雙氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "引擎室環保線組脆化 / 節溫器座漏水",
                        "severity": "高風險",
                        "mileage_range": "車齡 10 年以上",
                        "symptom": "線組外皮剝落短路導致引擎不順、塑膠水座破裂大漏水。",
                        "repair_cost_ntd": "整理線組與水管約 1.2 ~ 2.5 萬",
                        "advice": "車齡極老，殘值低於維修費，僅建議當純代步練車。"
                    }
                ],
                "yearly_prices": {
                    "2001": {"msrp": 68.9, "dealer": 5.5, "private": 3.5, "book": 2.0},
                    "2002": {"msrp": 68.9, "dealer": 6.0, "private": 4.0, "book": 2.5},
                    "2003": {"msrp": 69.9, "dealer": 6.8, "private": 4.5, "book": 3.0},
                    "2004": {"msrp": 69.9, "dealer": 7.5, "private": 5.0, "book": 3.5}
                }
            },
            {
                "gen_id": "focus-mk2",
                "gen_name": "MK2 / MK2.5 第二代 (國產4AT/TDCi)",
                "years": [2005, 2006, 2007, 2008, 2009, 2010, 2011],
                "is_major_change": True,
                "major_change_year": 2005,
                "major_change_note": "2005年大改款並正式在台國產化，採 Volvo/Mazda 共用 C1 平台；汽油版採 4速手自排，2.0 TDCi 柴油版(MK2.5)改用濕式6速雙離合。",
                "platform": "Ford C1 平台（與 Mazda3 一代共用）",
                "origin": "台灣國產（福特六和）",
                "photo_query": "Ford Focus Mk2 facelift",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "當年國產操控佳作，但漏水/線組/4AT電磁閥老化拉低殘值",
                    "reason": "早期福特妥善率口碑尚未建立，加上車齡已高，民間自售僅約 5~11 萬元。"
                },
                "trims": [
                    {
                        "trim_name": "1.8 / 2.0 汽油 (4速手自排)",
                        "msrp_wan": 65.9,
                        "engine_code": "Duratec-HE 1.8L / 2.0L 自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "148 ps / 6,000 rpm",
                        "torque": "19.4 kgm / 4,500 rpm",
                        "transmission": "4F27E 4速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "13.2 km/L",
                        "dimensions": "4337 x 1839 x 1497 mm (軸距 2640 mm)",
                        "safety": "2~4氣囊、ESP (MK2.5高階)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "水箱副水箱裂縫漏水 / 儀表板焊點脫落",
                        "severity": "中風險",
                        "mileage_range": "8萬公里以上",
                        "symptom": "儀表突然全部亮燈熄火發不動（經典儀表冷焊通病）、副水箱滲水。",
                        "repair_cost_ntd": "儀表重焊約 2,500~4,000 元；水管整理約 5,000 元",
                        "advice": "1.8/2.0 汽油 4AT 比 MK3 乾式雙離合耐用很多，適合極低預算代步。"
                    },
                    {
                        "part": "4AT 變速箱換檔頓挫 / 節氣門積碳熄火",
                        "severity": "中風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "1-2檔頓挫明顯、停等紅燈怠速不穩。",
                        "repair_cost_ntd": "變速箱電磁閥整理約 6,000~12,000 元",
                        "advice": "購買時留意冷車入檔有無延遲或劇烈衝擊。"
                    }
                ],
                "yearly_prices": {
                    "2005": {"msrp": 63.9, "dealer": 8.0, "private": 5.5, "book": 3.5},
                    "2006": {"msrp": 63.9, "dealer": 8.8, "private": 6.2, "book": 4.2},
                    "2007": {"msrp": 64.9, "dealer": 9.8, "private": 7.0, "book": 5.0},
                    "2008": {"msrp": 65.9, "dealer": 10.8, "private": 8.0, "book": 5.8},
                    "2009": {"msrp": 65.9, "dealer": 12.0, "private": 9.0, "book": 6.8},
                    "2010": {"msrp": 67.9, "dealer": 13.5, "private": 10.2, "book": 7.8},
                    "2011": {"msrp": 67.9, "dealer": 14.8, "private": 11.5, "book": 9.0}
                }
            },
            {
                "gen_id": "focus-mk3",
                "gen_name": "MK3 第三代（乾式雙離合器）",
                "years": [2012, 2013, 2014, 2015],
                "is_major_change": True,
                "major_change_year": 2012,
                "major_change_note": "2012年底大改款 MK3，全面換裝 PowerShift 6速乾式雙離合器變速箱 (6DCT250)，與前代 MK2 4AT 結構完全不同。",
                "platform": "Ford Global C-Platform（歐系底盤）",
                "origin": "台灣國產（福特六和）",
                "photo_query": "Ford Focus Mk III",
                "depreciation_alert": {
                    "level": "high",
                    "title": "PowerShift 變速箱災情導致殘值劇烈崩跌區間 (2012–2015)",
                    "reason": "搭載 Getrag 6DCT250 PowerShift 乾式雙離合器，台灣都會區塞車易過熱、TCM 控制模組故障與離合器撥叉咬死，過保後維修動輒 4~8 萬元，造成車商收購意願低、二手殘值遠低於同級日系車。"
                },
                "trims": [
                    {
                        "trim_name": "1.6L 自然進氣 (4D/5D)",
                        "msrp_wan": 65.9,
                        "engine_code": "Ti-VCT 1.6L 直列四缸自然進氣",
                        "displacement_cc": 1596,
                        "horsepower": "125 ps / 6,300 rpm",
                        "torque": "16.2 kgm / 4,000 rpm",
                        "transmission": "PowerShift 6速乾式雙離合器自手排 (6DCT250)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "15.0 km/L",
                        "dimensions": "4358 x 1823 x 1484 mm (軸距 2648 mm)",
                        "safety": "4氣囊、ESP車身動態穩定、HSA斜坡起步"
                    },
                    {
                        "trim_name": "2.0L GDI 汽油運動型 (5D)",
                        "msrp_wan": 75.9,
                        "engine_code": "2.0L GDI 缸內直噴自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "170 ps / 6,600 rpm",
                        "torque": "20.6 kgm / 4,450 rpm",
                        "transmission": "PowerShift 6速乾式雙離合器自手排 (6DCT250)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "14.6 km/L",
                        "dimensions": "4358 x 1823 x 1484 mm (軸距 2648 mm)",
                        "safety": "4~6氣囊、ESP、ACS主動都會行車防護"
                    }
                ],
                "common_issues": [
                    {
                        "part": "PowerShift 6DCT250 變速箱 (TCM與離合器)",
                        "severity": "高風險",
                        "mileage_range": "6萬 ~ 12萬公里",
                        "symptom": "低速起步嚴重抖動、換檔異音、行駛中突跳「變速箱故障」鎖檔或失去動力（無法入R/D檔）。",
                        "repair_cost_ntd": "TCM 模組約 1.8~2.8 萬；離合器總成+撥叉約 3.5~5.5 萬",
                        "advice": "買前務必查詢原廠 TCM 延保更換紀錄，試車時特別測試塞車蠕行與倒車反應。"
                    },
                    {
                        "part": "節溫器座 / 副水箱漏水",
                        "severity": "中風險",
                        "mileage_range": "8萬公里以上",
                        "symptom": "冷卻液異常減少、水溫過高警告。",
                        "repair_cost_ntd": "3,500 ~ 8,000 元",
                        "advice": "檢查副水箱接縫與水管接頭有無水漬。"
                    }
                ],
                "yearly_prices": {
                    "2012": {"msrp": 75.9, "dealer": 15.5, "private": 12.0, "book": 10.0},
                    "2013": {"msrp": 75.9, "dealer": 17.5, "private": 13.8, "book": 11.5},
                    "2014": {"msrp": 75.9, "dealer": 19.8, "private": 15.8, "book": 13.5},
                    "2015": {"msrp": 75.9, "dealer": 22.5, "private": 18.2, "book": 15.5}
                }
            },
            {
                "gen_id": "focus-mk35",
                "gen_name": "MK3.5 第三代小改款 (改回6AT)",
                "years": [2016, 2017, 2018],
                "is_major_change": False,
                "major_change_year": 2016,
                "major_change_note": "小改款（馬丁頭外觀），汽油車型全面「取消」乾式雙離合器，改用 SelectShift 6速傳統手自排與 1.5L EcoBoost 渦輪引擎。",
                "platform": "Ford Global C-Platform（小改款優化）",
                "origin": "台灣國產（福特六和）",
                "photo_query": "Ford Focus Mk3 facelift",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "放棄雙離合改回 6AT，殘值明顯較 MK3 穩定",
                    "reason": "1.5T 與 1.6L 全面改搭傳統液力變矩器 6速手自排，徹底解決 MK3 變速箱痛點，但因車系受前期口碑連累，中古車價仍具極高性價比。"
                },
                "trims": [
                    {
                        "trim_name": "1.5L EcoBoost 180 時尚/頂級運動型",
                        "msrp_wan": 89.9,
                        "engine_code": "EcoBoost 180 1.5L 直列四缸缸內直噴渦輪",
                        "displacement_cc": 1498,
                        "horsepower": "180 ps / 6,000 rpm",
                        "torque": "24.5 kgm / 1,600~5,000 rpm",
                        "transmission": "SelectShift 6速手自排（傳統自排）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "15.0 km/L",
                        "dimensions": "4360 x 1823 x 1470 mm (軸距 2648 mm)",
                        "safety": "6氣囊、ESP、ACS都會煞停、BLIS盲點偵測"
                    }
                ],
                "common_issues": [
                    {
                        "part": "1.5T 缸內直噴積碳與廢油氣",
                        "severity": "中風險",
                        "mileage_range": "6萬 ~ 10萬公里",
                        "symptom": "怠速微抖、油耗變差、冷車啟動不順。",
                        "repair_cost_ntd": "核桃沙清積碳約 6,000 ~ 10,000 元",
                        "advice": "建議定期清洗進氣道與節氣門。"
                    },
                    {
                        "part": "冷卻系統水管接頭 / 渦輪水塞滲漏",
                        "severity": "中風險",
                        "mileage_range": "7萬公里以上",
                        "symptom": "副水箱水位緩慢下降，引擎室有水箱精甜味。",
                        "repair_cost_ntd": "4,000 ~ 9,000 元",
                        "advice": "看車時檢查副水箱刻度與底部護板乾爽度。"
                    }
                ],
                "yearly_prices": {
                    "2016": {"msrp": 89.9, "dealer": 33.0, "private": 28.2, "book": 25.0},
                    "2017": {"msrp": 89.9, "dealer": 37.5, "private": 32.5, "book": 29.0},
                    "2018": {"msrp": 89.9, "dealer": 42.0, "private": 36.8, "book": 33.0}
                }
            },
            {
                "gen_id": "focus-mk4",
                "gen_name": "MK4 / MK4.5 第四代（全新C2平台）",
                "years": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2019,
                "major_change_note": "2019年大改款！換裝全新 C2 模組化底盤、1.5L EcoBoost 三缸渦輪引擎、旋鈕式 8速手自排及 Co-Pilot360 Level 2；2023年推出 MK4.5 並國產化 Wagon 旅行車。",
                "platform": "Ford C2 模組化底盤（高剛性輕量化）",
                "origin": "台灣國產（福特六和）/ ST 為德國進口",
                "photo_query": "Ford Focus Mk4",
                "depreciation_alert": {
                    "level": "low",
                    "title": "科技配備滿載且保值度大幅回升，需留意濕式正時皮帶保養",
                    "reason": "Level 2 輔助駕駛與強勁動力讓市場需求大增，Wagon 車型尤其搶手。但 1.5T 三缸引擎採用濕式正時皮帶設計，車況保養紀錄對殘值影響極大。"
                },
                "trims": [
                    {
                        "trim_name": "1.5L EcoBoost 182 ST-Line / Lommel",
                        "msrp_wan": 92.8,
                        "engine_code": "1.5L EcoBoost 三缸渦輪增壓（雙噴射）",
                        "displacement_cc": 1497,
                        "horsepower": "182 ps / 6,000 rpm",
                        "torque": "24.5 kgm / 1,600~4,500 rpm",
                        "transmission": "SelectShift 8速手自排（旋鈕式）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿 (ST-Line)",
                        "fuel_economy": "16.7 ~ 17.6 km/L",
                        "dimensions": "4378 x 1825 x 1480 mm (軸距 2700 mm)",
                        "safety": "6氣囊、Co-Pilot360 Level 2 (全速域ACC+車道置中)"
                    },
                    {
                        "trim_name": "MK4.5 Wagon ST-Line Vignale (2023+)",
                        "msrp_wan": 105.9,
                        "engine_code": "1.5L EcoBoost 三缸渦輪增壓",
                        "displacement_cc": 1497,
                        "horsepower": "182 ps / 6,000 rpm",
                        "torque": "24.5 kgm / 1,600~4,500 rpm",
                        "transmission": "SelectShift 8速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿 (SLA)",
                        "fuel_economy": "15.4 km/L",
                        "dimensions": "4672 x 1825 x 1469 mm (軸距 2700 mm)",
                        "safety": "6氣囊、Co-Pilot360、Matrix LED矩陣式頭燈"
                    }
                ],
                "common_issues": [
                    {
                        "part": "濕式正時皮帶（泡機油設計）",
                        "severity": "高風險",
                        "mileage_range": "8萬 ~ 12萬公里（或未按規範換油）",
                        "symptom": "皮帶橡膠剝落阻塞機油濾網，嚴重時機油壓力不足導致引擎損壞。",
                        "repair_cost_ntd": "預防性更換皮帶與清洗油底殼約 1.8 ~ 2.8 萬",
                        "advice": "必須確認前車主皆使用原廠認證機油且準時保養，建議每 5,000~7,500 公里換油。"
                    },
                    {
                        "part": "8AT 變速箱低速頓挫",
                        "severity": "中風險",
                        "mileage_range": "全里程",
                        "symptom": "市區 1-2 檔或倒檔切換偶發頓挫感。",
                        "repair_cost_ntd": "軟體升級/適應值歸零約 0 ~ 3,000 元",
                        "advice": "屬變速箱邏輯特性，試駕時確認無異常滑差或金屬敲擊聲即可。"
                    }
                ],
                "yearly_prices": {
                    "2019": {"msrp": 89.8, "dealer": 46.5, "private": 41.5, "book": 38.0},
                    "2020": {"msrp": 92.8, "dealer": 51.5, "private": 46.0, "book": 42.5},
                    "2021": {"msrp": 92.8, "dealer": 56.5, "private": 51.0, "book": 47.0},
                    "2022": {"msrp": 94.8, "dealer": 62.0, "private": 56.0, "book": 51.5},
                    "2023": {"msrp": 99.9, "dealer": 72.0, "private": 65.5, "book": 60.5},
                    "2024": {"msrp": 105.9, "dealer": 80.5, "private": 74.0, "book": 68.5},
                    "2025": {"msrp": 105.9, "dealer": 88.0, "private": 81.5, "book": 76.0}
                }
            }
        ]
    },
    {
        "id": "toyota-altis",
        "brand": "Toyota",
        "model": "Corolla Altis",
        "model_zh": "豐田 Corolla Altis",
        "category": "中型房車（國民神車）",
        "summary": "台灣市佔率最高的中型房車，自 2001 年第 9 代國產化起即稱霸車壇。9代/10代以 4AT 耐操著稱；10.5代(2010)換裝 CVT；11代後期(2017)補齊 6氣囊+VSC；12代(2019+)全面進化為 TNGA 雙A臂底盤與油電。",
        "generations": [
            {
                "gen_id": "altis-9",
                "gen_name": "第 9 代 (E120 首代國產神車)",
                "years": [2001, 2002, 2003, 2004, 2005, 2006, 2007],
                "is_major_change": True,
                "major_change_year": 2001,
                "major_change_note": "2001年和泰國瑞首度國產化 Corolla Altis，搭載 1ZZ-FE 1.8L + 4AT，一舉取代 Sentra 成為台灣銷售冠軍。",
                "platform": "Toyota MC 平台",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Corolla E120 sedan",
                "depreciation_alert": {
                    "level": "low",
                    "title": "20年以上老車仍具極佳流通性與零件便宜優勢",
                    "reason": "結構極度單純耐用，至今仍有大量外銷非洲/中東零件與代步需求，自售 6~11 萬極好脫手。"
                },
                "trims": [
                    {
                        "trim_name": "1.8E / 1.8J (4AT)",
                        "msrp_wan": 63.9,
                        "engine_code": "1ZZ-FE 1.8L VVT-i 自然進氣",
                        "displacement_cc": 1794,
                        "horsepower": "136 ps / 6,000 rpm",
                        "torque": "17.4 kgm / 4,200 rpm",
                        "transmission": "4速自排 (U341E)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後拖曳臂",
                        "fuel_economy": "14.5 km/L",
                        "dimensions": "4530 x 1705 x 1480 mm (軸距 2600 mm)",
                        "safety": "雙氣囊、ABS（無VSC）"
                    }
                ],
                "common_issues": [
                    {
                        "part": "中控台環保材質龜裂出油 / 高里程吃機油",
                        "severity": "一般耗材",
                        "mileage_range": "15萬公里以上",
                        "symptom": "前擋下中控台老化黏手龜裂、20萬公里以上汽門油封微吃機油。",
                        "repair_cost_ntd": "避光墊遮蓋即可；4AT 幾乎不會壞",
                        "advice": "注意檢查是否曾為營業計程車改回自用（檢查車門內框與里程紀錄）。"
                    }
                ],
                "yearly_prices": {
                    "2001": {"msrp": 63.9, "dealer": 8.0, "private": 5.5, "book": 3.5},
                    "2002": {"msrp": 63.9, "dealer": 8.8, "private": 6.2, "book": 4.0},
                    "2003": {"msrp": 63.9, "dealer": 9.8, "private": 7.0, "book": 4.8},
                    "2004": {"msrp": 63.9, "dealer": 10.8, "private": 8.0, "book": 5.5},
                    "2005": {"msrp": 64.9, "dealer": 11.8, "private": 9.0, "book": 6.5},
                    "2006": {"msrp": 64.9, "dealer": 13.0, "private": 10.0, "book": 7.5},
                    "2007": {"msrp": 65.9, "dealer": 14.5, "private": 11.2, "book": 8.5}
                }
            },
            {
                "gen_id": "altis-10",
                "gen_name": "第 10 代 / 10.5 代 (E140)",
                "years": [2008, 2009, 2010, 2011, 2012],
                "is_major_change": True,
                "major_change_year": 2008,
                "major_change_note": "2008年大改款10代(前期4AT)；2010年中推出 10.5代小改款，引擎換裝 2ZR-FE 雙VVT-i 並首度導入 Super CVT-i 變速箱。",
                "platform": "Toyota MC 平台",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Corolla Altis E140",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極高保值度，10.5代(2010+) CVT 省油表現大幅提升",
                    "reason": "零件滿街都是、保養極便宜，是台灣 15~25 萬預算區間最熱門代步首選。"
                },
                "trims": [
                    {
                        "trim_name": "1.8E / 1.8Z (10代4AT / 10.5代CVT)",
                        "msrp_wan": 67.9,
                        "engine_code": "1ZZ-FE (08-10) / 2ZR-FE (10.5代)",
                        "displacement_cc": 1798,
                        "horsepower": "132 ps (前期) / 140 ps (10.5代)",
                        "torque": "17.3 kgm / 17.6 kgm",
                        "transmission": "4AT (前期) / Super CVT-i (10.5代)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後拖曳臂",
                        "fuel_economy": "18.2 km/L (美規)",
                        "dimensions": "4540 x 1760 x 1465 mm (軸距 2600 mm)",
                        "safety": "2氣囊、ABS (全車系無VSC)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "電子方向機柱「叩」異音 / 冷氣繼電器",
                        "severity": "低風險",
                        "mileage_range": "8萬公里以上",
                        "symptom": "轉動方向盤時傳出輕微齒輪間隙聲、冷氣突不冷。",
                        "repair_cost_ntd": "方向機柱減震橡皮約 1,500 元；繼電器約 800 元",
                        "advice": "都是花幾千元就能根治的小問題。"
                    }
                ],
                "yearly_prices": {
                    "2008": {"msrp": 65.9, "dealer": 16.0, "private": 13.0, "book": 10.5},
                    "2009": {"msrp": 65.9, "dealer": 17.8, "private": 14.5, "book": 12.0},
                    "2010": {"msrp": 66.9, "dealer": 20.0, "private": 16.5, "book": 13.8},
                    "2011": {"msrp": 67.9, "dealer": 22.0, "private": 18.5, "book": 15.5},
                    "2012": {"msrp": 68.9, "dealer": 24.5, "private": 20.8, "book": 17.8}
                }
            },
            {
                "gen_id": "altis-11",
                "gen_name": "第 11 代（含 11.5 代小改款）",
                "years": [2013, 2014, 2015, 2016, 2017, 2018],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "2013年10月大改款第11代；2016年底(2017年式)小改款將 VSC/TRC 與 6氣囊下放，安全性與前期完全不同。",
                "platform": "Toyota MC 平台（後拖曳臂非獨立懸吊）",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Corolla Altis E170",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極度抗跌的市場基準指標，但須區分 2017 年式安全分水嶺",
                    "reason": "妥善率高且計程車/營業用需求大，殘值率長期居同級之冠；但 2013-2016 前期多數僅 2 氣囊且無 VSC，買家建議優先鎖定 2017 年後小改款。"
                },
                "trims": [
                    {
                        "trim_name": "1.8L 經典/豪華版 (2013-2016 前期)",
                        "msrp_wan": 69.9,
                        "engine_code": "2ZR-FE 1.8L Dual VVT-i 自然進氣",
                        "displacement_cc": 1798,
                        "horsepower": "140 ps / 6,400 rpm",
                        "torque": "17.6 kgm / 4,000 rpm",
                        "transmission": "Super CVT-i 無段變速（模擬7速）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑(拖曳臂)",
                        "fuel_economy": "19.4 km/L (美規)",
                        "dimensions": "4620 x 1775 x 1460 mm (軸距 2700 mm)",
                        "safety": "2氣囊、ABS/EBD（多數車型無 VSC 穩定系統）"
                    },
                    {
                        "trim_name": "1.8L 豪華版 (2017-2018 11.5代小改款)",
                        "msrp_wan": 73.9,
                        "engine_code": "2ZR-FE 1.8L Dual VVT-i 自然進氣",
                        "displacement_cc": 1798,
                        "horsepower": "140 ps / 6,400 rpm",
                        "torque": "17.6 kgm / 4,000 rpm",
                        "transmission": "Super CVT-i 無段變速（模擬7速）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑(拖曳臂)",
                        "fuel_economy": "15.6 km/L (歐規)",
                        "dimensions": "4620 x 1775 x 1460 mm (軸距 2700 mm)",
                        "safety": "6氣囊、VSC 車身穩定、TRC 循跡防滑"
                    }
                ],
                "common_issues": [
                    {
                        "part": "冷氣壓縮機繼電器故障",
                        "severity": "低風險",
                        "mileage_range": "5萬 ~ 10萬公里",
                        "symptom": "行駛中冷氣突然送風不冷。",
                        "repair_cost_ntd": "原廠改良版繼電器約 500 ~ 1,200 元",
                        "advice": "更換改良型繼電器即可根治，成本極低。"
                    },
                    {
                        "part": "Super CVT-i 變速箱高里程異音/抖動",
                        "severity": "中風險",
                        "mileage_range": "12萬公里以上",
                        "symptom": "低速加速微幅抖動或鋼帶哨音。",
                        "repair_cost_ntd": "整理變速箱約 2.5 ~ 4.0 萬",
                        "advice": "注意有無定期更換 CVT 專用油，並留意是否曾為營業計程車。"
                    }
                ],
                "yearly_prices": {
                    "2013": {"msrp": 69.9, "dealer": 26.5, "private": 23.0, "book": 20.0},
                    "2014": {"msrp": 69.9, "dealer": 29.0, "private": 25.2, "book": 22.0},
                    "2015": {"msrp": 69.9, "dealer": 32.0, "private": 28.0, "book": 24.8},
                    "2016": {"msrp": 71.9, "dealer": 35.5, "private": 31.2, "book": 27.8},
                    "2017": {"msrp": 73.9, "dealer": 40.5, "private": 36.0, "book": 32.5},
                    "2018": {"msrp": 73.9, "dealer": 44.5, "private": 39.8, "book": 36.0}
                }
            },
            {
                "gen_id": "altis-12",
                "gen_name": "第 12 代（TNGA 平台）",
                "years": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2019,
                "major_change_note": "2019年3月大改款第12代！換裝 TNGA (GA-C) 模組化底盤、後懸吊改為獨立雙A臂、標配 7氣囊與 TSS 主動安全，並首度推出 1.8L Hybrid 油電版。",
                "platform": "Toyota TNGA GA-C 高剛性底盤",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Corolla E210 sedan",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極高保值神車，油電 Hybrid 版殘值尤佳",
                    "reason": "結合 TNGA 操控體質、TSS 2.0 輔助駕駛與極低油耗，二手市場接手度極高，折舊曲線極為平緩。"
                },
                "trims": [
                    {
                        "trim_name": "1.8L 汽油豪華/尊爵",
                        "msrp_wan": 77.8,
                        "engine_code": "2ZR-FE 1.8L 直列四缸自然進氣",
                        "displacement_cc": 1798,
                        "horsepower": "140 ps / 6,400 rpm",
                        "torque": "17.6 kgm / 4,000 rpm",
                        "transmission": "Super CVT-i 無段變速（模擬7速）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "14.9 km/L",
                        "dimensions": "4630 x 1780 x 1435 mm (軸距 2700 mm)",
                        "safety": "7氣囊、TSS 2.0 (ACC+LTA車道維持)"
                    },
                    {
                        "trim_name": "1.8L Hybrid 油電尊爵/旗艦",
                        "msrp_wan": 89.8,
                        "engine_code": "2ZR-FXE 1.8L Atkinson循環 + 電動馬達",
                        "displacement_cc": 1798,
                        "horsepower": "綜效馬力 122 ps",
                        "torque": "引擎14.5 kgm + 馬達16.6 kgm",
                        "transmission": "E-CVT 電子無段變速系統",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "25.2 ~ 25.8 km/L",
                        "dimensions": "4630 x 1780 x 1435 mm (軸距 2700 mm)",
                        "safety": "7氣囊、TSS 2.0、大電池原廠8年/16萬公里保固"
                    }
                ],
                "common_issues": [
                    {
                        "part": "前傳動軸/底盤低速「叩」異音",
                        "severity": "低風險",
                        "mileage_range": "3萬 ~ 8萬公里",
                        "symptom": "起步或低速加減速轉換時底盤傳出輕微「叩」一聲。",
                        "repair_cost_ntd": "原廠技術通報打膠或更換墊片處理（約 0 ~ 3,000 元）",
                        "advice": "屬常見小問題，不影響行車安全。"
                    }
                ],
                "yearly_prices": {
                    "2019": {"msrp": 79.8, "dealer": 50.5, "private": 45.8, "book": 42.0},
                    "2020": {"msrp": 79.8, "dealer": 54.0, "private": 49.2, "book": 45.5},
                    "2021": {"msrp": 81.8, "dealer": 58.0, "private": 53.0, "book": 49.0},
                    "2022": {"msrp": 84.5, "dealer": 62.5, "private": 57.5, "book": 53.5},
                    "2023": {"msrp": 86.5, "dealer": 67.5, "private": 62.0, "book": 58.0},
                    "2024": {"msrp": 88.5, "dealer": 73.0, "private": 67.5, "book": 63.0},
                    "2025": {"msrp": 88.5, "dealer": 78.5, "private": 73.0, "book": 68.5}
                }
            }
        ]
    },
    {
        "id": "vw-golf",
        "brand": "Volkswagen",
        "model": "Golf",
        "model_zh": "福斯 Golf",
        "category": "進口中型掀背車",
        "summary": "歐系鋼砲與掀背指標。MK4/MK5 時期有環保材質天篷與 09G 變速箱老化；MK6 與 MK7 前期因 DQ200 乾式雙離合閥體災情導致折舊較高；MK7.5 改良後穩定度提升，MK8 導入 48V 輕油電。",
        "generations": [
            {
                "gen_id": "golf-mk4",
                "gen_name": "MK4 第四代 (經典歐系老鋼砲)",
                "years": [2000, 2001, 2002, 2003],
                "is_major_change": True,
                "major_change_year": 2000,
                "major_change_note": "PQ34 平台，台灣引進 1.6 / 2.0 4AT 及 1.8T GTI 手排，無雙離合器但老車電子與內裝環保材質老化明顯。",
                "platform": "VW PQ34 平台",
                "origin": "德國原裝進口",
                "photo_query": "Volkswagen Golf IV front",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "老歐系車環保內裝脫落 + 4AT 過熱風險，殘值約 5~9 萬",
                    "reason": "車齡超過 22 年，雖無 DSG 災情但冷卻管路、車窗升降機與環保漆老化維修成本高於車價。"
                },
                "trims": [
                    {
                        "trim_name": "1.6 / 2.0 4AT",
                        "msrp_wan": 88.0,
                        "engine_code": "1.6L / 2.0L SOHC 自然進氣",
                        "displacement_cc": 1984,
                        "horsepower": "115 ps / 5,200 rpm",
                        "torque": "17.3 kgm / 2,400 rpm",
                        "transmission": "01M 4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "11.8 km/L",
                        "dimensions": "4149 x 1735 x 1444 mm (軸距 2511 mm)",
                        "safety": "4氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "車窗升降機塑膠滑塊斷裂 / 天篷脫落 / 01M變速箱過熱",
                        "severity": "高風險",
                        "mileage_range": "車齡 12 年以上",
                        "symptom": "車窗玻璃突然掉進門板、頂篷下垂、高溫塞車鎖3檔。",
                        "repair_cost_ntd": "升降機約 3,500 元；變速箱整理 2.5 萬起",
                        "advice": "除非玩手排 1.8T GTI 情懷，一般代步不建議選這麼老的歐系車。"
                    }
                ],
                "yearly_prices": {
                    "2000": {"msrp": 85.0, "dealer": 6.5, "private": 4.2, "book": 2.5},
                    "2001": {"msrp": 85.0, "dealer": 7.0, "private": 4.8, "book": 3.0},
                    "2002": {"msrp": 88.0, "dealer": 7.8, "private": 5.5, "book": 3.5},
                    "2003": {"msrp": 88.0, "dealer": 8.8, "private": 6.2, "book": 4.2}
                }
            },
            {
                "gen_id": "golf-mk5",
                "gen_name": "MK5 第五代 (PQ35 後獨立懸吊)",
                "years": [2004, 2005, 2006, 2007, 2008, 2009],
                "is_major_change": True,
                "major_change_year": 2004,
                "major_change_note": "2004年大改款換裝 PQ35 平台（後懸吊升級獨立多連桿），前期 1.6/2.0 FSI 採愛信 6速自排，GTI 與 TDI 首度導入濕式 6速 DSG。",
                "platform": "VW PQ35 平台",
                "origin": "德國原裝進口",
                "photo_query": "Volkswagen Golf V front",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "PQ35 操控大躍進，但 09G 閥體與 1.4 雙增壓通病拉低殘值",
                    "reason": "後期 1.4 TSI 雙增壓引擎(170hp)容易活塞環斷裂吃機油；1.6 自然進氣雖慢但相對耐操。"
                },
                "trims": [
                    {
                        "trim_name": "1.6 / 2.0 FSI (6AT) / 2.0 GTI (DQ250)",
                        "msrp_wan": 99.8,
                        "engine_code": "1.6L NA / 2.0L EA113 渦輪 (GTI)",
                        "displacement_cc": 1595,
                        "horsepower": "102 ps (1.6) / 200 ps (GTI)",
                        "torque": "15.1 kgm / 28.6 kgm",
                        "transmission": "09G 6速手自排 (1.6) / DQ250 6速濕式 DSG (GTI)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "12.5 km/L",
                        "dimensions": "4204 x 1759 x 1479 mm (軸距 2578 mm)",
                        "safety": "6氣囊、ESP"
                    }
                ],
                "common_issues": [
                    {
                        "part": "09G 6速自排閥體頓挫 / 1.4 雙增壓活塞問題",
                        "severity": "高風險",
                        "mileage_range": "8萬 ~ 13萬公里",
                        "symptom": "熱車換檔劇烈頓挫（閥體油壓不足）；1.4 雙增壓失火吃機油。",
                        "repair_cost_ntd": "閥體翻修約 2.0 ~ 3.0 萬；GTI 凸輪軸頂筒檢查",
                        "advice": "MK5 建議買單純的 1.6L 或體質好的 GTI，避開早期 1.4 雙增壓。"
                    }
                ],
                "yearly_prices": {
                    "2004": {"msrp": 92.0, "dealer": 10.0, "private": 7.2, "book": 5.0},
                    "2005": {"msrp": 92.0, "dealer": 11.2, "private": 8.2, "book": 5.8},
                    "2006": {"msrp": 95.0, "dealer": 12.5, "private": 9.2, "book": 6.8},
                    "2007": {"msrp": 96.0, "dealer": 14.0, "private": 10.5, "book": 8.0},
                    "2008": {"msrp": 98.0, "dealer": 15.5, "private": 11.8, "book": 9.2},
                    "2009": {"msrp": 99.8, "dealer": 17.0, "private": 13.0, "book": 10.5}
                }
            },
            {
                "gen_id": "golf-mk6",
                "gen_name": "MK6 第六代 (早期DQ200災情)",
                "years": [2010, 2011, 2012],
                "is_major_change": True,
                "major_change_year": 2010,
                "major_change_note": "PQ35 末代車型，1.4 TSI / 1.6 TDI 全面搭載早期 DQ200 7速乾式雙離合器，2.0 GTI 則為濕式 DQ250。",
                "platform": "VW PQ35 平台",
                "origin": "德國原裝進口",
                "photo_query": "Volkswagen Golf VI front",
                "depreciation_alert": {
                    "level": "high",
                    "title": "早期 DQ200 閥體災情 + 雙增壓引擎老化，殘值跌至低點",
                    "reason": "早期 DQ200 Mechatronic 閥體蓄壓器破裂「死亡閃燈」與 1.4 雙增壓活塞環通病，使車商收購價偏低、維修整理預算需預留較多。"
                },
                "trims": [
                    {
                        "trim_name": "1.4 TSI (單渦輪 / 雙增壓)",
                        "msrp_wan": 108.8,
                        "engine_code": "EA111 1.4L TSI 直列四缸渦輪",
                        "displacement_cc": 1390,
                        "horsepower": "122 ps / 160 ps",
                        "torque": "20.4 kgm / 24.5 kgm",
                        "transmission": "DQ200 7速乾式雙離合器自手排 (DSG)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "15.2 km/L",
                        "dimensions": "4199 x 1786 x 1479 mm (軸距 2578 mm)",
                        "safety": "7氣囊、ESP"
                    },
                    {
                        "trim_name": "2.0 GTI (濕式DQ250)",
                        "msrp_wan": 145.8,
                        "engine_code": "EA888 2.0L TSI 渦輪增壓",
                        "displacement_cc": 1984,
                        "horsepower": "210 ps / 5,300 rpm",
                        "torque": "28.6 kgm / 1,700~5,200 rpm",
                        "transmission": "DQ250 6速濕式雙離合器自手排 (DSG)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "12.8 km/L",
                        "dimensions": "4213 x 1786 x 1469 mm (軸距 2578 mm)",
                        "safety": "7氣囊、ESP、XDS電子限滑差速器"
                    }
                ],
                "common_issues": [
                    {
                        "part": "DQ200 7速乾式雙離合器閥體與離合器片",
                        "severity": "高風險",
                        "mileage_range": "6萬 ~ 12萬公里",
                        "symptom": "檔位顯示閃爍（死亡閃燈）、無法進退檔、低速抖動。",
                        "repair_cost_ntd": "閥體維修約 2.5~4.0 萬；離合器片組約 3.0~4.0 萬",
                        "advice": "確認是否已更換改良型閥體與蓄壓器強化件。"
                    },
                    {
                        "part": "EA888 正時鍊條張力器 / 吃機油 (GTI)",
                        "severity": "高風險",
                        "mileage_range": "8萬公里以上",
                        "symptom": "冷車啟動異音、跳齒風險、機油消耗過快。",
                        "repair_cost_ntd": "正時鍊條組約 2.0~3.5 萬",
                        "advice": "建議購買後立即檢查鍊條張力器伸出格數。"
                    }
                ],
                "yearly_prices": {
                    "2010": {"msrp": 108.8, "dealer": 18.0, "private": 14.0, "book": 11.5},
                    "2011": {"msrp": 108.8, "dealer": 20.5, "private": 16.5, "book": 13.5},
                    "2012": {"msrp": 108.8, "dealer": 23.5, "private": 19.0, "book": 16.0}
                }
            },
            {
                "gen_id": "golf-mk7",
                "gen_name": "MK7 / MK7.5 第七代（MQB平台）",
                "years": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "2013年大改款首度導入 MQB 模組化底盤與 EA211 皮帶正時新引擎，徹底改善舊款 EA111 吃機油與鍊條問題；2017年中 MK7.5 小改款導入數位儀表與 280 TSI。",
                "platform": "VW MQB 模組化底盤",
                "origin": "德國原裝進口",
                "photo_query": "Volkswagen Golf VII facelift",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "MQB 底盤體質大幅躍進，MK7.5 妥善率與保值度顯著優於前期",
                    "reason": "2015年後 DQ200 已多次改良離合器材質與閥體邏輯，且 280 TSI 配備豐富，中古車市場詢問度高。"
                },
                "trims": [
                    {
                        "trim_name": "280 TSI (1.4L 渦輪，MK7/7.5主力)",
                        "msrp_wan": 109.8,
                        "engine_code": "EA211 1.4L TSI 直列四缸渦輪增壓",
                        "displacement_cc": 1395,
                        "horsepower": "150 ps / 5,000~6,000 rpm",
                        "torque": "25.5 kgm / 1,500~3,500 rpm",
                        "transmission": "DQ200 7速乾式雙離合器自手排 (DSG)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿 (1.0/1.2為扭力樑)",
                        "fuel_economy": "16.8 km/L",
                        "dimensions": "4258 x 1790 x 1492 mm (軸距 2620 mm)",
                        "safety": "7氣囊、MCB二次碰撞預煞、MK7.5高階具ACC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "水泵浦 / 節溫器座滲水",
                        "severity": "中風險",
                        "mileage_range": "6萬 ~ 10萬公里",
                        "symptom": "冷卻液減少、引擎下方滲水漬。",
                        "repair_cost_ntd": "更換總成約 1.2 ~ 2.0 萬",
                        "advice": "EA211/EA888 世代常見塑膠冷卻件老化，換裝改良件即可。"
                    },
                    {
                        "part": "DQ200 離合器片磨損與閥體偶發故障",
                        "severity": "中風險",
                        "mileage_range": "8萬 ~ 12萬公里",
                        "symptom": "塞車起步微抖或偶發故障燈。",
                        "repair_cost_ntd": "離合器片更換約 2.5 ~ 3.5 萬",
                        "advice": "7.5代改良後較穩定，市區建議善用 S 檔或手動模式減少半離合。"
                    }
                ],
                "yearly_prices": {
                    "2013": {"msrp": 106.8, "dealer": 28.5, "private": 24.0, "book": 21.0},
                    "2014": {"msrp": 106.8, "dealer": 32.0, "private": 27.5, "book": 24.0},
                    "2015": {"msrp": 106.8, "dealer": 36.0, "private": 31.2, "book": 27.5},
                    "2016": {"msrp": 108.8, "dealer": 40.5, "private": 35.5, "book": 31.5},
                    "2017": {"msrp": 109.8, "dealer": 46.5, "private": 41.0, "book": 36.5},
                    "2018": {"msrp": 109.8, "dealer": 52.0, "private": 46.2, "book": 41.5},
                    "2019": {"msrp": 109.8, "dealer": 58.0, "private": 52.0, "book": 47.0},
                    "2020": {"msrp": 112.8, "dealer": 64.5, "private": 58.0, "book": 52.5}
                }
            },
            {
                "gen_id": "golf-mk8",
                "gen_name": "MK8 第八代（48V eTSI）",
                "years": [2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2021,
                "major_change_note": "2021年大改款第8代，全面導入 48V 輕油電 (eTSI)、電子線傳排檔與全觸控數位座艙，引擎改為 EA211 evo 1.5L。",
                "platform": "VW MQB Evo 進化平台",
                "origin": "德國原裝進口",
                "photo_query": "Volkswagen Golf VIII front",
                "depreciation_alert": {
                    "level": "low",
                    "title": "新世代數位座艙與 48V 輕油電，中古行情堅挺",
                    "reason": "IQ.DRIVE Level 2 標配且油耗出色，惟早期電子系統軟體偶有誤報與 48V 電系維護需留意。"
                },
                "trims": [
                    {
                        "trim_name": "280 eTSI Style / R-Line (1.5L + 48V)",
                        "msrp_wan": 116.8,
                        "engine_code": "EA211 evo 1.5L TSI + 48V 輕油電",
                        "displacement_cc": 1498,
                        "horsepower": "150 ps / 5,000~6,000 rpm",
                        "torque": "25.5 kgm / 1,500~3,500 rpm",
                        "transmission": "DQ200 7速雙離合器自手排 (電子線傳)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "18.5 km/L",
                        "dimensions": "4284 x 1789 x 1491 mm (軸距 2619 mm)",
                        "safety": "7氣囊、IQ.DRIVE Level 2 半自動駕駛"
                    }
                ],
                "common_issues": [
                    {
                        "part": "方向盤電容離手偵測誤報 / 車機黑屏",
                        "severity": "中風險",
                        "mileage_range": "全里程（多為2021-2022批次）",
                        "symptom": "行駛中頻繁跳出「Travel Assist 無法使用」警示或車機重啟。",
                        "repair_cost_ntd": "原廠保固內更換方向盤總成或更新軟體",
                        "advice": "買前確認是否已回廠完成方向盤與車機軟體召回更新。"
                    }
                ],
                "yearly_prices": {
                    "2021": {"msrp": 114.8, "dealer": 73.0, "private": 66.5, "book": 61.0},
                    "2022": {"msrp": 116.8, "dealer": 80.5, "private": 74.0, "book": 68.0},
                    "2023": {"msrp": 119.8, "dealer": 88.5, "private": 81.5, "book": 75.5},
                    "2024": {"msrp": 122.8, "dealer": 96.5, "private": 89.0, "book": 83.0},
                    "2025": {"msrp": 122.8, "dealer": 104.0, "private": 96.5, "book": 90.0}
                }
            }
        ]
    },
    {
        "id": "honda-civic",
        "brand": "Honda",
        "model": "Civic",
        "model_zh": "本田 Civic (喜美)",
        "category": "中型房車 / 進口油電掀背",
        "summary": "7代 Ferio(2001-2005)為台灣三陽代工時期；8代/9代(2006-2016)為台灣本田國產 5AT 經典；11代(2023+)改為日本進口 2.0 e:HEV 油電掀背，各世代差異極大。",
        "generations": [
            {
                "gen_id": "civic-7",
                "gen_name": "第 7 代 (ES Ferio 三陽時期)",
                "years": [2001, 2002, 2003, 2004, 2005],
                "is_major_change": True,
                "major_change_year": 2001,
                "major_change_note": "2001年上市（改稱 Ferio），前懸吊由雙A臂改為麥花臣，是 K6/K8 後、台灣本田成立前的過渡世代。",
                "platform": "Honda Global Compact",
                "origin": "台灣國產（三陽工業時期）",
                "photo_query": "Honda Civic 7th generation sedan",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "當年改麥花臣且 4AT 變速箱較脆弱，殘值遠不如 8 代",
                    "reason": "D17A 引擎與 BMXA 4速自排高里程容易打滑及水箱沖汽缸墊片，目前僅剩 4~8 萬代步價。"
                },
                "trims": [
                    {
                        "trim_name": "1.7 EX-S / VTi (4AT)",
                        "msrp_wan": 65.9,
                        "engine_code": "D17A 1.7L SOHC VTEC",
                        "displacement_cc": 1668,
                        "horsepower": "130 ps / 6,300 rpm",
                        "torque": "15.8 kgm / 4,800 rpm",
                        "transmission": "4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "14.0 km/L",
                        "dimensions": "4435 x 1695 x 1440 mm (軸距 2620 mm)",
                        "safety": "雙氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "4AT 變速箱打滑 / 汽缸床墊片沖毀",
                        "severity": "高風險",
                        "mileage_range": "12萬公里以上",
                        "symptom": "冷車入檔延遲或高轉不進檔、水箱噴氣泡水溫高。",
                        "repair_cost_ntd": "變速箱翻修約 2.0 ~ 3.0 萬",
                        "advice": "建議多貼一點預算直接找 8 代 K12，妥善與外型差距極大。"
                    }
                ],
                "yearly_prices": {
                    "2001": {"msrp": 64.9, "dealer": 6.5, "private": 4.2, "book": 2.5},
                    "2002": {"msrp": 64.9, "dealer": 7.0, "private": 4.8, "book": 3.0},
                    "2003": {"msrp": 65.9, "dealer": 7.8, "private": 5.5, "book": 3.5},
                    "2004": {"msrp": 65.9, "dealer": 8.8, "private": 6.2, "book": 4.2},
                    "2005": {"msrp": 65.9, "dealer": 9.8, "private": 7.0, "book": 5.0}
                }
            },
            {
                "gen_id": "civic-8",
                "gen_name": "第 8 代 (K12 國產經典)",
                "years": [2006, 2007, 2008, 2009, 2010, 2011, 2012],
                "is_major_change": True,
                "major_change_year": 2006,
                "major_change_note": "2006年台灣本田國產化上市，改採太空艙雙層儀表與 R18A i-VTEC 引擎搭配 5速傳統自排，因造型與操控經典，二手市場保值度驚人。",
                "platform": "Honda Global Compact Platform",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda Civic 8th generation sedan Asia",
                "depreciation_alert": {
                    "level": "low",
                    "title": "罕見的高齡保值神車，但須留意老車改裝與調錶風險",
                    "reason": "5速傳統自排極為耐用，但車齡已逾 14~20 年，需仔細檢驗底盤橡膠與是否曾大改裝。"
                },
                "trims": [
                    {
                        "trim_name": "1.8 VTi / VTi-S",
                        "msrp_wan": 72.9,
                        "engine_code": "R18A1 1.8L SOHC i-VTEC",
                        "displacement_cc": 1799,
                        "horsepower": "140 ps / 6,300 rpm",
                        "torque": "17.7 kgm / 4,300 rpm",
                        "transmission": "5速手自排（傳統自排）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "14.5 km/L",
                        "dimensions": "4540 x 1755 x 1435 mm (軸距 2700 mm)",
                        "safety": "2氣囊（2.0S 具 VSA 穩定系統）"
                    }
                ],
                "common_issues": [
                    {
                        "part": "液壓引擎腳衰退",
                        "severity": "一般耗材",
                        "mileage_range": "6萬 ~ 10萬公里",
                        "symptom": "D檔踩煞車怠速時車室與方向盤劇烈共鳴震動。",
                        "repair_cost_ntd": "原廠全組約 9,000 ~ 13,000 元",
                        "advice": "K12 最著名通病，換原廠件即可恢復寧靜。"
                    },
                    {
                        "part": "方向機油封漏油 / 壓縮機異音",
                        "severity": "中風險",
                        "mileage_range": "12萬公里以上",
                        "symptom": "轉向重手滲油、冷氣不冷。",
                        "repair_cost_ntd": "方向機翻修約 8,000 ~ 15,000 元",
                        "advice": "老車必檢項目，頂車檢查底盤乾爽度。"
                    }
                ],
                "yearly_prices": {
                    "2006": {"msrp": 70.9, "dealer": 13.0, "private": 10.0, "book": 7.5},
                    "2007": {"msrp": 71.9, "dealer": 14.2, "private": 11.0, "book": 8.5},
                    "2008": {"msrp": 71.9, "dealer": 15.5, "private": 12.0, "book": 9.5},
                    "2009": {"msrp": 72.9, "dealer": 17.5, "private": 14.0, "book": 11.0},
                    "2010": {"msrp": 72.9, "dealer": 19.5, "private": 15.8, "book": 12.5},
                    "2011": {"msrp": 73.9, "dealer": 22.0, "private": 18.0, "book": 14.5},
                    "2012": {"msrp": 74.9, "dealer": 24.5, "private": 20.5, "book": 16.5}
                }
            },
            {
                "gen_id": "civic-9",
                "gen_name": "第 9 代 / 9.5 代 (K14 國產末代)",
                "years": [2013, 2014, 2015, 2016],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "9代上市，2014年小改款為 9.5代並將 VSA 與 4~6氣囊下放，為台灣本田國產 Civic 絕響。",
                "platform": "Honda K14 改良平台",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda Civic 9th generation sedan",
                "depreciation_alert": {
                    "level": "low",
                    "title": "末代國產本田房車，妥善率極高且中古搶手",
                    "reason": "結構簡單耐用，無渦輪或雙離合器負擔，9.5代(2014年後)配備 VSA 安全系統尤其保值。"
                },
                "trims": [
                    {
                        "trim_name": "1.8 VTi-S (9.5代主力)",
                        "msrp_wan": 79.9,
                        "engine_code": "R18Z1 1.8L i-VTEC 自然進氣",
                        "displacement_cc": 1798,
                        "horsepower": "141 ps / 6,500 rpm",
                        "torque": "17.8 kgm / 4,300 rpm",
                        "transmission": "5速手自排（含換檔撥片）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "15.0 km/L",
                        "dimensions": "4555 x 1755 x 1435 mm (軸距 2670 mm)",
                        "safety": "4~6氣囊、VSA 車身動態穩定 (9.5代)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "引擎腳老化 / 內裝飾板異音",
                        "severity": "一般耗材",
                        "mileage_range": "8萬公里以上",
                        "symptom": "怠速震動與行駛中門板塑料異音。",
                        "repair_cost_ntd": "引擎腳約 8,000 ~ 12,000 元",
                        "advice": "正常耗材，建議購買 2014 年後 9.5 代安全配備較齊全。"
                    }
                ],
                "yearly_prices": {
                    "2013": {"msrp": 79.9, "dealer": 30.0, "private": 25.8, "book": 22.0},
                    "2014": {"msrp": 79.9, "dealer": 34.0, "private": 29.5, "book": 25.5},
                    "2015": {"msrp": 79.9, "dealer": 37.5, "private": 33.0, "book": 28.8},
                    "2016": {"msrp": 79.9, "dealer": 41.5, "private": 36.8, "book": 32.0}
                }
            },
            {
                "gen_id": "civic-11",
                "gen_name": "第 11 代 (日本進口 e:HEV 油電掀背)",
                "years": [2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2023,
                "major_change_note": "2023年重返台灣市場！改以「日本原裝進口 5門掀背 + 2.0L e:HEV 油電」導入，新車價跳升至 139.9 萬元，與過去國產房車已完全不同級距。",
                "platform": "Honda Architecture 新世代高剛性平台",
                "origin": "日本原裝進口（埼玉工廠）",
                "photo_query": "Honda Civic e:HEV hatchback FL",
                "depreciation_alert": {
                    "level": "low",
                    "title": "進口油電高價定位，初期折舊受新車定價影響較明顯",
                    "reason": "139.9 萬新車價門檻高，第一、二年折舊金額約 25~35 萬。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 e:HEV 5門掀背",
                        "msrp_wan": 139.9,
                        "engine_code": "2.0L Atkinson缸內直噴 + 雙電動馬達",
                        "displacement_cc": 1993,
                        "horsepower": "馬達 184 ps (引擎 143 ps)",
                        "torque": "32.1 kgm (馬達驅動)",
                        "transmission": "E-CVT 電驅直聯系統",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "23.7 km/L",
                        "dimensions": "4550 x 1800 x 1415 mm (軸距 2735 mm)",
                        "safety": "11氣囊、Honda SENSING 全套"
                    }
                ],
                "common_issues": [
                    {
                        "part": "方向機齒條偶發異音（早期召回批次）",
                        "severity": "中風險",
                        "mileage_range": "2萬 ~ 5萬公里",
                        "symptom": "高速微調方向盤有黏滯感或輕微異音。",
                        "repair_cost_ntd": "原廠召回免費更換",
                        "advice": "買前確認已完成台本方向機召回檢修。"
                    }
                ],
                "yearly_prices": {
                    "2023": {"msrp": 139.9, "dealer": 103.0, "private": 95.0, "book": 88.0},
                    "2024": {"msrp": 139.9, "dealer": 112.0, "private": 104.0, "book": 97.0},
                    "2025": {"msrp": 139.9, "dealer": 122.0, "private": 114.0, "book": 106.0}
                }
            }
        ]
    },
    {
        "id": "nissan-sentra",
        "brand": "Nissan",
        "model": "Sentra",
        "model_zh": "日產 Sentra",
        "category": "中型房車",
        "summary": "2000年 Sentra 180/M1 是當年豪華房車代表，後期因怠速馬達與老車耗材殘值降至低點；2007年 Bluebird 與 2013年 B17 時期則受 Jatco CVT 變速箱災情影響；2020年底大改款 B18 脫胎換骨。",
        "generations": [
            {
                "gen_id": "sentra-180",
                "gen_name": "Sentra 180 / M1 (N16 世代)",
                "years": [2000, 2001, 2002, 2003, 2004, 2005, 2006],
                "is_major_change": True,
                "major_change_year": 2000,
                "major_change_note": "2000年推出 Sentra 180（2003小改款稱 M1），採 QG18DE 1.8L 引擎與 4AT，主打「新好男人」與豪華車室。",
                "platform": "Nissan MS 平台",
                "origin": "台灣國產（裕隆汽車）",
                "photo_query": "Nissan Sentra N16",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "怠速馬達漏水燒電腦經典通病，目前殘值 4~7 萬",
                    "reason": "車齡已逾 20 年，QG18DE 怠速馬達墊片老化滲水會直接燒毀行車電腦(ECU)，導致市場殘值偏低。"
                },
                "trims": [
                    {
                        "trim_name": "1.6 / 1.8 (4AT)",
                        "msrp_wan": 64.9,
                        "engine_code": "QG18DE 1.8L DOHC 自然進氣",
                        "displacement_cc": 1769,
                        "horsepower": "128 ps / 6,000 rpm",
                        "torque": "16.8 kgm / 2,800 rpm",
                        "transmission": "4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後QT懸吊",
                        "fuel_economy": "13.2 km/L",
                        "dimensions": "4495 x 1710 x 1445 mm (軸距 2535 mm)",
                        "safety": "單/雙氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "怠速控制馬達(IACV)滲水燒毀ECU",
                        "severity": "高風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "怠速不穩熄火、甚至行車電腦燒毀無法發動。",
                        "repair_cost_ntd": "外廠修改水路+換整新電腦約 8,000 ~ 15,000 元",
                        "advice": "買 M1/180 必確認是否已廢除怠速馬達水路或更換改良件。"
                    }
                ],
                "yearly_prices": {
                    "2000": {"msrp": 63.9, "dealer": 5.5, "private": 3.5, "book": 2.0},
                    "2001": {"msrp": 63.9, "dealer": 6.0, "private": 4.0, "book": 2.3},
                    "2002": {"msrp": 64.9, "dealer": 6.5, "private": 4.5, "book": 2.6},
                    "2003": {"msrp": 64.9, "dealer": 7.2, "private": 5.0, "book": 3.0},
                    "2004": {"msrp": 64.9, "dealer": 7.8, "private": 5.5, "book": 3.5},
                    "2005": {"msrp": 65.9, "dealer": 8.5, "private": 6.0, "book": 4.0},
                    "2006": {"msrp": 65.9, "dealer": 9.2, "private": 6.8, "book": 4.5}
                }
            },
            {
                "gen_id": "sentra-g11",
                "gen_name": "Bluebird Sylphy (G11 世代)",
                "years": [2007, 2008, 2009, 2010, 2011, 2012],
                "is_major_change": True,
                "major_change_year": 2007,
                "major_change_note": "2007年改名為 Bluebird Sylphy 上市，軸距拉長至 2700mm 並首度導入 2.0L + CVT。",
                "platform": "Nissan B 延伸平台",
                "origin": "台灣國產（裕隆汽車）",
                "photo_query": "Nissan Bluebird Sylphy G11",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "早期 2.0 CVT 過熱保護與高稅金，中古價親民",
                    "reason": "2.0L 稅金高一階且早期 CVT 散熱較弱，二手價落在 9~15 萬。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 豪華/旗艦",
                        "msrp_wan": 76.9,
                        "engine_code": "MR20DE 2.0L 自然進氣",
                        "displacement_cc": 1997,
                        "horsepower": "134 ps / 5,200 rpm",
                        "torque": "19.5 kgm / 4,400 rpm",
                        "transmission": "Xtronic CVT 無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "15.1 km/L",
                        "dimensions": "4610 x 1695 x 1510 mm (軸距 2700 mm)",
                        "safety": "2氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "CVT 長途高速過熱保護 / 冷氣壓縮機老化",
                        "severity": "中風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "高速爬坡鎖轉速無力、怠速冷氣不涼。",
                        "repair_cost_ntd": "加裝 CVT 冷卻器約 6,000~9,000 元",
                        "advice": "後座空間極大，適合預算 10 萬內重視空間的代步買家。"
                    }
                ],
                "yearly_prices": {
                    "2007": {"msrp": 74.9, "dealer": 10.5, "private": 8.0, "book": 5.8},
                    "2008": {"msrp": 74.9, "dealer": 11.5, "private": 9.0, "book": 6.8},
                    "2009": {"msrp": 75.9, "dealer": 12.8, "private": 10.0, "book": 7.8},
                    "2010": {"msrp": 76.9, "dealer": 14.0, "private": 11.2, "book": 8.8},
                    "2011": {"msrp": 76.9, "dealer": 15.2, "private": 12.2, "book": 9.8},
                    "2012": {"msrp": 76.9, "dealer": 16.5, "private": 13.5, "book": 11.0}
                }
            },
            {
                "gen_id": "sentra-b17",
                "gen_name": "B17 世代 (Super Sentra)",
                "years": [2013, 2014, 2015, 2016, 2017, 2018, 2019],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "2013年大改款恢復 Sentra 車名，搭載 MR18DE 引擎與 Jatco Xtronic CVT（附副變速箱）。",
                "platform": "Nissan V/B 延伸平台",
                "origin": "台灣國產（裕隆汽車）",
                "photo_query": "Nissan Sentra B17",
                "depreciation_alert": {
                    "level": "high",
                    "title": "Jatco CVT 變速箱災情區間 (2013–2017)，殘值明顯折價",
                    "reason": "早期 CVT 內部油壓與副變速箱行星齒輪容易磨損，導致轉速亂竄或無法行駛，引發車主集體抗議與 8 年延保，中古車商收購皆會大幅壓低價格預留維修風險。"
                },
                "trims": [
                    {
                        "trim_name": "1.8L 豪華/旗艦版",
                        "msrp_wan": 74.5,
                        "engine_code": "MR18DE 1.8L 直列四缸自然進氣",
                        "displacement_cc": 1798,
                        "horsepower": "131 ps / 6,000 rpm",
                        "torque": "17.8 kgm / 3,600 rpm",
                        "transmission": "Jatco Xtronic CVT 無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "18.7 km/L (美規)",
                        "dimensions": "4610 x 1760 x 1495 mm (軸距 2700 mm)",
                        "safety": "2~6氣囊 (前期多為2氣囊，2017小改款提升安全)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "Xtronic CVT 變速箱抖動/失效",
                        "severity": "高風險",
                        "mileage_range": "6萬 ~ 12萬公里",
                        "symptom": "行駛中轉速上下劇烈跳動、加速無力、亮故障燈甚至保護鎖檔。",
                        "repair_cost_ntd": "翻修/更換翻新變速箱約 3.5 ~ 6.0 萬",
                        "advice": "許多車輛已過8年延保期限，購車前務必實路高速+低速爬坡試駕並查驗變速箱更換紀錄。"
                    }
                ],
                "yearly_prices": {
                    "2013": {"msrp": 73.9, "dealer": 17.5, "private": 14.0, "book": 11.5},
                    "2014": {"msrp": 73.9, "dealer": 19.5, "private": 15.8, "book": 13.0},
                    "2015": {"msrp": 74.5, "dealer": 22.0, "private": 18.0, "book": 15.0},
                    "2016": {"msrp": 74.5, "dealer": 25.0, "private": 20.8, "book": 17.5},
                    "2017": {"msrp": 75.9, "dealer": 28.5, "private": 24.0, "book": 20.5},
                    "2018": {"msrp": 75.9, "dealer": 32.5, "private": 27.8, "book": 24.0},
                    "2019": {"msrp": 75.9, "dealer": 36.5, "private": 31.5, "book": 27.5}
                }
            },
            {
                "gen_id": "sentra-b18",
                "gen_name": "B18 新世代大改款",
                "years": [2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2020,
                "major_change_note": "2020年底大改款！換裝 CMF-C 歐日共用底盤、1.6L 第三代 HR16DE 熔射缸孔引擎與第五代 Xtronic CVT。",
                "platform": "Renault-Nissan CMF-C 平台",
                "origin": "台灣國產（裕隆汽車）",
                "photo_query": "Nissan Sentra B18",
                "depreciation_alert": {
                    "level": "low",
                    "title": "省油、配備豐富且改善變速箱體質，中古性價比極高",
                    "reason": "外觀帥氣且稅金降至 1.6L 級距，對二手買家相當划算。"
                },
                "trims": [
                    {
                        "trim_name": "1.6L 尊爵/尊爵智駕版",
                        "msrp_wan": 83.5,
                        "engine_code": "HR16DE 1.6L 直列四缸自然進氣（鏡面缸孔熔射）",
                        "displacement_cc": 1598,
                        "horsepower": "138 ps / 6,300 rpm",
                        "torque": "17.2 kgm / 4,000 rpm",
                        "transmission": "第五代 Xtronic CVT 無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "17.7 km/L",
                        "dimensions": "4641 x 1815 x 1447 mm (軸距 2712 mm)",
                        "safety": "6氣囊、ICC 全速域智慧定速、PFCW 超視距追撞警示"
                    }
                ],
                "common_issues": [
                    {
                        "part": "引擎腳老化造成怠速抖動",
                        "severity": "一般耗材",
                        "mileage_range": "4萬 ~ 8萬公里",
                        "symptom": "怠速開冷氣或停等紅燈時車身共振。",
                        "repair_cost_ntd": "原廠保固內出保或自費約 8,000 元",
                        "advice": "試車時留意怠速開冷氣的車室震動。"
                    }
                ],
                "yearly_prices": {
                    "2020": {"msrp": 79.9, "dealer": 44.5, "private": 39.5, "book": 36.0},
                    "2021": {"msrp": 81.9, "dealer": 48.5, "private": 43.5, "book": 39.5},
                    "2022": {"msrp": 83.5, "dealer": 53.0, "private": 47.8, "book": 43.8},
                    "2023": {"msrp": 83.5, "dealer": 58.0, "private": 52.5, "book": 48.5},
                    "2024": {"msrp": 87.9, "dealer": 64.5, "private": 58.5, "book": 54.0},
                    "2025": {"msrp": 87.9, "dealer": 71.0, "private": 65.0, "book": 60.0}
                }
            }
        ]
    },
    {
        "id": "toyota-rav4",
        "brand": "Toyota",
        "model": "RAV4",
        "model_zh": "豐田 RAV4",
        "category": "進口中型休旅車 (SUV)",
        "summary": "長期霸榜台灣進口車銷售冠軍。3代(2008-2012)為和泰重新日本進口；4代(2013-2018)導入 2.0/Hybrid；5代(2019+)換裝 TNGA-K 平台與全新 Direct Shift-CVT。",
        "generations": [
            {
                "gen_id": "rav4-3",
                "gen_name": "第 3 代 (XA30 2.4L 4AT)",
                "years": [2008, 2009, 2010, 2011, 2012],
                "is_major_change": True,
                "major_change_year": 2008,
                "major_change_note": "2008年底和泰重新日本原裝導入第3代 RAV4，採 2.4L 2AZ-FE + 4AT 搭配外掛式備胎設計。",
                "platform": "Toyota New MC 平台",
                "origin": "日本原裝進口",
                "photo_query": "Toyota RAV4 XA30",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "極保值老休旅，但須留意 2AZ-FE 引擎吃機油與 2.4L 高稅金",
                    "reason": "結構耐操且空間大，但 2AZ-FE 引擎活塞環積碳易吃機油，加上每年 17,410 元稅金影響後期價格。"
                },
                "trims": [
                    {
                        "trim_name": "2.4 2WD / 4WD",
                        "msrp_wan": 95.0,
                        "engine_code": "2AZ-FE 2.4L VVT-i 自然進氣",
                        "displacement_cc": 2362,
                        "horsepower": "170 ps / 6,000 rpm",
                        "torque": "22.8 kgm / 4,000 rpm",
                        "transmission": "4速手自排",
                        "drivetrain": "前驅 / 適時四驅",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "11.5 km/L",
                        "dimensions": "4625 x 1815 x 1720 mm (軸距 2660 mm)",
                        "safety": "2~6氣囊、VSC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "2AZ-FE 引擎高里程吃機油 / 方向機柱異音",
                        "severity": "中風險",
                        "mileage_range": "12萬公里以上",
                        "symptom": "每 5,000 公里機油減少 1 公升以上、原地轉向異音。",
                        "repair_cost_ntd": "大修活塞環約 2.5~3.5 萬；方向機十字接頭約 3,000 元",
                        "advice": "買前檢查機油尺油位與排氣管有無藍煙。"
                    }
                ],
                "yearly_prices": {
                    "2008": {"msrp": 92.0, "dealer": 19.5, "private": 16.0, "book": 13.0},
                    "2009": {"msrp": 92.0, "dealer": 21.5, "private": 17.8, "book": 14.5},
                    "2010": {"msrp": 95.0, "dealer": 24.0, "private": 20.0, "book": 16.5},
                    "2011": {"msrp": 95.0, "dealer": 26.5, "private": 22.5, "book": 19.0},
                    "2012": {"msrp": 95.0, "dealer": 29.5, "private": 25.2, "book": 21.5}
                }
            },
            {
                "gen_id": "rav4-4",
                "gen_name": "第 4 代 / 4.5 代 (XA40)",
                "years": [2013, 2014, 2015, 2016, 2017, 2018],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "2013年大改款第4代取消尾門備胎；2015年底推出 4.5代小改款，導入 2.0L 入門引擎與 2.5L Hybrid 油電及 TSS 主動安全。",
                "platform": "Toyota New MC 平台",
                "origin": "日本原裝進口",
                "photo_query": "Toyota RAV4 XA40 facelift",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極為保值的日本原裝休旅車",
                    "reason": "維修便宜、空間實用，2.0 尊爵與 2.5 Hybrid 在二手市場流動性極高。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 豪華 / 尊爵 (4.5代主力)",
                        "msrp_wan": 100.9,
                        "engine_code": "3ZR-FE 2.0L 直列四缸自然進氣",
                        "displacement_cc": 1987,
                        "horsepower": "146 ps / 6,200 rpm",
                        "torque": "19.1 kgm / 3,600 rpm",
                        "transmission": "Super CVT-i 無段變速（模擬7速）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "13.6 km/L",
                        "dimensions": "4605 x 1845 x 1685 mm (軸距 2660 mm)",
                        "safety": "7氣囊、VSC、4.5代高階具 TSS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "4.5代 2.0 CVT 閥體高里程頓挫 / 車頂架滲水",
                        "severity": "中風險",
                        "mileage_range": "10萬 ~ 15萬公里",
                        "symptom": "高速巡航微幅頓挫、戶外車頂篷邊緣水漬。",
                        "repair_cost_ntd": "翻修閥體約 2.5 ~ 4.5 萬；重打防水膠約 3,000 元",
                        "advice": "挑選有定期更換變速箱油保養紀錄的車源。"
                    }
                ],
                "yearly_prices": {
                    "2013": {"msrp": 96.9, "dealer": 34.0, "private": 29.5, "book": 26.0},
                    "2014": {"msrp": 96.9, "dealer": 37.5, "private": 32.8, "book": 29.0},
                    "2015": {"msrp": 96.9, "dealer": 41.5, "private": 36.5, "book": 32.5},
                    "2016": {"msrp": 100.9, "dealer": 47.0, "private": 41.8, "book": 37.5},
                    "2017": {"msrp": 100.9, "dealer": 52.0, "private": 46.5, "book": 42.0},
                    "2018": {"msrp": 100.9, "dealer": 57.0, "private": 51.5, "book": 46.5}
                }
            },
            {
                "gen_id": "rav4-5",
                "gen_name": "第 5 代 (XA50 TNGA-K平台)",
                "years": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2019,
                "major_change_note": "2019年3月大改款！採用全新 TNGA-K 平台、M20A-FKS 熱效率40%新引擎與帶起步齒輪的 Direct Shift-CVT，並全面標配 TSS 2.0。",
                "platform": "Toyota TNGA GA-K 高剛性平台",
                "origin": "日本原裝進口",
                "photo_query": "Toyota RAV4 XA50",
                "depreciation_alert": {
                    "level": "low",
                    "title": "台灣最保值進口 SUV，2.5 Hybrid 油電尤其搶手",
                    "reason": "空間、安全性與品牌光環兼具，新古車與三年內二手價極度堅挺。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 尊爵 / 旗艦",
                        "msrp_wan": 111.0,
                        "engine_code": "M20A-FKS 2.0L Dynamic Force 自然進氣",
                        "displacement_cc": 1987,
                        "horsepower": "173 ps / 6,600 rpm",
                        "torque": "20.7 kgm / 4,400~4,900 rpm",
                        "transmission": "Direct Shift-CVT (含實體起步齒輪)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "15.3 km/L",
                        "dimensions": "4600 x 1855 x 1685 mm (軸距 2690 mm)",
                        "safety": "7氣囊、TSS 2.0 全速域 Level 2"
                    },
                    {
                        "trim_name": "2.5 Hybrid 旗艦 / 4WD",
                        "msrp_wan": 124.0,
                        "engine_code": "A25A-FXS 2.5L 油電複合動力",
                        "displacement_cc": 2487,
                        "horsepower": "綜效 218 ps (2WD) / 222 ps (E-Four)",
                        "torque": "引擎 22.5 kgm + 馬達輔助",
                        "transmission": "E-CVT 電子無段變速",
                        "drivetrain": "前驅 / E-Four 電子四驅",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "21.3 km/L",
                        "dimensions": "4600 x 1855 x 1685 mm (軸距 2690 mm)",
                        "safety": "7氣囊、TSS 2.0、PVM 環景"
                    }
                ],
                "common_issues": [
                    {
                        "part": "早期車頂行李架膠條滲水 (2019-2020批次)",
                        "severity": "中風險",
                        "mileage_range": "2019~2020年式",
                        "symptom": "大雨或洗車後後廂兩側或頂篷滲水。",
                        "repair_cost_ntd": "原廠免費召回/專案密封修正",
                        "advice": "購買 2019-2020 年份務必確認已完成原廠車頂防水修正工程。"
                    }
                ],
                "yearly_prices": {
                    "2019": {"msrp": 104.9, "dealer": 66.5, "private": 61.0, "book": 56.5},
                    "2020": {"msrp": 106.9, "dealer": 72.0, "private": 66.0, "book": 61.0},
                    "2021": {"msrp": 109.0, "dealer": 77.5, "private": 71.5, "book": 66.0},
                    "2022": {"msrp": 111.0, "dealer": 83.5, "private": 77.5, "book": 72.0},
                    "2023": {"msrp": 117.0, "dealer": 91.5, "private": 85.0, "book": 79.0},
                    "2024": {"msrp": 117.0, "dealer": 98.5, "private": 92.0, "book": 85.5},
                    "2025": {"msrp": 117.0, "dealer": 105.5, "private": 99.0, "book": 92.0}
                }
            }
        ]
    },
    {
        "id": "honda-crv",
        "brand": "Honda",
        "model": "CR-V",
        "model_zh": "本田 CR-V",
        "category": "國產中型休旅車 (SUV)",
        "summary": "國產 SUV 長青霸主。2代(2003-2006)開創都會休旅熱潮；3代/4代(2007-2016)以 5AT 耐操著稱；5代(2017+)全面改為 1.5L 渦輪增壓 + CVT 與 Honda SENSING；6代(2023+)車體再放大。",
        "generations": [
            {
                "gen_id": "crv-2",
                "gen_name": "第 2 代 (RD 台灣本田首代國產)",
                "years": [2003, 2004, 2005, 2006],
                "is_major_change": True,
                "major_change_year": 2003,
                "major_change_note": "2003年台灣本田國產化首代車型，採 K20A 2.0L 引擎 + 4AT 與隱藏式野餐桌設計。",
                "platform": "Honda RD 平台",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda CR-V second generation",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "冷氣壓縮機「死亡之握」經典通病，老車殘值 9~14 萬",
                    "reason": "2代冷氣壓縮機容易咬死噴鐵屑進管路，但機械結構簡單好修，至今仍有不少露營玩家收購。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 EX / SX (4AT)",
                        "msrp_wan": 83.9,
                        "engine_code": "K20A4 2.0L DOHC i-VTEC",
                        "displacement_cc": 1998,
                        "horsepower": "150 ps / 6,500 rpm",
                        "torque": "19.4 kgm / 4,000 rpm",
                        "transmission": "4速自排",
                        "drivetrain": "前驅 / 適時四驅",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "11.2 km/L",
                        "dimensions": "4575 x 1780 x 1710 mm (軸距 2620 mm)",
                        "safety": "雙氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "冷氣壓縮機咬死噴黑油 / 方向機油封漏油",
                        "severity": "高風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "開冷氣異音後突然不冷、需整套清洗管路換新壓縮機。",
                        "repair_cost_ntd": "整套冷氣系統整理約 1.5 ~ 2.5 萬",
                        "advice": "看車時確認冷氣壓縮機有無異常高頻聲與冷度。"
                    }
                ],
                "yearly_prices": {
                    "2003": {"msrp": 82.9, "dealer": 11.0, "private": 8.0, "book": 5.5},
                    "2004": {"msrp": 82.9, "dealer": 12.2, "private": 9.0, "book": 6.5},
                    "2005": {"msrp": 83.9, "dealer": 13.5, "private": 10.2, "book": 7.5},
                    "2006": {"msrp": 83.9, "dealer": 15.0, "private": 11.5, "book": 8.8}
                }
            },
            {
                "gen_id": "crv-3",
                "gen_name": "第 3 代 / 3.5 代 (RE 5AT世代)",
                "years": [2007, 2008, 2009, 2010, 2011, 2012],
                "is_major_change": True,
                "major_change_year": 2007,
                "major_change_note": "2007年大改款取消外掛備胎，全面換裝 5速自排，新增 2.4L 4WD 版本。",
                "platform": "Honda RE 平台",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda CR-V third generation",
                "depreciation_alert": {
                    "level": "low",
                    "title": "5AT 耐操好養，2.0 省稅金版二手相當保值",
                    "reason": "空間大且故障率低，15~25萬預算家庭代步好選擇。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 VTi / 2.4 VTi-S (5AT)",
                        "msrp_wan": 88.9,
                        "engine_code": "R20A 2.0L / K24Z1 2.4L i-VTEC",
                        "displacement_cc": 1997,
                        "horsepower": "150 ps (2.0) / 170 ps (2.4)",
                        "torque": "19.4 kgm / 22.4 kgm",
                        "transmission": "5速手自排",
                        "drivetrain": "前驅 / 適時四驅",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "12.0 km/L",
                        "dimensions": "4530 x 1820 x 1680 mm (軸距 2620 mm)",
                        "safety": "2~4氣囊、VSA (2.4頂級)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "冷氣壓縮機離合器打滑 / 方向機滲油",
                        "severity": "中風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "怠速開冷氣間歇不冷、轉向異音。",
                        "repair_cost_ntd": "離合器線圈約 3,500~5,000 元",
                        "advice": "建議選 2.0 版本稅金較省。"
                    }
                ],
                "yearly_prices": {
                    "2007": {"msrp": 86.9, "dealer": 17.0, "private": 13.8, "book": 11.0},
                    "2008": {"msrp": 86.9, "dealer": 18.8, "private": 15.2, "book": 12.5},
                    "2009": {"msrp": 88.9, "dealer": 20.8, "private": 17.0, "book": 14.0},
                    "2010": {"msrp": 88.9, "dealer": 23.0, "private": 19.0, "book": 16.0},
                    "2011": {"msrp": 89.9, "dealer": 25.5, "private": 21.5, "book": 18.2},
                    "2012": {"msrp": 89.9, "dealer": 28.0, "private": 24.0, "book": 20.5}
                }
            },
            {
                "gen_id": "crv-4",
                "gen_name": "第 4 代 / 4.5 代 (RM 世代)",
                "years": [2013, 2014, 2015, 2016],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "國產末代自然進氣 + 5速傳統自排世代，無渦輪與 CVT 複雜結構。",
                "platform": "Honda RM 平台",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda CR-V fourth generation",
                "depreciation_alert": {
                    "level": "low",
                    "title": "自然進氣 5AT 極為耐用，中古家庭代步熱門",
                    "reason": "機械結構單純，2.4 VTi-S 動力足且維修便宜，殘值穩定。"
                },
                "trims": [
                    {
                        "trim_name": "2.4 VTi-S (4.5代主力)",
                        "msrp_wan": 96.9,
                        "engine_code": "K24Z9 2.4L DOHC i-VTEC 自然進氣",
                        "displacement_cc": 2354,
                        "horsepower": "190 ps / 7,000 rpm",
                        "torque": "22.6 kgm / 4,400 rpm",
                        "transmission": "5速手自排（傳統自排）",
                        "drivetrain": "前輪驅動 / 適時四驅",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "11.7 km/L",
                        "dimensions": "4545 x 1820 x 1685 mm (軸距 2620 mm)",
                        "safety": "4氣囊、VSA"
                    }
                ],
                "common_issues": [
                    {
                        "part": "壓縮機冷氣系統 / 三角架鐵套老化",
                        "severity": "一般耗材",
                        "mileage_range": "10萬公里以上",
                        "symptom": "底盤橡膠龜裂異音、壓縮機離合器磨損。",
                        "repair_cost_ntd": "鐵套約 5,000 ~ 8,000 元",
                        "advice": "注意 2.4L 稅金較高（每年 17,410 元）。"
                    }
                ],
                "yearly_prices": {
                    "2013": {"msrp": 97.9, "dealer": 30.5, "private": 26.5, "book": 23.0},
                    "2014": {"msrp": 97.9, "dealer": 34.0, "private": 29.8, "book": 26.0},
                    "2015": {"msrp": 96.9, "dealer": 38.0, "private": 33.5, "book": 29.5},
                    "2016": {"msrp": 96.9, "dealer": 42.5, "private": 37.8, "book": 33.5}
                }
            },
            {
                "gen_id": "crv-5",
                "gen_name": "第 5 代 / 5.5 代 (RW 1.5T 世代)",
                "years": [2017, 2018, 2019, 2020, 2021, 2022],
                "is_major_change": True,
                "major_change_year": 2017,
                "major_change_note": "2017年中大改款！首度導入 1.5L VTEC Turbo 渦輪引擎（193匹）+ CVT 與 Honda SENSING，稅金降至 1.5L 級距。",
                "platform": "Honda Ace 高剛性平台",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda CR-V fifth generation",
                "depreciation_alert": {
                    "level": "low",
                    "title": "1.5T 省稅金+大空間，國產休旅保值王",
                    "reason": "二手流通速度極快，5.5代(2020年後)強化後結構與標配 Honda SENSING 更受歡迎。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 VTi-S / S (5代/5.5代)",
                        "msrp_wan": 103.9,
                        "engine_code": "L15B7 1.5L VTEC Turbo 直列四缸渦輪",
                        "displacement_cc": 1498,
                        "horsepower": "193 ps / 5,600 rpm",
                        "torque": "24.8 kgm / 2,000~5,000 rpm",
                        "transmission": "CVT 無段變速（附換檔撥片）",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "14.6 ~ 14.7 km/L",
                        "dimensions": "4570 x 1855 x 1665 mm (軸距 2660 mm)",
                        "safety": "6氣囊、Honda SENSING"
                    }
                ],
                "common_issues": [
                    {
                        "part": "方向機柱/齒條異音 / 冷氣風箱漏冷媒",
                        "severity": "中風險",
                        "mileage_range": "3萬 ~ 8萬公里",
                        "symptom": "原地打方向盤傳出「扣扣」聲、空調吹暖風。",
                        "repair_cost_ntd": "風箱更換約 1.2 ~ 1.8 萬",
                        "advice": "看車時原地左右轉動方向盤聽有無異音。"
                    }
                ],
                "yearly_prices": {
                    "2017": {"msrp": 103.0, "dealer": 54.0, "private": 48.5, "book": 44.0},
                    "2018": {"msrp": 103.0, "dealer": 58.5, "private": 53.0, "book": 48.5},
                    "2019": {"msrp": 103.0, "dealer": 63.5, "private": 57.5, "book": 53.0},
                    "2020": {"msrp": 103.9, "dealer": 69.5, "private": 63.5, "book": 58.5},
                    "2021": {"msrp": 103.9, "dealer": 74.5, "private": 68.5, "book": 63.0},
                    "2022": {"msrp": 105.9, "dealer": 80.5, "private": 74.0, "book": 68.5}
                }
            },
            {
                "gen_id": "crv-6",
                "gen_name": "第 6 代 (RS 新世代)",
                "years": [2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2023,
                "major_change_note": "2023年8月大改款第6代，軸距加長至 2700mm、車體剛性提升並標配 10 氣囊。",
                "platform": "Honda Architecture 新世代平台",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda CR-V sixth generation",
                "depreciation_alert": {
                    "level": "low",
                    "title": "新車定價拉高，一至二年車齡二手價仍處高位",
                    "reason": "10氣囊與空間放大具吸引力，議價空間較明顯。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 VTi-S / Prestige",
                        "msrp_wan": 127.9,
                        "engine_code": "L15BE 1.5L VTEC Turbo 渦輪增壓",
                        "displacement_cc": 1498,
                        "horsepower": "193 ps / 6,000 rpm",
                        "torque": "24.8 kgm / 1,800~5,000 rpm",
                        "transmission": "CVT 無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "14.7 ~ 15.0 km/L",
                        "dimensions": "4690 x 1865 x 1680 mm (軸距 2700 mm)",
                        "safety": "10氣囊、Honda SENSING 全套"
                    }
                ],
                "common_issues": [
                    {
                        "part": "車機連線偶發卡頓 / 隔音表現",
                        "severity": "低風險",
                        "mileage_range": "全里程",
                        "symptom": "無線 CarPlay 偶發斷線、高速風切聲較明顯。",
                        "repair_cost_ntd": "軟體更新處理",
                        "advice": "試乘體驗高速靜肅性與車機功能。"
                    }
                ],
                "yearly_prices": {
                    "2023": {"msrp": 117.9, "dealer": 93.0, "private": 86.5, "book": 80.5},
                    "2024": {"msrp": 117.9, "dealer": 99.5, "private": 93.0, "book": 87.0},
                    "2025": {"msrp": 117.9, "dealer": 106.0, "private": 99.5, "book": 93.5}
                }
            }
        ]
    },
    {
        "id": "mazda-3",
        "brand": "Mazda",
        "model": "Mazda3",
        "model_zh": "馬自達 Mazda 3",
        "category": "進口中型房車 / 五門掀背",
        "summary": "1代/2代(2004-2014)為福特六和國產（與 Focus 共用底盤）；3代(2014年底+)轉為日本原裝進口並導入 Skyactiv 動力；4代(2019+)質感豪華化並改後扭力樑。",
        "generations": [
            {
                "gen_id": "mazda3-1",
                "gen_name": "第 1 代 (BK 國產時期)",
                "years": [2004, 2005, 2006, 2007, 2008, 2009],
                "is_major_change": True,
                "major_change_year": 2004,
                "major_change_note": "2004年國產上市取代 323，與 Focus MK2 共用 C1 底盤並搭 4速手自排。",
                "platform": "Mazda BK / Ford C1 平台",
                "origin": "台灣國產（福特六和代工）",
                "photo_query": "Mazda3 BK sedan",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "外型至今仍耐看，但老車變速箱電磁閥與引擎腳老化明顯",
                    "reason": "因 4AT 與部分零件與 Focus 共用，維修便宜，殘值 6~11 萬。"
                },
                "trims": [
                    {
                        "trim_name": "1.6 / 2.0S (4AT)",
                        "msrp_wan": 69.9,
                        "engine_code": "Z6 1.6L / LF 2.0L 自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "150 ps / 6,500 rpm",
                        "torque": "19.1 kgm / 4,500 rpm",
                        "transmission": "4速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "13.0 km/L",
                        "dimensions": "4490 x 1755 x 1465 mm (軸距 2640 mm)",
                        "safety": "雙氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "4AT 變速箱電磁閥 / 引擎腳 / 六角鎖",
                        "severity": "中風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "亮 AT 燈鎖檔、怠速劇震、車門中控鎖失靈。",
                        "repair_cost_ntd": "電磁閥整理約 6,000~10,000 元",
                        "advice": "注意買車時排除大改裝與事故車。"
                    }
                ],
                "yearly_prices": {
                    "2004": {"msrp": 67.9, "dealer": 7.5, "private": 5.0, "book": 3.5},
                    "2005": {"msrp": 67.9, "dealer": 8.5, "private": 5.8, "book": 4.0},
                    "2006": {"msrp": 68.9, "dealer": 9.5, "private": 6.8, "book": 4.8},
                    "2007": {"msrp": 68.9, "dealer": 10.8, "private": 7.8, "book": 5.8},
                    "2008": {"msrp": 69.9, "dealer": 12.0, "private": 9.0, "book": 6.8},
                    "2009": {"msrp": 69.9, "dealer": 13.5, "private": 10.2, "book": 7.8}
                }
            },
            {
                "gen_id": "mazda3-2",
                "gen_name": "第 2 代 (BL 微笑馬3 國產末代)",
                "years": [2010, 2011, 2012, 2013, 2014],
                "is_major_change": True,
                "major_change_year": 2010,
                "major_change_note": "2009年底大改款第2代（微笑大嘴造型），2.0/2.5 升級為 5速手自排，是台灣國產末代馬3。",
                "platform": "Mazda BL 平台",
                "origin": "台灣國產（福特六和代工）",
                "photo_query": "Mazda3 BL hatchback",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "中控台環保材質融化與 TCM 電腦過熱是最大通病",
                    "reason": "TCM 變速箱電腦鎖在變速箱上方易受熱故障（亮 AT 燈），外廠多改移置防火牆位置解決。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 尊貴/頂級 (5AT)",
                        "msrp_wan": 76.9,
                        "engine_code": "LF 2.0L MZR 自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "151 ps / 6,500 rpm",
                        "torque": "19.3 kgm / 4,000 rpm",
                        "transmission": "5速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "13.1 km/L",
                        "dimensions": "4490 x 1755 x 1470 mm (軸距 2640 mm)",
                        "safety": "2氣囊、ABS (後期頂級具 DSC)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "TCM 變速箱電腦過熱故障 / 中控台出油龜裂",
                        "severity": "高風險",
                        "mileage_range": "8萬 ~ 14萬公里",
                        "symptom": "行駛中亮 AT 燈鎖檔無法換檔、前擋下儀表台黏手反光。",
                        "repair_cost_ntd": "翻修並移置 TCM 約 8,000 ~ 14,000 元",
                        "advice": "買前確認 TCM 是否已外移散熱位置。"
                    }
                ],
                "yearly_prices": {
                    "2010": {"msrp": 74.9, "dealer": 15.5, "private": 12.2, "book": 9.8},
                    "2011": {"msrp": 74.9, "dealer": 17.5, "private": 14.0, "book": 11.5},
                    "2012": {"msrp": 75.9, "dealer": 19.8, "private": 16.0, "book": 13.5},
                    "2013": {"msrp": 76.9, "dealer": 22.5, "private": 18.5, "book": 15.8},
                    "2014": {"msrp": 76.9, "dealer": 25.5, "private": 21.2, "book": 18.2}
                }
            },
            {
                "gen_id": "mazda3-3",
                "gen_name": "第 3 代 (BM / BN 魂動進口世代)",
                "years": [2015, 2016, 2017, 2018],
                "is_major_change": True,
                "major_change_year": 2015,
                "major_change_note": "2014年底大改款第3代由國產轉為日本原裝進口，導入 Skyactiv-G 2.0 引擎與 6速手自排（徹底脫離福特時期底盤與4AT/5AT）。",
                "platform": "Mazda Skyactiv 底盤（後獨立多連桿）",
                "origin": "日本原裝進口",
                "photo_query": "Mazda3 BM sedan",
                "depreciation_alert": {
                    "level": "low",
                    "title": "進口品質+自然進氣6AT穩定，年輕族群熱門首選",
                    "reason": "動力與變速箱極為耐用，無雙離合器或 CVT 隱憂，2017小改款(BN)加入 GVC 與電子手煞車後更搶手。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 尊榮 / 頂級型 (4D/5D)",
                        "msrp_wan": 88.9,
                        "engine_code": "Skyactiv-G 2.0L 高壓縮比自然進氣",
                        "displacement_cc": 1998,
                        "horsepower": "165 ps / 6,000 rpm",
                        "torque": "21.4 kgm / 4,000 rpm",
                        "transmission": "Skyactiv-Drive 6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "15.9 km/L",
                        "dimensions": "4470 x 1795 x 1450 mm (軸距 2700 mm)",
                        "safety": "6氣囊、DSC動態穩定、2017後具 SCBS-F / BSM盲點"
                    }
                ],
                "common_issues": [
                    {
                        "part": "電動後視鏡收折塑膠齒輪滑牙",
                        "severity": "中風險",
                        "mileage_range": "3萬 ~ 8萬公里",
                        "symptom": "鎖車時後視鏡無法收折或馬達空轉聲。",
                        "repair_cost_ntd": "外廠改裝金屬齒輪約 1,500 ~ 2,500 元 / 邊",
                        "advice": "幾乎每台必遇通病，改金屬齒輪即可一勞永逸。"
                    },
                    {
                        "part": "MZD Connect 螢幕觸控亂跳/分層",
                        "severity": "中風險",
                        "mileage_range": "車齡 5 年以上",
                        "symptom": "高溫曝曬後螢幕邊緣起泡、觸控自動亂點（鬼點）。",
                        "repair_cost_ntd": "更換觸控玻璃或副廠安卓機約 4,500 ~ 12,000 元",
                        "advice": "看車時測試螢幕觸控與觀察邊緣是否有氣泡龜裂。"
                    }
                ],
                "yearly_prices": {
                    "2015": {"msrp": 88.9, "dealer": 33.5, "private": 29.0, "book": 25.5},
                    "2016": {"msrp": 88.9, "dealer": 37.0, "private": 32.5, "book": 28.8},
                    "2017": {"msrp": 89.9, "dealer": 42.0, "private": 37.0, "book": 33.0},
                    "2018": {"msrp": 89.9, "dealer": 46.5, "private": 41.2, "book": 37.0}
                }
            },
            {
                "gen_id": "mazda3-4",
                "gen_name": "第 4 代 (BP 新世代)",
                "years": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2019,
                "major_change_note": "2019年中大改款！內裝質感大幅豪華化並標配全速域 CTS (Level 2)，但後懸吊由獨立多連桿改為扭力樑。",
                "platform": "Mazda Skyactiv-Vehicle Architecture (後扭力樑)",
                "origin": "日本原裝進口",
                "photo_query": "Mazda3 BP hatchback",
                "depreciation_alert": {
                    "level": "low",
                    "title": "內裝質感同級最佳且機械穩定，殘值穩健",
                    "reason": "延續成熟的 2.0 Skyactiv-G + 6AT 動力總成，無重大機械災情，五年內中古車價穩定。"
                },
                "trims": [
                    {
                        "trim_name": "20S Carbon Edition / Signature (4D/5D)",
                        "msrp_wan": 99.8,
                        "engine_code": "Skyactiv-G 2.0L 直列四缸自然進氣",
                        "displacement_cc": 1998,
                        "horsepower": "165 ps / 6,000 rpm",
                        "torque": "21.7 kgm / 4,000 rpm",
                        "transmission": "Skyactiv-Drive 6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後蝶形仿生扭力樑",
                        "fuel_economy": "15.2 ~ 15.6 km/L",
                        "dimensions": "4460 x 1795 x 1435 mm (軸距 2725 mm)",
                        "safety": "7氣囊、全速域 MRCC + CTS 車道維持"
                    }
                ],
                "common_issues": [
                    {
                        "part": "鋼琴烤漆飾板易刮傷 / 方向盤皮質脫皮",
                        "severity": "低風險",
                        "mileage_range": "全里程",
                        "symptom": "排檔座周邊易有太陽紋。",
                        "repair_cost_ntd": "貼犀牛皮保護膜約 2,000 元",
                        "advice": "屬外觀細節，不影響機械性能。"
                    }
                ],
                "yearly_prices": {
                    "2019": {"msrp": 98.9, "dealer": 54.0, "private": 48.8, "book": 44.5},
                    "2020": {"msrp": 98.9, "dealer": 59.0, "private": 53.5, "book": 49.0},
                    "2021": {"msrp": 98.9, "dealer": 64.5, "private": 58.8, "book": 54.0},
                    "2022": {"msrp": 99.8, "dealer": 70.5, "private": 64.5, "book": 59.5},
                    "2023": {"msrp": 100.8, "dealer": 77.0, "private": 70.5, "book": 65.0},
                    "2024": {"msrp": 101.8, "dealer": 84.0, "private": 77.5, "book": 71.5},
                    "2025": {"msrp": 101.8, "dealer": 90.5, "private": 84.0, "book": 78.0}
                }
            }
        ]
    }
]
