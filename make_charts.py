"""Draw the 5 report charts from output/district_summary_2025.csv into output/charts/.
Run after build_district_table.py:  python3 make_charts.py
"""
import csv, os
from statistics import mean
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "output/charts/"
os.makedirs(OUT, exist_ok=True)
# Validated categorical palette (dataviz reference, light mode), fixed order.
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "font.size": 10, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
})

T = list(csv.DictReader(open("output/district_summary_2025.csv")))
v = lambda t, k: float(t[k])
for t in T:  # self-check: the public types add up to all public points
    parts = sum(v(t, f"{k}_pts") for k in ["bins_public_place", "spots", "stations_stores", "smart_bins", "street_shops", "ngo"])
    assert parts == v(t, "public_pts"), t["district"]


def r(a, b):
    ma, mb = mean(a), mean(b)
    n = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    return n / (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5


def source(fig, text):
    fig.text(0.01, 0.01, text, fontsize=8, color=INK2, ha="left", va="bottom")


# ---- Chart 1: public points per 10k by type, stacked horizontal bars ----
# Stack order = colour order (validated adjacent pairs). Smart bins take slot 3 (aqua) to match Solution C in Chart 5.
types = [("bins_public_place", "Public-place bins"), ("spots", "Recycling Spots"),
         ("smart_bins", "Smart bins (public)"), ("stations_stores", "Recycling Stations/Stores"), ("other", "Other (shops, NGO)")]
for t in T:
    t["other_per10k"] = v(t, "street_shops_per10k") + v(t, "ngo_per10k")
S = sorted(T, key=lambda t: v(t, "public_per10k"))
fig, ax = plt.subplots(figsize=(7.5, 6.2))
left = [0.0] * len(S)
for (k, label), col in zip(types, C):
    vals = [v(t, f"{k}_per10k") for t in S]
    ax.barh([t["district"] for t in S], vals, left=left, color=col, label=label, height=0.7,
            edgecolor=SURFACE, linewidth=1.5)
    left = [a + b for a, b in zip(left, vals)]
for i, t in enumerate(S):
    ax.text(left[i] + 0.15, i, f"{v(t, 'public_per10k'):.1f}", va="center", fontsize=8.5, color=INK)
ax.set_xlabel("Public-use collection points per 10,000 residents")
ax.grid(axis="y", visible=False)
ax.legend(loc="lower right", frameon=False, fontsize=8.5)
ax.set_title("Chart 1. Public-use recycling points per 10,000 residents, by type and district (n = 18)",
             loc="left", fontsize=11, color=INK)
source(fig, "Source: EPD Waste Less collection points (18 Sep 2025, 5,301 public points); C&SD mid-2025 population.")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT + "chart1_public_points_by_type.png", dpi=200)

# ---- Chart 2: income vs public-place bins and vs public smart bins ----
inc = [v(t, "median_hh_income_2025") / 1000 for t in T]
fig, axes = plt.subplots(1, 2, figsize=(8, 3.9), sharex=True)
for ax, (k, label), col in zip(axes, [("bins_public_place", "Public-place bins"), ("smart_bins", "Smart bins (public)")], [C[0], C[2]]):  # A blue, C (smart bins) aqua: same as Charts 1 and 5
    y = [v(t, f"{k}_per10k") for t in T]
    ax.scatter(inc, y, s=36, color=col, edgecolor=SURFACE, linewidth=1.5, zorder=3)
    for t, xi, yi in zip(T, inc, y):  # label only the extremes
        if yi in (max(y), min(y)) or xi in (max(inc), min(inc)):
            off = {"Kwun Tong": (-12, 26), "Wong Tai Sin": (30, -6)}.get(t["district"], (4, 3)) if k == "bins_public_place" else (4, 3)
            ax.annotate(t["district"], (xi, yi), xytext=off, textcoords="offset points", fontsize=7.5, color=INK2,
                        arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.5) if off != (4, 3) else None)
    ax.set_title(f"{label}: r = {r(inc, y):+.2f}", loc="left", fontsize=10, color=INK)
    ax.set_xlabel("Median monthly household income (HK$ '000, 2025)")
    ax.set_ylabel("Points per 10,000 residents")
