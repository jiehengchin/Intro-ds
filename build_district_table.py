"""Build output/district_summary_2025.csv from the raw files in data/ and print the stats used in the plan.
Run: python3 -I build_district_table.py   (no extra packages needed)
"""
import csv, json
from collections import Counter
from statistics import mean, median, stdev

D_DIR = "data/"
TYPES = {  # column name -> D1 `legend` value
    "bins_public_place": "Recycling Bins at Public Place",
    "stations_stores": "Recycling Stations/Recycling Stores",
    "spots": "Recycling Spots",
    "smart_bins": "Smart Bin",
    "street_shops": "Street Corner Recycling Shops",
    "ngo": "NGO Collection Points",
}
# EPD Waste Statistics for 2024, Plate 2.6, domestic waste (tpd). Islands = "NT - Outlying Islands" row.
DOM_TPD_2024 = {"Central and Western": 305, "Eastern": 551, "Southern": 190, "Wan Chai": 258, "Kowloon City": 292,
                "Kwun Tong": 433, "Sham Shui Po": 372, "Wong Tai Sin": 269, "Yau Tsim Mong": 486, "Kwai Tsing": 334,
                "North": 423, "Sai Kung": 325, "Sha Tin": 434, "Tai Po": 211, "Tsuen Wan": 232, "Tuen Mun": 453,
                "Yuen Long": 742, "Islands": 194}
# Chan et al. (2024) Table 2: GREEN@COMMUNITY recyclables, Sep 2020-Aug 2021, sum of 9 material columns (kg).
GC_KG_2021 = {"Islands": 457634, "Kwai Tsing": 856193, "Sai Kung": 811202, "Sha Tin": 1116037, "Tai Po": 641340,
              "Tsuen Wan": 255645, "Tuen Mun": 507338, "Yuen Long": 869311, "Kowloon City": 1013430,
              "Kwun Tong": 893244, "Sham Shui Po": 785834, "Wong Tai Sin": 437748, "Yau Tsim Mong": 373914,
              "Central and Western": 513903, "Southern": 223214, "Wan Chai": 333573, "Eastern": 1060606,
              "North": 660356}


