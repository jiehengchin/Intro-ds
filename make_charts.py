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

# ---- Chart 3: public vs restricted points per 10k (greys: not solutions A/B/C) ----
S = sorted(T, key=lambda t: v(t, "all_per10k"))
fig, ax = plt.subplots(figsize=(7.5, 6.2))
pub = [v(t, "public_per10k") for t in S]
res = [v(t, "restricted_per10k") for t in S]
names = [t["district"] for t in S]
ax.barh(names, pub, color=INK2, label="Public use", height=0.7, edgecolor=SURFACE, linewidth=1.5)
ax.barh(names, res, left=pub, color="#b9b8b2", label="Restricted (mostly private housing estates)", height=0.7,
        edgecolor=SURFACE, linewidth=1.5)
for i, t in enumerate(S):
    ax.text(pub[i] + res[i] + 0.3, i, f"{v(t, 'all_per10k'):.1f}  (HK${v(t, 'median_hh_income_2025') / 1000:.1f}k)",
            va="center", fontsize=8, color=INK2)
ax.set_xlim(0, max(a + b for a, b in zip(pub, res)) * 1.3)
ax.set_xlabel("Collection points per 10,000 residents (label: total, median household income)")
ax.grid(axis="y", visible=False)
ax.legend(loc="lower right", frameon=False, fontsize=8.5)
ax.set_title(f"Chart 3. Public vs restricted points per 10,000 residents (restricted vs income: r = "
             f"{r([v(t, 'restricted_per10k') for t in T], [v(t, 'median_hh_income_2025') for t in T]):+.2f})",
             loc="left", fontsize=11, color=INK)
source(fig, "Source: EPD Waste Less collection points (Sep 2025, 8,856 points); C&SD mid-2025 population and income.")
fig.tight_layout(rect=(0, 0.03, 1, 1))
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
# ---- Chart 5: three solutions compared on common units (small multiples) ----
S5 = list(csv.DictReader(open("output/solutions_comparison.csv")))
labels = ["A. Public-place\nbins", "B. GREEN@\nCOMMUNITY", "C. Smart\nbins"]
panels = [("per10k_hk", "Coverage\n(public points per 10,000 residents)", "{:.2f}"),
          ("district_cv", "Unevenness across districts\n(coefficient of variation)", "{:.2f}"),
          ("r_income", "Equity\n(r with district median income)", "{:+.2f}"),
          ("materials_per_point", "Range\n(materials accepted per point)", "{:.1f}")]
fig, axes = plt.subplots(1, 4, figsize=(10, 3.8))
for ax, (k, title, fmt) in zip(axes, panels):
    vals = [float(s5[k]) for s5 in S5]
    bars = ax.bar(labels, vals, color=C[:3], width=0.6, edgecolor=SURFACE, linewidth=1.5)
    for b_, val in zip(bars, vals):
        ax.annotate(fmt.format(val), (b_.get_x() + b_.get_width() / 2, val), xytext=(0, 3 if val >= 0 else -11),
                    textcoords="offset points", ha="center", fontsize=8.5, color=INK)
    ax.axhline(0, color=INK2, linewidth=0.8)
    ax.set_title(title, fontsize=9.5, color=INK)
    ax.tick_params(axis="x", labelsize=8)
    ax.grid(axis="x", visible=False)
    lo, hi = min(vals + [0]), max(vals + [0])
    ax.set_ylim(lo * 1.25, hi * 1.2 if hi > 0 else 0.1)
fig.suptitle("Chart 5. Three recycling solutions compared on common measures (Hong Kong, 18 districts)",
             x=0.01, ha="left", fontsize=11, color=INK)
source(fig, "Note: each panel has its own unit; compare bars within a panel, not across panels. Equity panel shows correlation coefficients (n = 18); only C's passes our reliability check, and A's and B's mainly reflect district size.\n"
       "Source: EPD Waste Less collection points (Sep 2025; public points only: A = 3,588, B = 491, C = 1,073); C&SD 2025 population and income.")
fig.tight_layout(rect=(0, 0.09, 1, 0.93))
fig.savefig(OUT + "chart5_solutions_compared.png", dpi=200)
print("saved 5 charts to", OUT)