fig.suptitle("Chart 2. District income vs two types of public recycling point (n = 18)", x=0.01, ha="left", fontsize=11, color=INK)
source(fig, "Note: the high public-place-bin values in Wan Chai and Central and Western partly serve workers and visitors, not residents.\n"
       "Source: EPD Waste Less collection points (Sep 2025); C&SD Table 130-06806 (income) and 110-02001 (population), 2025.")
fig.tight_layout(rect=(0, 0.08, 1, 0.95))
fig.savefig(OUT + "chart2_income_vs_type.png", dpi=200)

# ---- Chart 3: income vs public and vs restricted points per 10k (two scatters, same axes; greys: not solutions A/B/C) ----
inc3 = [v(t, "median_hh_income_2025") / 1000 for t in T]
ymax = max(v(t, "restricted_per10k") for t in T) * 1.12
fig, axes = plt.subplots(1, 2, figsize=(9, 4.4), sharex=True, sharey=True)
LAB3 = {"Central and Western": (-8, -14), "Wan Chai": (6, 2), "Islands": (6, -2), "Southern": (6, 2)}
ONLY_PUBLIC, ONLY_RESTR = {"Islands"}, {"Southern"}
for ax, (k, label, col) in zip(axes, [("public_per10k", "Public-use points", INK2), ("restricted_per10k", "Restricted points (mostly private estates)", "#9b9a94")]):
    y = [v(t, k) for t in T]
    mx, my = mean(inc3), mean(y)
    slope = sum((a_ - mx) * (b_ - my) for a_, b_ in zip(inc3, y)) / sum((a_ - mx) ** 2 for a_ in inc3)
    xs = [min(inc3), max(inc3)]
    ax.plot(xs, [my + slope * (x_ - mx) for x_ in xs], color=INK2, linewidth=1, linestyle="--", zorder=2)
    ax.scatter(inc3, y, s=46, color=col, edgecolor=INK2 if col != INK2 else SURFACE, linewidth=0.8, zorder=3)
    for t, xi, yi in zip(T, inc3, y):
        if t["district"] in LAB3 and not (k == "restricted_per10k" and t["district"] in ONLY_PUBLIC) and not (k == "public_per10k" and t["district"] in ONLY_RESTR):
            ax.annotate(t["district"], (xi, yi), xytext=LAB3[t["district"]], textcoords="offset points", fontsize=8.5, color=INK2)
    ax.set_title(f"{label}: r = {r(inc3, y):+.2f}", loc="left", fontsize=10, color=INK)
    ax.set_xlabel("Median monthly household income (HK$ '000, 2025)")
    ax.set_ylim(0, ymax)
axes[0].set_ylabel("Points per 10,000 residents")
fig.suptitle("Chart 3. District income vs public and restricted recycling points (n = 18)", x=0.01, ha="left", fontsize=11, color=INK)
source(fig, "Dashed line = least-squares trend. Same axes in both panels. Restricted points are limited to estate residents, staff, members or tenants.\n"
       "Source: EPD Waste Less collection points (Sep 2025, 8,856 points); C&SD 2025 population and Table 130-06806 (income).")
fig.tight_layout(rect=(0, 0.08, 1, 0.95))
fig.savefig(OUT + "chart3_public_vs_restricted.png", dpi=200)

# ---- Chart 4: recovery rates 2020-2024 (EPD Waste Statistics for 2024, Plate 3.2, p. 23) ----
years = [2020, 2021, 2022, 2023, 2024]
series = [("Commercial & industrial waste", [40, 43, 45, 46, 48]),
          ("Municipal solid waste (all)", [28, 31, 32, 33, 34]),
          ("Domestic waste", [19, 20, 20, 21, 22])]
fig, ax = plt.subplots(figsize=(7.5, 4.2))
# Not solutions A/B/C, so no A/B/C colours: highlight domestic waste (what household points affect), grey the rest.
STYLE = {"Commercial & industrial waste": ("#a3a29d", "--"), "Municipal solid waste (all)": (INK2, "-"),
         "Domestic waste": ("#6250d6", "-")}  # violet = palette slot 7, unused by Charts 1-3 and 5
