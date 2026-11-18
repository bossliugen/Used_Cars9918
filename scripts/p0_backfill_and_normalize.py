import json
import re
import shutil
from copy import deepcopy
from pathlib import Path

DB_PATH = Path("data/cars_db.json")
BACKUP_PATH = Path("data/cars_db.backup.json")

# 別名映射：防範資料庫中 model 命名略有差異（例如 "SX4" vs "SX4 / S-Cross"）
MODEL_ALIASES = {
    "Suzuki SX4": "Suzuki SX4 / S-Cross",
    "Suzuki S-Cross": "Suzuki SX4 / S-Cross",
    "Suzuki SX4 S-Cross": "Suzuki SX4 / S-Cross",
}

# 7 個嚴重缺漏早期世代之台灣真實市場行情、通病與完整工程規格補丁
HISTORICAL_PATCHES = {
    "Kia Sportage": {
        "generations": [
            {
                "gen_id": "sportage-gen3",
                "gen_name": "第 3 代 (SL 總代理太古期)",
                "years": [2011, 2012, 2013, 2014, 2015],
                "depreciation_alert": {
                    "level": "medium",
                    "title": "韓系早期冷門期折舊深，2.0 柴油扭力充沛但需留意 DPF 與四驅耦合器"
                },
                "common_issues": [
                    {
                        "part": "DPF 碳微粒濾清器阻塞 / EGR 閥積碳",
                        "mileage_range": "10萬公里以上",
                        "repair_cost_ntd": "清洗約 4,500 ~ 6,000 元；更換約 25,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2011, "msrp": 108.9, "dealer": 16.5, "private": 12.8, "book": 15.0},
                    {"year": 2015, "msrp": 113.9, "dealer": 24.5, "private": 20.0, "book": 22.5}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 汽油 2WD",
                        "msrp_wan": 108.9,
                        "displacement_cc": 1998,
                        "horsepower": "166 ps",
                        "engine_code": "G4KD",
                        "transmission": "6速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "2.0 CRDi 柴油 4WD",
                        "msrp_wan": 113.9,
                        "displacement_cc": 1995,
                        "horsepower": "184 ps",
                        "engine_code": "D4HA",
                        "transmission": "6速手自排",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "sportage-gen4",
                "gen_name": "第 4 代 (QL 森那美柴油主力期)",
                "years": [2016, 2017, 2018, 2019, 2020, 2021],
                "depreciation_alert": {
                    "level": "low",
                    "title": "2019 小改款後導入 Drive Wise 主動安全與 8AT，中古性價比極高"
                },
                "common_issues": [
                    {
                        "part": "方向機十字接頭異音 / 柴油噴油嘴銅墊片滲漏",
                        "mileage_range": "8萬公里以上",
                        "repair_cost_ntd": "接頭襯套更換約 2,500 元；噴油嘴墊片整理約 5,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2016, "msrp": 103.9, "dealer": 29.8, "private": 25.0, "book": 27.5},
                    {"year": 2019, "msrp": 113.9, "dealer": 44.5, "private": 39.2, "book": 41.5},
                    {"year": 2021, "msrp": 113.9, "dealer": 54.0, "private": 48.0, "book": 50.5}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 CRDi 豪華版",
                        "msrp_wan": 103.9,
                        "displacement_cc": 1995,
                        "horsepower": "185 ps",
                        "engine_code": "D4HA",
                        "transmission": "6速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "2.0 CRDi GT-Line AWD (小改款)",
                        "msrp_wan": 113.9,
                        "displacement_cc": 1995,
                        "horsepower": "185 ps",
                        "engine_code": "D4HA",
                        "transmission": "8速手自排",
                        "drivetrain": "AWD 四輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    "Kia Carnival": {
        "generations": [
            {
                "gen_id": "carnival-gen2",
                "gen_name": "第 2 代 (VQ 2.7汽油 / 2.9柴油)",
                "years": [2006, 2007, 2008, 2009, 2010],
                "depreciation_alert": {
                    "level": "high",
                    "title": "稅金高且車齡逾15年，殘值已觸底（10萬內），僅適合短期載貨或露營改裝"
                },
                "common_issues": [
                    {
                        "part": "電動滑門鋼索斷裂 / 2.9 柴油高壓共軌泵老化",
                        "mileage_range": "12萬公里以上",
                        "repair_cost_ntd": "滑門馬達總成約 8,500 元；油泵整理約 18,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2006, "msrp": 129.8, "dealer": 8.5, "private": 5.8, "book": 7.0},
                    {"year": 2010, "msrp": 135.0, "dealer": 13.5, "private": 10.0, "book": 11.8}
                ],
                "trims": [
                    {
                        "trim_name": "2.7 V6 汽油",
                        "msrp_wan": 129.8,
                        "displacement_cc": 2656,
                        "horsepower": "189 ps",
                        "engine_code": "G6EA",
                        "transmission": "5速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "2.9 CRDi 柴油",
                        "msrp_wan": 135.0,
                        "displacement_cc": 2902,
                        "horsepower": "185 ps",
                        "engine_code": "J3",
                        "transmission": "5速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "carnival-gen3",
                "gen_name": "第 3 代 (YP Grand Carnival 2.2 柴油)",
                "years": [2019, 2020],
                "depreciation_alert": {
                    "level": "low",
                    "title": "正七/八人座大空間，2.2 柴油搭配 8AT 妥善率佳，中古流通極快"
                },
                "common_issues": [
                    {
                        "part": "尿素系統 (SCR) 感知器異常 / 電動尾門撐桿衰退",
                        "mileage_range": "8萬公里以上",
                        "repair_cost_ntd": "尾門撐桿一對約 9,000 元；NOx 感知器約 12,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2019, "msrp": 138.9, "dealer": 64.0, "private": 57.5, "book": 60.5},
                    {"year": 2020, "msrp": 159.9, "dealer": 73.5, "private": 66.5, "book": 69.5}
                ],
                "trims": [
                    {
                        "trim_name": "2.2 CRDi 經典版",
                        "msrp_wan": 138.9,
                        "displacement_cc": 2199,
                        "horsepower": "200 ps",
                        "engine_code": "D4HB",
                        "transmission": "8速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "2.2 CRDi 豪華版",
                        "msrp_wan": 159.9,
                        "displacement_cc": 2199,
                        "horsepower": "200 ps",
                        "engine_code": "D4HB",
                        "transmission": "8速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    "Honda Accord": {
        "generations": [
            {
                "gen_id": "accord-gen6",
                "gen_name": "第 6 代 (K9 國產末代雙A臂)",
                "years": [1998, 1999, 2000, 2001, 2002],
                "depreciation_alert": {
                    "level": "medium",
                    "title": "國產經典雙A臂底盤，中古價 5~8 萬，買車需預留 4AT 變速箱整理預算"
                },
                "common_issues": [
                    {
                        "part": "4AT 自排變速箱打滑頓挫 / 分電盤與主繼電器老化",
                        "mileage_range": "15萬公里以上",
                        "repair_cost_ntd": "變速箱翻修約 18,000 ~ 24,000 元；分電盤總成約 4,500 元"
                    }
                ],
                "year_points": [
                    {"year": 1998, "msrp": 79.9, "dealer": 5.5, "private": 3.5, "book": 4.5},
                    {"year": 2002, "msrp": 84.9, "dealer": 7.8, "private": 5.2, "book": 6.5}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 EX-S",
                        "msrp_wan": 79.9,
                        "displacement_cc": 1997,
                        "horsepower": "150 ps",
                        "engine_code": "F20B",
                        "transmission": "4速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前雙A臂 / 後雙A臂",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "3.0 V6",
                        "msrp_wan": 84.9,
                        "displacement_cc": 2997,
                        "horsepower": "200 ps",
                        "engine_code": "J30A1",
                        "transmission": "4速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前雙A臂 / 後雙A臂",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "accord-gen7",
                "gen_name": "第 7 代 (K11 國產 K20A/K24A 世代)",
                "years": [2003, 2004, 2005, 2006, 2007],
                "depreciation_alert": {
                    "level": "low",
                    "title": "K 系列引擎耐用度極高，2.0 稅金省，10~15 萬內高妥善率代步大型房車"
                },
                "common_issues": [
                    {
                        "part": "動力方向機高壓油管滲油 / 引擎腳老化震動",
                        "mileage_range": "10萬公里以上",
                        "repair_cost_ntd": "方向機油管約 3,500 元；全車引擎腳正廠件約 9,500 元"
                    }
                ],
                "year_points": [
                    {"year": 2003, "msrp": 82.9, "dealer": 9.5, "private": 6.8, "book": 8.0},
                    {"year": 2007, "msrp": 89.9, "dealer": 14.5, "private": 11.0, "book": 12.8}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 EX-S",
                        "msrp_wan": 82.9,
                        "displacement_cc": 1998,
                        "horsepower": "150 ps",
                        "engine_code": "K20A",
                        "transmission": "5速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前雙A臂 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "3.0 V6",
                        "msrp_wan": 89.9,
                        "displacement_cc": 2997,
                        "horsepower": "240 ps",
                        "engine_code": "J30A4",
                        "transmission": "5速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前雙A臂 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "accord-gen8",
                "gen_name": "第 8 代 (K13 國產末代大型旗艦)",
                "years": [2008, 2009, 2010, 2011, 2012],
                "depreciation_alert": {
                    "level": "low",
                    "title": "車格放大且 5AT 結構單純，2.4 動力充沛，20萬內高質感房車首選"
                },
                "common_issues": [
                    {
                        "part": "冷氣壓縮機離合器間隙過大 / VTC 執行器冷啟動異音",
                        "mileage_range": "10萬公里以上",
                        "repair_cost_ntd": "壓縮機離合器組約 4,500 元；VTC 齒輪更換約 6,500 元"
                    }
                ],
                "year_points": [
                    {"year": 2008, "msrp": 92.9, "dealer": 16.5, "private": 13.0, "book": 14.8},
                    {"year": 2012, "msrp": 103.9, "dealer": 24.5, "private": 20.5, "book": 22.5}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 VTi",
                        "msrp_wan": 92.9,
                        "displacement_cc": 1997,
                        "horsepower": "156 ps",
                        "engine_code": "R20A3",
                        "transmission": "5速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前雙A臂 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "2.4 VTi-S",
                        "msrp_wan": 103.9,
                        "displacement_cc": 2354,
                        "horsepower": "180 ps",
                        "engine_code": "K24Z2",
                        "transmission": "5速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前雙A臂 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    "Suzuki SX4 / S-Cross": {
        "generations": [
            {
                "gen_id": "sx4-gen1",
                "gen_name": "第 1 代 (GY/RW 日本原裝 1.6 掀背/房車)",
                "years": [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013],
                "depreciation_alert": {
                    "level": "low",
                    "title": "M16A 引擎 + 傳統 4AT 極度耐操，10~18 萬練車與代步神車"
                },
                "common_issues": [
                    {
                        "part": "觸媒轉換器效率衰退 (亮 P0420) / 方向機惰桿間隙",
                        "mileage_range": "10萬公里以上",
                        "repair_cost_ntd": "副廠觸媒約 7,500 元；惰桿和尚頭整理約 3,500 元"
                    }
                ],
                "year_points": [
                    {"year": 2007, "msrp": 63.8, "dealer": 10.5, "private": 7.8, "book": 9.2},
                    {"year": 2013, "msrp": 69.8, "dealer": 18.5, "private": 15.0, "book": 16.8}
                ],
                "trims": [
                    {
                        "trim_name": "1.6 5D 掀背版",
                        "msrp_wan": 63.8,
                        "displacement_cc": 1586,
                        "horsepower": "107 ps",
                        "engine_code": "M16A",
                        "transmission": "4速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "1.6 4D 房車版",
                        "msrp_wan": 69.8,
                        "displacement_cc": 1586,
                        "horsepower": "107 ps",
                        "engine_code": "M16A",
                        "transmission": "4速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "powertrain": "燃油"
                    }
                ]
            },
            {
                "gen_id": "sx4-gen2",
                "gen_name": "第 2 代 (JY SX4 Crossover 匈牙利進口)",
                "years": [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
                "depreciation_alert": {
                    "level": "low",
                    "title": "2017 小改款換裝 1.4T 渦輪 + 6AT，徹底解決前期 CVT 疑慮，保值性大增"
                },
                "common_issues": [
                    {
                        "part": "2014-2016 前期 1.6 CVT 變速箱鋼帶磨損 / 全景天窗遮陽簾脫軌",
                        "mileage_range": "9萬公里以上",
                        "repair_cost_ntd": "CVT 翻修約 32,000 ~ 40,000 元；遮陽簾總成約 8,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2014, "msrp": 78.5, "dealer": 21.0, "private": 17.2, "book": 19.0},
                    {"year": 2018, "msrp": 85.8, "dealer": 34.5, "private": 30.0, "book": 32.0},
                    {"year": 2021, "msrp": 89.0, "dealer": 45.0, "private": 39.8, "book": 42.0}
                ],
                "trims": [
                    {
                        "trim_name": "1.6 GLX (前期自然進氣)",
                        "msrp_wan": 78.5,
                        "displacement_cc": 1586,
                        "horsepower": "120 ps",
                        "engine_code": "M16A",
                        "transmission": "CVT無段變速",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "1.4 Boosterjet (小改款渦輪)",
                        "msrp_wan": 85.8,
                        "displacement_cc": 1373,
                        "horsepower": "140 ps",
                        "engine_code": "K14C",
                        "transmission": "6速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後扭力樑",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    "Volvo V40": {
        "generations": [
            {
                "gen_id": "v40-gen1-pre",
                "gen_name": "第 1 代前期 (13-15年式 Powershift 雙離合器 / 早期 Drive-E)",
                "years": [2013, 2014, 2015],
                "depreciation_alert": {
                    "level": "high",
                    "title": "2013-2014 T4 搭載 Powershift 雙離合器變速箱，與 2015 後愛信 8AT 存在明顯價差斷層"
                },
                "common_issues": [
                    {
                        "part": "Powershift 變速箱閥體與離合器片頓挫 / 早期 Drive-E 引擎吃機油",
                        "mileage_range": "8萬公里以上",
                        "repair_cost_ntd": "變速箱閥體與離合器整理約 35,000 ~ 50,000 元"
                    }
                ],
                "year_points": [
                    {"year": 2013, "msrp": 129.9, "dealer": 24.5, "private": 19.5, "book": 22.0},
                    {"year": 2015, "msrp": 135.0, "dealer": 32.0, "private": 26.8, "book": 29.5}
                ],
                "trims": [
                    {
                        "trim_name": "T4 豪華版 / 旗艦版",
                        "msrp_wan": 129.9,
                        "displacement_cc": 1596,
                        "horsepower": "180 ps",
                        "engine_code": "B4164T",
                        "transmission": "6速雙離合器自手排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "D4 豪華版 / R-Design",
                        "msrp_wan": 135.0,
                        "displacement_cc": 1969,
                        "horsepower": "190 ps",
                        "engine_code": "D4204T14",
                        "transmission": "8速手自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後多連桿",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    "Toyota Tercel": {
        "generations": [
            {
                "gen_id": "tercel-gen5-pre",
                "gen_name": "第 5 代前期 (AL50 國產 1.3 / 1.5 初期)",
                "years": [1995, 1996, 1997, 1998, 1999],
                "depreciation_alert": {
                    "level": "low",
                    "title": "台灣經典耐操神車，4~6 萬現金代步價，零件隨處可得"
                },
                "common_issues": [
                    {
                        "part": "分電盤漏油與高壓線老化 / 水箱上下塑膠水室裂化",
                        "mileage_range": "15萬公里以上",
                        "repair_cost_ntd": "分電盤油封與整理約 2,500 元；水箱更換約 3,200 元"
                    }
                ],
                "year_points": [
                    {"year": 1996, "msrp": 43.9, "dealer": 4.8, "private": 3.0, "book": 3.8},
                    {"year": 1999, "msrp": 46.5, "dealer": 6.2, "private": 4.2, "book": 5.2}
                ],
                "trims": [
                    {
                        "trim_name": "1.3 GL",
                        "msrp_wan": 43.9,
                        "displacement_cc": 1295,
                        "horsepower": "72 ps",
                        "engine_code": "2E",
                        "transmission": "3速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後拖曳臂",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "1.5 CL / XE",
                        "msrp_wan": 46.5,
                        "displacement_cc": 1497,
                        "horsepower": "94 ps",
                        "engine_code": "5E-FE",
                        "transmission": "4速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後拖曳臂",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    },
    "Nissan Cefiro": {
        "generations": [
            {
                "gen_id": "cefiro-a32",
                "gen_name": "第 2 代 (A32 國產 VQ20 / VQ30 百萬名車經典期)",
                "years": [1996, 1997, 1998, 1999],
                "depreciation_alert": {
                    "level": "medium",
                    "title": "VQ 引擎極度平順安靜，但 2.0 拖重車身油耗偏高，中古行情 5~8 萬"
                },
                "common_issues": [
                    {
                        "part": "考耳 (點火線圈) 單缸失火 / 惰速馬達積碳導致熄火",
                        "mileage_range": "12萬公里以上",
                        "repair_cost_ntd": "6 支考耳全換約 6,000 元；惰速馬達更換約 4,500 元"
                    }
                ],
                "year_points": [
                    {"year": 1996, "msrp": 86.9, "dealer": 5.5, "private": 3.5, "book": 4.5},
                    {"year": 1999, "msrp": 92.9, "dealer": 7.5, "private": 5.0, "book": 6.2}
                ],
                "trims": [
                    {
                        "trim_name": "2.0 Excimo",
                        "msrp_wan": 86.9,
                        "displacement_cc": 1995,
                        "horsepower": "150 ps",
                        "engine_code": "VQ20DE",
                        "transmission": "4速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後QT懸吊",
                        "powertrain": "燃油"
                    },
                    {
                        "trim_name": "3.0 Brougham VIP",
                        "msrp_wan": 92.9,
                        "displacement_cc": 2988,
                        "horsepower": "220 ps",
                        "engine_code": "VQ30DE",
                        "transmission": "4速自排",
                        "drivetrain": "FF 前輪驅動",
                        "suspension": "前麥花臣 / 後QT懸吊",
                        "powertrain": "燃油"
                    }
                ]
            }
        ]
    }
}


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
        "純電", "電動", "BEV", "EV6", "IONIQ 5", "IONIQ 6", "BZ4X", "IX1", "IX",
        "MODEL 3", "MODEL Y", "MODEL S", "MODEL X", "N7", "MG4", "TAYCAN", "EQA", "EQB", "EQE", "EQS"
    ]
    hybrid_keywords = ["油電", "HYBRID", "PHEV", "MHEV", "48V", "12V", "E:HEV", "E-POWER", "輕油電", "插電"]

    if any(k in combined for k in ev_keywords) and "油電" not in combined and "HYBRID" not in combined:
        return "純電"
    if any(k in combined for k in hybrid_keywords):
        return "油電"
    return "燃油"


def enrich_year_point(yp: dict, ref_year: int = 2026) -> dict:
    """補齊 year_points 前端圖表所需之 book 與各項 residual_*_pct 欄位"""
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
        yp.setdefault("residual_dealer_pct", 0.0)
        yp.setdefault("residual_private_pct", 0.0)
        yp.setdefault("residual_book_pct", 0.0)

    yp["dealer_private_spread_wan"] = round(dealer - private, 1)
    age = max(1, ref_year - int(yp.get("year", ref_year)))
    yp.setdefault("avg_annual_depreciation_wan", round((msrp - dealer) / age, 2) if msrp > dealer else 0.0)
    return yp


def slugify_id(text: str) -> str:
    """為既有世代生成安全唯一識別碼"""
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug or "gen-default"


def enrich_trim(trim: dict, full_model_name: str, fallback_msrp: float = 0.0) -> dict:
    """對齊 js/app.js renderSmartFinder() 所需之完整 trim 欄位"""
    if "trim_name" not in trim or not trim["trim_name"]:
        trim["trim_name"] = trim.pop("name", None) or "標準車型"
    elif "name" in trim:
        trim.pop("name", None)

    trim.setdefault("msrp_wan", fallback_msrp)
    trim.setdefault("displacement_cc", 0)
    trim.setdefault("horsepower", "N/A")
    trim.setdefault("engine_code", "N/A")
    trim.setdefault("transmission", "自排")
    trim.setdefault("drivetrain", "FF 前輪驅動")
    trim.setdefault("suspension", "前麥花臣 / 後多連桿")

    raw_t = str(trim.get("transmission", ""))
    raw_p = str(trim.get("powertrain", "") or trim.get("fuel", ""))
    t_name = str(trim.get("trim_name", ""))

    t_std = normalize_transmission(raw_t)
    p_std = normalize_powertrain(raw_p, t_name, full_model_name)

    trim["powertrain"] = p_std
    trim["transmission_std"] = t_std
    trim["powertrain_std"] = p_std
    return trim


def run_p0_migration():
    if not DB_PATH.exists() and not BACKUP_PATH.exists():
        raise FileNotFoundError(f"找不到資料庫檔案：{DB_PATH}")

    if BACKUP_PATH.exists():
        shutil.copy2(BACKUP_PATH, DB_PATH)
        print(f"[Restore] 已從 {BACKUP_PATH} 還原乾淨底稿後執行修復...")
    else:
        shutil.copy2(DB_PATH, BACKUP_PATH)
        print(f"[Backup] 已建立安全備份：{BACKUP_PATH}")

    with DB_PATH.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)

    is_dict_wrapper = isinstance(raw_data, dict)
    cars_list = raw_data.get("cars") or raw_data.get("models") or [] if is_dict_wrapper else raw_data

    patched_models = []
    total_trims_normalized = 0

    for car in cars_list:
        brand = str(car.get("brand", "")).strip()
        model = str(car.get("model", "")).strip()
        full_name = f"{brand} {model}".strip()
        canonical_key = MODEL_ALIASES.get(full_name, full_name)

        if canonical_key in HISTORICAL_PATCHES:
            patch = HISTORICAL_PATCHES[canonical_key]
            existing_gens = car.get("generations", [])
            existing_gen_names = {g.get("gen_name") for g in existing_gens}
            existing_gen_ids = {g.get("gen_id") for g in existing_gens if g.get("gen_id")}

            added_count = 0
            for new_gen in patch["generations"]:
                if (
                    new_gen["gen_name"] not in existing_gen_names
                    and new_gen["gen_id"] not in existing_gen_ids
                ):
                    existing_gens.append(deepcopy(new_gen))
                    added_count += 1

            existing_gens.sort(key=lambda g: min(g.get("years", [9999])))
            car["generations"] = existing_gens

            all_years = sorted({y for g in existing_gens for y in g.get("years", [])})
            if all_years:
                if "years" in car:
                    car["years"] = all_years
                if "year_min" in car:
                    car["year_min"] = all_years[0]
                if "year_max" in car:
                    car["year_max"] = all_years[-1]

            if added_count > 0:
                patched_models.append((canonical_key, f"{all_years[0]}-{all_years[-1]}", len(all_years)))

        all_t_std = set()
        all_p_std = set()

        for idx, gen in enumerate(car.get("generations", []), start=1):
            if not gen.get("gen_id"):
                gen["gen_id"] = f"{slugify_id(full_name)}-gen{idx}"

            yps = gen.get("year_points", [])
            for yp in yps:
                enrich_year_point(yp)

            if yps:
                avg_res = sum(float(yp.get("residual_dealer_pct", 0)) for yp in yps) / len(yps)
                gen["avg_residual_dealer_pct"] = round(avg_res, 1)
            else:
                gen.setdefault("avg_residual_dealer_pct", 0.0)

            fallback_msrp = float(yps[0].get("msrp", 0)) if yps else 0.0

            if not isinstance(gen.get("trims"), list) or len(gen["trims"]) == 0:
                gen["trims"] = [{"trim_name": "全車系標準編制", "msrp_wan": fallback_msrp}]

            for trim in gen["trims"]:
                enrich_trim(trim, full_name, fallback_msrp)
                all_t_std.add(trim["transmission_std"])
                all_p_std.add(trim["powertrain_std"])
                total_trims_normalized += 1

        if isinstance(car.get("trims"), list):
            for trim in car["trims"]:
                enrich_trim(trim, full_name)
                all_t_std.add(trim["transmission_std"])
                all_p_std.add(trim["powertrain_std"])
                total_trims_normalized += 1

        car["filter_transmissions"] = sorted(all_t_std) if all_t_std else ["自排"]
        car["filter_powertrains"] = sorted(all_p_std) if all_p_std else ["燃油"]

    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=2)

    print(f"\n[Done] P0 修復與前端 Schema 對齊完成！共掃描 {len(cars_list)} 個車系，處理 {total_trims_normalized} 筆規格。")
    print(f"[Patched Models] 成功補齊早期世代之車系（共 {len(patched_models)} / 7 款）：")
    for m_name, span, yr_cnt in patched_models:
        print(f"  - {m_name}: 年份涵蓋擴充至 [{span}]（共 {yr_cnt} 年）")


if __name__ == "__main__":
    run_p0_migration()
