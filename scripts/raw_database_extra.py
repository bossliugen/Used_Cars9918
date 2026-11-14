# -*- coding: utf-8 -*-
"""
台灣市售車擴充資料庫（含 2000 年起歷代車型、通病與外型照片搜尋關鍵字）
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
                "photo_query": "Toyota Corolla Cross XG10",
                "depreciation_alert": {
                    "level": "low",
                    "title": "全台流通量最大跨界休旅，極度保值且轉手極快",
                    "reason": "1.8L 稅金省、空間實用且 TSS 標配，油電版保值度尤佳，惟須留意是否為營業多元計程車退役。"
                },
                "trims": [
                    {
                        "trim_name": "1.8L 汽油尊爵 / 豪華",
                        "msrp_wan": 87.9,
                        "engine_code": "2ZR-FE 1.8L 自然進氣",
                        "displacement_cc": 1798,
                        "horsepower": "140 ps / 6,400 rpm",
                        "torque": "17.5 kgm / 4,000 rpm",
                        "transmission": "Super CVT-i 模擬7速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "14.5 km/L",
                        "dimensions": "4460 x 1825 x 1620 mm (軸距 2640 mm)",
                        "safety": "7氣囊、TSS 2.0"
                    },
                    {
                        "trim_name": "1.8L Hybrid 油電尊爵 / GR Sport",
                        "msrp_wan": 95.9,
                        "engine_code": "2ZR-FXE 1.8L Hybrid 油電複合動力",
                        "displacement_cc": 1798,
                        "horsepower": "綜效 122 ps",
                        "torque": "14.5 kgm + 馬達輔助",
                        "transmission": "E-CVT 電子無段變速",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "21.9 km/L",
                        "dimensions": "4460 x 1825 x 1620 mm (軸距 2640 mm)",
                        "safety": "7氣囊、TSS 2.0"
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
        "summary": "2006年 2代(XP90) 首度國產化即成都會小車霸主；2014年 3代(XP150)車格放大並於 2016年改裝 CVT；2023停產後二手保值依舊強勁。",
        "generations": [
            {
                "gen_id": "yaris-2",
                "gen_name": "第 2 代 (XP90 首代國產小鴨)",
                "years": [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
                "is_major_change": True,
                "major_change_year": 2006,
                "major_change_note": "2006年底台灣國產上市，採中置儀表板與 1NZ-FE 1.5L 引擎 + 傳統 4速自排，耐操好停。",
                "platform": "Toyota B 平台",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Yaris XP90",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極為保值的練車神車，4AT 幾乎開不壞",
                    "reason": "1.5L 省稅金、車身短好停車，12年以上老鴨至今仍有 13~23 萬行情。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 E / G / S (4AT)",
                        "msrp_wan": 57.9,
                        "engine_code": "1NZ-FE 1.5L VVT-i 自然進氣",
                        "displacement_cc": 1497,
                        "horsepower": "109 ps / 6,000 rpm",
                        "torque": "14.4 kgm / 4,200 rpm",
                        "transmission": "4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "17.4 km/L (美規)",
                        "dimensions": "3785 x 1695 x 1520 mm (軸距 2460 mm)",
                        "safety": "2氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "發電機軸承異音 / 避震器上座與引擎腳老化",
                        "severity": "一般耗材",
                        "mileage_range": "10萬公里以上",
                        "symptom": "怠速震動或發電機高頻異音。",
                        "repair_cost_ntd": "發電機約 4,500 元；引擎腳約 6,000 元",
                        "advice": "無重大通病，注意確認非租賃或駕訓班淘汰車。"
                    }
                ],
                "yearly_prices": {
                    "2007": {"msrp": 54.9, "dealer": 15.0, "private": 12.0, "book": 9.5},
                    "2008": {"msrp": 55.9, "dealer": 16.5, "private": 13.5, "book": 10.8},
                    "2009": {"msrp": 55.9, "dealer": 18.0, "private": 14.8, "book": 12.0},
                    "2010": {"msrp": 56.9, "dealer": 19.5, "private": 16.2, "book": 13.5},
                    "2011": {"msrp": 56.9, "dealer": 21.2, "private": 17.8, "book": 15.0},
                    "2012": {"msrp": 57.9, "dealer": 23.0, "private": 19.5, "book": 16.5},
                    "2013": {"msrp": 57.9, "dealer": 24.8, "private": 21.2, "book": 18.0}
                }
            },
            {
                "gen_id": "yaris-3",
                "gen_name": "第 3 代 (XP150 大鴨)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
                "is_major_change": True,
                "major_change_year": 2014,
                "major_change_note": "2014年底大改款第3代車格放大，2016年換裝 2NR-FE 引擎與模擬7速 CVT，2019年全面標配 VSC 與 7氣囊。",
                "platform": "Toyota B 平台",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Yaris XP150",
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
        "summary": "5代(2002-2006)與6代(2006-2011)為經典國產主管房車；7代(2012-2018)導入 Hybrid 油電；8代(2019+)全面轉為日本原裝進口 TNGA-K 平台。",
        "generations": [
            {
                "gen_id": "camry-5",
                "gen_name": "第 5 代 (XV30 國產主管房車)",
                "years": [2002, 2003, 2004, 2005],
                "is_major_change": True,
                "major_change_year": 2002,
                "major_change_note": "2002年國瑞首度國產化 Camry，採 2.0L 1AZ-FE 與 3.0L V6 搭配 4AT。",
                "platform": "Toyota K 平台",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Camry XV30",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "1AZ 引擎汽缸蓋螺絲滑牙通病 + 老車內裝龜裂",
                    "reason": "車齡逾 20 年，高里程 1AZ 引擎容易出現汽缸蓋鋁合金螺牙滑牙滲水，殘值 6~10 萬。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 E / G (4AT)",
                        "msrp_wan": 86.9,
                        "engine_code": "1AZ-FE 2.0L VVT-i 自然進氣",
                        "displacement_cc": 1998,
                        "horsepower": "150 ps / 6,000 rpm",
                        "torque": "20.1 kgm / 4,000 rpm",
                        "transmission": "4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前/後麥花臣",
                        "fuel_economy": "12.0 km/L",
                        "dimensions": "4815 x 1795 x 1490 mm (軸距 2720 mm)",
                        "safety": "2氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "1AZ 引擎汽缸蓋螺絲滑牙滲水 / 中控台黏手龜裂",
                        "severity": "高風險",
                        "mileage_range": "15萬公里以上",
                        "symptom": "副水箱冒泡失水、機油乳化。",
                        "repair_cost_ntd": "重做缸體螺牙套管約 1.5 ~ 2.5 萬",
                        "advice": "買前務必檢查冷卻水是否混濁與水箱壓力。"
                    }
                ],
                "yearly_prices": {
                    "2002": {"msrp": 84.9, "dealer": 8.0, "private": 5.5, "book": 3.5},
                    "2003": {"msrp": 84.9, "dealer": 9.0, "private": 6.2, "book": 4.2},
                    "2004": {"msrp": 86.9, "dealer": 10.0, "private": 7.0, "book": 4.8},
                    "2005": {"msrp": 86.9, "dealer": 11.2, "private": 8.0, "book": 5.8}
                }
            },
            {
                "gen_id": "camry-6",
                "gen_name": "第 6 代 (XV40 2.0/2.4/3.5)",
                "years": [2006, 2007, 2008, 2009, 2010, 2011],
                "is_major_change": True,
                "major_change_year": 2006,
                "major_change_note": "2006年大改款，2.0 維持 4AT、2.4 升為 5AT、3.5 V6 採 6AT。",
                "platform": "Toyota K 平台",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Camry XV40",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "2.4L 2AZ-FE 吃機油通病 + 環保中控台融化",
                    "reason": "2.4L 引擎高里程易吃機油且稅金高一階，2.0E 反而因省稅且無 2AZ 吃機油問題較好脫手。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 E (4AT) / 2.4 G (5AT)",
                        "msrp_wan": 88.9,
                        "engine_code": "1AZ-FE 2.0L / 2AZ-FE 2.4L",
                        "displacement_cc": 1998,
                        "horsepower": "147 ps (2.0) / 167 ps (2.4)",
                        "torque": "19.4 kgm / 22.9 kgm",
                        "transmission": "4速自排 / 5速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前/後麥花臣",
                        "fuel_economy": "12.5 km/L",
                        "dimensions": "4825 x 1820 x 1470 mm (軸距 2775 mm)",
                        "safety": "2氣囊、ABS (高階具 VSC)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "中控台環保材質融化反光 / 2.4L 吃機油 / HID霧化",
                        "severity": "中風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "中控台黏手反光、2.4L 機油消耗。",
                        "repair_cost_ntd": "包覆皮面約 6,000 元",
                        "advice": "挑 2.0 版本省稅金，或確認 2.4 是否已整理活塞環。"
                    }
                ],
                "yearly_prices": {
                    "2006": {"msrp": 84.9, "dealer": 13.5, "private": 10.2, "book": 7.8},
                    "2007": {"msrp": 84.9, "dealer": 15.0, "private": 11.5, "book": 8.8},
                    "2008": {"msrp": 86.9, "dealer": 16.8, "private": 13.0, "book": 10.2},
                    "2009": {"msrp": 86.9, "dealer": 18.5, "private": 14.5, "book": 11.5},
                    "2010": {"msrp": 88.9, "dealer": 20.5, "private": 16.5, "book": 13.2},
                    "2011": {"msrp": 88.9, "dealer": 22.8, "private": 18.5, "book": 15.0}
                }
            },
            {
                "gen_id": "camry-7",
                "gen_name": "第 7 代 (XV50 國產末代 / Hybrid)",
                "years": [2012, 2013, 2014, 2015, 2016, 2017, 2018],
                "is_major_change": True,
                "major_change_year": 2012,
                "major_change_note": "2012年大改款首度國產化 2.5 Hybrid 油電；2015年小改款將 2.0L 引擎升級為 6AR-FSE + 6速手自排。",
                "platform": "Toyota K 平台",
                "origin": "台灣國產（國瑞汽車）",
                "photo_query": "Toyota Camry XV50",
                "depreciation_alert": {
                    "level": "low",
                    "title": "2015年後 2.0 6AT 極度穩定，油電版須留意大電池壽命",
                    "reason": "空間寬敞且保養極省，2015後 2.0 豪華版是中大型國產房車首選。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 豪華 (6AT) / 2.5 Hybrid",
                        "msrp_wan": 92.9,
                        "engine_code": "6AR-FSE 2.0L (2015+) / 2AR-FXE 2.5L Hybrid",
                        "displacement_cc": 1998,
                        "horsepower": "167 ps (2.0) / 綜效 205 ps (Hybrid)",
                        "torque": "20.3 kgm (2.0)",
                        "transmission": "6速手自排 / E-CVT",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前/後麥花臣",
                        "fuel_economy": "13.5 km/L (2.0) / 19.6 km/L (Hybrid)",
                        "dimensions": "4850 x 1825 x 1480 mm (軸距 2775 mm)",
                        "safety": "2~4氣囊、VSC (高階)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "Hybrid 大電池與 ABS 蓄壓器老化 (高里程油電)",
                        "severity": "中風險",
                        "mileage_range": "15萬公里或車齡8年以上",
                        "symptom": "儀表亮 Hybrid 系統檢查燈、煞車泵浦頻繁作動。",
                        "repair_cost_ntd": "原廠更換大電池約 5~6.5 萬",
                        "advice": "預算考量建議買 2015 年後 2.0 6AT 汽油版，養護最省心。"
                    }
                ],
                "yearly_prices": {
                    "2012": {"msrp": 89.9, "dealer": 26.0, "private": 22.0, "book": 18.5},
                    "2013": {"msrp": 89.9, "dealer": 28.5, "private": 24.5, "book": 21.0},
                    "2014": {"msrp": 89.9, "dealer": 31.5, "private": 27.2, "book": 23.5},
                    "2015": {"msrp": 92.9, "dealer": 36.5, "private": 32.0, "book": 28.0},
                    "2016": {"msrp": 92.9, "dealer": 40.5, "private": 35.8, "book": 31.5},
                    "2017": {"msrp": 93.9, "dealer": 44.5, "private": 39.5, "book": 35.0},
                    "2018": {"msrp": 93.9, "dealer": 49.0, "private": 43.8, "book": 39.0}
                }
            },
            {
                "gen_id": "camry-8",
                "gen_name": "第 8 代 (XV70 日本進口 TNGA)",
                "years": [2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2019,
                "major_change_note": "2018年底大改款由國產轉為日本原裝進口，採 TNGA-K 平台與後雙A臂，2021年新增 2.0L Dynamic Force + Direct Shift-CVT。",
                "platform": "Toyota TNGA GA-K",
                "origin": "日本原裝進口",
                "photo_query": "Toyota Camry XV70",
                "depreciation_alert": {
                    "level": "low",
                    "title": "進口品質且長途舒適度高，2.0 省稅金版受歡迎",
                    "reason": "前三年折舊較 RAV4 稍多，中古入手性價比極高。"
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
        "summary": "魔術大空間小車代表。2代(2008-2014)採耐操 5AT；3代(2015-2020)改搭 CVT；4代(2021年底+)大改款導入超省油 e:HEV 油電系統。",
        "generations": [
            {
                "gen_id": "fit-2",
                "gen_name": "第 2 代 (GE 首代國產 5AT)",
                "years": [2008, 2009, 2010, 2011, 2012, 2013, 2014],
                "is_major_change": True,
                "major_change_year": 2008,
                "major_change_note": "2008年台灣本田首度國產 Fit，搭載 L15A 1.5L 引擎與耐用的 5速手自排。",
                "platform": "Honda Global Small Car",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda Fit GE8",
                "depreciation_alert": {
                    "level": "low",
                    "title": "5AT 耐操好養且空間驚人，20萬內代步超熱門",
                    "reason": "同級少見 5速傳統自排，幾乎無變速箱大修災情，殘值非常抗跌。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 VTi / VTi-S (5AT)",
                        "msrp_wan": 63.9,
                        "engine_code": "L15A7 1.5L SOHC i-VTEC",
                        "displacement_cc": 1497,
                        "horsepower": "120 ps / 6,600 rpm",
                        "torque": "14.8 kgm / 4,800 rpm",
                        "transmission": "5速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "14.5 km/L",
                        "dimensions": "3900 x 1695 x 1525 mm (軸距 2500 mm)",
                        "safety": "2~4氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "點火考耳(Coil)老化 / 後門防水膜滲水",
                        "severity": "一般耗材",
                        "mileage_range": "10萬公里以上",
                        "symptom": "加速頓挫亮引擎燈、雨天後座腳踏墊積水。",
                        "repair_cost_ntd": "考耳4支約 4,000 元；門板重貼防水膠約 1,500 元",
                        "advice": "小問題好處理，注意 2011 小改款後質感較佳。"
                    }
                ],
                "yearly_prices": {
                    "2008": {"msrp": 59.9, "dealer": 16.0, "private": 13.0, "book": 10.5},
                    "2009": {"msrp": 59.9, "dealer": 17.5, "private": 14.2, "book": 11.5},
                    "2010": {"msrp": 61.9, "dealer": 19.2, "private": 15.8, "book": 13.0},
                    "2011": {"msrp": 63.9, "dealer": 21.5, "private": 18.0, "book": 15.0},
                    "2012": {"msrp": 63.9, "dealer": 23.5, "private": 19.8, "book": 16.8},
                    "2013": {"msrp": 63.9, "dealer": 25.5, "private": 21.8, "book": 18.5},
                    "2014": {"msrp": 63.9, "dealer": 27.5, "private": 23.5, "book": 20.0}
                }
            },
            {
                "gen_id": "fit-3",
                "gen_name": "第 3 代 (GK 世代)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020],
                "is_major_change": True,
                "major_change_year": 2015,
                "major_change_note": "大改款3代改搭 Earth Dreams CVT（取代舊款5AT），空間機能極佳，2017小改款提升安全配備。",
                "platform": "Honda Global Small Car",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda Fit GK5",
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
                "major_change_note": "2021年底大改款！內裝極簡化並標配 Honda SENSING，e:HEV 油電版市區油耗達 39.57 km/L。",
                "platform": "Honda Global Small Car 新世代",
                "origin": "台灣國產（台灣本田）",
                "photo_query": "Honda Fit GR e:HEV",
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
        "summary": "1代(2016-2021)採 1.8L 自然進氣引擎；2代(2022年中+)大改款換裝 1.5L 引擎與 Honda SENSING，空間與外型更精緻。",
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
                "photo_query": "Honda HR-V RU",
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
                "photo_query": "Honda HR-V RV 2022",
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
        "summary": "以強勁渦輪動力挑戰 CR-V/RAV4。MK2(2013-2019)有1.5T/2.0T與漏水/積碳通病；MK3(2020+)換裝 C2 平台與 8AT、Co-Pilot360，折舊較快使得二手 CP 值極高。",
        "generations": [
            {
                "gen_id": "kuga-mk2",
                "gen_name": "MK2 / MK2.5 (EcoBoost 6AT)",
                "years": [2013, 2014, 2015, 2016, 2017, 2018, 2019],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "2013年首度國產歐系休旅，採 SelectShift 6速手自排（非雙離合），2017小改款升級外型與配備。",
                "platform": "Ford Global C-Platform",
                "origin": "台灣國產（福特六和）",
                "photo_query": "Ford Kuga Mk2",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "折舊較日系休旅快，但二手價格極為親民",
                    "reason": "1.5T / 2.0T 渦輪引擎高里程需留意冷卻系統與積碳整理，早期 1.6T 水箱漏水亦須檢查。"
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
                    "2013": {"msrp": 99.8, "dealer": 21.0, "private": 17.0, "book": 14.0},
                    "2014": {"msrp": 99.8, "dealer": 24.0, "private": 19.5, "book": 16.5},
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
                "photo_query": "Ford Kuga Mk3",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "配備與動力同級最強，但折舊幅度明顯大於 CR-V/RAV4",
                    "reason": "1.5T 需留意濕式正時皮帶換油規範，2.0T ST-Line 則為正統四缸較無皮帶隱憂。"
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
                        "advice": "重視長期妥善率可優先考慮 2.0T ST-Line，或確認 1.5T 原廠保養紀錄。"
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
        "summary": "1代(KE 2012-2016)曾導入 2.2D 柴油引發大規模噴水/沖墊片災情導致柴油版殘值崩跌；2代(KF 2017+)改以 2.0 汽油為主力，極為穩定保值。",
        "generations": [
            {
                "gen_id": "cx5-1",
                "gen_name": "第 1 代 (KE 世代，含2.2D柴油災情)",
                "years": [2012, 2013, 2014, 2015, 2016],
                "is_major_change": True,
                "major_change_year": 2012,
                "major_change_note": "2012年導入 Skyactiv 首發休旅 CX-5，提供 2.0 汽油與 2.2D 柴油。",
                "platform": "Mazda Skyactiv 平台",
                "origin": "日本原裝進口",
                "photo_query": "Mazda CX-5 KE",
                "depreciation_alert": {
                    "level": "high",
                    "title": "1代 2.2D 柴油引擎「噴水/沖墊片」災情導致殘值極低",
                    "reason": "2.2D 柴油版在台灣發生大規模副水箱噴水、機油乳化災情（引發自救會與原廠延保），使 1 代柴油殘值暴跌；2.0 汽油版則完全正常。"
                },
                "trims": [
                    {
                        "trim_name": "2.0L Skyactiv-G 汽油 (極推薦)",
                        "msrp_wan": 106.8,
                        "engine_code": "Skyactiv-G 2.0L 自然進氣",
                        "displacement_cc": 1998,
                        "horsepower": "155~165 ps / 6,000 rpm",
                        "torque": "20.4 kgm / 4,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前驅 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "13.2 km/L",
                        "dimensions": "4540 x 1840 x 1710 mm (軸距 2700 mm)",
                        "safety": "6氣囊、DSC"
                    },
                    {
                        "trim_name": "2.2D Skyactiv-D 柴油 AWD (高風險)",
                        "msrp_wan": 133.8,
                        "engine_code": "Skyactiv-D 2.2L 雙渦輪柴油",
                        "displacement_cc": 2191,
                        "horsepower": "175 ps / 4,500 rpm",
                        "torque": "42.8 kgm / 2,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "i-ACTIV AWD 四輪驅動",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "15.2 km/L",
                        "dimensions": "4540 x 1840 x 1710 mm (軸距 2700 mm)",
                        "safety": "6氣囊、DSC、盲點偵測"
                    }
                ],
                "common_issues": [
                    {
                        "part": "2.2D 柴油引擎汽缸蓋墊片沖毀噴水 / 進氣歧管積碳",
                        "severity": "高風險",
                        "mileage_range": "8萬 ~ 14萬公里",
                        "symptom": "高速行駛副水箱噴水、水溫過高、DPF 阻塞。",
                        "repair_cost_ntd": "引擎大修約 6~10 萬",
                        "advice": "買 1 代 CX-5 請務必只選 2.0 汽油版，完全避開 2.2D 柴油。"
                    }
                ],
                "yearly_prices": {
                    "2012": {"msrp": 106.8, "dealer": 24.0, "private": 19.5, "book": 16.5},
                    "2013": {"msrp": 106.8, "dealer": 26.5, "private": 22.0, "book": 18.5},
                    "2014": {"msrp": 106.8, "dealer": 29.5, "private": 24.5, "book": 21.0},
                    "2015": {"msrp": 106.8, "dealer": 33.0, "private": 28.0, "book": 24.0},
                    "2016": {"msrp": 106.8, "dealer": 37.5, "private": 32.0, "book": 28.0}
                }
            },
            {
                "gen_id": "cx5-2",
                "gen_name": "第 2 代 (KF 汽油 2.0 / 2.5T)",
                "years": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2017,
                "major_change_note": "2017年中大改款2代，車室隔音與豪華感大幅躍升，後續取消 2.2D 柴油，改以 2.0 NA 與 2.5T 為主。",
                "platform": "Mazda Skyactiv 平台（後獨立多連桿）",
                "origin": "日本原裝進口",
                "photo_query": "Mazda CX-5 KF",
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
                        "advice": "選 2.0 汽油版幾乎無大毛病。"
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
                "photo_query": "Nissan Kicks",
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
        "summary": "1代(2008-2016)採 2.0T + 傳統6AT/濕式DQ500；2代(2017+)改用 MQB 平台並全面搭載濕式 DSG，妥善率較乾式 DQ200 好上許多。",
        "generations": [
            {
                "gen_id": "tiguan-1",
                "gen_name": "第 1 代 (5N PQ35 平台)",
                "years": [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "is_major_change": True,
                "major_change_year": 2009,
                "major_change_note": "台灣首代 Tiguan，早期搭愛信 6AT，2012小改款後改搭濕式 7速 DQ500 DSG，1.4TSI 則採濕式 6速 DQ250。",
                "platform": "VW PQ35 平台",
                "origin": "德國原裝進口",
                "photo_query": "Volkswagen Tiguan 5N",
                "depreciation_alert": {
                    "level": "high",
                    "title": "早期 EA888 吃機油/正時鍊條 + 水泵浦漏水拉低殘值",
                    "reason": "1代 2.0 TSI 搭載早期 EA888 二代引擎，高里程容易吃機油、積碳與鍊條張力器異常，二手價僅 16~30 萬。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 TSI Trend & Fun / Sport & Style",
                        "msrp_wan": 144.8,
                        "engine_code": "EA888 2.0L TSI 渦輪增壓",
                        "displacement_cc": 1984,
                        "horsepower": "180 ~ 200 ps",
                        "torque": "28.6 kgm",
                        "transmission": "6AT / DQ500 7速濕式 DSG",
                        "drivetrain": "4MOTION 四輪驅動",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "10.8 km/L",
                        "dimensions": "4426 x 1809 x 1703 mm (軸距 2604 mm)",
                        "safety": "6氣囊、ESP"
                    }
                ],
                "common_issues": [
                    {
                        "part": "EA888 吃機油 / 正時鍊條 / 塑膠水泵浦滲水",
                        "severity": "高風險",
                        "mileage_range": "8萬 ~ 12萬公里",
                        "symptom": "每兩千公里補機油、冷車啟動異音、天篷脫落。",
                        "repair_cost_ntd": "整理吃機油與鍊條約 4~6 萬",
                        "advice": "買前確認是否已大修過活塞環與正時鍊條。"
                    }
                ],
                "yearly_prices": {
                    "2010": {"msrp": 142.8, "dealer": 18.0, "private": 14.0, "book": 11.0},
                    "2011": {"msrp": 142.8, "dealer": 20.5, "private": 16.0, "book": 13.0},
                    "2012": {"msrp": 144.8, "dealer": 23.5, "private": 19.0, "book": 15.5},
                    "2013": {"msrp": 144.8, "dealer": 26.5, "private": 21.8, "book": 18.0},
                    "2014": {"msrp": 144.8, "dealer": 30.0, "private": 25.0, "book": 21.0},
                    "2015": {"msrp": 144.8, "dealer": 34.0, "private": 28.5, "book": 24.5},
                    "2016": {"msrp": 144.8, "dealer": 38.5, "private": 33.0, "book": 28.5}
                }
            },
            {
                "gen_id": "tiguan-2",
                "gen_name": "第 2 代 (MQB 濕式 DSG 世代)",
                "years": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2017,
                "major_change_note": "大改款採 MQB 平台，全車系搭載「濕式」雙離合器變速箱，2021小改款導入 IQ.DRIVE 與觸控空調。",
                "platform": "VW MQB 模組化平台",
                "origin": "德國原裝進口",
                "photo_query": "Volkswagen Tiguan AD1",
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
        "summary": "3代(SH 2008-2012)採 4AT + 水平對臥；4代(SJ 2013-2017)換裝 CVT 並曾有早期閥體電磁閥通病；5代(SK 2018+)採 SGP 平台與 EyeSight。",
        "generations": [
            {
                "gen_id": "forester-3",
                "gen_name": "第 3 代 (SH 4AT世代)",
                "years": [2008, 2009, 2010, 2011, 2012],
                "is_major_change": True,
                "major_change_year": 2008,
                "major_change_note": "2008年大改款脫離旅行車外型正式成為正統 SUV，搭 4速手自排與 2.0 NA / 2.5 XT 渦輪。",
                "platform": "Subaru SI-Chassis",
                "origin": "日本原裝進口",
                "photo_query": "Subaru Forester SH",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "水平對臥汽缸床墊片滲油 + 老車油耗高，殘值 13~23 萬",
                    "reason": "無 CVT 疑慮但水平對臥拆裝工資較高，2.5 XT 渦輪版稅金與油耗亦高。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 X / 2.5 XT 渦輪 (4AT)",
                        "msrp_wan": 108.0,
                        "engine_code": "EJ20 2.0L / EJ255 2.5L 水平對臥",
                        "displacement_cc": 1994,
                        "horsepower": "150 ps (2.0) / 230 ps (2.5XT)",
                        "torque": "20.0 kgm / 32.6 kgm",
                        "transmission": "4速手自排",
                        "drivetrain": "SAWD 全時四驅",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "10.5 km/L",
                        "dimensions": "4560 x 1780 x 1700 mm (軸距 2615 mm)",
                        "safety": "6氣囊、VDC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "汽缸蓋/汽缸床墊片滲油 / 塑膠副水箱脆裂",
                        "severity": "中風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "引擎下方漏油滴到排氣管冒白煙、水溫高。",
                        "repair_cost_ntd": "墊片整理約 1.5 ~ 2.5 萬",
                        "advice": "頂車檢查引擎下半部油漬與水箱管路。"
                    }
                ],
                "yearly_prices": {
                    "2008": {"msrp": 102.0, "dealer": 14.5, "private": 11.2, "book": 8.5},
                    "2009": {"msrp": 102.0, "dealer": 16.5, "private": 13.0, "book": 10.0},
                    "2010": {"msrp": 105.0, "dealer": 18.5, "private": 14.8, "book": 11.8},
                    "2011": {"msrp": 108.0, "dealer": 21.0, "private": 17.0, "book": 13.8},
                    "2012": {"msrp": 108.0, "dealer": 23.5, "private": 19.5, "book": 16.0}
                }
            },
            {
                "gen_id": "forester-4",
                "gen_name": "第 4 代 (SJ 2.0i / 2.0XT)",
                "years": [2013, 2014, 2015, 2016, 2017],
                "is_major_change": True,
                "major_change_year": 2013,
                "major_change_note": "2013年大改款換裝 FB20/FA20 DIT 新世代引擎與 Lineartronic CVT。",
                "platform": "Subaru SI-Chassis",
                "origin": "日本原裝進口",
                "photo_query": "Subaru Forester SJ",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "早期 Lineartronic CVT 電磁閥故障與輪軸承異音",
                    "reason": "2.0XT 渦輪版動力強但零件保養費較高，導致中古折舊較 RAV4 快。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 i-L / 2.0 XT (240匹渦輪)",
                        "msrp_wan": 118.0,
                        "engine_code": "FB20 2.0L NA / FA20F 2.0L DIT 渦輪",
                        "displacement_cc": 1995,
                        "horsepower": "150 ps (NA) / 240 ps (XT)",
                        "torque": "20.2 kgm / 35.7 kgm",
                        "transmission": "Lineartronic CVT",
                        "drivetrain": "SAWD 全時四驅",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "fuel_economy": "12.5 km/L",
                        "dimensions": "4595 x 1795 x 1735 mm (軸距 2640 mm)",
                        "safety": "7氣囊、VDC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "CVT 閥體鎖止電磁閥故障 / 後輪軸承嗡嗡聲",
                        "severity": "中風險",
                        "mileage_range": "8萬 ~ 12萬公里",
                        "symptom": "儀表全亮（ABS/AT/引擎燈齊亮）、車速60以上後方嗡嗡聲。",
                        "repair_cost_ntd": "電磁閥約 1.5~2.5 萬；軸承約 4,500 元/輪",
                        "advice": "外廠皆可單換改良電磁閥，不需換整顆變速箱。"
                    }
                ],
                "yearly_prices": {
                    "2013": {"msrp": 115.0, "dealer": 27.0, "private": 22.5, "book": 19.0},
                    "2014": {"msrp": 115.0, "dealer": 30.5, "private": 25.8, "book": 22.0},
                    "2015": {"msrp": 118.0, "dealer": 34.5, "private": 29.5, "book": 25.5},
                    "2016": {"msrp": 118.0, "dealer": 38.5, "private": 33.5, "book": 29.0},
                    "2017": {"msrp": 118.0, "dealer": 43.0, "private": 37.8, "book": 33.0}
                }
            },
            {
                "gen_id": "forester-5",
                "gen_name": "第 5 代 (SK SGP平台)",
                "years": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2018,
                "major_change_note": "2018年大改款換裝 SGP 全球模組化底盤、2.0L 直噴自然進氣引擎與 EyeSight 雙鏡頭輔助系統。",
                "platform": "Subaru Global Platform (SGP)",
                "origin": "日本原裝進口",
                "photo_query": "Subaru Forester SK",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "安全配備滿載且中古價親民，留意 TVC 溫控閥",
                    "reason": "二手折舊較快，反而是高安全性的超值選擇。"
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
        "summary": "1代(2005)與 ix35(2010)早期品牌保值較低；3代 Tucson(2016)與 4代 Tucson L(2021年底+)質感與動力躍升，油電版採 6AT 尤受歡迎。",
        "generations": [
            {
                "gen_id": "tucson-3",
                "gen_name": "第 3 代 Tucson (2.0 汽油 / 1.6T 雙離合)",
                "years": [2016, 2017, 2018, 2019, 2020],
                "is_major_change": True,
                "major_change_year": 2016,
                "major_change_note": "2016年大改款恢復 Tucson 車名（取代 ix35），提供 2.0 NA 6AT 與 1.6T 7速雙離合。",
                "platform": "Hyundai 歐化底盤",
                "origin": "台灣國產（三陽南陽）",
                "photo_query": "Hyundai Tucson TL",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "品牌折舊較快，中古價極為便宜",
                    "reason": "1.6T 雙離合須注意低速頓挫，2.0 NA 6AT 動力較溫順但最耐操。"
                },
                "trims": [
                    {
                        "trim_name": "2.0 汽油 (6AT) / 1.6T 雙離合",
                        "msrp_wan": 95.9,
                        "engine_code": "Nu 2.0L NA / Gamma 1.6L 渦輪",
                        "displacement_cc": 1999,
                        "horsepower": "155 ps (2.0) / 177 ps (1.6T)",
                        "torque": "19.6 kgm / 26.8 kgm",
                        "transmission": "6速手自排 / 7速雙離合",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "12.8 km/L",
                        "dimensions": "4475 x 1850 x 1660 mm (軸距 2670 mm)",
                        "safety": "6氣囊、ESP"
                    }
                ],
                "common_issues": [
                    {
                        "part": "1.6T 7速雙離合抖動 / 方向機齒條異音",
                        "severity": "中風險",
                        "mileage_range": "6萬公里以上",
                        "symptom": "低速蠕行抖動、轉向輕微叩叩聲。",
                        "repair_cost_ntd": "離合器組約 3 萬",
                        "advice": "預算型買家選 2.0 6AT 最省心。"
                    }
                ],
                "yearly_prices": {
                    "2016": {"msrp": 89.9, "dealer": 29.0, "private": 24.5, "book": 21.0},
                    "2017": {"msrp": 93.9, "dealer": 33.5, "private": 28.8, "book": 25.0},
                    "2018": {"msrp": 95.9, "dealer": 38.0, "private": 33.0, "book": 29.0},
                    "2019": {"msrp": 95.9, "dealer": 43.0, "private": 37.8, "book": 33.5},
                    "2020": {"msrp": 95.9, "dealer": 48.0, "private": 42.5, "book": 38.0}
                }
            },
            {
                "gen_id": "tucson-4",
                "gen_name": "第 4 代 Tucson L (1.6T / 油電)",
                "years": [2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2021,
                "major_change_note": "2021年底大改款加長軸距至 2755mm（L版），1.6T 汽油採 7速雙離合、2023年新增 1.6T Turbo Hybrid 採 6速手自排。",
                "platform": "Hyundai N3 第三代平台",
                "origin": "台灣國產（三陽南陽）",
                "photo_query": "Hyundai Tucson NX4",
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
        "summary": "台灣豪華品牌最暢銷車款！1代(AZ10 2014-2021)的 NX200 以超低故障率與親民售價稱霸；2代(AZ20 2021年底+)換裝 TNGA-K 平台與 LSS+ 3.0。",
        "generations": [
            {
                "gen_id": "nx-1",
                "gen_name": "第 1 代 (AZ10 NX200 / NX300h)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
                "is_major_change": True,
                "major_change_year": 2015,
                "major_change_note": "2014年底上市；2017年底小改款推出高CP值的 NX200 (2.0 NA + CVT) 入門款銷量爆衝，2020年式升級全速域 LSS+ 2.0。",
                "platform": "Toyota New MC 豪華強化平台",
                "origin": "日本原裝進口",
                "photo_query": "Lexus NX AZ10",
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
                    "2015": {"msrp": 189.0, "dealer": 62.0, "private": 55.5, "book": 50.0},
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
                "major_change_year": 2022,
                "major_change_note": "2021年底大改款2代！改採 TNGA-K 平台、電子門把、大螢幕與 LSS+ 3.0，NX200 換裝 173匹 M20A 引擎。",
                "platform": "Toyota TNGA GA-K",
                "origin": "日本原裝進口",
                "photo_query": "Lexus NX AZ20",
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
        "model_zh": "賓士 C-Class (C200 / C300)",
        "category": "豪華進口中型房車",
        "summary": "2000年起 W203、W204 到 W205 皆為台灣最熱門雙B入門房車。早期 W203/W204 受 M271 引擎正時鍊條與環保線組影響殘值掉很快；W205 含大量美規 C300 外匯車。",
        "generations": [
            {
                "gen_id": "c-w203",
                "gen_name": "W203 世代 (C200K / C230K)",
                "years": [2000, 2001, 2002, 2003, 2004, 2005, 2006],
                "is_major_change": True,
                "major_change_year": 2000,
                "major_change_note": "2000年大改款花生燈造型，台灣主力為 1.8 機械增壓 C200K / C230K 搭 5速手自排。",
                "platform": "Mercedes W203 後驅平台",
                "origin": "德國原裝進口",
                "photo_query": "Mercedes-Benz W203 sedan",
                "depreciation_alert": {
                    "level": "high",
                    "title": "M271 引擎正時鍊條跳齒 + 凸輪軸漏油吃線組，殘值剩 9~16 萬",
                    "reason": "早期 1.8 機械增壓凸輪軸電磁閥漏油會順著毛細現象滲進 ECU 電腦，維修費動輒數萬，使車價大跌。"
                },
                "trims": [
                    {
                        "trim_name": "C200 Kompressor (1.8機械增壓 5AT)",
                        "msrp_wan": 198.0,
                        "engine_code": "M271 1.8L 直列四缸機械增壓",
                        "displacement_cc": 1796,
                        "horsepower": "163 ps / 5,500 rpm",
                        "torque": "24.5 kgm / 3,000 rpm",
                        "transmission": "5G-TRONIC 5速手自排",
                        "drivetrain": "後輪驅動 (FR)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "11.0 km/L",
                        "dimensions": "4526 x 1728 x 1426 mm (軸距 2715 mm)",
                        "safety": "6氣囊、ESP"
                    }
                ],
                "common_issues": [
                    {
                        "part": "M271 凸輪軸調整器漏油吃線組 / 正時鍊條拉長",
                        "severity": "高風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "冷車啟動喀啦異音、ECU 線組含油亮故障燈。",
                        "repair_cost_ntd": "正時鍊條+齒輪約 3.5~5.0 萬",
                        "advice": "買 W203 必裝阻油線並檢查正時鍊條。"
                    }
                ],
                "yearly_prices": {
                    "2001": {"msrp": 195.0, "dealer": 11.0, "private": 8.0, "book": 5.5},
                    "2002": {"msrp": 195.0, "dealer": 12.0, "private": 8.8, "book": 6.2},
                    "2003": {"msrp": 198.0, "dealer": 13.0, "private": 9.8, "book": 7.0},
                    "2004": {"msrp": 198.0, "dealer": 14.2, "private": 10.8, "book": 8.0},
                    "2005": {"msrp": 202.0, "dealer": 15.8, "private": 12.2, "book": 9.2},
                    "2006": {"msrp": 202.0, "dealer": 17.5, "private": 13.8, "book": 10.5}
                }
            },
            {
                "gen_id": "c-w204",
                "gen_name": "W204 世代 (C200 / C250 / C300)",
                "years": [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
                "is_major_change": True,
                "major_change_year": 2007,
                "major_change_note": "2007年大改款方正霸氣造型，2011小改款導入 7G-TRONIC 7AT 與大量美規 C250 1.8T 外匯車。",
                "platform": "Mercedes W204 後驅平台",
                "origin": "德國/南非進口（含大量美規外匯）",
                "photo_query": "Mercedes-Benz W204 sedan",
                "depreciation_alert": {
                    "level": "high",
                    "title": "M271 CGI 凸輪軸齒輪磨損 + ESL 方向盤鎖死經典通病",
                    "reason": "1.8T 凸輪軸齒輪磨損與插鑰匙方向盤鎖死模組(ESL)損壞是 W204 最出名高價通病。"
                },
                "trims": [
                    {
                        "trim_name": "C200 / C250 CGI (1.8T 7AT)",
                        "msrp_wan": 215.0,
                        "engine_code": "M271 EVO 1.8L 缸內直噴渦輪",
                        "displacement_cc": 1796,
                        "horsepower": "184 ps (C200) / 204 ps (C250)",
                        "torque": "27.5 kgm / 31.6 kgm",
                        "transmission": "5AT (前期) / 7G-TRONIC (2011+)",
                        "drivetrain": "後輪驅動 (FR)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "13.0 km/L",
                        "dimensions": "4591 x 1770 x 1447 mm (軸距 2760 mm)",
                        "safety": "7氣囊、ESP"
                    }
                ],
                "common_issues": [
                    {
                        "part": "M271 凸輪軸齒輪磨損 / ESL電子方向盤鎖死",
                        "severity": "高風險",
                        "mileage_range": "8萬 ~ 14萬公里",
                        "symptom": "插鑰匙完全無法過電發動（ESL故障）；冷車發動瞬間噠噠異音。",
                        "repair_cost_ntd": "ESL模擬器約 8,000~15,000 元；凸輪軸齒輪組約 3.5~5.5 萬",
                        "advice": "買 2011-2014 後期款 C250 須特別聆聽冷車發動瞬間異音。"
                    }
                ],
                "yearly_prices": {
                    "2007": {"msrp": 205.0, "dealer": 22.0, "private": 17.5, "book": 14.0},
                    "2008": {"msrp": 205.0, "dealer": 24.5, "private": 19.8, "book": 16.0},
                    "2009": {"msrp": 209.0, "dealer": 27.5, "private": 22.5, "book": 18.5},
                    "2010": {"msrp": 209.0, "dealer": 30.5, "private": 25.0, "book": 21.0},
                    "2011": {"msrp": 215.0, "dealer": 35.5, "private": 29.5, "book": 25.0},
                    "2012": {"msrp": 215.0, "dealer": 39.5, "private": 33.0, "book": 28.5},
                    "2013": {"msrp": 218.0, "dealer": 44.0, "private": 37.5, "book": 32.5},
                    "2014": {"msrp": 218.0, "dealer": 49.0, "private": 42.0, "book": 37.0}
                }
            },
            {
                "gen_id": "c-w205",
                "gen_name": "W205 世代 (C200 / 外匯 C300)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020],
                "is_major_change": True,
                "major_change_year": 2015,
                "major_change_note": "大改款 W205，2018年底小改款換裝 1.5T+48V (C200) 與改良 M264 2.0T (C300) + 9G-TRONIC 變速箱。",
                "platform": "Mercedes MRA 後驅平台",
                "origin": "德國/南非/美國進口（含大量美規外匯）",
                "photo_query": "Mercedes-Benz W205 sedan",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "外匯車源極多、車價落差大，須嚴防事故/調錶外匯車",
                    "reason": "過保後折舊明顯；2019小改款 48V BSG 啟動馬達故障率亦須留意。"
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
                        "symptom": "亮 48V 電池故障無法發動；冷車引擎室汽油味。",
                        "repair_cost_ntd": "48V BSG 維修約 3.5 ~ 6.5 萬",
                        "advice": "外匯車務必查閱 Carfax 報告並檢驗萊茵認證。"
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
        "model_zh": "寶馬 3系列 (318i / 320i / 330i)",
        "category": "豪華進口中型運動房車",
        "summary": "E46(2000-2005)與 E90(2005-2011)因 N42/N46 四缸漏油與氣門油封吃機油通病使殘值跌破20萬；F30(2012-2018)後期換 B48 與 G20(2019+)後妥善率大幅躍升。",
        "generations": [
            {
                "gen_id": "bmw-e46",
                "gen_name": "E46 世代 (經典後驅老寶馬)",
                "years": [2000, 2001, 2002, 2003, 2004],
                "is_major_change": True,
                "major_change_year": 2000,
                "major_change_note": "經典 E46 世代，前期 318i/320i(M52/M54 六缸)較耐操，後期 318i 換裝 N42 四缸容易吃機油漏油。",
                "platform": "BMW E46 後驅平台",
                "origin": "德國原裝進口",
                "photo_query": "BMW E46 sedan",
                "depreciation_alert": {
                    "level": "high",
                    "title": "冷卻副水箱爆裂 + 漏油通病，老車殘值 9~15 萬",
                    "reason": "20年以上雙B冷卻塑膠管路脆化極易水溫過高沖墊片，僅 6 缸 M54 車型具玩家收藏價。"
                },
                "trims": [
                    {
                        "trim_name": "318i / 320i (5AT)",
                        "msrp_wan": 188.0,
                        "engine_code": "N42B20 四缸 / M54B22 直列六缸",
                        "displacement_cc": 1995,
                        "horsepower": "143 ps (318i) / 170 ps (320i)",
                        "torque": "20.4 kgm / 21.4 kgm",
                        "transmission": "5速手自排",
                        "drivetrain": "後輪驅動 (FR)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "10.5 km/L",
                        "dimensions": "4471 x 1739 x 1415 mm (軸距 2725 mm)",
                        "safety": "6氣囊、DSC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "塑膠副水箱爆裂 / 引擎墊片漏油 / 氣門油封老化",
                        "severity": "高風險",
                        "mileage_range": "12萬公里以上",
                        "symptom": "突然爆水管水溫紅燈、怠速踩油門冒藍煙。",
                        "repair_cost_ntd": "水路全套+油封整理約 2.5~4.0 萬",
                        "advice": "喜愛 E46 建議找直列六缸 320i/325i/330i。"
                    }
                ],
                "yearly_prices": {
                    "2000": {"msrp": 182.0, "dealer": 10.0, "private": 7.0, "book": 4.5},
                    "2001": {"msrp": 182.0, "dealer": 11.0, "private": 7.8, "book": 5.2},
                    "2002": {"msrp": 188.0, "dealer": 12.0, "private": 8.8, "book": 6.0},
                    "2003": {"msrp": 188.0, "dealer": 13.5, "private": 9.8, "book": 6.8},
                    "2004": {"msrp": 188.0, "dealer": 15.0, "private": 11.0, "book": 8.0}
                }
            },
            {
                "gen_id": "bmw-e90",
                "gen_name": "E90 世代 (N46 漏油王時期)",
                "years": [2005, 2006, 2007, 2008, 2009, 2010, 2011],
                "is_major_change": True,
                "major_change_year": 2005,
                "major_change_note": "2005年大改款 E90，全面採失壓續跑胎與 6速手自排，但 318i/320i 搭載惡名昭彰的 N46 四缸引擎。",
                "platform": "BMW E90 後驅平台",
                "origin": "德國原裝進口",
                "photo_query": "BMW E90 sedan",
                "depreciation_alert": {
                    "level": "high",
                    "title": "N46 四缸「氣門油封吃機油 + 全車漏油」導致殘值崩跌",
                    "reason": "E90 320i 幾乎每台必遇汽門油封硬化冒藍煙、真空泵漏油與變速箱油底殼滲油，造成市場價格僅剩 18~32 萬。"
                },
                "trims": [
                    {
                        "trim_name": "320i (N46四缸) / 323i・325i (N52六缸)",
                        "msrp_wan": 199.0,
                        "engine_code": "N46B20 2.0L 四缸 / N52B25 2.5L 六缸",
                        "displacement_cc": 1995,
                        "horsepower": "150~156 ps (320i) / 218 ps (325i)",
                        "torque": "20.4 kgm / 25.5 kgm",
                        "transmission": "ZF 6速手自排",
                        "drivetrain": "後輪驅動 (FR)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "11.5 km/L",
                        "dimensions": "4520 x 1817 x 1421 mm (軸距 2760 mm)",
                        "safety": "6氣囊、DSC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "N46 汽門油封硬化冒藍煙 / 引擎墊片漏油",
                        "severity": "高風險",
                        "mileage_range": "8萬公里以上",
                        "symptom": "停紅燈後大腳油門排氣管噴藍煙、引擎室燒機油臭味。",
                        "repair_cost_ntd": "免拆缸頭換氣門油封+墊片約 2.5~3.5 萬",
                        "advice": "買 E90 強烈建議挑 N52 直列六缸 (323i/325i)，體質遠勝 N46 四缸。"
                    }
                ],
                "yearly_prices": {
                    "2005": {"msrp": 192.0, "dealer": 18.0, "private": 14.0, "book": 11.0},
                    "2006": {"msrp": 192.0, "dealer": 19.8, "private": 15.5, "book": 12.2},
                    "2007": {"msrp": 195.0, "dealer": 21.8, "private": 17.2, "book": 13.8},
                    "2008": {"msrp": 195.0, "dealer": 24.0, "private": 19.2, "book": 15.5},
                    "2009": {"msrp": 199.0, "dealer": 27.0, "private": 21.8, "book": 18.0},
                    "2010": {"msrp": 199.0, "dealer": 30.0, "private": 24.5, "book": 20.5},
                    "2011": {"msrp": 199.0, "dealer": 33.5, "private": 27.5, "book": 23.0}
                }
            },
            {
                "gen_id": "bmw-f30",
                "gen_name": "F30 世代 (N20前期 / B48後期)",
                "years": [2012, 2013, 2014, 2015, 2016, 2017, 2018],
                "is_major_change": True,
                "major_change_year": 2012,
                "major_change_note": "2012年大改款 F30 全面渦輪化 + ZF 8AT；前期(2012-2015)採 N20 引擎，2016小改款後換裝極穩定的 B48 引擎。",
                "platform": "BMW F30 後驅平台",
                "origin": "德國原裝進口",
                "photo_query": "BMW F30 sedan",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "前期 N20 正時鍊條導板脆裂風險；2016+ B48 引擎大幅改善",
                    "reason": "2012-2015 N20 引擎塑膠鍊條導板高里程可能碎裂阻塞機油泵，2016年後 B48 中古價明顯較高。"
                },
                "trims": [
                    {
                        "trim_name": "320i / 328i / 330i (ZF 8AT)",
                        "msrp_wan": 203.0,
                        "engine_code": "N20B20 (12-15) / B48B20 (16-18)",
                        "displacement_cc": 1998,
                        "horsepower": "184 ps (320i) / 245~252 ps (328i/330i)",
                        "torque": "27.5 kgm / 35.7 kgm",
                        "transmission": "ZF Steptronic 8速手自排",
                        "drivetrain": "後輪驅動 (FR)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "14.5 km/L",
                        "dimensions": "4624 x 1811 x 1429 mm (軸距 2810 mm)",
                        "safety": "6氣囊、DSC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "N20 正時鍊條導板脆裂 (2012-2015) / 渦輪回油管",
                        "severity": "高風險",
                        "mileage_range": "8萬 ~ 12萬公里",
                        "symptom": "高轉異音、機油壓力過低警示。",
                        "repair_cost_ntd": "預防更換鍊條與導板組約 3.5~4.5 萬",
                        "advice": "預算夠直接鎖定 2016 年後 LCI 小改款 B48 引擎（320i/330i）。"
                    }
                ],
                "yearly_prices": {
                    "2012": {"msrp": 192.0, "dealer": 42.0, "private": 35.5, "book": 30.5},
                    "2013": {"msrp": 192.0, "dealer": 46.5, "private": 39.5, "book": 34.5},
                    "2014": {"msrp": 195.0, "dealer": 51.5, "private": 44.0, "book": 38.5},
                    "2015": {"msrp": 195.0, "dealer": 57.0, "private": 49.0, "book": 43.0},
                    "2016": {"msrp": 203.0, "dealer": 66.0, "private": 58.0, "book": 51.5},
                    "2017": {"msrp": 203.0, "dealer": 73.0, "private": 64.5, "book": 57.5},
                    "2018": {"msrp": 203.0, "dealer": 81.0, "private": 72.0, "book": 64.5}
                }
            },
            {
                "gen_id": "bmw-g20",
                "gen_name": "G20 世代 (B48 + ZF 8AT)",
                "years": [2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2019,
                "major_change_note": "2019年大改款 G20，換裝 CLAR 高剛性平台與極成熟的 B48 2.0T 引擎 + ZF 8速手自排，全面標配 5AU 智慧駕駛。",
                "platform": "BMW CLAR 後驅平台",
                "origin": "德國原裝進口",
                "photo_query": "BMW G20 sedan",
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
        "category": "國產/進口都會小車",
        "summary": "2代(ZC11S 2005-2010)由太子汽車國產曾爆紅，但後期因太子倒閉停產影響零件供應與殘值；3代(ZC72S 2011-2017)金鈴恢復日本進口；4代(2018+)採輕量化與輕油電，中古極為搶手。",
        "generations": [
            {
                "gen_id": "swift-2",
                "gen_name": "第 2 代 (ZC11S/ZC21S 太子國產時期)",
                "years": [2005, 2006, 2007, 2008, 2009, 2010],
                "is_major_change": True,
                "major_change_year": 2005,
                "major_change_note": "2005年太子汽車首度國產化大改款 Swift，採 1.5L M15A + 4AT 搭配歐風可愛造型，當年熱銷但 2011 年太子停產後原廠零件待料較久。",
                "platform": "Suzuki ZC 全球戰略小車平台",
                "origin": "台灣國產（太子汽車）",
                "photo_query": "Suzuki Swift ZC11S",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "太子汽車停產 + 4AT 散熱/水箱老化，二手價 8~14 萬",
                    "reason": "雖外型經典好開，但車齡 16 年以上且太子汽車停產後部分國產專用內裝料件較難尋，加上僅2氣囊無ESP。"
                },
                "trims": [
                    {
                        "trim_name": "1.5 GL / GLX (4AT)",
                        "msrp_wan": 52.8,
                        "engine_code": "M15A 1.5L DOHC VVT 自然進氣",
                        "displacement_cc": 1490,
                        "horsepower": "110 ps / 6,000 rpm",
                        "torque": "14.6 kgm / 4,000 rpm",
                        "transmission": "4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "15.2 km/L",
                        "dimensions": "3695 x 1690 x 1510 mm (軸距 2390 mm)",
                        "safety": "2氣囊、ABS（無ESP）"
                    }
                ],
                "common_issues": [
                    {
                        "part": "水箱散熱不良 / 冷氣壓縮機 / 變速箱油管老化",
                        "severity": "中風險",
                        "mileage_range": "10萬公里以上",
                        "symptom": "怠速開冷氣水溫偏高、4AT 換檔微頓挫、三角架鐵套龜裂。",
                        "repair_cost_ntd": "換鋁水箱約 5,000 元；壓縮機整理約 7,000 元",
                        "advice": "M15A 引擎本體耐操，購買時特別檢查冷卻水箱與底盤異音。"
                    }
                ],
                "yearly_prices": {
                    "2005": {"msrp": 49.8, "dealer": 9.5, "private": 6.8, "book": 4.5},
                    "2006": {"msrp": 51.8, "dealer": 10.5, "private": 7.5, "book": 5.2},
                    "2007": {"msrp": 51.8, "dealer": 11.8, "private": 8.5, "book": 6.0},
                    "2008": {"msrp": 52.8, "dealer": 13.0, "private": 9.5, "book": 7.0},
                    "2009": {"msrp": 52.8, "dealer": 14.5, "private": 10.8, "book": 8.0},
                    "2010": {"msrp": 53.8, "dealer": 16.0, "private": 12.2, "book": 9.2}
                }
            },
            {
                "gen_id": "swift-3",
                "gen_name": "第 3 代 (ZC72S 恢復日本進口)",
                "years": [2011, 2012, 2013, 2014, 2015, 2016, 2017],
                "is_major_change": True,
                "major_change_year": 2011,
                "major_change_note": "2011年金鈴汽車改為日本原裝進口導入 3代(1.4L 4AT)，2013年底小改款改為 1.2L K12B + CVT。",
                "platform": "Suzuki ZC72S 平台",
                "origin": "日本原裝進口",
                "photo_query": "Suzuki Swift ZC72S",
                "depreciation_alert": {
                    "level": "low",
                    "title": "日本進口品質穩定，1.4 4AT 與 1.2 CVT 皆極省油",
                    "reason": "缺點為當時全車系僅 2 氣囊且無 ESP（僅 Sport 手排版例外），壓抑了部分安全取向買家出價。"
                },
                "trims": [
                    {
                        "trim_name": "1.4 GLX (11-13) / 1.2 GLX (14-17)",
                        "msrp_wan": 62.8,
                        "engine_code": "K14B 1.4L / K12B 1.2L 自然進氣",
                        "displacement_cc": 1242,
                        "horsepower": "95 ps (1.4) / 94 ps (1.2)",
                        "torque": "13.3 kgm / 12.0 kgm",
                        "transmission": "4AT (11-13) / CVT (14-17)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "16.5 km/L",
                        "dimensions": "3850 x 1695 x 1510 mm (軸距 2430 mm)",
                        "safety": "2氣囊、ABS（無ESP）"
                    },
                    {
                        "trim_name": "Swift Sport 1.6L (ZC32S 性能版)",
                        "msrp_wan": 79.8,
                        "engine_code": "M16A 1.6L 高轉自然進氣",
                        "displacement_cc": 1586,
                        "horsepower": "136 ps / 6,900 rpm",
                        "torque": "16.3 kgm / 4,400 rpm",
                        "transmission": "6速手排 / 運動化 CVT (附換檔撥片)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "Monroe 運動化懸吊 / 前麥花臣 後扭力樑",
                        "fuel_economy": "15.1 km/L",
                        "dimensions": "3890 x 1695 x 1510 mm (軸距 2430 mm)",
                        "safety": "6氣囊、ESP 車身動態穩定、HID 頭燈"
                    }
                ],
                "common_issues": [
                    {
                        "part": "前避震器上座異音 / 隔音偏單薄",
                        "severity": "一般耗材",
                        "mileage_range": "8萬公里以上",
                        "symptom": "過坑洞前方叩叩聲、高速風切聲。",
                        "repair_cost_ntd": "上座李仔串整理約 4,000 ~ 6,000 元",
                        "advice": "機械耐用度極佳，適合都會代步。"
                    }
                ],
                "yearly_prices": {
                    "2011": {"msrp": 59.8, "dealer": 19.0, "private": 15.5, "book": 12.8},
                    "2012": {"msrp": 59.8, "dealer": 21.0, "private": 17.2, "book": 14.5},
                    "2013": {"msrp": 62.8, "dealer": 23.5, "private": 19.5, "book": 16.5},
                    "2014": {"msrp": 62.8, "dealer": 25.8, "private": 21.5, "book": 18.5},
                    "2015": {"msrp": 62.8, "dealer": 28.0, "private": 23.8, "book": 20.5},
                    "2016": {"msrp": 62.8, "dealer": 30.5, "private": 26.0, "book": 22.8},
                    "2017": {"msrp": 62.8, "dealer": 33.0, "private": 28.5, "book": 25.0}
                }
            },
            {
                "gen_id": "swift-4",
                "gen_name": "第 4 代 (ZC83S/A2L 輕油電)",
                "years": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2018,
                "major_change_note": "2017年底大改款採 HEARTECT 輕量化底盤並標配 6氣囊+ESP，前期為 1.0T 渦輪+6AT，2021年改為 1.2L 輕油電+CVT並標配 ACC。",
                "platform": "Suzuki HEARTECT 平台",
                "origin": "日本原裝進口",
                "photo_query": "Suzuki Swift ZC83S",
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
                    },
                    {
                        "trim_name": "1.0T GLX Boosterjet 渦輪 (2018-2020)",
                        "msrp_wan": 66.9,
                        "engine_code": "K10C 1.0L 三缸缸內直噴渦輪",
                        "displacement_cc": 998,
                        "horsepower": "111 ps / 5,500 rpm",
                        "torque": "16.3 kgm / 1,500-4,000 rpm",
                        "transmission": "6速手自排 (非CVT)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "19.2 km/L",
                        "dimensions": "3840 x 1735 x 1480 mm (軸距 2450 mm)",
                        "safety": "6氣囊、ESP（無ACC）"
                    },
                    {
                        "trim_name": "Swift Sport 1.4T (ZC33S 性能鋼砲版)",
                        "msrp_wan": 82.0,
                        "engine_code": "K14C/K14D 1.4L Boosterjet 渦輪 (+48V輕油電)",
                        "displacement_cc": 1373,
                        "horsepower": "140 ps (前期6AT) / 129.2 ps + 電推 (後期6MT)",
                        "torque": "23.5 kgm / 2,500-3,500 rpm",
                        "transmission": "6速手自排 (18-20) / 6速純手排 (20+)",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "Monroe 專屬運動化懸吊 / 專屬寬體空力套件",
                        "fuel_economy": "16.6 ~ 19.5 km/L",
                        "dimensions": "3890 x 1735 x 1480 mm (軸距 2450 mm)",
                        "safety": "6氣囊、ACC、BSM 盲點、雙出排氣尾管"
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
    },
    {
        "id": "mazda-2",
        "brand": "Mazda",
        "model": "Mazda2",
        "model_zh": "馬自達 Mazda2",
        "category": "進口都會小車",
        "summary": "2代(DE 2008-2014)以日製進口與靈活操控打入台灣市場；3代(DJ 2015+)換上魂動外型與 Skyactiv 1.5L+6AT，省油耐用且妥善率高。",
        "generations": [
            {
                "gen_id": "mazda2-de",
                "gen_name": "第 2 代 (DE 日本進口 4AT)",
                "years": [2008, 2009, 2010, 2011, 2012, 2013, 2014],
                "is_major_change": True,
                "major_change_year": 2008,
                "major_change_note": "2008年日本原裝進口導入，採 1.5L MZR + 4AT 變速箱，底盤輕巧好開，但僅 2 氣囊且無 ESP。",
                "platform": "Mazda DE / Ford Fiesta 同源平台",
                "origin": "日本原裝進口",
                "photo_query": "Mazda2 DE",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "安全配備陽春 (2氣囊無ESP)，但機械極耐操",
                    "reason": "1.5L 自然進氣與 4AT 結構簡單，二手價 11~19 萬，適合作為低預算市區代步車。"
                },
                "trims": [
                    {
                        "trim_name": "1.5L 尊貴 / 頂級 (4AT)",
                        "msrp_wan": 65.5,
                        "engine_code": "ZY-VE 1.5L 自然進氣",
                        "displacement_cc": 1498,
                        "horsepower": "103 ps / 6,000 rpm",
                        "torque": "13.8 kgm / 4,000 rpm",
                        "transmission": "4速自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "15.2 km/L",
                        "dimensions": "3885 x 1695 x 1475 mm (軸距 2490 mm)",
                        "safety": "2氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "後視鏡收折馬達齒輪崩牙 / 避震器上座異音",
                        "severity": "一般耗材",
                        "mileage_range": "8萬公里以上",
                        "symptom": "電動收折空轉不停、過坑洞前輪異音。",
                        "repair_cost_ntd": "金屬齒輪更換約 1,500 元/側",
                        "advice": "通病皆屬小額耗材，引擎變速箱極為穩定。"
                    }
                ],
                "yearly_prices": {
                    "2008": {"msrp": 59.5, "dealer": 11.0, "private": 8.2, "book": 6.0},
                    "2009": {"msrp": 61.5, "dealer": 12.2, "private": 9.2, "book": 7.0},
                    "2010": {"msrp": 63.5, "dealer": 13.5, "private": 10.5, "book": 8.0},
                    "2011": {"msrp": 64.5, "dealer": 15.0, "private": 11.8, "book": 9.2},
                    "2012": {"msrp": 65.5, "dealer": 16.5, "private": 13.0, "book": 10.5},
                    "2013": {"msrp": 65.5, "dealer": 18.0, "private": 14.5, "book": 11.8},
                    "2014": {"msrp": 65.5, "dealer": 19.8, "private": 16.0, "book": 13.2}
                }
            },
            {
                "gen_id": "mazda2-dj",
                "gen_name": "第 3 代 (DJ 魂動 Skyactiv)",
                "years": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
                "is_major_change": True,
                "major_change_year": 2015,
                "major_change_note": "2015年大改款換裝 Skyactiv-G 1.5L + 6速手自排，質感大幅提升並標配 6氣囊+DSC，2020+ 再加入 GVC Plus。",
                "platform": "Mazda Skyactiv-Chassis 小型平台",
                "origin": "泰國 / 日本進口",
                "photo_query": "Mazda2 DJ",
                "depreciation_alert": {
                    "level": "low",
                    "title": "6AT 穩健耐用 + 1.5L 省稅省油",
                    "reason": "市場能見度雖不如 Yaris/Swift，但無 CVT 壽命疑慮，內裝質感同級領先。"
                },
                "trims": [
                    {
                        "trim_name": "1.5L Skyactiv-G 尊榮 / 旗艦",
                        "msrp_wan": 74.9,
                        "engine_code": "P5-VPS 1.5L Skyactiv-G 自然進氣",
                        "displacement_cc": 1496,
                        "horsepower": "107~116 ps / 6,000 rpm",
                        "torque": "14.2~15.1 kgm / 4,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "17.4 ~ 17.9 km/L",
                        "dimensions": "4060 x 1695 x 1495 mm (軸距 2570 mm)",
                        "safety": "6氣囊、DSC、BSM盲點(後期)"
                    }
                ],
                "common_issues": [
                    {
                        "part": "後座空間偏窄 / 後視鏡收折馬達",
                        "severity": "一般耗材",
                        "mileage_range": "6萬公里以上",
                        "symptom": "後視鏡收折卡頓、MZD 主機觸控排線偶發漂移。",
                        "repair_cost_ntd": "收折馬達約 2,000 元",
                        "advice": "建議 2 人使用為主，4 人家庭建議看 Mazda3。"
                    }
                ],
                "yearly_prices": {
                    "2015": {"msrp": 69.9, "dealer": 24.5, "private": 20.5, "book": 17.5},
                    "2016": {"msrp": 69.9, "dealer": 27.0, "private": 22.8, "book": 19.8},
                    "2017": {"msrp": 74.9, "dealer": 30.0, "private": 25.5, "book": 22.2},
                    "2018": {"msrp": 74.9, "dealer": 33.0, "private": 28.5, "book": 25.0},
                    "2019": {"msrp": 74.9, "dealer": 36.5, "private": 31.8, "book": 28.0},
                    "2020": {"msrp": 74.9, "dealer": 41.0, "private": 36.0, "book": 32.0},
                    "2021": {"msrp": 74.9, "dealer": 45.0, "private": 40.0, "book": 35.8},
                    "2022": {"msrp": 74.9, "dealer": 49.5, "private": 44.5, "book": 40.0},
                    "2023": {"msrp": 78.9, "dealer": 55.0, "private": 49.5, "book": 44.5},
                    "2024": {"msrp": 78.9, "dealer": 60.5, "private": 55.0, "book": 49.5}
                }
            }
        ]
    },
    {
        "id": "mazda-5",
        "brand": "Mazda",
        "model": "Mazda5",
        "model_zh": "馬自達 Mazda5",
        "category": "國產側滑門休旅 (MPV)",
        "summary": "台灣家庭神車代表之一！雙側電動滑門搭配 5+2 座空間，1代(2005-2011)與 2代(2012-2016)皆採 2.0L 自然進氣，因實用性極高至今中古車市場依然搶手。",
        "generations": [
            {
                "gen_id": "mazda5-1",
                "gen_name": "第 1 代 (CR 國產經典滑門)",
                "years": [2005, 2006, 2007, 2008, 2009, 2010, 2011],
                "is_major_change": True,
                "major_change_year": 2005,
                "major_change_note": "2005年福特六和國產上市，導入雙側滑門與 6+1 座椅變化，2008年小改款升級 5AT。",
                "platform": "Mazda CR / C1 平台",
                "origin": "台灣國產",
                "photo_query": "Mazda5 CR",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "車齡高、底盤耗材老化，但滑門剛性需求撐住殘值",
                    "reason": "15年以上老車需預留冷氣與底盤橡膠整理預算，購買時確認側滑門馬達順暢。"
                },
                "trims": [
                    {
                        "trim_name": "2.0L 尊貴 / 頂級 (4AT / 5AT)",
                        "msrp_wan": 79.9,
                        "engine_code": "LF 2.0L DOHC 自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "148 ps / 6,000 rpm",
                        "torque": "19.2 kgm / 4,500 rpm",
                        "transmission": "4速/5速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後多連桿",
                        "fuel_economy": "11.5 km/L",
                        "dimensions": "4505 x 1755 x 1665 mm (軸距 2750 mm)",
                        "safety": "2氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "電動滑門鋼索/馬達老化 & 變速箱電磁閥",
                        "severity": "中風險",
                        "mileage_range": "12萬公里以上",
                        "symptom": "滑門開關卡頓、冷車換檔頓挫、前輪胎內側吃胎。",
                        "repair_cost_ntd": "單側滑門整理約 6,000 元；後仰角調整器約 4,500 元",
                        "advice": "優先找 2008 年小改款 5AT 車型，油耗與順暢度較佳。"
                    }
                ],
                "yearly_prices": {
                    "2006": {"msrp": 76.9, "dealer": 9.8, "private": 7.0, "book": 4.8},
                    "2007": {"msrp": 76.9, "dealer": 10.8, "private": 7.8, "book": 5.5},
                    "2008": {"msrp": 79.9, "dealer": 12.5, "private": 9.2, "book": 6.8},
                    "2009": {"msrp": 79.9, "dealer": 14.0, "private": 10.5, "book": 8.0},
                    "2010": {"msrp": 80.9, "dealer": 15.8, "private": 12.0, "book": 9.2},
                    "2011": {"msrp": 81.9, "dealer": 17.5, "private": 13.8, "book": 10.8}
                }
            },
            {
                "gen_id": "mazda5-2",
                "gen_name": "第 2 代 (CW 微笑末代滑門)",
                "years": [2012, 2013, 2014, 2015, 2016],
                "is_major_change": True,
                "major_change_year": 2012,
                "major_change_note": "2012年大改款導入微笑水箱護罩，後期旗艦補齊 6 氣囊與 DSC，2016年停產後無後繼車。",
                "platform": "Mazda CW 平台",
                "origin": "台灣國產",
                "photo_query": "Mazda5 CW",
                "depreciation_alert": {
                    "level": "low",
                    "title": "停產絕版國產滑門 MPV，保值度極強",
                    "reason": "百萬內唯一雙側滑門 7 人座，至今仍是二胎家庭熱門首選，後期 6 氣囊版最搶手。"
                },
                "trims": [
                    {
                        "trim_name": "2.0L 旗艦型 (5AT / 6氣囊)",
                        "msrp_wan": 88.9,
                        "engine_code": "LF-VDS 2.0L 自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "147 ps / 6,000 rpm",
                        "torque": "18.8 kgm / 4,500 rpm",
                        "transmission": "5速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "12.2 km/L",
                        "dimensions": "4585 x 1750 x 1615 mm (軸距 2750 mm)",
                        "safety": "前期2氣囊 / 後期旗艦6氣囊+DSC"
                    }
                ],
                "common_issues": [
                    {
                        "part": "後輪吃胎 / 水箱節溫器老化",
                        "severity": "一般耗材",
                        "mileage_range": "10萬公里以上",
                        "symptom": "後輪滾動噪音大、水溫爬升慢。",
                        "repair_cost_ntd": "後束角拉桿定位整理約 5,000 元",
                        "advice": "建議挑選 2014-2016 年旗艦版（具 6 氣囊與 DSC）。"
                    }
                ],
                "yearly_prices": {
                    "2012": {"msrp": 85.9, "dealer": 21.5, "private": 17.5, "book": 14.5},
                    "2013": {"msrp": 86.9, "dealer": 24.0, "private": 19.8, "book": 16.5},
                    "2014": {"msrp": 88.9, "dealer": 27.0, "private": 22.5, "book": 19.0},
                    "2015": {"msrp": 88.9, "dealer": 30.5, "private": 25.8, "book": 22.0},
                    "2016": {"msrp": 89.9, "dealer": 34.5, "private": 29.5, "book": 25.5}
                }
            }
        ]
    },
    {
        "id": "mazda-6",
        "brand": "Mazda",
        "model": "Mazda6",
        "model_zh": "馬自達 Mazda6",
        "category": "中大型房車 / 旅行車",
        "summary": "1代(GG 2002-2007)奠定日式跑房車口碑；3代(GJ/GL 2013+)導入魂動美學與 Wagon 旅行車極受青睞，但 3代前期 2.2D 柴油版與 CX-5 同樣有沖墊片災情。",
        "generations": [
            {
                "gen_id": "mazda6-gg",
                "gen_name": "第 1 代 (GG 經典日式跑房車)",
                "years": [2003, 2004, 2005, 2006, 2007],
                "is_major_change": True,
                "major_change_year": 2003,
                "major_change_note": "2003年上市主打 Zoom-Zoom 操控，提供 2.0 / 2.3S 運動版。",
                "platform": "Mazda GG 平台",
                "origin": "日本進口 / 國產",
                "photo_query": "Mazda6 GG",
                "depreciation_alert": {
                    "level": "medium",
                    "title": "車齡逾 19 年，2.3S 版需留意吃機油",
                    "reason": "二手殘值僅剩代步價 6~11 萬，2.0 汽油相對耐用，2.3L 引擎高里程易耗機油。"
                },
                "trims": [
                    {
                        "trim_name": "2.0L / 2.3S 運動版",
                        "msrp_wan": 88.9,
                        "engine_code": "LF 2.0L / L3 2.3L 自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "147 ps (2.0) / 166 ps (2.3)",
                        "torque": "18.8 kgm / 21.1 kgm",
                        "transmission": "4AT / 5AT",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前雙A臂 / 後多連桿",
                        "fuel_economy": "11.8 km/L",
                        "dimensions": "4690 x 1780 x 1435 mm (軸距 2675 mm)",
                        "safety": "2氣囊、ABS"
                    }
                ],
                "common_issues": [
                    {
                        "part": "動力方向機油管滲油 / 前雙A臂鐵套異音",
                        "severity": "中風險",
                        "mileage_range": "15萬公里以上",
                        "symptom": "轉向異音、底盤鬆散。",
                        "repair_cost_ntd": "底盤鐵套整理約 1~1.5 萬",
                        "advice": "此年份以 2.0L 為主，看車重點在變速箱與冷氣。"
                    }
                ],
                "yearly_prices": {
                    "2003": {"msrp": 82.9, "dealer": 6.5, "private": 4.2, "book": 2.5},
                    "2004": {"msrp": 83.9, "dealer": 7.2, "private": 4.8, "book": 3.0},
                    "2005": {"msrp": 85.9, "dealer": 8.0, "private": 5.5, "book": 3.6},
                    "2006": {"msrp": 87.9, "dealer": 9.0, "private": 6.2, "book": 4.2},
                    "2007": {"msrp": 88.9, "dealer": 10.2, "private": 7.2, "book": 5.0}
                }
            },
            {
                "gen_id": "mazda6-gj",
                "gen_name": "第 3 代 (GJ/GL 魂動 Sedan / Wagon)",
                "years": [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
                "is_major_change": True,
                "major_change_year": 2014,
                "major_change_note": "日本原裝進口 3代導入魂動設計與 Skyactiv，2017年追加 Wagon 旅行車（後期導入 2.5L NA），二手旅行車極保值。",
                "platform": "Mazda Skyactiv-Chassis 大型平台",
                "origin": "日本原裝進口",
                "photo_query": "Mazda6 GJ Wagon",
                "depreciation_alert": {
                    "level": "high",
                    "title": "務必避開 2.2D 柴油版！2.0 / 2.5 汽油 Wagon 非常保值",
                    "reason": "2.2D 柴油與 1代 CX-5 同顆引擎存在副水箱噴水災情，導致柴油價崩；2.0/2.5 汽油與 Wagon 旅行車則完全正常且搶手。"
                },
                "trims": [
                    {
                        "trim_name": "2.0L Skyactiv-G 房車 / Wagon",
                        "msrp_wan": 116.9,
                        "engine_code": "PE-VPS 2.0L Skyactiv-G 自然進氣",
                        "displacement_cc": 1998,
                        "horsepower": "165 ps / 6,000 rpm",
                        "torque": "21.7 kgm / 4,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "14.8 km/L",
                        "dimensions": "4865 x 1840 x 1450 mm (軸距 2830 mm)",
                        "safety": "6氣囊、MRCC 全速域定速(後期)"
                    },
                    {
                        "trim_name": "2.5L Skyactiv-G Wagon 旗艦進化型 (旅行車)",
                        "msrp_wan": 132.9,
                        "engine_code": "PY-VPS 2.5L Skyactiv-G 自然進氣",
                        "displacement_cc": 2488,
                        "horsepower": "194 ps / 6,000 rpm",
                        "torque": "26.3 kgm / 4,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "13.0 km/L",
                        "dimensions": "4805 x 1840 x 1480 mm (軸距 2750 mm)",
                        "safety": "6氣囊、MRCC 全速域、360環景"
                    },
                    {
                        "trim_name": "2.2D Skyactiv-D 柴油版 (高風險)",
                        "msrp_wan": 138.9,
                        "engine_code": "SH-VPTR 2.2L 雙渦輪柴油",
                        "displacement_cc": 2191,
                        "horsepower": "175 ps / 4,500 rpm",
                        "torque": "42.8 kgm / 2,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後獨立多連桿",
                        "fuel_economy": "19.0 km/L",
                        "dimensions": "4865 x 1840 x 1450 mm (軸距 2830 mm)",
                        "safety": "6氣囊、盲點偵測"
                    }
                ],
                "common_issues": [
                    {
                        "part": "2.2D 柴油沖汽缸墊片噴水（僅柴油）",
                        "severity": "高風險",
                        "mileage_range": "8萬公里以上",
                        "symptom": "副水箱噴水、引擎高溫。",
                        "repair_cost_ntd": "引擎大修約 6~10 萬",
                        "advice": "買 Mazda6 請直接鎖定 2.0 或 2.5 汽油（尤推 Wagon 旅行車）。"
                    }
                ],
                "yearly_prices": {
                    "2014": {"msrp": 116.9, "dealer": 29.0, "private": 24.5, "book": 21.0},
                    "2015": {"msrp": 116.9, "dealer": 33.0, "private": 28.0, "book": 24.5},
                    "2016": {"msrp": 116.9, "dealer": 37.5, "private": 32.5, "book": 28.5},
                    "2017": {"msrp": 118.9, "dealer": 43.0, "private": 37.5, "book": 33.0},
                    "2018": {"msrp": 119.9, "dealer": 49.0, "private": 43.0, "book": 38.0},
                    "2019": {"msrp": 124.9, "dealer": 56.0, "private": 49.5, "book": 44.0},
                    "2020": {"msrp": 124.9, "dealer": 63.0, "private": 56.5, "book": 50.5},
                    "2021": {"msrp": 124.9, "dealer": 70.0, "private": 63.5, "book": 57.0},
                    "2022": {"msrp": 129.9, "dealer": 78.0, "private": 71.0, "book": 64.5},
                    "2023": {"msrp": 132.9, "dealer": 86.0, "private": 79.0, "book": 72.0}
                }
            }
        ]
    },
    {
        "id": "mazda-cx30",
        "brand": "Mazda",
        "model": "CX-30",
        "model_zh": "馬自達 CX-30",
        "category": "跨界休旅車 (SUV)",
        "summary": "2019年底導入的精品級跨界休旅，採與 4代 Mazda3 相同的 Skyactiv 2.0L + 6AT，內裝質感媲美豪華品牌且完全無嚴重通病，中古行情非常穩健。",
        "generations": [
            {
                "gen_id": "cx30-dm",
                "gen_name": "第 1 代 (DM 日本進口 Skyactiv)",
                "years": [2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2020,
                "major_change_note": "2019年底上市，標配 7氣囊與全速域 CTS/MRCC 主動安全，2022年後逐步下放 360 環景與 Bose 音響。",
                "platform": "Mazda Skyactiv-Vehicle Architecture",
                "origin": "日本原裝進口",
                "photo_query": "Mazda CX-30",
                "depreciation_alert": {
                    "level": "low",
                    "title": "6AT 變速箱成熟穩定，內裝質感同級最佳",
                    "reason": "兼顧都會好停車身尺碼與輕度休旅視野，女性與小家庭買家指名度高。"
                },
                "trims": [
                    {
                        "trim_name": "20S 尊榮 / 頂級 / Signature (2.0L)",
                        "msrp_wan": 99.8,
                        "engine_code": "PE-VPS 2.0L Skyactiv-G 自然進氣",
                        "displacement_cc": 1998,
                        "horsepower": "165 ps / 6,000 rpm",
                        "torque": "21.7 kgm / 4,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前輪驅動 (FF)",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "fuel_economy": "15.0 km/L",
                        "dimensions": "4395 x 1795 x 1540 mm (軸距 2655 mm)",
                        "safety": "7氣囊、MRCC 全速域、CTS 車道維持"
                    }
                ],
                "common_issues": [
                    {
                        "part": "後照鏡收折馬達 / 車身防刮塑料白化",
                        "severity": "一般耗材",
                        "mileage_range": "5萬公里以上",
                        "symptom": "洗車進水後偶發收折不完全；大型輪弧塑料日曬白化。",
                        "repair_cost_ntd": "保固內免費出保；自費約 2,000 元",
                        "advice": "機械體質極佳，優先選 2022 年後配備 360 環景與全速域車道置中的年式。"
                    }
                ],
                "yearly_prices": {
                    "2020": {"msrp": 96.9, "dealer": 54.5, "private": 49.5, "book": 45.0},
                    "2021": {"msrp": 96.9, "dealer": 59.5, "private": 54.5, "book": 49.8},
                    "2022": {"msrp": 99.8, "dealer": 65.5, "private": 60.0, "book": 55.0},
                    "2023": {"msrp": 102.8, "dealer": 72.0, "private": 66.5, "book": 61.0},
                    "2024": {"msrp": 103.8, "dealer": 79.0, "private": 73.0, "book": 67.5},
                    "2025": {"msrp": 103.8, "dealer": 86.5, "private": 80.5, "book": 74.5}
                }
            }
        ]
    },
    {
        "id": "mazda-mx5",
        "brand": "Mazda",
        "model": "MX-5",
        "model_zh": "馬自達 MX-5 敞篷跑車",
        "category": "雙座敞篷跑車",
        "summary": "全球最暢銷雙座敞篷小跑車！NC 3代(2006-2015)與 ND 4代(2016+)皆以極致輕量化與 50:50 前後配重聞名，台灣中古市場極度保值，幾乎沒有明顯折舊崩盤。",
        "generations": [
            {
                "gen_id": "mx5-nc",
                "gen_name": "第 3 代 (NC 電動硬頂敞篷)",
                "years": [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
                "is_major_change": True,
                "major_change_year": 2007,
                "major_change_note": "導入電動收折硬頂 (PRHT) 與 2.0L 引擎 + 6速手自排，在台灣日常停放更安心。",
                "platform": "Mazda NC 縱置後驅平台",
                "origin": "日本原裝進口",
                "photo_query": "Mazda MX-5 NC",
                "depreciation_alert": {
                    "level": "low",
                    "title": "經典敞篷小跑車，市場保值度驚人",
                    "reason": "15年車齡仍維持 45~58 萬行情，稀有性高且後驅樂趣純粹。"
                },
                "trims": [
                    {
                        "trim_name": "2.0L 電動硬頂敞篷 (6AT)",
                        "msrp_wan": 122.0,
                        "engine_code": "LF-VE 2.0L 自然進氣",
                        "displacement_cc": 1999,
                        "horsepower": "160 ps / 6,700 rpm",
                        "torque": "19.2 kgm / 5,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前置後驅 (FR)",
                        "suspension": "前雙A臂 / 後多連桿",
                        "fuel_economy": "11.5 km/L",
                        "dimensions": "4020 x 1720 x 1255 mm (軸距 2330 mm)",
                        "safety": "4氣囊、DSC 車身穩定"
                    }
                ],
                "common_issues": [
                    {
                        "part": "電動硬頂排水孔堵塞滲水 / 副水箱塑膠老化",
                        "severity": "中風險",
                        "mileage_range": "10年以上",
                        "symptom": "大雨後座椅後方積水、塑膠副水箱脆化。",
                        "repair_cost_ntd": "換裝鋁製副水箱約 5,000 元",
                        "advice": "定期疏通排水孔即可，建議預防性更換鋁製副水箱。"
                    }
                ],
                "yearly_prices": {
                    "2008": {"msrp": 118.0, "dealer": 46.0, "private": 41.0, "book": 32.0},
                    "2010": {"msrp": 120.0, "dealer": 50.0, "private": 44.5, "book": 36.0},
                    "2012": {"msrp": 122.0, "dealer": 55.0, "private": 49.0, "book": 40.0},
                    "2014": {"msrp": 122.0, "dealer": 60.0, "private": 54.0, "book": 45.0}
                }
            },
            {
                "gen_id": "mx5-nd",
                "gen_name": "第 4 代 (ND 軟頂 / RF 硬頂敞篷)",
                "years": [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "is_major_change": True,
                "major_change_year": 2016,
                "major_change_note": "2016年大改款車重降至僅約 1 噸！2019年起 ND2 馬力由 160ps 提升至 184ps，並提供 6MT 手排與 RF 硬頂。",
                "platform": "Mazda ND Skyactiv 輕量化後驅平台",
                "origin": "日本原裝進口",
                "photo_query": "Mazda MX-5 ND",
                "depreciation_alert": {
                    "level": "low",
                    "title": "極度保值！184ps 手排版二手價居高不下",
                    "reason": "2.0L 低稅金純種後驅敞篷，妥善率極佳、養車成本比歐系跑車低非常多。"
                },
                "trims": [
                    {
                        "trim_name": "2.0L 軟頂敞篷 6MT 手排 (ND2 184ps)",
                        "msrp_wan": 135.0,
                        "engine_code": "PE-VPS 2.0L 高轉 Skyactiv-G",
                        "displacement_cc": 1998,
                        "horsepower": "184 ps / 7,000 rpm (前期160ps)",
                        "torque": "20.9 kgm / 4,000 rpm",
                        "transmission": "6速純手排",
                        "drivetrain": "前置後驅 (FR) + LSD 限滑差速器",
                        "suspension": "前雙A臂 / 後多連桿",
                        "fuel_economy": "14.8 km/L",
                        "dimensions": "3915 x 1735 x 1230 mm (軸距 2310 mm)",
                        "safety": "4氣囊、盲點偵測、Bilstein 避震(後期)"
                    },
                    {
                        "trim_name": "2.0L RF 電動硬頂敞篷 (6AT 自排)",
                        "msrp_wan": 152.0,
                        "engine_code": "PE-VPS 2.0L Skyactiv-G",
                        "displacement_cc": 1998,
                        "horsepower": "184 ps / 7,000 rpm",
                        "torque": "20.9 kgm / 4,000 rpm",
                        "transmission": "6速手自排",
                        "drivetrain": "前置後驅 (FR)",
                        "suspension": "前雙A臂 / 後多連桿",
                        "fuel_economy": "14.2 km/L",
                        "dimensions": "3915 x 1735 x 1235 mm (軸距 2310 mm)",
                        "safety": "4氣囊、盲點、SCBS 都會煞車"
                    }
                ],
                "common_issues": [
                    {
                        "part": "前期 2016 手排變速箱二/三檔齒輪強度（ND1）",
                        "severity": "中風險",
                        "mileage_range": "激烈操駕車主",
                        "symptom": "2016-2017 年式手排大腳換檔偶發崩齒，2018+ 已強化改良。",
                        "repair_cost_ntd": "強化變速箱約 4~6 萬",
                        "advice": "強烈建議挑選 2019 年式以後的 ND2（184ps + 改良齒輪）。"
                    }
                ],
                "yearly_prices": {
                    "2016": {"msrp": 129.8, "dealer": 69.0, "private": 63.0, "book": 54.0},
                    "2017": {"msrp": 132.0, "dealer": 73.0, "private": 67.0, "book": 58.0},
                    "2018": {"msrp": 132.0, "dealer": 78.0, "private": 72.0, "book": 63.0},
                    "2019": {"msrp": 134.0, "dealer": 86.0, "private": 79.5, "book": 70.0},
                    "2020": {"msrp": 134.0, "dealer": 91.0, "private": 84.5, "book": 75.0},
                    "2021": {"msrp": 134.0, "dealer": 96.5, "private": 90.0, "book": 80.5},
                    "2022": {"msrp": 135.0, "dealer": 102.0, "private": 95.5, "book": 86.0},
                    "2023": {"msrp": 135.0, "dealer": 108.0, "private": 101.5, "book": 92.0},
                    "2024": {"msrp": 140.0, "dealer": 115.0, "private": 108.0, "book": 98.5},
                    "2025": {"msrp": 140.0, "dealer": 123.0, "private": 116.0, "book": 106.0}
                }
            }
        ]
    }
]