for label, ys in series:
    col, ls = STYLE[label]
    ax.plot(years, ys, color=col, linestyle=ls, linewidth=2.6 if label == "Domestic waste" else 1.6,
            marker="o", markersize=5, markeredgecolor=SURFACE, label=label)
    ax.annotate(f"{label} {ys[-1]}%", (years[-1], ys[-1]), xytext=(8, 0), textcoords="offset points",
                va="center", fontsize=8.5, color=INK)
ax.axhline(55, color=INK2, linewidth=1, linestyle="--")
ax.text(2020, 56, "Blueprint 2035 target for MSW: about 55%", fontsize=8.5, color=INK2)
ax.set_xticks(years)
ax.set_xlim(2019.8, 2026.3)
ax.set_ylim(0, 65)
ax.set_ylabel("Recovery rate (%)")
ax.grid(axis="x", visible=False)
ax.legend(loc="lower right", frameon=False, fontsize=8.5)
ax.set_title("Chart 4. Hong Kong waste recovery rates, 2020-2024", loc="left", fontsize=11, color=INK)
source(fig, "Source: EPD, Monitoring of Solid Waste in Hong Kong: Waste Statistics for 2024, Plate 3.2; Waste Blueprint 2035, p. 17.")
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(OUT + "chart4_recovery_rates.png", dpi=200)
# ---- Chart 5: three solutions compared as a scorecard (one row per measure, darker = better) ----
S5 = list(csv.DictReader(open("output/solutions_comparison.csv")))
col5 = lambda k: [float(x[k]) for x in S5]
# (row label, cell texts, numbers used for shading or None, higher is better)
rows5 = [("Coverage", "public points per 10,000 residents", [f"{x:.2f}" for x in col5("per10k_hk")], col5("per10k_hk"), True),
         ("Materials accepted", "kinds per point", [f"{x:.1f}" for x in col5("materials_per_point")], col5("materials_per_point"), True),
         ("Evenness across districts", "lower = more even", [f"{x:.2f}" for x in col5("district_cv")], col5("district_cv"), False),
         ("Opening hours", "", ["Not stated\n(open-air)", "Stores 10-13 h a day;\nSpots 3 h a week", "80% open\n7 am-midnight"], None, True),
         ("Who it reaches", "", ["Parks, offices,\ncountryside", "Thinnest in the\nbiggest districts", "Public rental\nestates"], None, True),
         ("Tonnes collected a year", "", ["Not published", "47,500", "up to 20,000\n(food waste)"], None, True),
         ("Cost per tonne", "", ["Not published", "HK$10,100", "Not published"], None, True)]
fig, ax = plt.subplots(figsize=(11, 4.7))
ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(len(rows5) + 1.1, -0.1)
X0, W = 0.27, 0.243
names5 = ["A. Public-place bins", "B. GREEN@COMMUNITY", "C. Smart bins"]
for j, (nm, col) in enumerate(zip(names5, C[:3])):
    ax.add_patch(plt.Rectangle((X0 + j * W + 0.005, 0.05), W - 0.01, 0.8, color=col))
    ax.text(X0 + j * W + W / 2, 0.45, nm, ha="center", va="center", color="white", fontsize=11, fontweight="bold")
for i, (lab, sub, cells, nums, hib) in enumerate(rows5, start=1):
    ax.text(0.0, i + 0.38, lab, ha="left", va="center", fontsize=14, fontweight="bold", color=INK)
    if sub: ax.text(0.0, i + 0.72, sub, ha="left", va="center", fontsize=10, color=INK2)
    rank = None
    if nums: order = sorted(range(3), key=lambda k: nums[k], reverse=hib); rank = {k: r_ for r_, k in enumerate(order)}
    for j, txt in enumerate(cells):
        x = X0 + j * W + 0.005
        shade = {0: 0.95, 1: 0.55, 2: 0.22}[rank[j]] if rank else None
        grey = txt.startswith("Not published") or txt.startswith("Not stated")
        face = C[j] if shade else ("#ecebe7" if not grey else "#f6f5f2")
        ax.add_patch(plt.Rectangle((x, i + 0.04), W - 0.01, 0.9, color=face, alpha=shade if shade else 1, linewidth=0))
        dark = shade is not None and shade > 0.6
        ax.text(x + (W - 0.01) / 2, i + 0.49, txt, ha="center", va="center", linespacing=1.15,
                fontsize=19 if shade else 11.5, fontweight="bold" if shade else None,
                color="white" if dark else (INK2 if grey else INK), style="italic" if grey else None)
