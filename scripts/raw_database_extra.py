# -*- coding: utf-8 -*-
"""
台灣市售車擴充資料庫（國產/進口休旅、跨界、掀背與豪華品牌）
"""

EXTRA_CARS_DATABASE = [
    {
        "id": "toyota-corolla-cross",
        "brand": "Toyota",
        "model": "Corolla Cross",
        "model_zh": "豐田 Corolla Cross",
        "category": "國產跨界休旅 (CUV)",
        "summary": "2020年底上市即成為台灣新車銷售總冠軍（新世代神車）。搭載 TNGA-C 底盤與 1.8L 汽油 / Hybrid 油電，妥善率極高且中古保值率稱霸同級。",
        "generations": [
            {
                "gen_id": "cc-1",
                "gen_name": "第 1 代 (XG10，含2024小改款)",
                "years": [2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2020,
                "major_change_note": "2020年10月全新車系上市，採 TNGA GA-C 平台（後扭力樑），2024年10月小改款升級電子手煞車與 Auto Hold。",
                "platform": "Toyota TNGA GA-C",
                "origin": "台灣國產（國瑞汽車）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "全台流通量最大跨界休旅，極度保值且轉手極快",
                    "reason": "1.8L 稅金省、空間實用且 TSS 標配，油電版保值度尤佳，惟須留意是否為營業多元計程車退役。"
                },
                "trims": [
                    {
                        "trim_name": "1.8L 汽油尊爵",
                        "msrp_wan": 87.9,
                        "engine_code": "2ZR-FE 1.8L 直列四缸自然進氣",
                        "displacement_cc": 1798,
                        "horsepower": "140 ps / 6,400 rpm",
                        "torque": "17.5 kgm / 4,000 rpm",
                        "transmission": "Super CVT-i (模擬7速)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "14.5 km/L",
                        "dimensions": "4460 x 1825 x 1620 mm (軸距 2640 mm)",
                        "safety": "7氣囊、TSS 2.0 (2024小改款升至全速域+EPB)"
                    },
                    {
                        "trim_name": "1.8L Hybrid 油電尊爵",
                        "msrp_wan": 93.9,
                        "engine_code": "2ZR-FXE 1.8L 油電複合動力",
                        "displacement_cc": 1798,
                        "horsepower": "綜效 122 ps",
                        "torque": "引擎 14.5 kgm + 馬達 16.6 kgm",
                        "transmission": "E-CVT 電子無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "21.9 ~ 23.5 km/L",
                        "dimensions": "4460 x 1825 x 1620 mm (軸距 2640 mm)",
                        "safety": "7氣囊、TSS 2.0、大電池8年保固"
                    }
                ],
                "common_issues": [
                    {
                        "part": "車美仕主機卡頓 / 前期無電子手煞車",
                        "severity": "低風險",
                        "mileage_range": "全里程",
                        "symptom": "2020-2023 年式採腳踏式駐煞車且早期主機偶發閃退。",
                        "repair_cost_ntd": "更新軟體或外廠升級 CarPlay",
                        "advice": "機械結構極度穩定，買二手注意核對里程排除營業用車。"
                    }
                ],
                "yearly_prices": {
                    "2020": {"msrp": 85.5, "dealer": 58.0, "private": 53.0, "book": 49.0},
                    "2021": {"msrp": 85.5, "dealer": 61.5, "private": 56.5, "book": 52.5},
                    "2022": {"msrp": 87.5, "dealer": 65.5, "private": 60.5, "book": 56.0},
                    "2023": {"msrp": 89.5, "dealer": 70.0, "private": 64.5, "book": 60.0},
                    "2024": {"msrp": 87.9, "dealer": 74.5, "private": 69.0, "book": 64.0},
                    "2025": {"msrp": 87.9, "dealer": 79.5, "private": 74.0, "book": 69.0}
                }
            }
        ]
    },
    {
        "id": "toyota-yaris",
        "brand": "Toyota",
        "model": "Yaris",
        "model_zh": "豐田 Yaris (小鴨)",
        "category": "國產小型掀背車",
        "summary": "台灣都會代步與新手練車首選，2014年大改款3代(XP150)車身放大、2016年改為 Dual VVT-i + CVT、2019年小改款標配 7 氣囊與 VSC；2023停產由 Yaris Cross 接棒。",
        "generations": [
            {
                "gen_id": "yaris-3",
                "gen_name": "第 3 代 (XP150 經典小鴨)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
                "is_major_change": True,
                "major_change_year": 2014,
                "major_change_note": "2014年底大改款第3代車格放大，2016年換裝 2NR-FE 引擎與模擬7速 CVT（取代舊款4AT），2019年全面標配 VSC 與 7氣囊。",
                "platform": "Toyota B 平台",
                "origin": "台灣國產（國瑞汽車）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "停產後中古需求依舊火熱，代步神車極抗跌",
                    "reason": "1.5L 省稅好停車且維修極便宜，建議優先選 2019 年後具備 VSC 與 7 氣囊版本。"
                },
                "trims": [
                    {
                        "trim_name": "1.5L 豪華 / 經典 (2016+ CVT)",
                        "msrp_wan": 65.5,
                        "engine_code": "2NR-FE 1.5L Dual VVT-i 自然進氣",
                        "displacement_cc": 1496,
                        "horsepower": "107 ps / 6,000 rpm",
                        "torque": "14.3 kgm / 4,200 rpm",
                        "transmission": "Super CVT-i (模擬7速)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "16.8 km/L",
                        "dimensions": "4145 x 1730 x 1500 mm (軸距 2550 mm)",
                        "safety": "2019年後標配 7氣囊 + VSC/TRC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "隔音較單薄 / 發電機碳刷磨損",
                        "severity": "一般耗材",
                        "mileage_range": "10萬公里以上",
                        "symptom": "高速風切聲明顯、高里程發電機充電異常。",
                        "repair_cost_ntd": "發電機整理約 4,500 ~ 7,000 元",
                        "advice": "幾乎無重大通病，注意排除租賃車與外送營業車。"
                    }
                ],
                "yearly_prices": {
                    "2015": {"msrp": 59.9, "dealer": 27.5, "private": 24.0, "book": 21.0},
                    "2016": {"msrp": 61.9, "dealer": 30.5, "private": 27.0, "book": 24.0},
                    "2017": {"msrp": 63.9, "dealer": 33.5, "private": 29.8, "book": 26.5},
                    "2018": {"msrp": 63.9, "dealer": 36.5, "private": 32.5, "book": 29.0},
                    "2019": {"msrp": 65.5, "dealer": 41.0, "private": 36.8, "book": 33.0},
                    "2020": {"msrp": 65.5, "dealer": 44.5, "private": 40.0, "book": 36.5},
                    "2021": {"msrp": 65.5, "dealer": 48.0, "private": 43.5, "book": 39.5},
                    "2022": {"msrp": 66.5, "dealer": 52.0, "private": 47.5, "book": 43.0}
                }
            }
        ]
    },
    {
        "id": "toyota-camry",
        "brand": "Toyota",
        "model": "Camry",
        "model_zh": "豐田 Camry",
        "category": "中大型房車",
        "summary": "7代(2012-2018)為國產商務房車；8代(2018年底+)全面轉為日本原裝進口 TNGA-K 平台，2.5 Hybrid 與 2.0 汽油質感與操控大幅提升。",
        "generations": [
            {
                "gen_id": "camry-8",
                "gen_name": "第 8 代 (XV70 日本進口 TNGA)",
                "years": [2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2018,
                "major_change_note": "2018年底大改款由國產轉為日本原裝進口，採 TNGA-K 平台與後雙A臂，2021年新增 2.0L Dynamic Force + Direct Shift-CVT。",
                "platform": "Toyota TNGA GA-K",
                "origin": "日本原裝進口",
                "depreciation_alert": {
                    "level": "low",
                    "title": "進口品質且長途舒適度高，2.0 省稅金版受歡迎",
                    "reason": "因大型房車市場縮水，前三年折舊較 RAV4 稍多，中古入手性價比極高。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 汽油尊爵 / 2.5 Hybrid 旗艦",
                        "msrp_wan": 110.9,
                        "engine_code": "M20A-FKS 2.0L / A25A-FXS 2.5L Hybrid",
                        "displacement_cc": 1987,
                        "horsepower": "173 ps (2.0) / 綜效 218 ps (Hybrid)",
                        "torque": "21.0 kgm (2.0)",
                        "transmission": "Direct Shift-CVT / E-CVT",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "16.2 km/L (2.0) / 24.6 km/L (Hybrid)",
                        "dimensions": "4885 x 1840 x 1445 mm (軸距 2825 mm)",
                        "safety": "7氣囊、TSS 2.0"
                    }
                ],
                "common_issues": [
                    {
                        "part": "低扁平比輪胎與底盤隔音",
                        "severity": "一般耗材",
                        "mileage_range": "4萬公里以上",
                        "symptom": "18吋胎噪較明顯，高里程油電大電池檢查。",
                        "repair_cost_ntd": "輪胎換裝靜音胎",
                        "advice": "機械體質極佳，注意 2.5L 稅金較 2.0L 高一階。"
                    }
                ],
                "yearly_prices": {
                    "2019": {"msrp": 106.9, "dealer": 61.0, "private": 55.5, "book": 51.0},
                    "2020": {"msrp": 106.9, "dealer": 66.0, "private": 60.0, "book": 55.5},
                    "2021": {"msrp": 109.9, "dealer": 72.0, "private": 66.0, "book": 61.0},
                    "2022": {"msrp": 110.9, "dealer": 78.5, "private": 72.0, "book": 66.5},
                    "2023": {"msrp": 110.9, "dealer": 85.0, "private": 78.5, "book": 72.5},
                    "2024": {"msrp": 112.9, "dealer": 92.5, "private": 86.0, "book": 79.5}
                }
            }
        ]
    },
    {
        "id": "honda-fit",
        "brand": "Honda",
        "model": "Fit",
        "model_zh": "本田 Fit",
        "category": "國產小型掀背車",
        "summary": "魔術大空間小車代表。3代(2014-2021)採 1.5 i-VTEC + CVT；4代(2021年底+)大改款導入超省油 e:HEV 油電系統，但新車價拉高至 80 萬級距。",
        "generations": [
            {
                "gen_id": "fit-3",
                "gen_name": "第 3 代 (GK 世代)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020],
                "is_major_change": True,
                "major_change_year": 2014,
                "major_change_note": "2014年大改款3代改搭 Earth Dreams CVT（取代舊款5AT），空間機能極佳，2017小改款提升安全配備。",
                "platform": "Honda Global Small Car",
                "origin": "台灣國產（台灣本田）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "空間大且省油耐用，年輕首購族熱門車款",
                    "reason": "機械結構簡單，二手價格穩定，建議挑選 S 版具備 4~6 氣囊與 VSA。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 S版",
                        "msrp_wan": 68.9,
                        "engine_code": "L15Z1 1.5L SOHC i-VTEC",
                        "displacement_cc": 1497,
                        "horsepower": "120 ps / 6,600 rpm",
                        "torque": "14.8 kgm / 4,600 rpm",
                        "transmission": "CVT 無段變速 (模擬7速)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "17.4 km/L",
                        "dimensions": "3990 x 1695 x 1525 mm (軸距 2530 mm)",
                        "safety": "4~6氣囊、VSA"
                    }
                ],
                "common_issues": [
                    {
                        "part": "CVT 變速箱油老化 / 引擎腳微震",
                        "severity": "一般耗材",
                        "mileage_range": "8萬公里以上",
                        "symptom": "怠速抖動、低速微頓挫。",
                        "repair_cost_ntd": "引擎腳約 7,000 元",
                        "advice": "定期 4 萬公里更換原廠 HCF-2 變速箱油。"
                    }
                ],
                "yearly_prices": {
                    "2015": {"msrp": 65.9, "dealer": 28.0, "private": 24.5, "book": 21.5},
                    "2016": {"msrp": 65.9, "dealer": 31.0, "private": 27.2, "book": 24.0},
                    "2017": {"msrp": 68.9, "dealer": 34.5, "private": 30.5, "book": 27.0},
                    "2018": {"msrp": 68.9, "dealer": 38.0, "private": 34.0, "book": 30.5},
                    "2019": {"msrp": 68.9, "dealer": 42.0, "private": 37.5, "book": 33.8},
                    "2020": {"msrp": 68.9, "dealer": 46.0, "private": 41.5, "book": 37.5}
                }
            },
            {
                "gen_id": "fit-4",
                "gen_name": "第 4 代 (GR e:HEV 油電)",
                "years": [2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2021,
                "major_change_note": "2021年底大改款！內裝全面極簡化並標配 Honda SENSING，e:HEV 油電版市區油耗達 39.57 km/L，定價大幅拉升至 79.9~82.9 萬。",
                "platform": "Honda Global Small Car 新世代",
                "origin": "台灣國產（台灣本田）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極致省油都會小車，e:HEV 油電版二手搶手",
                    "reason": "e:HEV 幾乎以電驅為主、行路質感佳，中古保值度優於同級汽油小車。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 e:HEV 油電版",
                        "msrp_wan": 82.9,
                        "engine_code": "1.5L Atkinson + 雙電動馬達",
                        "displacement_cc": 1498,
                        "horsepower": "馬達 109 ps",
                        "torque": "25.8 kgm (馬達驅動)",
                        "transmission": "E-CVT 電驅直聯",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "26.9 km/L (市區 39.57)",
                        "dimensions": "4045 x 1695 x 1535 mm (軸距 2530 mm)",
                        "safety": "6氣囊、Honda SENSING"
                    }
                ],
                "common_issues": [
                    {
                        "part": "後座安全帶或方向機小召回 / 隔音表現",
                        "severity": "低風險",
                        "mileage_range": "全里程",
                        "symptom": "高速引擎介入充電時拉轉聲較明顯。",
                        "repair_cost_ntd": "原廠召回免費處理",
                        "advice": "機械極為成熟，確認已完成召回檢修即可。"
                    }
                ],
                "yearly_prices": {
                    "2021": {"msrp": 79.9, "dealer": 54.0, "private": 49.0, "book": 45.0},
                    "2022": {"msrp": 79.9, "dealer": 58.0, "private": 53.0, "book": 49.0},
                    "2023": {"msrp": 82.9, "dealer": 63.0, "private": 57.5, "book": 53.5},
                    "2024": {"msrp": 82.9, "dealer": 68.0, "private": 62.5, "book": 58.0},
                    "2025": {"msrp": 82.9, "dealer": 73.0, "private": 67.5, "book": 62.5}
                }
            }
        ]
    },
    {
        "id": "honda-hrv",
        "brand": "Honda",
        "model": "HR-V",
        "model_zh": "本田 HR-V",
        "category": "國產跨界休旅 (CUV)",
        "summary": "1代(2016-2022)採 1.8L 自然進氣引擎；2代(2022年中+)大改款換裝 1.5L 引擎與 Honda SENSING，空間與外型更精緻但動力偏溫順。",
        "generations": [
            {
                "gen_id": "hrv-1",
                "gen_name": "第 1 代 (RU 1.8L)",
                "years": [2016, 2017, 2018, 2019, 2020, 2021],
                "is_major_change": True,
                "major_change_year": 2016,
                "major_change_note": "2016年國產上市，採 1.8L R18 引擎 + CVT，魔術後座空間極大。",
                "platform": "Honda Global Compact",
                "origin": "台灣國產（台灣本田）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "結構耐用無渦輪負擔，家庭與女性車主熱門",
                    "reason": "1.8L NA + CVT 穩定度高，2019小改款後隔音略改善。"
                },
                "trims": [
                    {
                        "trim_name": "1.8 S版",
                        "msrp_wan": 84.0,
                        "engine_code": "R18Z9 1.8L SOHC i-VTEC",
                        "displacement_cc": 1799,
                        "horsepower": "143 ps / 6,500 rpm",
                        "torque": "17.5 kgm / 4,300 rpm",
                        "transmission": "CVT 無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "14.5 km/L",
                        "dimensions": "4334 x 1772 x 1605 mm (軸距 2610 mm)",
                        "safety": "6氣囊、VSA (缺ADAS)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "隔音較差 / 早期局部漆面防鏽",
                        "severity": "一般耗材",
                        "mileage_range": "全里程",
                        "symptom": "高速胎噪明顯、早期車門接縫檢查防鏽。",
                        "repair_cost_ntd": "隔音強化約 1 萬內",
                        "advice": "挑選 S 版配備較齊全。"
                    }
                ],
                "yearly_prices": {
                    "2016": {"msrp": 84.9, "dealer": 37.5, "private": 33.0, "book": 29.5},
                    "2017": {"msrp": 84.9, "dealer": 41.0, "private": 36.5, "book": 32.5},
                    "2018": {"msrp": 84.9, "dealer": 45.0, "private": 40.0, "book": 36.0},
                    "2019": {"msrp": 84.0, "dealer": 49.5, "private": 44.5, "book": 40.0},
                    "2020": {"msrp": 84.0, "dealer": 53.5, "private": 48.5, "book": 44.0},
                    "2021": {"msrp": 84.0, "dealer": 58.0, "private": 52.5, "book": 48.0}
                }
            },
            {
                "gen_id": "hrv-2",
                "gen_name": "第 2 代 (RV 1.5L)",
                "years": [2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2022,
                "major_change_note": "2022年6月大改款，全車系換裝 1.5L 引擎（121匹）並標配 Honda SENSING 全速域輔助駕駛。",
                "platform": "Honda 新世代小型 SUV 平台",
                "origin": "台灣國產（台灣本田）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "1.5L 省稅金與 Level 2 加持，保值度穩健",
                    "reason": "動力雖不如渦輪車狂暴，但日常代步省油好養。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 S+ / Prestige",
                        "msrp_wan": 89.9,
                        "engine_code": "L15ZF 1.5L DOHC i-VTEC",
                        "displacement_cc": 1498,
                        "horsepower": "121 ps / 6,600 rpm",
                        "torque": "14.8 kgm / 4,300 rpm",
                        "transmission": "CVT 無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "17.0 km/L",
                        "dimensions": "4330 x 1790 x 1590 mm (軸距 2610 mm)",
                        "safety": "6氣囊、Honda SENSING"
                    }
                ],
                "common_issues": [
                    {
                        "part": "爬坡動力偏溫順 / 方向機偶發異音",
                        "severity": "低風險",
                        "mileage_range": "全里程",
                        "symptom": "滿載爬坡需拉高轉速。",
                        "repair_cost_ntd": "原廠保養為主",
                        "advice": "建議先試乘確認動力是否符合用車需求。"
                    }
                ],
                "yearly_prices": {
                    "2022": {"msrp": 87.9, "dealer": 64.5, "private": 59.0, "book": 54.5},
                    "2023": {"msrp": 89.9, "dealer": 69.5, "private": 64.0, "book": 59.0},
                    "2024": {"msrp": 89.9, "dealer": 75.0, "private": 69.5, "book": 64.5},
                    "2025": {"msrp": 89.9, "dealer": 80.5, "private": 75.0, "book": 70.0}
                }
            }
        ]
    },
    {
        "id": "ford-kuga",
        "brand": "Ford",
        "model": "Kuga",
        "model_zh": "福特 Kuga",
        "category": "國產中型休旅 (SUV)",
        "summary": "以強勁渦輪動力與高性價比挑戰 CR-V/RAV4。MK2(2013-2019)有1.5T/2.0T與漏水/積碳通病；MK3(2020+)換裝 C2 平台與 8AT、Co-Pilot360，操控極佳但折舊較快，二手 CP 值極高。",
        "generations": [
            {
                "gen_id": "kuga-mk2",
                "gen_name": "MK2 / MK2.5 (EcoBoost 6AT)",
                "years": [2015, 2016, 2017, 2018, 2019],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "國產歐系休旅，採 SelectShift 6速手自排（非雙離合），2017小改款升級外型與配備。",
                "platform": "Ford Global C-Platform",
                "origin": "台灣國產（福特六和）",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "折舊較日系休旅快，但二手價格極為親民",
                    "reason": "1.5T / 2.0T 渦輪引擎高里程需留意冷卻系統與積碳整理。"
                },
                "trims": [
                    {
                        "trim_name": "EcoBoost 180 (1.5T) / 245 (2.0T AWD)",
                        "msrp_wan": 99.8,
                        "engine_code": "1.5L / 2.0L EcoBoost 缸內直噴渦輪",
                        "displacement_cc": 1498,
                        "horsepower": "182 ps (1.5T) / 245 ps (2.0T)",
                        "torque": "24.5 kgm / 38.0 kgm",
                        "transmission": "SelectShift 6速手自排",
                        "drivetrain": "前驅 / 智慧四驅",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "12.9 km/L",
                        "dimensions": "4536 x 1838 x 1695 mm (軸距 2690 mm)",
                        "safety": "7氣囊、2017後高階具 ACC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "渦輪冷卻水管/水塞滲漏與進氣積碳",
                        "severity": "中風險",
                        "mileage_range": "7萬 ~ 12萬公里",
                        "symptom": "副水箱水位下降、冷車微抖。",
                        "repair_cost_ntd": "清積碳與水管整理約 1.0 ~ 1.8 萬",
                        "advice": "買前檢查底盤護板乾爽度與變速箱換檔順暢度。"
                    }
                ],
                "yearly_prices": {
                    "2015": {"msrp": 99.8, "dealer": 27.0, "private": 22.5, "book": 19.5},
                    "2016": {"msrp": 99.8, "dealer": 31.0, "private": 26.5, "book": 23.0},
                    "2017": {"msrp": 99.8, "dealer": 36.5, "private": 31.5, "book": 28.0},
                    "2018": {"msrp": 99.8, "dealer": 41.5, "private": 36.5, "book": 32.5},
                    "2019": {"msrp": 99.8, "dealer": 46.5, "private": 41.0, "book": 37.0}
                }
            },
            {
                "gen_id": "kuga-mk3",
                "gen_name": "MK3 (C2 平台 1.5T/2.0T 8AT)",
                "years": [2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2020,
                "major_change_note": "2020年6月大改款！換裝 C2 平台、旋鈕 8AT 與 Co-Pilot360 Level 2，提供 1.5T 三缸(180匹)與 2.0T ST-Line 四缸(250匹)。",
                "platform": "Ford C2 模組化底盤",
                "origin": "台灣國產（福特六和）",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "配備與動力同級最強，但折舊幅度明顯大於 CR-V/RAV4",
                    "reason": "新車折讓與品牌口碑使中古價甜美，1.5T 需留意濕式正時皮帶換油規範，2.0T ST-Line 則為正統四缸較無皮帶隱憂。"
                },
                "trims": [
                    {
                        "trim_name": "EcoBoost 180 旗艦 / 250 ST-Line",
                        "msrp_wan": 119.9,
                        "engine_code": "1.5L 三缸渦輪 / 2.0L 四缸雙渦流渦輪",
                        "displacement_cc": 1999,
                        "horsepower": "180 ps (180) / 250 ps (250)",
                        "torque": "26.3 kgm / 38.7 kgm",
                        "transmission": "SelectShift 8速手自排",
                        "drivetrain": "前驅 (180) / AWD四驅 (250)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "15.8 km/L (180) / 12.1 km/L (250)",
                        "dimensions": "4621 x 1882 x 1678 mm (軸距 2710 mm)",
                        "safety": "7氣囊、Co-Pilot360 Level 2"
                    }
                ],
                "common_issues": [
                    {
                        "part": "1.5T 濕式正時皮帶保養規範 / 8AT 低速頓挫",
                        "severity": "中風險",
                        "mileage_range": "6萬 ~ 10萬公里",
                        "symptom": "1.5T 未用認證機油恐致皮帶劣化；2.0T 較穩定但油耗較高。",
                        "repair_cost_ntd": "預防換皮帶約 2 萬；軟體更新改善頓挫",
                        "advice": "預算夠且重視長期妥善率可優先考慮 2.0T ST-Line，或確認 1.5T 原廠保養紀錄。"
                    }
                ],
                "yearly_prices": {
                    "2020": {"msrp": 116.9, "dealer": 54.0, "private": 48.0, "book": 43.5},
                    "2021": {"msrp": 119.9, "dealer": 60.5, "private": 54.5, "book": 49.5},
                    "2022": {"msrp": 122.9, "dealer": 67.5, "private": 61.0, "book": 56.0},
                    "2023": {"msrp": 123.9, "dealer": 76.0, "private": 69.0, "book": 63.5},
                    "2024": {"msrp": 123.9, "dealer": 85.0, "private": 78.0, "book": 72.0},
                    "2025": {"msrp": 123.9, "dealer": 94.0, "private": 86.5, "book": 80.0}
                }
            }
        ]
    },
    {
        "id": "mazda-cx5",
        "brand": "Mazda",
        "model": "CX-5",
        "model_zh": "馬自達 CX-5",
        "category": "進口中型休旅 (SUV)",
        "summary": "進口質感休旅代表，2代(KF 2017+)全面採 2.0L Skyactiv-G + 6AT 為主力（另有 2.5T 渦輪），注意 1代柴油引擎(2.2D)曾有噴水/沖墊片災情，汽油版則極為穩定。",
        "generations": [
            {
                "gen_id": "cx5-2",
                "gen_name": "第 2 代 (KF 汽油 2.0 / 2.5T)",
                "years": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2017,
                "major_change_note": "2017年中大改款2代，車室隔音與豪華感大幅躍升，後續取消問題較多的 2.2D 柴油，改以 2.0 NA 與 2.5T 為主。",
                "platform": "Mazda Skyactiv 平台（後獨立多連桿）",
                "origin": "日本原裝進口",
                "depreciation_alert": {
                    "level": "low",
                    "title": "汽油 2.0 + 6AT 極為耐用，中古人氣與保值度穩定",
                    "reason": "無雙離合或 CVT 疑慮，2019年後導入全速域 MRCC 與 CarPlay 後最受歡迎。"
                },
                "trims": [
                    {
                        "trim_name": "20S Touring / Select Plus (2.0 NA)",
                        "msrp_wan": 107.9,
                        "engine_code": "Skyactiv-G 2.0L 自然進氣",
                        "displacement_cc": 1998,
                        "horsepower": "165 ps / 6,000 rpm",
                        "torque": "21.7 kgm / 4,000 rpm",
                        "transmission": "Skyactiv-Drive 6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "13.5 ~ 14.8 km/L",
                        "dimensions": "4575 x 1845 x 1680 mm (軸距 2700 mm)",
                        "safety": "6氣囊、i-ACTIVSENSE Level 2"
                    }
                ],
                "common_issues": [
                    {
                        "part": "電動後視鏡收折馬達 / 中控螢幕偶發問題",
                        "severity": "中風險",
                        "mileage_range": "5萬 ~ 9萬公里",
                        "symptom": "後視鏡收折不順、2017-2018早期螢幕偶發分層。",
                        "repair_cost_ntd": "金屬齒輪改裝約 2,000 元/邊",
                        "advice": "避開早期 2.2D 柴油版本，選 2.0 汽油版幾乎無大毛病。"
                    }
                ],
                "yearly_prices": {
                    "2017": {"msrp": 109.8, "dealer": 49.0, "private": 44.0, "book": 39.5},
                    "2018": {"msrp": 109.8, "dealer": 54.0, "private": 48.5, "book": 44.0},
                    "2019": {"msrp": 111.9, "dealer": 60.0, "private": 54.5, "book": 49.5},
                    "2020": {"msrp": 111.9, "dealer": 66.0, "private": 60.0, "book": 55.0},
                    "2021": {"msrp": 111.9, "dealer": 72.0, "private": 65.5, "book": 60.5},
                    "2022": {"msrp": 107.9, "dealer": 78.5, "private": 72.0, "book": 66.5},
                    "2023": {"msrp": 107.9, "dealer": 85.0, "private": 78.5, "book": 72.5},
                    "2024": {"msrp": 107.9, "dealer": 91.5, "private": 84.5, "book": 78.5},
                    "2025": {"msrp": 107.9, "dealer": 97.5, "private": 90.5, "book": 84.5}
                }
            }
        ]
    },
    {
        "id": "nissan-kicks",
        "brand": "Nissan",
        "model": "Kicks",
        "model_zh": "日產 Kicks",
        "category": "國產跨界休旅 (CUV)",
        "summary": "2018年底上市即熱銷的都會小休旅，2022年底小改款由 1.5L 換裝為 1.6L 第三代熔射引擎並升級 ICC 全速域與 EPB 電子手煞車。",
        "generations": [
            {
                "gen_id": "kicks-1",
                "gen_name": "第 1 代 (1.5L 前期 / 1.6L 小改款)",
                "years": [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2018,
                "major_change_note": "2018年國產上市；2022年10月大幅度小改款，引擎由 1.5L(124hp) 升級為 1.6L(135hp) 並新增全速域 ICC。",
                "platform": "Nissan V 平台",
                "origin": "台灣國產（裕隆汽車）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "省油好開且造型討喜，中古流通量大",
                    "reason": "1.5/1.6 皆為省稅金自然進氣配置，建議每 4 萬公里定期保養 CVT。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 / 1.6 智行旗艦版",
                        "msrp_wan": 85.0,
                        "engine_code": "HR15DE 1.5L / HR16DE 1.6L (2022+)",
                        "displacement_cc": 1598,
                        "horsepower": "124 ps (前期) / 135 ps (2022+)",
                        "torque": "15.0 kgm / 16.7 kgm",
                        "transmission": "第五代 Xtronic CVT",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "16.0 ~ 17.3 km/L",
                        "dimensions": "4328 x 1760 x 1613 mm (軸距 2620 mm)",
                        "safety": "6氣囊、AVM 環景、2022+具 ICC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "冷氣壓縮機電磁閥 / 引擎腳微震",
                        "severity": "一般耗材",
                        "mileage_range": "6萬公里以上",
                        "symptom": "怠速冷氣不涼或車室微震。",
                        "repair_cost_ntd": "電磁閥或引擎腳約 5,000 ~ 9,000 元",
                        "advice": "前期缺 ACC 與手拉式手煞車，在意輔助駕駛建議找 2022 年底後改款。"
                    }
                ],
                "yearly_prices": {
                    "2018": {"msrp": 79.9, "dealer": 41.0, "private": 36.5, "book": 32.5},
                    "2019": {"msrp": 79.9, "dealer": 44.5, "private": 39.8, "book": 35.5},
                    "2020": {"msrp": 79.9, "dealer": 48.5, "private": 43.5, "book": 39.0},
                    "2021": {"msrp": 79.9, "dealer": 52.5, "private": 47.5, "book": 43.0},
                    "2022": {"msrp": 85.0, "dealer": 59.0, "private": 53.5, "book": 49.0},
                    "2023": {"msrp": 85.0, "dealer": 64.5, "private": 59.0, "book": 54.0},
                    "2024": {"msrp": 85.0, "dealer": 70.0, "private": 64.5, "book": 59.5},
                    "2025": {"msrp": 85.0, "dealer": 75.5, "private": 69.5, "book": 64.5}
                }
            }
        ]
    },
    {
        "id": "vw-tiguan",
        "brand": "Volkswagen",
        "model": "Tiguan",
        "model_zh": "福斯 Tiguan",
        "category": "進口中型休旅 (SUV)",
        "summary": "台灣最熱銷德系進口 SUV。2代(AD1 2016-2024)改用 MQB 平台並全面搭載濕式 DSG（280TSI 為 DQ250 6速濕式、330/380 為 DQ500/DQ381 7速濕式），妥善率較乾式 DQ200 好上許多。",
        "generations": [
            {
                "gen_id": "tiguan-2",
                "gen_name": "第 2 代 (MQB 濕式 DSG 世代)",
                "years": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2016,
                "major_change_note": "2016年底大改款採 MQB 平台，全車系搭載「濕式」雙離合器變速箱，2021小改款導入 IQ.DRIVE 與觸控空調。",
                "platform": "VW MQB 模組化平台",
                "origin": "德國原裝進口",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "濕式 DSG 較耐操，但需留意水泵浦滲水與閥體電腦",
                    "reason": "歐系休旅保養與零件單價較日系高，五年後折舊幅度略快於 RAV4。"
                },
                "trims": [
                    {
                        "trim_name": "280 TSI Elegance (1.5T) / 330 TSI (2.0T)",
                        "msrp_wan": 139.8,
                        "engine_code": "EA211 evo 1.5L / EA888 2.0L 渦輪",
                        "displacement_cc": 1498,
                        "horsepower": "150 ps (280) / 190 ps (330)",
                        "torque": "25.5 kgm / 32.6 kgm",
                        "transmission": "DQ250/DQ381 濕式雙離合器自手排",
                        "drivetrain": "前驅 (280) / 4MOTION 四驅 (330)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "14.2 ~ 15.1 km/L",
                        "dimensions": "4509 x 1839 x 1675 mm (軸距 2678 mm)",
                        "safety": "7氣囊、IQ.DRIVE Level 2"
                    }
                ],
                "common_issues": [
                    {
                        "part": "水泵浦節溫器總成滲水 / 濕式 DSG 閥體感知器",
                        "severity": "中風險",
                        "mileage_range": "6萬 ~ 10萬公里",
                        "symptom": "冷卻水位下降、偶發「變速箱處於緊急模式」。",
                        "repair_cost_ntd": "水泵浦約 1.8 萬；閥體感知器修理包約 2.0 ~ 3.5 萬",
                        "advice": "選擇有完整原廠或專修廠保養紀錄、準時換 DSG 油的車源。"
                    }
                ],
                "yearly_prices": {
                    "2017": {"msrp": 122.8, "dealer": 54.0, "private": 47.5, "book": 42.5},
                    "2018": {"msrp": 128.8, "dealer": 61.0, "private": 54.0, "book": 48.5},
                    "2019": {"msrp": 132.8, "dealer": 68.5, "private": 61.5, "book": 55.5},
                    "2020": {"msrp": 132.8, "dealer": 76.0, "private": 68.5, "book": 62.5},
                    "2021": {"msrp": 139.8, "dealer": 86.0, "private": 78.0, "book": 71.5},
                    "2022": {"msrp": 139.8, "dealer": 95.0, "private": 87.0, "book": 80.0},
                    "2023": {"msrp": 144.8, "dealer": 105.0, "private": 96.5, "book": 89.0},
                    "2024": {"msrp": 144.8, "dealer": 115.0, "private": 106.0, "book": 98.0}
                }
            }
        ]
    },
    {
        "id": "subaru-forester",
        "brand": "Subaru",
        "model": "Forester",
        "model_zh": "速霸陸 Forester (森林人)",
        "category": "進口四驅休旅 (AWD SUV)",
        "summary": "全時四輪驅動與水平對臥引擎代表，5代(SK 2018+)採 SGP 平台與 EyeSight 主動安全，安全性口碑極佳，但保養成本與折舊較 Toyota 高。",
        "generations": [
            {
                "gen_id": "forester-5",
                "gen_name": "第 5 代 (SK SGP平台)",
                "years": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2018,
                "major_change_note": "2018年大改款換裝 SGP 全球模組化底盤、2.0L 直噴自然進氣引擎與 EyeSight 雙鏡頭輔助系統。",
                "platform": "Subaru Global Platform (SGP)",
                "origin": "日本原裝進口",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "安全配備滿載且中古價親民，留意冷氣與膠條耗材",
                    "reason": "受品牌保養據點與水平對臥維修成本印象影響，二手折舊較快，反而是高安全性的超值選擇。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 i-S EyeSight",
                        "msrp_wan": 125.8,
                        "engine_code": "FB20 2.0L 水平對臥四缸直噴",
                        "displacement_cc": 1995,
                        "horsepower": "156 ps / 6,000 rpm",
                        "torque": "20.0 kgm / 4,000 rpm",
                        "transmission": "Lineartronic CVT 無段變速",
                        "drivetrain": "SAWD 對稱式全時四輪驅動",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "13.5 km/L",
                        "dimensions": "4625 x 1815 x 1730 mm (軸距 2670 mm)",
                        "safety": "7氣囊、EyeSight 4.0 (2022+)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "TVC溫控閥 (2019-2021) / 冷氣風箱",
                        "severity": "中風險",
                        "mileage_range": "6萬 ~ 10萬公里",
                        "symptom": "熱水閥故障亮引擎燈、冷氣微漏冷媒。",
                        "repair_cost_ntd": "溫控閥約 1.5 ~ 2.2 萬（原廠有延長保固方案）",
                        "advice": "檢查是否有定期更換差速器油與 CVT 油。"
                    }
                ],
                "yearly_prices": {
                    "2018": {"msrp": 119.8, "dealer": 50.0, "private": 44.5, "book": 40.0},
                    "2019": {"msrp": 119.8, "dealer": 55.5, "private": 49.5, "book": 44.5},
                    "2020": {"msrp": 119.8, "dealer": 61.5, "private": 55.0, "book": 50.0},
                    "2021": {"msrp": 122.8, "dealer": 68.0, "private": 61.5, "book": 56.0},
                    "2022": {"msrp": 125.8, "dealer": 76.5, "private": 69.5, "book": 63.5},
                    "2023": {"msrp": 125.8, "dealer": 84.5, "private": 77.5, "book": 71.0},
                    "2024": {"msrp": 125.8, "dealer": 93.0, "private": 85.5, "book": 79.0}
                }
            }
        ]
    },
    {
        "id": "hyundai-tucson",
        "brand": "Hyundai",
        "model": "Tucson L",
        "model_zh": "現代 Tucson / Tucson L",
        "category": "國產中型休旅 (SUV)",
        "summary": "3代(2016-2021)與 4代大改款 Tucson L(2021年底+)外型前衛、軸距放大並提供 1.6T 雙離合與 1.6T 渦輪油電(6AT)，近年妥善與保值度顯著進步。",
        "generations": [
            {
                "gen_id": "tucson-4",
                "gen_name": "第 4 代 Tucson L (1.6T / 油電)",
                "years": [2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2021,
                "major_change_note": "2021年底大改款加長軸距至 2755mm（L版），1.6T 汽油採 7速雙離合、2023年新增 1.6T Turbo Hybrid 採 6速手自排。",
                "platform": "Hyundai N3 第三代平台",
                "origin": "台灣國產（三陽南陽）",
                "depreciation_alert": {
                    "level": "low",
                    "title": "空間與造型極具競爭力，渦輪油電版尤受青睞",
                    "reason": "1.6T 雙離合需留意市區塞車離合器溫度；Turbo Hybrid 改用 6AT 後更受中古買家歡迎。"
                },
                "trims": [
                    {
                        "trim_name": "GLT-B 1.6T 汽油 / GLTH-C 渦輪油電",
                        "msrp_wan": 109.9,
                        "engine_code": "Smartstream 1.6L 渦輪 / 1.6T Hybrid",
                        "displacement_cc": 1598,
                        "horsepower": "180 ps (汽油) / 綜效 230 ps (油電)",
                        "torque": "27.0 kgm / 35.7 kgm",
                        "transmission": "7速雙離合 (汽油) / 6速手自排 (油電)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "15.2 km/L (汽油) / 21.1 km/L (油電)",
                        "dimensions": "4630 x 1865 x 1670 mm (軸距 2755 mm)",
                        "safety": "6氣囊、Hyundai SmartSense Level 2"
                    }
                ],
                "common_issues": [
                    {
                        "part": "汽油版 7速乾式雙離合低速微抖",
                        "severity": "中風險",
                        "mileage_range": "6萬公里以上",
                        "symptom": "長期塞車低速半離合產生微抖或過熱提示。",
                        "repair_cost_ntd": "離合器組約 3.0 ~ 4.0 萬",
                        "advice": "若常走市區塞車路段，建議優先找 1.6T 油電版（搭配傳統 6AT）。"
                    }
                ],
                "yearly_prices": {
                    "2021": {"msrp": 106.9, "dealer": 64.0, "private": 58.0, "book": 53.5},
                    "2022": {"msrp": 108.9, "dealer": 70.5, "private": 64.5, "book": 59.5},
                    "2023": {"msrp": 110.9, "dealer": 78.0, "private": 71.5, "book": 66.0},
                    "2024": {"msrp": 112.9, "dealer": 85.5, "private": 79.0, "book": 73.0},
                    "2025": {"msrp": 112.9, "dealer": 93.0, "private": 86.0, "book": 80.0}
                }
            }
        ]
    },
    {
        "id": "lexus-nx",
        "brand": "Lexus",
        "model": "NX",
        "model_zh": "凌志 NX",
        "category": "豪華進口中型休旅",
        "summary": "台灣豪華品牌最暢銷車款！1代(AZ10 2014-2021)的 NX200 以超低故障率與親民售價稱霸；2代(AZ20 2021年底+)換裝 TNGA-K 平台與 LSS+ 3.0，二手保值率稱冠豪華車壇。",
        "generations": [
            {
                "gen_id": "nx-1",
                "gen_name": "第 1 代 (AZ10 NX200 / NX300h)",
                "years": [2016, 2017, 2018, 2019, 2020, 2021],
                "is_major_change": True,
                "major_change_year": 2014,
                "major_change_note": "2017年底推出小改款與高CP值的 NX200 (2.0 NA + CVT) 入門款，銷量爆衝，2020年式全面升級全速域 LSS+ 2.0。",
                "platform": "Toyota New MC 豪華強化平台",
                "origin": "日本原裝進口",
                "depreciation_alert": {
                    "level": "low",
                    "title": "豪華品牌保值之王，養車成本接近日系國產",
                    "reason": "NX200 採自然進氣 + CVT，幾乎沒有歐系豪華車常見的漏油或電子故障通病。"
                },
                "trims": [
                    {
                        "trim_name": "NX200 菁英版 / 豪華版",
                        "msrp_wan": 157.0,
                        "engine_code": "3ZR-FAE 2.0L 自然進氣",
                        "displacement_cc": 1987,
                        "horsepower": "150 ps / 6,100 rpm",
                        "torque": "19.3 kgm / 3,800 rpm",
                        "transmission": "Multidrive G-AI CVT (模擬8速)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "13.6 km/L",
                        "dimensions": "4640 x 1845 x 1645 mm (軸距 2660 mm)",
                        "safety": "8氣囊、LSS+ (2020後全速域)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "動力偏溫順 / 後視鏡馬達偶發異音",
                        "severity": "一般耗材",
                        "mileage_range": "8萬公里以上",
                        "symptom": "NX200 起步較不慍不火；高里程避震器上座老化。",
                        "repair_cost_ntd": "耗材保養價格極合理",
                        "advice": "優先鎖定 2020 年式後標配全速域 LSS+ 2.0 與 CarPlay 車型。"
                    }
                ],
                "yearly_prices": {
                    "2016": {"msrp": 189.0, "dealer": 69.0, "private": 62.5, "book": 57.0},
                    "2017": {"msrp": 152.0, "dealer": 76.0, "private": 69.5, "book": 64.0},
                    "2018": {"msrp": 152.0, "dealer": 84.0, "private": 77.0, "book": 71.0},
                    "2019": {"msrp": 157.0, "dealer": 92.0, "private": 85.0, "book": 78.5},
                    "2020": {"msrp": 157.0, "dealer": 102.0, "private": 94.5, "book": 87.5},
                    "2021": {"msrp": 157.0, "dealer": 111.0, "private": 103.5, "book": 96.0}
                }
            },
            {
                "gen_id": "nx-2",
                "gen_name": "第 2 代 (AZ20 TNGA-K 平台)",
                "years": [2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2021,
                "major_change_note": "2021年底大改款2代！改採 TNGA-K 平台、電子門把、大螢幕與 LSS+ 3.0，NX200 換裝 173匹 M20A 引擎。",
                "platform": "Toyota TNGA GA-K",
                "origin": "日本原裝進口",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極高流通性與超低折舊，三年內二手價極堅挺",
                    "reason": "新車曾長期缺車排隊，使中古車價長期維持高檔。"
                },
                "trims": [
                    {
                        "trim_name": "NX200 豪華 / NX350h 油電",
                        "msrp_wan": 171.0,
                        "engine_code": "M20A-FKS 2.0L / A25A-FXS 2.5L Hybrid",
                        "displacement_cc": 1987,
                        "horsepower": "173 ps (200) / 綜效 243 ps (350h)",
                        "torque": "21.0 kgm (200)",
                        "transmission": "Direct Shift-CVT / E-CVT",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立雙A臂",
                        "fuel_economy": "15.8 km/L (200) / 19.7 km/L (350h)",
                        "dimensions": "4660 x 1865 x 1660 mm (軸距 2690 mm)",
                        "safety": "8氣囊、LSS+ 3.0"
                    }
                ],
                "common_issues": [
                    {
                        "part": "電子門把初期適應 / 大螢幕軟體更新",
                        "severity": "低風險",
                        "mileage_range": "全里程",
                        "symptom": "偶發 12V 電瓶蓄電量提醒（短程少開）。",
                        "repair_cost_ntd": "原廠保固內處理",
                        "advice": "妥善率極高，檢查車身號碼確認總代理公司車。"
                    }
                ],
                "yearly_prices": {
                    "2022": {"msrp": 163.0, "dealer": 131.0, "private": 122.0, "book": 114.0},
                    "2023": {"msrp": 171.0, "dealer": 141.0, "private": 132.0, "book": 124.0},
                    "2024": {"msrp": 171.0, "dealer": 150.0, "private": 141.0, "book": 132.5},
                    "2025": {"msrp": 171.0, "dealer": 158.0, "private": 149.0, "book": 140.0}
                }
            }
        ]
    },
    {
        "id": "benz-c-class",
        "brand": "Mercedes-Benz",
        "model": "C-Class",
        "model_zh": "賓士 C-Class (C300 / C200)",
        "category": "豪華進口中型房車",
        "summary": "台灣外匯車與總代理最熱門豪華房車。W205(2014-2021)含大量美規 C300 外匯車；W206(2021年底+)全面換裝 1.5T+48V 輕油電與大螢幕內裝，豪華車前五年折舊幅度較國產車顯著。",
        "generations": [
            {
                "gen_id": "c-w205",
                "gen_name": "W205 世代 (C200 / 外匯 C300)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020],
                "is_major_change": True,
                "major_change_year": 2014,
                "major_change_note": "2014年底大改款 W205，2018年底小改款換裝 1.5T+48V (C200) 與改良 M264 2.0T (C300) + 9G-TRONIC 變速箱。",
                "platform": "Mercedes MRA 後驅平台",
                "origin": "德國/南非/美國進口（含大量美規外匯）",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "外匯車源極多、車價落差大，須嚴防事故/調錶外匯車",
                    "reason": "豪華車維修保養單價高，過保後折舊明顯；2019小改款 48V BSG 啟動馬達故障率亦須留意。"
                },
                "trims": [
                    {
                        "trim_name": "C300 (2.0T) / C200 (1.5T+48V)",
                        "msrp_wan": 248.0,
                        "engine_code": "M274 / M264 2.0L 渦輪增壓",
                        "displacement_cc": 1991,
                        "horsepower": "245 ~ 258 ps (C300)",
                        "torque": "37.7 kgm",
                        "transmission": "7G-TRONIC / 9G-TRONIC 9速手自排",
                        "drivetrain": "後輪驅動 (FR) / 4MATIC",
                        "suspension": "前/後獨立多連桿",
                        "fuel_economy": "12.5 ~ 14.3 km/L",
                        "dimensions": "4686 x 1810 x 1442 mm (軸距 2840 mm)",
                        "safety": "7氣囊、23P 智慧駕駛輔助 (選配)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "48V 輕油電 BSG 故障 (2019+小改款) / 高壓油管滲油",
                        "severity": "高風險",
                        "mileage_range": "6萬 ~ 10萬公里",
                        "symptom": "亮 48V 電池故障無法發動；冷車引擎室汽油味（高壓油管）。",
                        "repair_cost_ntd": "48V BSG 維修約 3.5 ~ 6.5 萬；凸輪軸感應器滲油約 1.5 萬",
                        "advice": "外匯車務必查閱 Carfax/AutoCheck 報告並檢驗萊茵認證。"
                    }
                ],
                "yearly_prices": {
                    "2015": {"msrp": 235.0, "dealer": 68.0, "private": 59.0, "book": 52.0},
                    "2016": {"msrp": 235.0, "dealer": 76.0, "private": 66.5, "book": 59.0},
                    "2017": {"msrp": 240.0, "dealer": 85.0, "private": 75.0, "book": 67.0},
                    "2018": {"msrp": 240.0, "dealer": 96.0, "private": 85.5, "book": 77.0},
                    "2019": {"msrp": 248.0, "dealer": 112.0, "private": 100.0, "book": 91.0},
                    "2020": {"msrp": 248.0, "dealer": 126.0, "private": 114.0, "book": 104.0}
                }
            }
        ]
    },
    {
        "id": "bmw-3-series",
        "brand": "BMW",
        "model": "3 Series",
        "model_zh": "寶馬 3系列 (320i / 330i)",
        "category": "豪華進口中型運動房車",
        "summary": "豪華後驅操控標竿。F30(2012-2018)後期 B48 引擎大幅改善 N20 漏油問題；G20(2019+)採 CLAR 平台與新世代 B48 引擎 + ZF 8AT，妥善率與操控口碑俱佳。",
        "generations": [
            {
                "gen_id": "bmw-g20",
                "gen_name": "G20 世代 (B48 + ZF 8AT)",
                "years": [2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2019,
                "major_change_note": "2019年大改款 G20，換裝 CLAR 高剛性平台與極成熟的 B48 2.0T 引擎 + ZF 8速手自排，全面標配 5AU 智慧駕駛。",
                "platform": "BMW CLAR 後驅平台",
                "origin": "德國原裝進口",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "B48 + ZF8AT 體質極佳，留意歐系冷卻管路耗材",
                    "reason": "前三年豪華車折舊較快，四至六年車齡中古入手非常划算。"
                },
                "trims": [
                    {
                        "trim_name": "320i M Sport / 330i M Sport",
                        "msrp_wan": 246.0,
                        "engine_code": "B48B20 2.0L TwinPower Turbo",
                        "displacement_cc": 1998,
                        "horsepower": "184 ps (320i) / 258 ps (330i)",
                        "torque": "30.6 kgm / 40.8 kgm",
                        "transmission": "ZF Steptronic 8速手自排",
                        "drivetrain": "後輪驅動 (FR)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "14.2 km/L",
                        "dimensions": "4709 x 1827 x 1435 mm (軸距 2851 mm)",
                        "safety": "6氣囊、5AU Level 2 半自動駕駛"
                    }
                ],
                "common_issues": [
                    {
                        "part": "熱管理模組 / 機油濾芯座滲水滲油",
                        "severity": "中風險",
                        "mileage_range": "7萬 ~ 10萬公里",
                        "symptom": "副水箱水位緩降、引擎側邊滲漏。",
                        "repair_cost_ntd": "塑膠冷卻件預防更換約 1.8 ~ 3.0 萬",
                        "advice": "B48 引擎與 ZF8AT 相當耐用，只需固定里程預防性更新塑膠水管與水箱蓋。"
                    }
                ],
                "yearly_prices": {
                    "2019": {"msrp": 239.0, "dealer": 106.0, "private": 95.0, "book": 86.0},
                    "2020": {"msrp": 239.0, "dealer": 119.0, "private": 108.0, "book": 98.0},
                    "2021": {"msrp": 243.0, "dealer": 134.0, "private": 122.0, "book": 112.0},
                    "2022": {"msrp": 246.0, "dealer": 149.0, "private": 136.0, "book": 125.0},
                    "2023": {"msrp": 246.0, "dealer": 168.0, "private": 154.0, "book": 142.0},
                    "2024": {"msrp": 246.0, "dealer": 186.0, "private": 172.0, "book": 159.0}
                }
            }
        ]
    },
    {
        "id": "suzuki-swift",
        "brand": "Suzuki",
        "model": "Swift",
        "model_zh": "鈴木 Swift",
        "category": "進口都會小車",
        "summary": "日本原裝進口小車，省稅省油好停車。2021年後改採 1.2L + 12V 輕油電，2024年大改款換裝 1.2L 三缸輕油電，二手保值率在進口小車中名列前茅。",
        "generations": [
            {
                "gen_id": "swift-4",
                "gen_name": "第 4 代 (1.0T / 1.2L 輕油電)",
                "years": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2017,
                "major_change_note": "2017年底大改款採 HEARTECT 輕量化底盤，前期為 1.0T 渦輪+6AT，2021年改為 1.2L 輕油電+CVT並標配 ACC。",
                "platform": "Suzuki HEARTECT 平台",
                "origin": "日本原裝進口",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極省油且日本進口身分，中古搶手度極高",
                    "reason": "稅金屬最低級距（1.2L 每年僅 8,640 元），維修單純。"
                },
                "trims": [
                    {
                        "trim_name": "1.2 GLX 輕油電 (2021+)",
                        "msrp_wan": 72.0,
                        "engine_code": "K12D 1.2L 四缸 + 12V SHVS 輕油電",
                        "displacement_cc": 1197,
                        "horsepower": "83 ps / 6,000 rpm",
                        "torque": "11.0 kgm / 2,800 rpm",
                        "transmission": "CVT 無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "22.3 km/L",
                        "dimensions": "3845 x 1735 x 1480 mm (軸距 2450 mm)",
                        "safety": "6氣囊、ACC 主動定速、AEB"
                    }
                ],
                "common_issues": [
                    {
                        "part": "隔音較單薄 / 輕油電小電池壽命",
                        "severity": "一般耗材",
                        "mileage_range": "車齡 5 年以上",
                        "symptom": "高速風切聲與底盤噪音較明顯。",
                        "repair_cost_ntd": "一般保養耗材極便宜",
                        "advice": "喜愛動力可找 2018-2020 年 1.0T 6AT 版；喜愛省油安全選 2021+ 1.2 輕油電。"
                    }
                ],
                "yearly_prices": {
                    "2018": {"msrp": 66.9, "dealer": 35.5, "private": 31.5, "book": 28.0},
                    "2019": {"msrp": 66.9, "dealer": 38.5, "private": 34.5, "book": 31.0},
                    "2020": {"msrp": 66.9, "dealer": 42.0, "private": 37.5, "book": 34.0},
                    "2021": {"msrp": 70.0, "dealer": 47.0, "private": 42.5, "book": 38.5},
                    "2022": {"msrp": 72.0, "dealer": 51.0, "private": 46.5, "book": 42.0},
                    "2023": {"msrp": 72.0, "dealer": 55.0, "private": 50.5, "book": 46.0},
                    "2024": {"msrp": 73.0, "dealer": 60.0, "private": 55.0, "book": 50.5}
                }
            }
        ]
    }
]
