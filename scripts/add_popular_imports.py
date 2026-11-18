import json
import shutil
from copy import deepcopy
from datetime import datetime
from pathlib import Path

DB_PATH = Path("data/cars_db.json")
BACKUP_PATH = Path("data/cars_db.backup_before_imports.json")

# 12 款台灣熱門進口車系完整資料庫（對齊 renderSmartFinder() 前端 Schema）
NEW_IMPORT_MODELS = [
    {
        "brand": "Mercedes-Benz",
        "model": "G-Class",
        "summary": "頂級硬派豪華越野圖騰，2018年大改款(W463A)換裝前雙A臂懸吊後公路舒適性大幅躍進，G63與G350d在台二手保值率極度強勢。",
        "generations": [
            {
                "gen_id": "mb-g-class-w463",
                "gen_name": "第 1 代後期 (W463 經典固定軸時期)",
                "years": [2013, 2014, 2015, 2016, 2017],
                "depreciation_alert": {
                    "level": "low",
                    "title": "經典方正外型與 V8 聲浪支撐行情，200–320 萬區間抗跌性極強"
                },
                "common_issues": [
                    {
                        "part": "三把差速器鎖止作動器卡滯 / 車門六角鎖與電動窗升降機老化",
                        "mileage_range": "8萬公里以上",
                        "repair_cost_ntd": "差速器鎖感應器與作動器整理約 18,000 ~ 28,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2014, "msrp": 588.0, "dealer": 225.0, "private": 205.0, "book": 215.0},
                    {"year": 2017, "msrp": 635.0, "dealer": 315.0, "private": 290.0, "book": 300.0}
                ],
                "trims": [
                    {
                        "trim_name": "G350 BlueTEC / G350d",
                        "msrp_wan": 588.0,
                        "displacement_cc": 2987,
                        "horsepower": "245 ps",
                        "engine_code": "OM642",
                        "transmission": "7速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "前固定軸 / 後固定軸",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "G63 AMG",
                        "msrp_wan": 865.0,
                        "displacement_cc": 5461,
                        "horsepower": "571 ps",
                        "engine_code": "M157",
                        "transmission": "7速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "前固定軸 / 後固定軸",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "mb-g-class-w463a",
                "gen_name": "第 2 代 (W463A 雙螢幕獨立前懸吊世代)",
                "years": [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "新車長期候車與加價效應，5年車仍保有 65% 以上高殘值"
                },
                "common_issues": [
                    {
                        "part": "前擋風玻璃垂直角度易遭跳石擊裂 / 48V 輕油電啟動馬達發電機 (ISG)",
                        "mileage_range": "6萬公里以上",
                        "repair_cost_ntd": "原廠隔熱前擋更換約 45,000 ~ 65,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2019, "msrp": 662.0, "dealer": 435.0, "private": 405.0, "book": 418.0},
                    {"year": 2022, "msrp": 698.0, "dealer": 545.0, "private": 510.0, "book": 525.0},
                    {"year": 2024, "msrp": 715.0, "dealer": 635.0, "private": 600.0, "book": 615.0}
                ],
                "trims": [
                    {
                        "trim_name": "G350d / G400d",
                        "msrp_wan": 662.0,
                        "displacement_cc": 2925,
                        "horsepower": "330 ps",
                        "engine_code": "OM656",
                        "transmission": "9速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "前雙A臂 / 後固定軸",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "AMG G63",
                        "msrp_wan": 950.0,
                        "displacement_cc": 3982,
                        "horsepower": "585 ps",
                        "engine_code": "M177",
                        "transmission": "9速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "前雙A臂 / 後固定軸",
                        "powertrain": "油電"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Mercedes-Benz",
        "model": "EQA",
        "summary": "基於 MFA2 平台打造的賓士入門純電都會休旅，企業長租到期車源陸續釋出，120–150 萬即可入主三芒星純電休旅。",
        "generations": [
            {
                "gen_id": "mb-eqa-h243",
                "gen_name": "第 1 代 (H243 EQA 250 / 小改款)",
                "years": [2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "medium",
                    "title": "前兩年折舊幅度達 35%–42%，二年期準新車性價比優於新車"
                },
                "common_issues": [
                    {
                        "part": "充電蓋電磁閥卡滯無法彈開 / MBUX 車機系統偶發黑屏重啟",
                        "mileage_range": "4萬公里以上",
                        "repair_cost_ntd": "充電蓋執行器更換約 6,500 元；軟體刷新約 2,500 元"
                    }
                ],
                "year_points": [
                    {"year": 2022, "msrp": 215.0, "dealer": 122.0, "private": 110.0, "book": 116.0},
                    {"year": 2024, "msrp": 217.0, "dealer": 158.0, "private": 144.0, "book": 150.0}
                ],
                "trims": [
                    {
                        "trim_name": "EQA 250",
                        "msrp_wan": 215.0,
                        "displacement_cc": 0,
                        "horsepower": "190 ps",
                        "engine_code": "EM0027 (66.5kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "純電"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Mercedes-Benz",
        "model": "EQE",
        "summary": "EVA2 純電專用平台中大型豪華房車，具備極低風阻與後輪轉向選配，因新車定價高且純電迭代快，中古折價空間極大。",
        "generations": [
            {
                "gen_id": "mb-eqe-v295",
                "gen_name": "第 1 代 (V295 EQE 300 / AMG EQE 43)",
                "years": [2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "high",
                    "title": "前三年折舊高達 45%–50%，2年車已跌破 190 萬，適合接手折舊甜美期"
                },
                "common_issues": [
                    {
                        "part": "隱藏式車門把手伸縮馬達異音 / 高壓電池冷卻液閥門滲漏",
                        "mileage_range": "5萬公里以上",
                        "repair_cost_ntd": "單組門把總成更換約 14,000 元；冷卻閥門整理約 18,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2022, "msrp": 326.0, "dealer": 168.0, "private": 152.0, "book": 160.0},
                    {"year": 2024, "msrp": 326.0, "dealer": 218.0, "private": 198.0, "book": 208.0}
                ],
                "trims": [
                    {
                        "trim_name": "EQE 300",
                        "msrp_wan": 326.0,
                        "displacement_cc": 0,
                        "horsepower": "245 ps",
                        "engine_code": "EVA2-RWD (89kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "FR 後輪驅動",
                        "suspension": "前四連桿 / 後多連桿",
                        "powertrain": "純電"
                    },
                    {
                        "trim_name": "AMG EQE 43 4MATIC",
                        "msrp_wan": 482.0,
                        "displacement_cc": 0,
                        "horsepower": "476 ps",
                        "engine_code": "EVA2-AWD (90.5kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "AIRMATIC 氣壓懸吊",
                        "powertrain": "純電"
                    }
                ]
            }
        ]
    },
    {
        "brand": "BMW",
        "model": "X6",
        "summary": "豪華跨界跑旅指標車系，台灣總代理與美規外匯車源均相當龐大，B58 直列六缸動力搭配 ZF 8AT 妥善率表現穩健。",
        "generations": [
            {
                "gen_id": "bmw-x6-f16",
                "gen_name": "第 2 代 (F16 xDrive35i / xDrive30d)",
                "years": [2015, 2016, 2017, 2018, 2019],
                "depreciation_alert": {
                    "level": "medium",
                    "title": "車齡進入 7–10 年階段，85–135 萬即可入主，需留意後氣壓懸吊氣囊老化"
                },
                "common_issues": [
                    {
                        "part": "後軸氣壓懸吊氣囊漏氣塌陷 / N55 引擎氣門室蓋與機油芯座墊片滲油",
                        "mileage_range": "9萬公里以上",
                        "repair_cost_ntd": "後氣壓氣囊一對更換約 18,000 ~ 24,000 元；墊片全套整理約 16,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2015, "msrp": 366.0, "dealer": 88.0, "private": 76.0, "book": 82.0},
                    {"year": 2018, "msrp": 373.0, "dealer": 128.0, "private": 114.0, "book": 120.0}
                ],
                "trims": [
                    {
                        "trim_name": "xDrive35i",
                        "msrp_wan": 366.0,
                        "displacement_cc": 2979,
                        "horsepower": "306 ps",
                        "engine_code": "N55B30",
                        "transmission": "8速手自排",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前雙A臂 / 後多連桿(含後氣壓)",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "xDrive30d",
                        "msrp_wan": 373.0,
                        "displacement_cc": 2993,
                        "horsepower": "258 ps",
                        "engine_code": "N57D30",
                        "transmission": "8速手自排",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前雙A臂 / 後多連桿(含後氣壓)",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "bmw-x6-g06",
                "gen_name": "第 3 代 (G06 xDrive40i 48V輕油電)",
                "years": [2020, 2021, 2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "B58 引擎口碑極佳且配備 5AU 半自動駕駛，中古市場指名度高"
                },
                "common_issues": [
                    {
                        "part": "主動式進氣格柵百葉窗馬達故障 / 水箱冷卻液副水箱蓋滲漏",
                        "mileage_range": "7萬公里以上",
                        "repair_cost_ntd": "進氣格柵作動器更換約 12,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2020, "msrp": 365.0, "dealer": 195.0, "private": 178.0, "book": 186.0},
                    {"year": 2023, "msrp": 399.0, "dealer": 278.0, "private": 258.0, "book": 268.0}
                ],
                "trims": [
                    {
                        "trim_name": "xDrive40i M Sport",
                        "msrp_wan": 380.0,
                        "displacement_cc": 2998,
                        "horsepower": "333 ps",
                        "engine_code": "B58B30",
                        "transmission": "8速手自排",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前雙A臂 / 後多連桿",
                        "powertrain": "油電"
                    }
                ]
            }
        ]
    },
    {
        "brand": "BMW",
        "model": "i4",
        "summary": "保留經典 4 系列 Gran Coupe 操控基因的純電轎跑，WLTP 續航達 590 公里，為台灣豪華純電轎跑銷售冠軍，中古流通極快。",
        "generations": [
            {
                "gen_id": "bmw-i4-g26",
                "gen_name": "第 1 代 (G26 eDrive40 / M50)",
                "years": [2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "相較純電休旅更抗跌，eDrive40 二年車穩守 165–185 萬區間"
                },
                "common_issues": [
                    {
                        "part": "冷卻液切換閥 (Coolant Changeover Valve) 故障碼 / 後軸氣壓水平調整感應器",
                        "mileage_range": "5萬公里以上",
                        "repair_cost_ntd": "冷卻切換閥更換約 15,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2022, "msrp": 255.0, "dealer": 162.0, "private": 148.0, "book": 155.0},
                    {"year": 2024, "msrp": 275.0, "dealer": 205.0, "private": 190.0, "book": 198.0}
                ],
                "trims": [
                    {
                        "trim_name": "eDrive40",
                        "msrp_wan": 255.0,
                        "displacement_cc": 0,
                        "horsepower": "340 ps",
                        "engine_code": "HA0001N0 (83.9kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "FR 後輪驅動",
                        "suspension": "前雙接頭彈簧柱 / 後五連桿(後氣壓)",
                        "powertrain": "純電"
                    },
                    {
                        "trim_name": "M50",
                        "msrp_wan": 310.0,
                        "displacement_cc": 0,
                        "horsepower": "544 ps",
                        "engine_code": "Dual-Motor (83.9kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "M 自適應電子懸吊",
                        "powertrain": "純電"
                    }
                ]
            }
        ]
    },
    {
        "brand": "BMW",
        "model": "iX",
        "summary": "BMW 新世代純電旗艦休旅，碳纖維複合車體結構與極簡座艙，台灣道路能見度高，xDrive40 為中古市場交易主力。",
        "generations": [
            {
                "gen_id": "bmw-ix-i20",
                "gen_name": "第 1 代 (I20 xDrive40 / xDrive50)",
                "years": [2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "medium",
                    "title": "新車逾 330 萬，2–3 年車折舊至 185–225 萬，高階豪華純電高 CP 值選擇"
                },
                "common_issues": [
                    {
                        "part": "高壓電池冷卻系統電磁閥滲漏 / 21-22吋大尺碼低滾阻輪胎磨耗快",
                        "mileage_range": "4萬公里以上",
                        "repair_cost_ntd": "四輪性能電車胎更換約 36,000 ~ 48,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2022, "msrp": 320.0, "dealer": 185.0, "private": 170.0, "book": 178.0},
                    {"year": 2024, "msrp": 348.0, "dealer": 248.0, "private": 230.0, "book": 238.0}
                ],
                "trims": [
                    {
                        "trim_name": "xDrive40 旗艦版",
                        "msrp_wan": 336.0,
                        "displacement_cc": 0,
                        "horsepower": "326 ps",
                        "engine_code": "Dual-Motor (76.6kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前雙A臂 / 後五連桿",
                        "powertrain": "純電"
                    },
                    {
                        "trim_name": "xDrive50 旗艦版",
                        "msrp_wan": 436.0,
                        "displacement_cc": 0,
                        "horsepower": "523 ps",
                        "engine_code": "Dual-Motor (111.5kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前後軸自動水平氣壓懸吊",
                        "powertrain": "純電"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Toyota",
        "model": "GR Yaris",
        "summary": "WRC 世界拉力錦標賽認證血統鋼炮，1.6T 三缸渦輪搭配 GR-FOUR 四驅與 6 速純手排，台灣配額稀少、中古保值率堪稱神話級。",
        "generations": [
            {
                "gen_id": "toyota-gr-yaris-gxpa16",
                "gen_name": "第 1 代 (GXPA16 前期6MT / 2025小改款)",
                "years": [2021, 2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "極度抗跌理財神車，無賽道事故之原版件車源殘值長期高於 82%"
                },
                "common_issues": [
                    {
                        "part": "激烈操駕導致離合器片與雙質量飛輪磨耗 / 後差速器油溫過高保護",
                        "mileage_range": "4萬公里以上 (視賽道頻率)",
                        "repair_cost_ntd": "強化離合器組連工帶料約 35,000 ~ 48,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2021, "msrp": 179.0, "dealer": 148.0, "private": 140.0, "book": 135.0},
                    {"year": 2023, "msrp": 196.0, "dealer": 168.0, "private": 160.0, "book": 152.0},
                    {"year": 2025, "msrp": 205.0, "dealer": 192.0, "private": 184.0, "book": 175.0}
                ],
                "trims": [
                    {
                        "trim_name": "1.6 RZ High Performance (6MT)",
                        "msrp_wan": 196.0,
                        "displacement_cc": 1618,
                        "horsepower": "261 ps",
                        "engine_code": "G16E-GTS",
                        "transmission": "6速手排",
                        "drivetrain": "AWD GR-FOUR四輪驅動",
                        "suspension": "前麥花臣 / 後雙A臂",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Toyota",
        "model": "GR Supra",
        "summary": "與 BMW Z4 共同開發之經典雙門後驅跑車，台灣以 3.0T Premium 為主力，2023 年追加 6 速純手排版本，二手市場關注度極高。",
        "generations": [
            {
                "gen_id": "toyota-gr-supra-a90",
                "gen_name": "第 5 代 (A90 / DB42 2.0T & 3.0T)",
                "years": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "3.0T B58 引擎改裝潛力大且聲浪迷人，6MT 手排版行情高於自排版約 15–20 萬"
                },
                "common_issues": [
                    {
                        "part": "改寫 ECU 電腦後傳動軸與差速器油封滲油 / 前下巴低趴刮傷",
                        "mileage_range": "5萬公里以上",
                        "repair_cost_ntd": "原廠前保桿下擾流更新約 12,000 元；變速箱油底殼總成約 9,500 元"
                    }
                ],
                "year_points": [
                    {"year": 2020, "msrp": 248.0, "dealer": 172.0, "private": 160.0, "book": 165.0},
                    {"year": 2023, "msrp": 266.0, "dealer": 215.0, "private": 202.0, "book": 206.0}
                ],
                "trims": [
                    {
                        "trim_name": "2.0T",
                        "msrp_wan": 215.0,
                        "displacement_cc": 1998,
                        "horsepower": "258 ps",
                        "engine_code": "B48B20",
                        "transmission": "8速手自排",
                        "drivetrain": "FR 後輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "3.0T Premium (8AT)",
                        "msrp_wan": 266.0,
                        "displacement_cc": 2998,
                        "horsepower": "340 ps",
                        "engine_code": "B58B30",
                        "transmission": "8速手自排",
                        "drivetrain": "FR 後輪驅動",
                        "suspension": "AVS 可變阻尼電子懸吊",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "3.0T Premium (6MT 手排版)",
                        "msrp_wan": 269.0,
                        "displacement_cc": 2998,
                        "horsepower": "340 ps",
                        "engine_code": "B58B30",
                        "transmission": "6速手排",
                        "drivetrain": "FR 後輪驅動",
                        "suspension": "AVS 可變阻尼電子懸吊",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Honda",
        "model": "Civic Type R",
        "summary": "紐柏林最速前驅鋼炮傳奇，FK8 與 FL5 透過貿易商大量引進台灣，純手排與 K20C1 紅頭渦輪引擎造就極端保值神話。",
        "generations": [
            {
                "gen_id": "honda-civic-type-r-fk8",
                "gen_name": "第 5 代 (FK8 英國製貿易商主力期)",
                "years": [2017, 2018, 2019, 2020, 2021],
                "depreciation_alert": {
                    "level": "low",
                    "title": "經歷 5–8 年車齡仍站穩 145–175 萬，保值率遠超同價位歐系跑車"
                },
                "common_issues": [
                    {
                        "part": "激烈換檔 2 檔同步齒輪磨損打齒 / 高溫環境下水箱散熱效率不足",
                        "mileage_range": "6萬公里以上",
                        "repair_cost_ntd": "變速箱 2 檔同步器整理約 28,000 ~ 38,000 元；加大鋁水箱約 18,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2018, "msrp": 238.0, "dealer": 152.0, "private": 142.0, "book": 138.0},
                    {"year": 2021, "msrp": 248.0, "dealer": 178.0, "private": 168.0, "book": 160.0}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 VTEC Turbo (FK8 6MT)",
                        "msrp_wan": 238.0,
                        "displacement_cc": 1996,
                        "horsepower": "320 ps",
                        "engine_code": "K20C1",
                        "transmission": "6速手排",
                        "drivetrain": "FF 前輪驅動(含LSD)",
                        "suspension": "雙軸麥花臣電子阻尼 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "honda-civic-type-r-fl5",
                "gen_name": "第 6 代 (FL5 日本製最新世代)",
                "years": [2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "貿易商引進新車約 298–318 萬，準新車中古行情緊貼 255–285 萬"
                },
                "common_issues": [
                    {
                        "part": "電動轉向齒條 (EPS) 異音召回件 / 麂皮桶椅側翼上下車磨損",
                        "mileage_range": "3萬公里以上",
                        "repair_cost_ntd": "轉向機齒條總成更換約 32,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2023, "msrp": 308.0, "dealer": 262.0, "private": 250.0, "book": 235.0},
                    {"year": 2025, "msrp": 298.0, "dealer": 282.0, "private": 272.0, "book": 255.0}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 VTEC Turbo (FL5 6MT)",
                        "msrp_wan": 298.0,
                        "displacement_cc": 1996,
                        "horsepower": "330 ps",
                        "engine_code": "K20C1",
                        "transmission": "6速手排",
                        "drivetrain": "FF 前輪驅動(含LSD)",
                        "suspension": "雙軸麥花臣電子阻尼 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Volkswagen",
        "model": "Arteon",
        "summary": "福斯品牌美型旗艦獵跑，提供 Fastback 五門斜背與 Shooting Brake 五門獵跑雙車型，EA888 動力搭配濕式 DQ381 七速雙離合器。",
        "generations": [
            {
                "gen_id": "vw-arteon-3h",
                "gen_name": "第 1 代小改款 (3H Fastback / Shooting Brake)",
                "years": [2021, 2022, 2023, 2024],
                "depreciation_alert": {
                    "level": "medium",
                    "title": "新車 155–208 萬，3年車折舊至 95–125 萬，Shooting Brake 獵跑版殘值高出斜背版約 8–10 萬"
                },
                "common_issues": [
                    {
                        "part": "EA888 Gen3/4 水泵浦總成與節溫器滲漏 / 方向盤電容式觸控模組誤觸報錯",
                        "mileage_range": "7萬公里以上",
                        "repair_cost_ntd": "改良型鋁合金水泵浦總成更換約 14,000 ~ 18,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2021, "msrp": 173.8, "dealer": 96.0, "private": 86.0, "book": 91.0},
                    {"year": 2023, "msrp": 185.8, "dealer": 124.0, "private": 112.0, "book": 118.0}
                ],
                "trims": [
                    {
                        "trim_name": "330 TSI Elegance / R-Line",
                        "msrp_wan": 173.8,
                        "displacement_cc": 1984,
                        "horsepower": "190 ps",
                        "engine_code": "EA888 Gen3B",
                        "transmission": "7速雙離合器自手排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "430 TSI R-Line Performance (4MOTION)",
                        "msrp_wan": 205.8,
                        "displacement_cc": 1984,
                        "horsepower": "272 ps",
                        "engine_code": "EA888 Gen4",
                        "transmission": "7速雙離合器自手排",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "DCC 主動式底盤控制系統",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Land Rover",
        "model": "Range Rover Sport",
        "summary": "兼具全地形越野實力與公路運動操控的英國豪華休旅旗艦，L494 世代採用全鋁合金車體大幅減重，2023 年邁入全新 L461 世代。",
        "generations": [
            {
                "gen_id": "lr-rr-sport-l494",
                "gen_name": "第 2 代 (L494 全鋁合金車體世代)",
                "years": [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
                "depreciation_alert": {
                    "level": "high",
                    "title": "前期 2014–2016 車源已跌破 95 萬，入手門檻低但須預留氣壓懸吊與柴油系統整備金"
                },
                "common_issues": [
                    {
                        "part": "四輪電子氣壓懸吊氣囊與打氣泵老化 / 3.0 柴油 E-Diff 電子差速器與進氣歧管龜裂",
                        "mileage_range": "9萬公里以上",
                        "repair_cost_ntd": "單支氣壓避震器更換約 22,000 ~ 32,000 元；進氣歧管總成約 28,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2015, "msrp": 489.0, "dealer": 88.0, "private": 74.0, "book": 80.0},
                    {"year": 2019, "msrp": 479.0, "dealer": 158.0, "private": 140.0, "book": 148.0},
                    {"year": 2022, "msrp": 465.0, "dealer": 225.0, "private": 205.0, "book": 215.0}
                ],
                "trims": [
                    {
                        "trim_name": "3.0 SDV6 HSE / D300",
                        "msrp_wan": 489.0,
                        "displacement_cc": 2993,
                        "horsepower": "306 ps",
                        "engine_code": "306DT / AJ20D6",
                        "transmission": "8速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "電子氣壓懸吊系統",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "3.0 V6 SC / P400 48V輕油電",
                        "msrp_wan": 479.0,
                        "displacement_cc": 2995,
                        "horsepower": "400 ps",
                        "engine_code": "AJ126 / AJ20P6",
                        "transmission": "8速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "電子氣壓懸吊系統",
                        "powertrain": "油電"
                    }
                ]
            },
            {
                "gen_id": "lr-rr-sport-l461",
                "gen_name": "第 3 代 (L461 MLA-Flex 旗艦世代)",
                "years": [2023, 2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "新世代外觀與 Pivi Pro 質感大幅升級，3.0 汽柴油雙動力保值性明顯優於前代"
                },
                "common_issues": [
                    {
                        "part": "隱藏式伸縮車門把手感應異常 / 48V 輕油電系統軟體偶發警示燈",
                        "mileage_range": "4萬公里以上",
                        "repair_cost_ntd": "保固期內多以軟體更新解決，過保門把總成約 16,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2023, "msrp": 459.0, "dealer": 335.0, "private": 310.0, "book": 322.0},
                    {"year": 2025, "msrp": 462.0, "dealer": 395.0, "private": 370.0, "book": 382.0}
                ],
                "trims": [
                    {
                        "trim_name": "D300 Dynamic SE",
                        "msrp_wan": 459.0,
                        "displacement_cc": 2997,
                        "horsepower": "300 ps",
                        "engine_code": "AJ20D6 (MHEV)",
                        "transmission": "8速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "動態氣壓懸吊系統",
                        "powertrain": "油電"
                    },
                    {
                        "trim_name": "P400 Dynamic SE",
                        "msrp_wan": 471.0,
                        "displacement_cc": 2996,
                        "horsepower": "400 ps",
                        "engine_code": "AJ20P6 (MHEV)",
                        "transmission": "8速手自排",
                        "drivetrain": "4WD 全時四輪驅動",
                        "suspension": "動態氣壓懸吊系統",
                        "powertrain": "油電"
                    }
                ]
            }
        ]
    },
    {
        "brand": "Volvo",
        "model": "EX30",
        "summary": "採用吉利 SEA 浩瀚純電平台打造的 Volvo 新世代都會休旅，雙馬達版本具備 3.6 秒破百驚人性能，140–175 萬級距詢問度極高。",
        "generations": [
            {
                "gen_id": "volvo-ex30-gen1",
                "gen_name": "第 1 代 (Single Motor Extended / Twin Motor Performance)",
                "years": [2024, 2025],
                "depreciation_alert": {
                    "level": "low",
                    "title": "新車定價親民（142–174 萬），一年期準新車市場折讓約 18–25 萬"
                },
                "common_issues": [
                    {
                        "part": "全車功能高度整合於 12.3 吋中控螢幕，早期 OTA 韌體偶發藍牙或 CarPlay 斷線",
                        "mileage_range": "2萬公里以上",
                        "repair_cost_ntd": "回廠執行最新 OTA 軟體升級即可排除"
                    }
                ],
                "year_points": [
                    {"year": 2024, "msrp": 174.9, "dealer": 146.0, "private": 135.0, "book": 140.0},
                    {"year": 2025, "msrp": 174.9, "dealer": 156.0, "private": 145.0, "book": 150.0}
                ],
                "trims": [
                    {
                        "trim_name": "Single Motor Extended Range (單馬達後驅)",
                        "msrp_wan": 142.0,
                        "displacement_cc": 0,
                        "horsepower": "272 ps",
                        "engine_code": "SEA-RWD (69kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "FR 後輪驅動",
                        "suspension": "前麥花臣 / 後五連桿",
                        "powertrain": "純電"
                    },
                    {
                        "trim_name": "Twin Motor Performance (雙馬達四驅)",
                        "msrp_wan": 174.9,
                        "displacement_cc": 0,
                        "horsepower": "428 ps",
                        "engine_code": "SEA-AWD (69kWh)",
                        "transmission": "單速固定齒比",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前麥花臣 / 後五連桿",
                        "powertrain": "純電"
                    }
                ]
            }
        ]
    }
]


def normalize_transmission(raw_trans: str) -> str:
    """標準化變速箱為前端篩選鍵值：'手排' 或 '自排'"""
    if not raw_trans:
        return "自排"
    t = raw_trans.upper()
    if ("手排" in t and "自" not in t) or any(k in t for k in ["5MT", "6MT", "MANUAL"]):
        return "手排"
    return "自排"


def normalize_powertrain(raw_power: str, trim_name: str = "", model_name: str = "") -> str:
    """標準化動力形式為前端篩選鍵值：'純電'、'油電' 或 '燃油'"""
    combined = f"{raw_power} {trim_name} {model_name}".upper()
    ev_keywords = [
        "純電", "電動", "BEV", "EQA", "EQE", "EQB", "EQS", "I4", "IX", "IX1", "EX30",
        "EV6", "IONIQ", "BZ4X", "MODEL 3", "MODEL Y", "N7", "MG4", "TAYCAN"
    ]
    hybrid_keywords = ["油電", "HYBRID", "PHEV", "MHEV", "48V", "12V", "E:HEV", "E-POWER", "輕油電"]

    if any(k in combined for k in ev_keywords) and "油電" not in combined and "HYBRID" not in combined:
        return "純電"
    if any(k in combined for k in hybrid_keywords):
        return "油電"
    return "燃油"


def enrich_model_schema(car_obj: dict, ref_year: int = 2026) -> dict:
    """補齊 renderSmartFinder() 所需全部衍生欄位"""
    car = deepcopy(car_obj)
    full_name = f"{car['brand']} {car['model']}".strip()
    all_t_std = set()
    all_p_std = set()

    for gen in car.get("generations", []):
        yps = gen.get("year_points", [])
        for yp in yps:
            msrp = float(yp.get("msrp", 0) or 0)
            dealer = float(yp.get("dealer", 0) or 0)
            private = float(yp.get("private", 0) or 0)
            book = float(yp.get("book") or round((dealer + private) / 2, 1))
            yp["book"] = book

            if msrp > 0:
                yp["residual_dealer_pct"] = round((dealer / msrp) * 100, 1)
                yp["residual_private_pct"] = round((private / msrp) * 100, 1)
                yp["residual_book_pct"] = round((book / msrp) * 100, 1)
            else:
                yp["residual_dealer_pct"] = 0.0
                yp["residual_private_pct"] = 0.0
                yp["residual_book_pct"] = 0.0

            yp["dealer_private_spread_wan"] = round(dealer - private, 1)
            age = max(1, ref_year - int(yp.get("year", ref_year)))
            yp["avg_annual_depreciation_wan"] = round((msrp - dealer) / age, 2) if msrp > dealer else 0.0

        if yps:
            gen["avg_residual_dealer_pct"] = round(
                sum(float(yp["residual_dealer_pct"]) for yp in yps) / len(yps), 1
            )
        else:
            gen["avg_residual_dealer_pct"] = 0.0

        for trim in gen.get("trims", []):
            t_std = normalize_transmission(trim.get("transmission", ""))
            p_std = normalize_powertrain(
                trim.get("powertrain", ""), trim.get("trim_name", ""), full_name
            )
            trim["transmission_std"] = t_std
            trim["powertrain_std"] = p_std
            all_t_std.add(t_std)
            all_p_std.add(p_std)

    car["filter_transmissions"] = sorted(all_t_std) if all_t_std else ["自排"]
    car["filter_powertrains"] = sorted(all_p_std) if all_p_std else ["燃油"]
    return car


def count_total_year_records(cars_list: list) -> int:
    """計算全庫總年式紀錄筆數（涵蓋各世代 years 陣列或 year_points 聯集）"""
    total = 0
    for car in cars_list:
        for gen in car.get("generations", []):
            years_set = set(gen.get("years", []))
            for yp in gen.get("year_points", []):
                if "year" in yp:
                    years_set.add(yp["year"])
            total += len(years_set)
    return total


def main():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"找不到資料庫檔案：{DB_PATH}")

    shutil.copy2(DB_PATH, BACKUP_PATH)
    print(f"[Backup] 已建立安全備份：{BACKUP_PATH}")

    with DB_PATH.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)

    is_dict_wrapper = isinstance(raw_data, dict)
    if is_dict_wrapper:
        list_key = "cars" if "cars" in raw_data else ("models" if "models" in raw_data else "cars")
        cars_list = raw_data.setdefault(list_key, [])
    else:
        cars_list = raw_data

    existing_keys = {
        (str(c.get("brand", "")).strip().lower(), str(c.get("model", "")).strip().lower())
        for c in cars_list
    }

    added_models = []
    skipped_models = []

    for candidate in NEW_IMPORT_MODELS:
        key = (candidate["brand"].strip().lower(), candidate["model"].strip().lower())
        if key in existing_keys:
            skipped_models.append(f"{candidate['brand']} {candidate['model']}")
            continue

        enriched = enrich_model_schema(candidate)
        cars_list.append(enriched)
        existing_keys.add(key)
        added_models.append(f"{enriched['brand']} {enriched['model']}")

    cars_list.sort(key=lambda c: (str(c.get("brand", "")).lower(), str(c.get("model", "")).lower()))

    total_models = len(cars_list)
    total_year_records = count_total_year_records(cars_list)

    if is_dict_wrapper:
        meta = raw_data.setdefault("meta", {})
        meta["total_models"] = total_models
        meta["total_year_records"] = total_year_records
        meta["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=2)

    print(f"\n[Done] 熱門進口車系擴充完成！")
    print(f"  - 本次新增車系 ({len(added_models)} 款): {', '.join(added_models) if added_models else '無'}")
    if skipped_models:
        print(f"  - 已存在略過 ({len(skipped_models)} 款): {', '.join(skipped_models)}")
    print(f"  - 最新 meta.total_models: {total_models}")
    print(f"  - 最新 meta.total_year_records: {total_year_records}")


if __name__ == "__main__":
    main()