ax.text(0.0, len(rows5) + 1.05, "Darker = better on that measure (rows 1-3). Grey = no published figure. "
        "Compare within a row, not across rows.\nSource: EPD Waste Less collection points (Sep 2025; public points A = 3,588, B = 491, C = 1,073); "
        "C&SD 2025 population; LegCo LCQ2 (2026) and Panel paper (2024). Tonnes and cost are not like-for-like.",
        fontsize=9, color=INK2, va="top")
ax.set_title("Chart 5. Three recycling solutions compared: no single winner", loc="left", fontsize=14, color=INK, pad=6)
fig.tight_layout(); fig.savefig(OUT + "chart5_solutions_compared.png", dpi=200)

# ---- Charts 6-9: also used on the poster (large fonts so they stay legible when shrunk) ----
VIOLET, PINK, MUTED = "#6250d6", "#e87ba4", "#a3a29d"   # palette slots not used by A/B/C
TD = {t["district"]: t for t in T}
D = list(TD)
ABBR = {"Central and Western": "Central & Western"}
for t in T:
    t["no_bins"] = v(t, "public_per10k") - v(t, "bins_public_place_per10k")

# ---- Chart 6: dot plot: each district with and without public-place bins ----
Sd = sorted(T, key=lambda t: v(t, "public_per10k"))
fig, ax = plt.subplots(figsize=(8.5, 6.2))
for i, t in enumerate(Sd):
    hi, lo = v(t, "public_per10k"), t["no_bins"]
    ax.plot([lo, hi], [i, i], color="#cfcec9", linewidth=3, zorder=1, solid_capstyle="round")
    ax.scatter([hi], [i], s=75, color=C[0], zorder=3)
    ax.scatter([lo], [i], s=75, color=VIOLET, zorder=3)
    ax.text(hi + 0.35, i, f"{hi:.1f}", va="center", fontsize=10.5, color=C[0])
    ax.text(lo - 0.35, i, f"{lo:.1f}", va="center", ha="right", fontsize=10.5, color=VIOLET)