def r(a, b):
    ma, mb = mean(a), mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    return num / (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5


def rank(v):
    s = sorted(v)
    return [s.index(x) + (s.count(x) - 1) / 2 for x in v]


def csd(file, sv, year):
    rows = json.load(open(D_DIR + file))["dataSet"]
    return {d["DCDesc"]: d["figure"] for d in rows if d["sv"] == sv and d["period"] == year}


pts = list(csv.DictReader(open(D_DIR + "download_20250918_1654_geotagging_converted.csv", encoding="utf-8-sig")))
name = lambda s: "Central and Western" if s == "Central_Western" else s.replace("_", " ")
pop = {k: v * 1000 for k, v in csd("pop.json", "MYPOPN_LAND", "2025").items()}
pop21 = {k: v * 1000 for k, v in csd("pop.json", "MYPOPN_LAND", "2021").items()}
pop24 = {k: v * 1000 for k, v in csd("pop.json", "MYPOPN_LAND", "2024").items()}
area, dens = csd("pop.json", "LA", "2025"), csd("pop.json", "POPN_D", "2025")
inc = csd("income.json", "MED_DH_INC", "2025")

c = Counter()
for p in pts:
    if not p["legend"]:
        continue  # 2 blank rows excluded
    d, pub = name(p["district_id"]), p["accessibilty_notes"] == "Note: For public use"
    c[d, "all"] += 1
    c[d, "public"] += pub
    c[d, "restricted"] += not pub
    c[d, "private_estate"] += p["legend"].startswith("Private")
    for col, leg in TYPES.items():
        c[d, col] += pub and p["legend"] == leg  # public points only
    c[d, "gc"] += pub and p["legend"] in (TYPES["stations_stores"], TYPES["spots"])

districts = sorted(DOM_TPD_2024)
per10k = lambda d, k: round(c[d, k] / pop[d] * 1e4, 2)
cols = ["all", "public", "restricted", "private_estate", *TYPES, "gc"]
table = []
for d in districts:
    row = {"district": d, "pop_2025": int(pop[d]), "area_km2": area[d], "pop_density_2025": dens[d],
           "median_hh_income_2025": inc[d]}
    row |= {f"{k}_pts": c[d, k] for k in cols}
    row |= {f"{k}_per10k": per10k(d, k) for k in cols}
    row["domestic_kg_pp_day_2024"] = round(DOM_TPD_2024[d] / pop24[d] * 1000, 2)
    row["gc_recyclables_kg_per_resident_2020_21"] = round(GC_KG_2021[d] / pop21[d], 2)
    table.append(row)

with open("output/district_summary_2025.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(table[0]))
    w.writeheader()
    w.writerows(table)

# ---- stats printed for the plan ----
col = lambda k: [row[k] for row in table]
pub, inc_v, dens_v = col("public_per10k"), col("median_hh_income_2025"), col("pop_density_2025")
assert sum(col("all_pts")) == 8856 and sum(col("public_pts")) == 5301  # self-check against the raw counts
print(f"public/10k: mean {mean(pub):.1f} sd {stdev(pub):.1f} median {median(pub):.1f} "
      f"min {min(pub)} ({districts[pub.index(min(pub))]}) max {max(pub)} ({districts[pub.index(max(pub))]})")
print("r(income, density) =", round(r(inc_v, dens_v), 2))
for k in ["public", "restricted", "private_estate", *TYPES, "gc"]:
    v = col(f"{k}_per10k")
    print(f"{k:18s} r_inc {r(v, inc_v):+.2f}  r_dens {r(v, dens_v):+.2f}")
for lab, y in [("dens", dens_v), ("inc", inc_v), ("dom", col("domestic_kg_pp_day_2024"))]:
    loo = [r(pub[:i] + pub[i + 1:], y[:i] + y[i + 1:]) for i in range(18)]
    wc = districts.index("Wan Chai")
    print(f"{lab}: pearson {r(pub, y):+.2f} spearman {r(rank(pub), rank(y)):+.2f} "
          f"LOO {min(loo):+.2f}..{max(loo):+.2f} exWC {loo[wc]:+.2f}")
gcv, rec = col("gc_per10k"), col("gc_recyclables_kg_per_resident_2020_21")
print("recyclables vs gc/10k r =", round(r(rec, gcv), 2))
nobin = [round(p - b, 2) for p, b in zip(pub, col("bins_public_place_per10k"))]
print("public excl. public-place bins: min", min(nobin), districts[nobin.index(min(nobin))],
      "max", max(nobin), districts[nobin.index(max(nobin))])
med = median(gcv)
for d in sorted(districts, key=lambda d: per10k(d, "gc"))[:3]:
    need = med * pop[d] / 1e4 - c[d, "gc"]
    print(f"bottom gc: {d} {per10k(d, 'gc')}/10k ({c[d, 'gc']} pts) -> +{need:.0f} Spots to reach median {med:.2f}")

# ---- Solutions comparison (A, B, C) on common units -> output/solutions_comparison.csv ----
SOL = {"A. Public-place bins": ("bins_public_place",), "B. GREEN@COMMUNITY": ("stations_stores", "spots"),
       "C. Smart bins": ("smart_bins",)}
hk_pop = sum(pop[d] for d in districts)
sol_rows = []
for sol, keys in SOL.items():
    legs = {TYPES[k] for k in keys}
    sel = [p for p in pts if p["accessibilty_notes"] == "Note: For public use" and p["legend"] in legs]
    dens_d = [sum(c[d, k] for k in keys) / pop[d] * 1e4 for d in districts]
    sol_rows.append({
        "solution": sol, "public_points": len(sel),
        "per10k_hk": round(len(sel) / hk_pop * 1e4, 2),
        "district_max_over_min": round(max(dens_d) / min(dens_d), 1),
        "r_income": round(r(dens_d, inc_v), 2),
        "materials_per_point": round(mean(len([w for w in p["waste_type"].split(",") if w.strip()]) for p in sel), 1),
        "food_waste_share": round(sum("Food Waste" in p["waste_type"] for p in sel) / len(sel), 2),
        "district_cv": round(stdev(dens_d) / mean(dens_d), 2),  # SD / mean: unevenness not driven by 2 extremes
        "hours_not_stated_share": round(sum(not p["openhour_en"].strip() for p in sel) / len(sel), 3),
        "open_7am_to_midnight_share": round(sum(p["openhour_en"].startswith("7:00am - 12:00am") for p in sel) / len(sel), 2),
    })
# Literature figures (tonnes, HK$) standardised to common units. Sources in comments.
LIT = {"B. GREEN@COMMUNITY": dict(tonnes_per_year=47500,       # LCQ2 (HKSAR Government, 2026): 2025
                                  cost_hkd=480e6,              # LCQ2: operating cost 2025-26
                                  points_for_tonnage=None),    # None -> divide by D1 public points (Sep 2025)
       "C. Smart bins": dict(tonnes_per_year=55 * 365,         # LegCo paper CB(1)606/2024: ~55 t/day domestic food waste (upper bound)
                             cost_hkd=None, points_for_tonnage=605)}  # same paper: 605 bins, May 2024
for row in sol_rows:
    lit = LIT.get(row["solution"])
    if not lit:
        row |= {"tonnes_per_year": "", "tonnes_per_point": "", "kg_per_resident": "", "hkd_per_tonne": ""}
        continue
    t, n = lit["tonnes_per_year"], lit["points_for_tonnage"] or row["public_points"]
    row |= {"tonnes_per_year": t, "tonnes_per_point": round(t / n), "kg_per_resident": round(t * 1000 / hk_pop, 1),
            "hkd_per_tonne": round(lit["cost_hkd"] / t, -2) if lit["cost_hkd"] else ""}
with open("output/solutions_comparison.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(sol_rows[0]))
    w.writeheader()
    w.writerows(sol_rows)
for row in sol_rows:
    print(row)

# ---- Robustness of the per-type correlations -> output/robustness_by_type.csv ----
import random
inc_xei = csd("income.json", "MED_DH_INC_XEI", "2025")
random.seed(1)


def perm_p(x, y, n=10000):
    """Two-sided permutation p-value for Pearson r (no extra packages)."""
    obs, y2, hits = abs(r(x, y)), list(y), 0
    for _ in range(n):
        random.shuffle(y2)
        hits += abs(r(x, y2)) >= obs
    return (hits + 1) / (n + 1)


TESTS = ["public", "restricted", "private_estate", *TYPES, "gc"]
rob = []
for k in TESTS:
    v = col(f"{k}_per10k")
    v24 = [c[d, k] / pop24[d] * 1e4 for d in districts]
    for lab, y in [("income", inc_v), ("pop_density", dens_v)]:
        loo = [r(v[:i] + v[i + 1:], y[:i] + y[i + 1:]) for i in range(18)]
        rob.append({"type": k, "vs": lab, "pearson": round(r(v, y), 2), "spearman": round(r(rank(v), rank(y)), 2),
                    "loo_min": round(min(loo), 2), "loo_max": round(max(loo), 2),
                    "excl_wan_chai": round(loo[districts.index("Wan Chai")], 2),
                    "pearson_pop2024": round(r(v24, y), 2),
                    "pearson_income_econ_active": round(r(v, [inc_xei[d] for d in districts]), 2) if lab == "income" else "",
                    "perm_p": round(perm_p(v, y), 4)})
bonf = 0.05 / len(rob)
for row in rob:
    row["survives_bonferroni"] = row["perm_p"] < bonf
    row["sign_stable"] = len({x > 0 for x in (row["pearson"], row["spearman"], row["loo_min"], row["loo_max"])}) == 1
with open("output/robustness_by_type.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rob[0]))
    w.writeheader()
    w.writerows(rob)
print(f"robustness: {len(rob)} tests, Bonferroni threshold p < {bonf:.4f}")
for row in rob:
    print(row)

# ---- Why the patterns? District size, land area and public-housing share -> output/explanations.csv ----
import math
# Housing Authority, Report on Population and Households in HA PRH (Sep 2026), Table 1: PRH authorised population.
# "PRH" there includes PRH flats in TPS estates and HOS/BRO/MSS/GSH courts. Wan Chai has none.
PRH_POP_2026 = {"Central and Western": 1900, "Eastern": 90100, "Islands": 83300, "Kowloon City": 69200,
                "Kwai Tsing": 256800, "Kwun Tong": 352700, "North": 89100, "Sai Kung": 70000, "Sha Tin": 189100,
                "Sham Shui Po": 166300, "Southern": 62100, "Tai Po": 53200, "Tsuen Wan": 52800, "Tuen Mun": 160200,
                "Wan Chai": 0, "Wong Tai Sin": 186400, "Yau Tsim Mong": 7100, "Yuen Long": 176000}
assert abs(sum(PRH_POP_2026.values()) - 2066200) <= 1000  # report total; district figures rounded to nearest 100


def partial(x, y, z):
    """Correlation of x and y holding z fixed (first-order partial correlation)."""
    rxy, rxz, ryz = r(x, y), r(x, z), r(y, z)
    return (rxy - rxz * ryz) / math.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))


prh = [PRH_POP_2026[d] / pop[d] for d in districts]       # public-housing share of residents (2026 / 2025)
logpop = [math.log(pop[d]) for d in districts]
inv_pop = [1 / pop[d] for d in districts]
areas = [area[d] for d in districts]
expl = []
for k in ["public", "restricted", "bins_public_place", "spots", "stations_stores", "smart_bins", "gc"]:
    v = col(f"{k}_per10k")
    raw = [c[d, k] for d in districts]
    expl.append({"type": k,
                 "r_income": round(r(v, inc_v), 2), "r_prh_share": round(r(v, prh), 2),
                 "r_log_pop": round(r(v, logpop), 2), "r_one_over_pop": round(r(v, inv_pop), 2),
                 "partial_income_given_logpop": round(partial(v, inc_v, logpop), 2),
                 "partial_logpop_given_income": round(partial(v, logpop, inc_v), 2),
                 "partial_income_given_prh": round(partial(v, inc_v, prh), 2),
                 "partial_prh_given_income": round(partial(v, prh, inc_v), 2),
                 "r_pop_density": round(r(v, dens_v), 2),
                 "partial_density_given_logpop": round(partial(v, dens_v, logpop), 2),
                 "raw_count_r_pop": round(r(raw, [pop[d] for d in districts]), 2),
                 "raw_count_r_area": round(r(raw, areas), 2)})
with open("output/explanations.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(expl[0]))
    w.writeheader()
    w.writerows(expl)
print("income vs PRH share r =", round(r(inc_v, prh), 2), "| income vs log pop r =", round(r(inc_v, logpop), 2))
print("PRH share:", {d: round(x, 2) for d, x in sorted(zip(districts, prh), key=lambda t: -t[1])})
for row in expl:
    print(row)
print("perm p: smart bins vs PRH share =", round(perm_p(col("smart_bins_per10k"), prh), 4),
      "| public vs log pop =", round(perm_p(col("public_per10k"), logpop), 4),
      "| GC vs 1/pop =", round(perm_p(col("gc_per10k"), inv_pop), 4))

# ---- Housing mix from the 2021 Population Census (public rental, subsidised ownership, PRIVATE) ----
# C&SD 2021 Population Census, statistics by District Council district (data/census2021/DC_21C.CSV),
# columns pop_pub / pop_s / pop_pri = population living in each type of housing.
cen = list(csv.reader(open(D_DIR + "census2021/DC_21C.CSV", encoding="utf-8-sig")))
key = cen[4]
num = lambda x: float(x) if x.replace(".", "", 1).isdigit() else 0.0
share = {}
for row_ in cen[5:]:
    if row_[2].strip() in districts:
        t = num(row_[key.index("t_pop")])
        share[row_[2].strip()] = {k: num(row_[key.index(f"pop_{k}")]) / t for k in ("pub", "s", "pri")}
assert len(share) == 18
c_pub = [share[d]["pub"] for d in districts]
c_sub = [share[d]["s"] for d in districts]
c_pri = [share[d]["pri"] for d in districts]
print("census vs HA public-rental share r =", round(r(c_pub, prh), 2),
      "| income vs private share r =", round(r(inc_v, c_pri), 2), "| income vs census PRH share r =", round(r(inc_v, c_pub), 2))
hous = []
for k in ["public", "restricted", "private_estate", "bins_public_place", "spots", "stations_stores", "smart_bins", "gc"]:
    v = col(f"{k}_per10k")
    hous.append({"type": k, "r_income": round(r(v, inc_v), 2),
                 "r_private_share": round(r(v, c_pri), 2), "r_public_rental_share": round(r(v, c_pub), 2),
                 "r_subsidised_share": round(r(v, c_sub), 2),
                 "partial_income_given_private": round(partial(v, inc_v, c_pri), 2),
                 "partial_private_given_income": round(partial(v, c_pri, inc_v), 2),
                 "partial_income_given_public_rental": round(partial(v, inc_v, c_pub), 2),
                 "partial_public_rental_given_income": round(partial(v, c_pub, inc_v), 2),
                 "perm_p_private": round(perm_p(v, c_pri), 4), "perm_p_public_rental": round(perm_p(v, c_pub), 4)})
with open("output/housing_mix.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(hous[0]))
    w.writeheader()
    w.writerows(hous)
for row_ in hous:
    print(row_)