ax.set_yticks(range(len(Sd))); ax.set_yticklabels([ABBR.get(t["district"], t["district"]) for t in Sd], fontsize=11.5)
ax.set_xlim(-0.5, 17); ax.set_xlabel("Public-use points per 10,000 residents", fontsize=12)
ax.grid(axis="y", visible=False)
ax.scatter([], [], s=75, color=C[0], label="All public points")
ax.scatter([], [], s=75, color=VIOLET, label="Without public-place bins")
ax.legend(loc="lower right", frameon=False, fontsize=12)
ax.set_title("Chart 6. The gap between districts is mostly public-place bins", loc="left", fontsize=13, color=INK)
source(fig, "Source: EPD Waste Less collection points (Sep 2025); C&SD 2025 population. Sorted by all public points.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(OUT + "chart6_rank_shift.png", dpi=200); plt.close(fig)

# ---- Chart 7: the real drivers (smart bins vs public-rental share; GREEN@COMMUNITY vs population) ----
cen = list(csv.reader(open("data/census2021/DC_21C.CSV", encoding="utf-8-sig")))
ckey = cen[4]
cnum = lambda x: float(x) if x.replace(".", "", 1).isdigit() else 0.0
prh = {r_[2].strip(): cnum(r_[ckey.index("pop_pub")]) / cnum(r_[ckey.index("t_pop")]) for r_ in cen[5:] if r_[2].strip() in TD}
assert len(prh) == 18
fig, axes = plt.subplots(1, 3, figsize=(14, 4.3))
# A: public-place bins vs population density (a stand-in for how much countryside a district has)
x = [v(TD[d], "pop_density_2025") / 1000 for d in D]; y = [v(TD[d], "bins_public_place_per10k") for d in D]
axes[0].scatter(x, y, s=70, color=C[0], edgecolor=SURFACE, zorder=3)
OFFA = {"Wan Chai": (-52, 4), "Islands": (8, 2), "North": (8, 2), "Tai Po": (8, 2), "Kwun Tong": (-58, 8), "Wong Tai Sin": (-30, 8)}
for d, xi, yi in zip(D, x, y):
    if d in OFFA:
        axes[0].annotate(ABBR.get(d, d), (xi, yi), xytext=OFFA[d], textcoords="offset points", fontsize=11, color=INK2)
axes[0].set_xlabel("Population density ('000 per km², 2025)"); axes[0].set_ylabel("Public-place bins per 10,000 residents")
axes[0].set_title(f"A. Bins thin out in dense districts: r = {r(x, y):+.2f}", fontsize=12.5, loc="left", color=INK)
# B: GREEN@COMMUNITY vs district population
x = [v(TD[d], "pop_2025") / 1000 for d in D]; y = [v(TD[d], "gc_per10k") for d in D]
axes[1].scatter(x, y, s=70, color=C[1], edgecolor=SURFACE, zorder=3)
OFF1 = {"Yuen Long": (-82, -5), "Sha Tin": (-62, 8), "Tuen Mun": (-20, 10), "Wan Chai": (8, 4), "Central and Western": (8, 4)}
for d, xi, yi in zip(D, x, y):
    if d in OFF1:
        axes[1].annotate(ABBR.get(d, d), (xi, yi), xytext=OFF1[d], textcoords="offset points", fontsize=11, color=INK2)
axes[1].set_xlabel("District population ('000, 2025)"); axes[1].set_ylabel("GREEN@COMMUNITY per 10,000")
axes[1].set_title("B. Coverage falls as districts grow", fontsize=12.5, loc="left", color=INK)
# C: smart bins vs public-rental share
x = [prh[d] * 100 for d in D]; y = [v(TD[d], "smart_bins_per10k") for d in D]
axes[2].scatter(x, y, s=70, color=C[2], edgecolor=SURFACE, zorder=3)
OFF0 = {"Kwun Tong": (-62, -16), "Kwai Tsing": (-85, -2), "Wong Tai Sin": (-95, 4), "Central and Western": (6, 12), "Yau Tsim Mong": (10, -6)}
for d, xi, yi in zip(D, x, y):
    if d in OFF0:
        axes[2].annotate(ABBR.get(d, d), (xi, yi), xytext=OFF0[d], textcoords="offset points", fontsize=11, color=INK2)
axes[2].set_xlabel("Residents in public rental housing (%, 2021 Census)"); axes[2].set_ylabel("Smart bins per 10,000 residents")
axes[2].set_title(f"C. Smart bins follow housing: r = {r(x, y):+.2f}", fontsize=12.5, loc="left", color=INK)
fig.suptitle("Chart 7. Each public solution follows a different driver (n = 18 districts)", x=0.01, ha="left", fontsize=13, color=INK)
source(fig, "Public points only. Density is only a moderate, fragile link for A (a stand-in for countryside; land area fits better). Restricted private-estate bins follow income instead (Chart 3).")
fig.tight_layout(rect=(0, 0.04, 1, 0.94)); fig.savefig(OUT + "chart7_drivers.png", dpi=200); plt.close(fig)

# ---- Chart 8: correlation with income before and after holding the real driver fixed ----
E = {r_["type"]: r_ for r_ in csv.DictReader(open("output/explanations.csv"))}
H = {r_["type"]: r_ for r_ in csv.DictReader(open("output/housing_mix.csv"))}
rows = [("Public-place bins (A)", float(E["bins_public_place"]["r_income"]), float(E["bins_public_place"]["partial_income_given_logpop"]), C[0], "district size"),
        ("GREEN@COMMUNITY (B)", float(E["gc"]["r_income"]), float(E["gc"]["partial_income_given_logpop"]), C[1], "district size"),
        ("Smart bins (C)", float(E["smart_bins"]["r_income"]), float(H["smart_bins"]["partial_income_given_public_rental"]), C[2], "public-rental share"),
        ("Restricted estate points", float(E["restricted"]["r_income"]), float(E["restricted"]["partial_income_given_logpop"]), INK2, "district size")]
fig, ax = plt.subplots(figsize=(8.5, 4.6))
bw = 0.36
for i, (lab, a_, b_, col, fixed) in enumerate(rows):
    ax.bar(i - bw / 2, a_, bw, color=col, alpha=0.35, edgecolor=col, linewidth=1.5)
    ax.bar(i + bw / 2, b_, bw, color=col)
    for xx, val in ((i - bw / 2, a_), (i + bw / 2, b_)):
        ax.text(xx, val + (0.03 if val >= 0 else -0.03), f"{val:+.2f}", ha="center", va="bottom" if val >= 0 else "top", fontsize=11.5, color=INK)
ax.axhline(0, color=INK2, linewidth=1)
ax.set_xticks(range(len(rows)))
ax.set_xticklabels([f"{r_[0]}\nholding {r_[4]} fixed" for r_ in rows], fontsize=10.5)
ax.set_ylim(-0.85, 1.0); ax.set_ylabel("Correlation (r) with district income", fontsize=11)
ax.grid(axis="x", visible=False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(facecolor="#b9b8b2", label="Raw"), Patch(facecolor=INK2, label="After holding the real driver fixed")],
          loc="upper left", frameon=False, fontsize=11, ncol=2)
ax.set_title("Chart 8. Income patterns shrink once the real driver is held fixed", loc="left", fontsize=13, color=INK, pad=10)
source(fig, "How to read: each pair compares the raw link with income to what is left after removing the overlap with district size (or public-rental share for C).\n"
       "A bar near zero means income adds little once size or housing is accounted for. n = 18 districts; associations, not causes. Source: output/explanations.csv, housing_mix.csv.")
fig.tight_layout(rect=(0, 0.09, 1, 1)); fig.savefig(OUT + "chart8_income_vs_driver.png", dpi=200); plt.close(fig)

# ---- Chart 9: robustness: r with income and its leave-one-district-out range ----
R = [r_ for r_ in csv.DictReader(open("output/robustness_by_type.csv")) if r_["vs"] == "income"]
NAMES = {"public": "All public", "restricted": "Restricted", "private_estate": "Private estate", "bins_public_place": "Public-place bins",
         "stations_stores": "Stations/Stores", "spots": "Spots", "smart_bins": "Smart bins", "street_shops": "Street shops",
         "ngo": "NGO points", "gc": "GREEN@COMMUNITY"}
R.sort(key=lambda r_: float(r_["pearson"]))
fig, ax = plt.subplots(figsize=(8.5, 4.8))
for i, r_ in enumerate(R):
    ok = r_["survives_bonferroni"] == "True"
    col = VIOLET if ok else MUTED
    ax.plot([float(r_["loo_min"]), float(r_["loo_max"])], [i, i], color=col, linewidth=3, zorder=2)
    ax.scatter([float(r_["pearson"])], [i], s=110, color=col, zorder=3)
ax.set_yticks(range(len(R))); ax.set_yticklabels([NAMES[r_["type"]] for r_ in R], fontsize=12)
for lab, r_ in zip(ax.get_yticklabels(), R):
    if r_["survives_bonferroni"] == "True": lab.set_fontweight("bold")
ax.axvline(0, color=INK2, linewidth=1); ax.grid(axis="y", visible=False)
ax.set_xlabel("r with district income (dot) and its leave-one-district-out range (line)", fontsize=11)
ax.text(0.98, 0.04, "violet = reliable (holds up in every check)", transform=ax.transAxes, ha="right", fontsize=11.5, color=VIOLET)
ax.set_title("Chart 9. Only three income patterns are reliable", loc="left", fontsize=13, color=INK)
source(fig, "Source: output/robustness_by_type.csv (Appendix B); n = 18 districts.")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(OUT + "chart9_robustness.png", dpi=200); plt.close(fig)
print("saved 9 charts to", OUT)
