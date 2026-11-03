# Who Gets a Recycling Point? Comparing Collection-Point Types Across Hong Kong's 18 Districts

**Course:** DSC1001/GE1356 Introduction to Data Science | **Group:** XX | **Option:** 2 (Analyse Data Solutions)

> **Sections 5–9 match `GE1356 Report Draft.md`; sections 3–4 here are more detailed working notes.**
>
> Legend: **[TODO]** = still to do; **[VERIFY]** = check against the cited source before submission. Figures marked ✅ were recomputed from the raw files in `data/` on 3 Nov 2026.

---

## 1. Abstract

*(~150 words, written last.)* Problem → data → method → key finding → recommendation.

## 2. Introduction

### 2.1 Background
- In 2024 Hong Kong landfilled 10,510 tonnes of municipal solid waste (MSW) per day, or 1.40 kg/person/day ✅ (EPD 2025b, §1 and Plate 2.8).
- By weight, food waste made up 29%, paper 23% and plastics 18% ✅ (EPD 2025b, Plates 2.8 and 2.10).
- The MSW recovery rate was 34% in 2024 ✅. Domestic waste recovery was only 22% ✅ (EPD 2025b, Plate 3.2). The *Waste Blueprint for Hong Kong 2035* targets about 55% ✅ (EEB 2021).
- Households can only recycle where a collection point exists. The government runs several kinds of point: public-place recycling bins, GREEN@COMMUNITY Recycling Stations, Stores and Spots, and smart bins (mostly food waste). Private housing estates add their own points.

### 2.2 Problem Statement
Recycling points may not be spread in line with where people live. If some districts are under-served, the gap matters for meeting the 2035 target and for fairness. This is a hypothesis to test. Our data also shows that the answer depends on **which type of point** you count. Guo et al. (2018) found the same in Hong Kong for 28 other services: a "per-population" measure gave pro-rich results, and a "distance" measure gave pro-poor results.

### 2.3 Research Question
**How evenly does Hong Kong's recycling network reach residents across the 18 districts, and how do its three main solutions compare?**

**Objectives**
1. Measure how evenly public recycling points reach residents in each district (RQ1).
2. Compare three solutions (A public-place bins, B GREEN@COMMUNITY, C smart bins) on common units of **access, equity and range**, plus output and cost where published (RQ2). This compares where and how they reach residents, not how much recycling each achieves, because output data exist only for B.
3. Test whether access is linked to district income and density and **explain why** (district size, land area, housing type) (RQ3), and test the link to waste or recycling (RQ4). The "why" matters for the research question because it shows whether each gap is unfair and how it could be fixed.
4. Recommend where and how access could be improved.

- **RQ1 (spread):** How much does public-use point density per 10,000 residents vary between districts?
- **RQ2 (solutions compared):** How do three solutions compare on common units: **(A) passive public-place bins, (B) the staffed GREEN@COMMUNITY network (Stations, Stores, Spots), (C) smart bins (mostly food waste)**? Measures: coverage, unevenness, equity, materials accepted, opening hours, and, from the literature, tonnes and HK$ per tonne. Private estate points are context, not a solution.
- **RQ3 (equity):** For each type, is density related to district income and population density, and what explains the pattern (district size, land area, public-rental and private housing shares)?
- **RQ4 (partly tested):** Do districts with more points landfill less waste or recycle more? We test it two ways (landfill data, and district recycling volumes from Chan et al. 2024) and report that neither can confirm it (see 5.6).

### 2.4 Why Option 2 fits
We compare existing "solutions" (the collection-point types) on coverage and equity. We use official datasets (allowed under the Option 2 tip: "data.gov.hk") and at least 8 official reports and papers, each contributing an extracted statistic (Section 3.2).

---

## 3. Data

### 3.1 Data Source Requirement
Option 2 (Literature Extraction): at least **8** academic papers or official reports, each with a statistic extracted and standardized. Datasets (D1, D2 and the optional boundary file D4) are listed separately and are **not** counted toward the 8. The report calls the three EPD waste-statistics reports "D3" when they are used as data (sources 1–3 here).

### 3.2 Source Register

**Datasets (not counted toward the 8)**

| # | Source | What we use |
|---|---|---|
| D1 | EPD, [Waste Less – Recyclable Collection Points Data](https://data.gov.hk/en-data/dataset/hk-epd-recycteam-waste-less-recyclable-collection-points-data) ([data dictionary](https://www.epd.gov.hk/datagovhk/psi-Recyclable-dataDictionary-en.pdf)). File `download_20250918_1654_geotagging_converted.csv`, snapshot of 18 Sep 2025, 8,858 rows | District, `legend` (point type), `accessibilty_notes` (public/restricted), materials, opening hours |
| D2 | C&SD Table [110-02001](https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-02001) (`pop.json`) and Table [130-06806](https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-130-06806) (`income.json`) | Mid-year land population, land area, density; median monthly household income (`MED_DH_INC`) |
| D5 | HAD [district boundaries](https://data.gov.hk/en-data/dataset/hk-had-json1-hong-kong-administrative-boundaries) (`hksar_18_district_boundary.json`) | Optional map; not used in the report (dropped from its References) |
| D4 | C&SD [2021 Population Census statistics by District Council district](https://www.census2021.gov.hk/doc/DC_21C.zip) (`data/census2021/DC_21C.CSV`) | Population by type of housing → public-rental, subsidised-ownership and **private** shares per district. Used in 5.5 (Table 5) ✅. HK totals match C&SD's published 29.3% / 15.7% / 52.9%. |
| D4b | Housing Authority, [*Report on Population and Households in HA PRH*](https://www.housingauthority.gov.hk/en/common/pdf/about-us/publications-and-statistics/PopulationReport.pdf) (Sep 2026), `data/refs/ha_prh_population_report.pdf` | Cross-check only: HA public-rental share vs Census public-rental share r = 0.98 ✅ |

**Reports and papers (counted toward the 8)**

| # | Source | Type | Extracted statistic | Status |
|---|---|---|---|---|
| 1 | EPD, *Monitoring of Solid Waste in Hong Kong: Waste Statistics for 2024* (Dec 2025), `msw2024_eng.pdf` | Official report | 10,510 tpd; 1.40 kg/person/day; MSW recovery 34%, domestic 22% (Plate 3.2, 2020–2024 series); district domestic waste (Plate 2.6) | ✅ read |
| 2 | EPD, *… Waste Statistics for 2023*, `msw2023_eng.pdf` | Official report | 10,884 tpd; 1.44 kg; recovery 33%; Plate 2.6 for 2023 | ✅ read |
| 3 | EPD, *… Waste Statistics for 2022*, `msw2022_eng.pdf` | Official report | 1.51 kg; recovery 32% (31% in 2021); Plate 2.6 for 2022 | ✅ read |
| 4 | Environment Bureau (2021). [*Waste Blueprint for Hong Kong 2035*](https://www.eeb.gov.hk/sites/default/files/pdf/waste_blueprint_2035_eng.pdf) | Policy report | Medium-term targets: cut per-capita MSW disposal by 40–45% and raise the recovery rate to about 55% (p. 17). Policy aim: "provide every district with more adequate recycling outlets", and Stores to go especially where "3-nil" buildings are (both p. 8). Baseline 1.47 kg/person/day | ✅ read |
| 5 | Audit Commission (2020), [*Report No. 74, Ch. 8: Provision and management of Community Green Stations*](https://www.aud.gov.hk/pdf_e/e74ch08.pdf) | Official audit report | Policy goal of one station per district (18). By Feb 2020 only 9 (50%) were built, 2 under construction and 7 at planning or site selection; $286.8M approved for 11 projects | ✅ summary read |
| 6 | Zhao, T., Shang, X., Li, L., Li, W., Li, Y., Guan, M., Ding, A., Zhang, J. & Tian, Y. (2025). Measuring walking convenience of Hong Kong resource recycling services: Utilizing a spatially refined model framework of multiple recyclable wastes. *Resources, Conservation and Recycling*, 215, 108153. [doi:10.1016/j.resconrec.2025.108153](https://doi.org/10.1016/j.resconrec.2025.108153) | Academic paper (HK) | Walking Recycling Capability Index (WRCI) at 0.25 km² grid scale. By 2025 nearly 70% of Hong Kong's area has zero or low WRCI. **9 of 18 districts are low-WRCI for paper, plastic and metal** (Fig. 5f; the paper's labels "KTO" and "KTS" are not spelled out, so we do not name them). 35.98% of grid cells cannot recycle glass on foot. Authors call for more facilities in dense Kowloon and Hong Kong Island | ✅ read |
| 7 | Chan, T.H.C., Hui, T.Y. & Chan, J.K.Y. (2024). From trash to treasure: Assessing the effectiveness of the Green@Community recycling network in Hong Kong. *Recycling*, 9(6), 110. [doi:10.3390/recycling9060110](https://doi.org/10.3390/recycling9060110) | Academic paper (HK) | **Table 2: kg of recyclables collected by GREEN@COMMUNITY in each of the 18 districts**, Sep 2020–Aug 2021 (from the stores' Facebook pages); used in 5.6. Phase 1 had 11 Stations, 22 Stores and 100+ Spots. Spots are "pop-up booths ... on a regular weekly schedule" for residents with no facility nearby. Survey (199 valid responses): GREEN$ card holders and Store visitors were more likely to recycle | ✅ read |
| 8 | Ma, F.C., Wong, T.L., Chan, C.N. & Ran, L. (2023). Revising the effectiveness of municipal waste management in Hong Kong. *Frontiers in Environmental Science*, 11. [doi:10.3389/fenvs.2023.1178363](https://doi.org/10.3389/fenvs.2023.1178363) | Academic paper (HK) | Survey, n = 100: 50% disagreed that recycling bins are sufficient (27% strongly) vs 26% who agreed; bin adequacy differs by region (ANOVA F(4,95) = 6.70, p < 0.05), lowest in Kowloon West (1.35 out of 5) | ✅ read |
| 9 | Guo, Y., Chang, S.-S., Chen, M. & Yip, P.S.F. (2018). Do poorer areas have poorer access to services in Hong Kong? A small-area analysis based on multiple spatial accessibility indicators. *Social Indicators Research*, 138(1), 1–21. [doi:10.1007/s11205-017-1658-5](https://doi.org/10.1007/s11205-017-1658-5) | Academic paper (HK) | 28 services across 1,620 neighbourhoods, grouped into poverty quintiles (324 each). The service-to-population ratio gives a "pro-rich" pattern; the road distance to the nearest service gives a "pro-poor" one. The conclusion depends on the indicator | ✅ read |
| 10 | LegCo [LCQ2: Operation of GREEN@COMMUNITY (8 Jul 2026)](https://www.info.gov.hk/gia/general/202607/08/P2026070800357.htm) | Government reply | Network: 12 Stations, 82 Stores, about 600 Spots, 140+ smart recycling bin sets (800+ points). Collected about 27,000 t (2023) → 47,500 t (2025). Operating cost $313M (2023-24) → $480M (2025-26). 50 Stores in public-housing estates since 2023. Plan to run the network **district by district** with one operator each | ✅ read |
| 11 | LegCo Panel on Environmental Affairs, [LC Paper CB(1)606/2024(01)](https://legco.gov.hk/yr2024/english/panels/ea/papers/eafseh20240527cb1-606-1-e.pdf) (27 May 2024), `data/refs/legco_ea_2024-05-27_food_waste.pdf` | Government paper | 605 food-waste smart bins in 171 PRH estates; domestic food waste recycled 1.4 → about 55 t/day; GREEN@COMMUNITY 26,000 t in 2023 (20,300 t in 2022) | ✅ read |
| 12 | EPD press release, [*EPD responds to concerns regarding food waste recycling services*](https://www.info.gov.hk/gia/general/202404/16/P2024041600707.htm) (16 Apr 2024), `data/refs/gov_2024-04-16_release.html` | Government release | About 530 smart bins in about 150 of 213 PRH estates (70%); target 700+ in all estates by Aug 2024 | ✅ read |
| 13 | DiGiacomo, A., Wu, D. W.-L., Lenkic, P., Fraser, B., Zhao, J. & Kingstone, A. (2018). Convenience improves composting and recycling rates in high-density residential buildings. *J. Environmental Planning and Management*, 61(2), 309–331. [doi:10.1080/09640568.2017.1305332](https://doi.org/10.1080/09640568.2017.1305332) | Academic paper (Vancouver) | Randomised field experiments: bins closer → composting +70% and +139%, recycling +147% (containers), +137% (paper) | ✅ full text read |
| 14 | Li, C. J., Zhang, Y., Nouvellet, P., Okoro, J. O., Wang, X. & Harder, M. K. (2020). Distance is a barrier to recycling – or is it? Surprises from a clean test. *Waste Management*, 108, 183–188. [doi:10.1016/j.wasman.2020.04.022](https://doi.org/10.1016/j.wasman.2020.04.022) | Academic paper (Shanghai) | 1,200 households, smart-card logs: distance explains 3% of participation; no effect on frequency among participants | ✅ abstract (Brighton repository) |
| 15 | Yau, Y. (2012). Stakeholder engagement in waste recycling in a high-rise setting. *Sustainable Development*, 20(2), 115–127. [doi:10.1002/sd.468](https://doi.org/10.1002/sd.468) | Academic paper (HK) | 122 private estates: income, age, reward schemes linked to more recyclables; floor-based facilities alone unlikely to raise recycling | ✅ abstract (CityU repository) |

> **Count:** sources 1–15 give 15 sources with an extracted statistic, or 13 if a strict marker counts reports 1–3 as one series. Report Table 1 adds a **standardised value** column for each (tonnes per year, HK$ per tonne, kg per resident, share of districts). 5 of the 7 academic papers are Hong Kong studies; 13–14 (Vancouver, Shanghai) fill the gap on whether access raises recycling. Do not cite any source we have not opened.
>
> **Cross-check D1 against source 10:** LCQ2 lists 12 Stations, 82 Stores, about 600 Spots and 140+ smart recycling bin sets ✅. D1 has 93 Stations/Stores (matches 12 + 82 = 94) but only 398 Spots. The difference is the Sep 2025 snapshot vs growth by mid-2026; say so. D1's 1,443 "Smart Bin" rows are mostly **food-waste** smart bins, not the 140 GREEN@COMMUNITY smart recycling bins.

### 3.3 Data Status
- [x] D1 checked ✅: 8,858 rows, all `cp_state = Accepted`, 18 districts, no missing coordinates. 58 coordinates are shared by 120 rows; 246 addresses repeat. **Decision:** keep all rows. Each row is a separate bin or set of bins, and the EPD lists them separately. State this.
- [x] D2: 2024 **and 2025** mid-year population and income are both in the files. Main analysis uses **2025** (matches the Sep 2025 snapshot); 2024 is the robustness check.
- [x] Sources 1–3: Plates 2.6, 2.7, 2.8 and 3.2 located and checked.
- [x] Sources 4–15 and D4: downloaded to `data/refs/` and read on 3 Nov 2026. Full texts of 14–15 are paywalled (403); details confirmed from university repository records.
- [ ] Appendix A download log (date, URL, file) for every file.
- Derived (not raw): **`output/district_summary_2025.csv`** ✅, built by `build_district_table.py` (one row per district: 2025 population, area, density, income; public, restricted and per-type counts and per-10k rates; 2024 domestic waste per person; 2020–21 GREEN@COMMUNITY recyclables per resident). Type columns count **public** points only. The 2 blank-`legend` rows are excluded, so all points = 8,856. The old `output/district_summary_2024*.csv` files are superseded. Rule: `data/` holds only raw downloads; everything we compute goes in `output/`.
- Solutions table: `output/solutions_comparison.csv` ✅ (also written by `build_district_table.py`).
- Charts: `output/charts/chart1–5*.png` ✅ (Chart 5 = the three solutions compared), drawn by `make_charts.py` from the table above (Chart 4 from Plate 3.2 values). Re-create in Excel if the group prefers; the numbers are the same.

### 3.4 Variables

| Variable | Definition | Source |
|---|---|---|
| Public point density | Points with `accessibilty_notes` = "For public use" ÷ population × 10,000 | D1, D2 |
| Density by type | Same, separately for each `legend` value (table 3.5) | D1, D2 |
| Restricted point density | Points for "residents of the estate only", "residents only", staff, members or tenants | D1, D2 |
| Population density | Land population ÷ land area (persons/km²) | D2 |
| Median household income | `MED_DH_INC`: median monthly household income of **all** domestic households (per the C&SD series code; the economically-active series `_XEI` is separate), HK$, including economically inactive (for example retired) households. Income = total cash income from all jobs plus rent, interest, pensions and government subsidies (C&SD table notes) ✅. HK 2025: $30,000. Districts with many retirees therefore look poorer; the economically-active series (`MED_DH_INC_XEI`, HK $40,000) gives a similar r | D2 |
| Domestic waste per person (RQ4 only) | Plate 2.6 domestic waste (tpd) ÷ population × 1,000 (kg/person/day). EPD: "indicative reference only" | 1–3, D2 |
| Recovery rate (context) | MSW, domestic, and C&I; 2020–2024 | 1 (Plate 3.2) |

### 3.5 Point Types Used (the "solutions")
We use the dataset's own `legend` categories rather than our own groupings.

| Type (`legend`) | All rows | Public | What it is (from D1 fields) |
|---|---|---|---|
| Recycling Bins at Public Place | 3,588 | 3,588 | Bins in parks, playgrounds, sports grounds, beaches, refuse collection points, villages, government buildings and hiking roads |
| Private Collection Points | 3,177 | 0 | Housing estates, malls, companies; restricted |
| Smart Bin | 1,443 | 1,073 | 1,288 of 1,443 accept food waste; 925 of the 1,073 public ones are at estate or court addresses |
| Recycling Spots (GREEN@COMMUNITY) | 398 | 398 | Fixed site, **open about 3 hours once a week** (for example "Saturday 10 am to 1 pm") |
| Recycling Stations/Stores (GREEN@COMMUNITY) | 93 | 93 | Staffed, open most days |
| Street Corner Recycling Shops | 106 | 106 | |
| NGO Collection Points | 51 | 43 | |
| (blank) | 2 | 0 | Excluded |
| **Total** | **8,858** | **5,301** | |

---

## 4. Methodology

### 4.1 Approach
Descriptive statistics, computed in Python (`build_district_table.py`) and reproducible in Excel (COUNTIFS, CORREL). No survey, no model fitting. Unit of analysis: district (n = 18).

### 4.2 Metric

$$\text{Point density}=\frac{\text{points of a given type in the district}}{\text{district population}}\times 10{,}000$$

### 4.3 Steps
1. Filter D1 by `accessibilty_notes` (public vs restricted) and `legend` (type).
2. Count by district; map `district_id` to C&SD names (for example `Central_Western` → "Central and Western").
3. Divide by 2025 population. Repeat with 2024 as a check.
4. For each type, compute mean, median, SD, range, and Pearson *r* with income and with population density.
5. **Evaluation (robustness):** for every *r* in Table 3, report (a) Spearman, (b) leave-one-out range, (c) excluding Wan Chai, (d) 2024 population, (e) alternative income (economically active households), and (f) a permutation p-value (10,000 shuffles) with a Bonferroni correction for 20 tests (p < 0.0025). A result is "reliable" only if its sign holds in all checks **and** it passes the correction. Output: `output/robustness_by_type.csv`.
6. **Explanation:** correlate each density with district population (log and 1 ÷ population), land area, and the public-rental and private shares (D4, 2021 Census), plus partial correlations (income holding size fixed; income holding each housing share fixed). Output: `output/explanations.csv` (uses HA 2026 public-rental shares; smart bins r = 0.94) and `output/housing_mix.csv` (uses Census 2021 shares; smart bins r = 0.96, the figure the report uses).

### 4.4 Bias and Validity Controls
- Official sources only, each cited. Every derived number can be reproduced from the files in `data/`.
- Definitions come from the data provider: "public" = the EPD's own access note; types = the EPD's own `legend`. This limits our room to pick favourable definitions, at the cost of inheriting the EPD's labels.
- We report results that contradict our hypothesis (RQ4) rather than dropping them.
- One cleaning log (Appendix A) so any member can rebuild the table.

### 4.5 Data Ethics
- No personal data. All data is aggregate and published by government.
- **Ecological fallacy:** district correlations say nothing about individual households ("richer people recycle more" is *not* a valid conclusion).
- Equity framing: we describe gaps and do not rank districts as "bad". The denominator (residents) favours districts with large daytime or visitor populations (Wan Chai, Central and Western, Yau Tsim Mong), so we state this.

---

## 5. Analysis and Results

*(Each chart gets: title, axes with units, source, 2–3 sentences of reading, and the statistic behind it. All numbers use 2025 population from `output/district_summary_2025.csv` unless stated.)*

### 5.1 Chart 1: Stacked Bar, Public Points per 10,000 Residents by Type, 18 Districts (sorted) — RQ1
- Total public density ✅: mean 7.9, median 7.3, SD 3.0, range 4.8 (Wong Tai Sin) to 15.2 (Wan Chai), a 3.2× gap. Kwun Tong and Tuen Mun 5.4, Yuen Long 6.2. Ranking mostly reflects district size: public density vs log population r = −0.81 (see 5.5).
- Public-place bins are 68% of all public points ✅ and drive the ranking: 81% of Wan Chai's public points (12.3 of 15.2 per 10k). Some are in Revenue Tower, Immigration Tower and on Tai Tam Reservoir Road and Black's Link (country park). **They do not serve residents at home.**
- Without public-place bins, the range narrows to 1.5 (Sai Kung) to 3.6 (Islands) per 10k ✅, and Kwai Tsing, Kwun Tong and Wong Tai Sin move from the bottom half into the top half.

### 5.2 Chart 2: Paired Scatter, Income vs (a) Public-Place Bins and (b) Public Smart Bins per 10k — RQ3, the headline
Correlation with median household income and population density, per 10k residents, 2025 ✅:

| Type | r vs income | r vs pop. density |
|---|---|---|
| All restricted points | **+0.79** | −0.07 |
| Private estate (restricted) | **+0.77** | −0.04 |
| Public-place bins | **+0.55** | **−0.53** |
| Recycling Spots | **+0.53** | −0.21 |
| Stations/Stores | −0.10 | −0.01 |
| Stations/Stores + Spots (GREEN@COMMUNITY) | +0.49 | −0.20 |
| Public smart bins | **−0.67** | +0.23 |
| All public points | +0.49 | −0.48 |

**Reading:** the "pro-rich" pattern in all public points (+0.49) comes from public-place bins and Spots. Stations/Stores show no pattern (consistent with being spread across districts, as policy intends). The newer food-waste smart bins go the other way (−0.67) and are concentrated in public-housing estates. Different types tilt in opposite directions, matching Guo et al. (2018): the conclusion depends on what you count. Caution: the public-place-bin correlation (+0.55) is pulled up by Wan Chai and Central and Western, where many bins serve workers and visitors and the resident denominator is small. **See 5.5: most of these income links are really district size (A, Spots, B) and public rental housing (smart bins, +0.96).**

### 5.3 Chart 3: Stacked Bar, Public vs Restricted Points per 10,000, by District — RQ3
- Restricted (mostly private-estate) density tracks income strongly (r = +0.79 ✅). All points per 10k vs income: r = +0.83 ✅. Central and Western has 21.3 restricted points per 10k; Kwai Tsing has 2.4.
- Reading: richer districts **have** more restricted points, mostly in private housing estates that only their residents can use. This is an association at district level; it may reflect how much private housing a district has rather than income itself (ecological fallacy, 4.5).

### 5.4 Chart 4: Line Chart, Recovery Rate 2020–2024: MSW, Domestic, C&I (EPD 2025b, Plate 3.2) — Context
- MSW recovery: 28%, 31%, 32%, 33%, 34% (2020–2024). Domestic: 19%, 20%, 20%, 21%, 22%. C&I: 40%, 43%, 45%, 46%, 48%. ✅ (checked by eye against Plate 3.2, printed p. 23: green = MSW, blue = domestic, orange = C&I).
- Reading: domestic recovery (the part household collection points affect) is less than half of C&I and rising only about 0.75 points a year (19% → 22% over 4 years). At this rate the 2035 target of about 55% overall is far off.

### 5.5 Evaluation (robustness checks; poster "Evaluation" box)

Mirrors report 5.5 / Table 4 (full results: `output/robustness_by_type.csv`). Main correlations with income:

| Density per 10k | r | Spearman | LOO range | excl. WC | Perm. p | Passes Bonferroni (p < 0.0025)? |
|---|---|---|---|---|---|---|
| All restricted | +0.79 | +0.73 | +0.73 to +0.87 | +0.74 | 0.0005 | Yes |
| Private-estate (restricted) | +0.77 | +0.65 | +0.68 to +0.86 | +0.71 | 0.0006 | Yes |
| Public smart bins (C) | −0.67 | −0.64 | −0.76 to −0.60 | −0.65 | 0.0024 | Yes, just |
| Public-place bins (A) | +0.55 | +0.63 | +0.38 to +0.65 | +0.38 | 0.018 | No |
| Spots | +0.53 | +0.36 | +0.35 to +0.64 | +0.35 | 0.024 | No |
| GREEN@COMMUNITY (B) | +0.49 | +0.27 | +0.29 to +0.59 | +0.29 | 0.039 | No |
| All public | +0.49 | +0.62 | +0.29 to +0.60 | +0.29 | 0.039 | No |

- Every sign holds in all checks, but only 3 of 20 tests are **reliable**: restricted (+0.79), private-estate (+0.77) and smart bins (−0.67). The rest are "moderate and fragile" patterns.
- All public vs population density: −0.48 (p = 0.037; −0.56 without Wan Chai); not reliable after correction. Public vs domestic waste: see 5.6.
- Income and density are themselves correlated (r = −0.38), so with 18 districts we **cannot separate** their effects. **This analysis is exploratory.**

**Why? (report Table 5; `output/explanations.csv`, `output/housing_mix.csv`)** Income is linked to housing mix (+0.72 with private share, −0.71 with public-rental share; 2021 Census) and to district size (−0.54 with log population).

| Density per 10k | r income | income, size fixed | r public-rental | income, pub-rental fixed | r private | income, private fixed | Best explanation |
|---|---|---|---|---|---|---|---|
| All public | +0.49 | +0.11 | −0.42 | +0.30 | +0.47 | +0.25 | District size (+0.87 with 1/pop) |
| Public-place bins (A) | +0.55 | +0.23 | −0.57 | +0.25 | +0.56 | +0.26 | Size; counts follow land area (+0.74) |
| Spots | +0.53 | +0.13 | −0.35 | +0.43 | +0.49 | +0.29 | Size (+0.94 with 1/pop) |
| GREEN@COMMUNITY (B) | +0.49 | +0.04 | −0.29 | +0.42 | +0.44 | +0.28 | Size (+0.92 with 1/pop); 17–39 points per district |
| Smart bins (C) | −0.67 | −0.56 | +0.96 | +0.01 | −0.82 | −0.21 | Public rental housing (perm. p ≈ 0.0001) |
| All restricted | +0.79 | +0.69 | −0.56 | +0.67 | +0.66 | +0.60 | Income, even after private share (private given income only +0.23) |

Restricted: YTM is 89% private but has 4.1 restricted/10k vs C&W 95% private with 21.3. Likely (untested): old tenement buildings without property management rarely run estate recycling; managed, higher-income estates do (cf. Yau 2012).
**Link to the research question (report 5.5):** size gaps = allocation problem → Rec 2 (scale to population); countryside/office bins = measurement problem → Rec 1 (measure by type); housing type decides which solution reaches whom, so older private buildings without management fall in a gap → Rec 3 (target Stores there; Blueprint p. 8 already says Stores should go where "3-nil" buildings are). Example: Yau Tsim Mong, 89% private, smart 0.4/10k, restricted 4.1/10k, only 2 Stations/Stores.
Public-rental share (Census 2021): Kwun Tong 58%, Kwai Tsing 56%, Wong Tai Sin 49% … Wan Chai 4%, C&W 4%, YTM 3%. Private share: Wan Chai 95%, C&W 95%, YTM 89% … Wong Tai Sin 19%.

### 5.6 RQ4: Does Access Relate to Waste and Recycling? (Partly Tested)
- Public density vs domestic waste per person: r = +0.35 (2022), +0.40 (2023), +0.48 (2024) ✅, so the sign is opposite to the hypothesis. Without Wan Chai, r = 0.25–0.29 in each year.
- Why we do not trust it: (1) the EPD says district figures are "indicative reference only" and are estimated from waste-facility intake records (Plate 2.6, note 1). (2) Wan Chai's domestic waste rose from 188 to 258 tpd (+37%) in two years with flat population. (3) Plate 2.6's "NT – Outlying Islands" includes Ma Wan (part of Tsuen Wan district) and Hei Ling Chau, so the Islands row does not match the district. (4) Districts with many workers and visitors (Wan Chai, Yau Tsim Mong) both generate more waste and have more public-place bins.
- **Second test, using recycling instead of waste (Chan et al. 2024, Table 2):** GREEN@COMMUNITY recyclables collected per resident (Sep 2020–Aug 2021 ÷ 2021 population) range from 0.80 kg (Tsuen Wan) to 2.47 kg (Kowloon City, Islands) ✅. Correlation with today's Stations/Stores/Spots per 10k: r = +0.47 (+0.34 without Islands) ✅. With income: r = +0.22; with population density: r = −0.04 ✅. The sign is in the expected direction: more facilities go with more recycling.
- Caveats: the tonnages come from Facebook posts. Table 2 sums to 11.8 million kg, while the paper's text says about 18 million kg. Appendix C has only charts, so the paper does not explain the gap; we use Table 2 as published and state the discrepancy. The volumes are from 2020–21, when the network had about 133 facilities, but our points are from 2025 (about 490). n = 18.
- **Conclusion:** the landfill data cannot show whether access reduces waste. The one district recycling series we found points weakly the expected way but is too old and too rough to confirm it. Show both tests as one small table, not a main chart.

### 5.7 Chart 5: Three Solutions Compared on Common Measures — RQ2
See report section 5.7 and Table 6. A: coverage 4.79 per 10k, unevenness 6.0×, r +0.55, 2.6 materials, output and cost not published. B: 0.65, 5.3×, +0.49, 8.4 materials, 47,500 t (2025), about HK$10,100 per tonne. C: 1.43, 6.4×, −0.67, 1.2 materials (90% food waste), ≤ about 20,000 t per year, cost not published. No solution wins on every measure.

### 5.8 Summary Table (Appendix B in full)
Sorted by public points per 10k. Income = 2025 median monthly household income. Source: `output/district_summary_2025.csv` ✅

| District | Pop. 2025 | Public pts | Public /10k | Public-place bins /10k | Spots /10k | Stations/Stores (count) | Public smart bins /10k | Restricted /10k | Income (HK$) |
|---|---|---|---|---|---|---|---|---|---|
| Wan Chai | 163,000 | 247 | 15.2 | 12.3 | 1.53 | 3 | 0.7 | 13.0 | 43,300 |
| Islands | 198,400 | 289 | 14.6 | 11.0 | 1.41 | 4 | 1.7 | 3.2 | 31,800 |
| Tai Po | 329,900 | 329 | 10.0 | 8.3 | 0.73 | 5 | 0.8 | 4.1 | 30,700 |
| North | 341,600 | 335 | 9.8 | 7.7 | 0.61 | 5 | 1.3 | 3.2 | 26,200 |
| Tsuen Wan | 302,600 | 256 | 8.5 | 6.0 | 0.59 | 4 | 1.5 | 4.3 | 34,200 |
| Southern | 259,500 | 216 | 8.3 | 6.3 | 0.58 | 2 | 1.2 | 8.9 | 36,000 |
| Sai Kung | 504,500 | 406 | 8.1 | 6.6 | 0.42 | 5 | 0.8 | 4.5 | 40,600 |
| Central and Western | 231,900 | 186 | 8.0 | 5.7 | 1.12 | 3 | 0.4 | 21.3 | 45,000 |
| Yau Tsim Mong | 301,600 | 237 | 7.9 | 6.4 | 0.66 | 2 | 0.4 | 4.1 | 30,300 |
| Eastern | 508,000 | 339 | 6.7 | 4.5 | 0.51 | 7 | 1.2 | 4.5 | 33,400 |
| Kwai Tsing | 494,500 | 311 | 6.3 | 2.8 | 0.63 | 8 | 2.5 | 2.4 | 25,700 |
| Yuen Long | 680,500 | 420 | 6.2 | 4.2 | 0.25 | 5 | 1.4 | 3.2 | 30,000 |
| Kowloon City | 427,900 | 246 | 5.8 | 3.8 | 0.47 | 4 | 1.1 | 6.8 | 31,300 |
| Sha Tin | 692,400 | 388 | 5.6 | 3.6 | 0.29 | 6 | 1.6 | 3.9 | 31,800 |
| Sham Shui Po | 437,700 | 241 | 5.5 | 3.2 | 0.43 | 5 | 1.6 | 5.0 | 25,000 |
| Kwun Tong | 669,700 | 364 | 5.4 | 2.4 | 0.37 | 10 | 2.3 | 2.6 | 24,900 |
| Tuen Mun | 548,400 | 296 | 5.4 | 3.4 | 0.35 | 7 | 1.4 | 3.8 | 27,400 |
| Wong Tai Sin | 405,800 | 195 | 4.8 | 2.0 | 0.57 | 8 | 1.9 | 2.5 | 25,600 |

---

## 6. Recommendations

Linked directly to the findings. Each is a proposal, with its assumption stated.

1. **Measure access by type, not by point count.** EPD and district planners should report Station/Store/Spot coverage separately from public-place bins. A bin in an office tower lobby is not household access. This is timely: the government plans to run GREEN@COMMUNITY **district by district** with one operator each (LCQ2, 2026), so a per-district, per-type baseline is directly usable. *(From 5.1)*
2. **Scale GREEN@COMMUNITY to population (each district has a similar 17–39 points, so the most populous are thinnest; 5.5). Add Spots in the districts lowest on Stations/Stores/Spots per 10k: Yuen Long (0.32), Sha Tin (0.38) and Tuen Mun (0.47)** ✅, against a median of 0.70. These are large New Territories towns where per-person GREEN@COMMUNITY coverage is thinnest. Raising them to the median needs about **59 more Spots** (Yuen Long +25, Sha Tin +22, Tuen Mun +12) ✅. That is about 15% of the 398 Spots in D1, and the network already grew to about 600 by 2026 (LCQ2), so this is a feasible scale. The median is an illustrative target, and the recycling gain is unknown (5.6). Each Spot opens only about 3 hours a week, so longer hours are the alternative. Zhao et al. (2025) find 9 of 18 districts low on walking access, which could be cross-checked against this list. *(From 5.1, 5.2, 5.8. Zhao et al. (2025) find 9 of 18 districts low on walking access, which could be cross-checked against this list.)*
3. **Target Recycling Stores at older private housing without management.** Smart bins reach public rental estates and managed private estates have their own bins, but older private buildings without management ("3-nil" buildings) get neither. The Blueprint (p. 8) already says Stores should go where 3-nil buildings are. Start with districts with much private housing but few managed-estate bins, e.g. Yau Tsim Mong (89% private, 2 Stations/Stores). We couldn't count 3-nil buildings directly. *(From 5.5)*
4. **Publish output and cost data for every solution, by district.** Only GREEN@COMMUNITY has published tonnage and cost (about HK$10,100 per tonne in 2025-26, LCQ2). Public-place bins and smart bins have none, and researchers had to rebuild district figures from Facebook posts (Chan et al. 2024). This would allow a cost-effectiveness comparison of A, B and C and a proper test of RQ4. *(From 5.6, 5.7)*


---

## 7. Limitations
- **Counts ignore capacity and opening hours:** a 3-hour weekly Spot counts the same as a 7-day Station.
- **Residents as denominator:** commercial districts (Wan Chai, Central and Western, Yau Tsim Mong) look over-served because points also serve workers and visitors.
- **"Public" is the EPD's label (assumption).** We rely on the EPD's "For public use" label to decide what counts as public access, rather than inventing our own definition. 925 of the 1,073 public smart bins are at housing-estate addresses, and we did not verify on site whether non-residents can reach them. If some are inside residents-only areas, smart-bin coverage (Solution C) is overstated, and the −0.67 result shows where bins are placed rather than who can use them.
- **Snapshot:** D1 is one day (18 Sep 2025). The network grew afterwards (about 600 Spots by July 2026 vs 398 in D1; LCQ2).
- **No distance measure:** we count points per district, not walking distance. Guo et al. (2018) show distance can reverse the conclusion; Zhao et al. (2025) measure walking access directly and find it uneven.
- **Access is not the same as use:** Evidence that nearby points make people recycle more is limited. Ma et al. (2023) report what residents **say** (convenience is their main reason to recycle). Chan et al. (2024) find that people who visited a Recycling Store recycle more, which is an association, not proof. Zhao et al. (2025) measure walking access, not behaviour. Outside HK, a Vancouver randomised experiment found bins closer → recycling +137–147% (DiGiacomo et al. 2018); but in Shanghai distance explained only 3% of participation (Li et al. 2020), and in HK private estates floor-level facilities alone were unlikely to raise recycling without incentives (Yau 2012). Our own test (RQ4) could not confirm the link either. We therefore study access because residents say it matters, not because it is proven to raise recycling.
- **Small n and confounding:** 18 districts; income is linked to size, density and housing mix (public rental and private shares); partial correlations (5.5) help but cannot fully separate them; one district (Wan Chai) moves several results.
- **Uneven solution data:** output and cost are published only for GREEN@COMMUNITY, so the three solutions cannot be compared on cost-effectiveness.
- **Waste data** is indicative and does not match district boundaries exactly (5.6).
- **Year alignment:** points from 2025, population and income from 2025 (2024 as a check), waste from 2022–2024.

## 8. Conclusion
- **RQ1:** Public-use points per 10,000 residents vary 3.2-fold, from 4.8 (Wong Tai Sin) to 15.2 (Wan Chai). But most of that spread comes from public-place bins in parks, offices and on hiking roads, not from facilities near homes.
- **RQ2 (solutions):** No solution is best on every measure. A (public-place bins) has the widest coverage (4.79 per 10k) but takes few materials (2.6) and has no published output or cost. B (GREEN@COMMUNITY) takes the most materials (8.4) and is the only one with published cost (about HK$10,100 per tonne), but has the thinnest coverage (0.65). C (smart bins) reaches public rental estates (+0.96 with public-rental share, hence −0.67 with income) but is about 90% food waste.
- **RQ3 (equity):** Most apparent income patterns are really **district size and housing type** (5.5): coverage is thinnest in the most populous districts; smart bins follow public rental housing (+0.96); public-place bins follow land area. Only restricted estate points still follow income (+0.69 size fixed, +0.60 private share fixed), probably because managed private estates, not old tenements, run their own recycling.
- **RQ4:** Not answerable with current data. The landfill figures give the opposite sign but are indicative and unstable. The one district recycling series (2020–21) points weakly the expected way (r = +0.47).
- What we learned about data: the headline depends on the definition of "access" (Guo et al., 2018).

## 9. Member Responsibilities

| Member | Student ID | Responsibility |
|---|---|---|
| 1 | | Datasets D1, D2, D4, cleaning log |
| 2 | | Reports and papers 1–15, extraction table |
| 3 | | Metrics, type breakdown, summary table |
| 4 | | Charts 1–2 |
| 5 | | Charts 3–4, robustness checks (5.5–5.6) |
| 6 | | Report editing, poster, presentation |

## 10. References
*(Done in the report: APA 7 for sources 1–15 and datasets D1, D2, D4 (Census 2021) and D4b (HA), with access dates.)*

## Appendix
- A. Cleaning and download log
- B. Full 18-district table by type
- C. Calculation notes (formulas used in Excel)

---

### Q&A Preparation (2 minutes; have one-sentence answers ready)
1. *"Wan Chai is top. What are its points?"* → 81% are public-place bins, in parks, on hillside roads like Black's Link and at government offices like Revenue Tower. They serve workers and hikers, but we divide by only 163,000 residents. That's why we split by type.
2. *"Is a Spot equal to a Station?"* → No. Spots open about 3 hours a week. It's a stated limitation, and we report types separately.
3. *"Is r = 0.49 significant?"* → Not after correcting for 20 tests (permutation p = 0.039, threshold 0.0025), and it depends on Wan Chai (0.29 without it). Only the smart-bin (−0.67), restricted-point (+0.79) and private-estate (+0.77) results pass, so we call the rest moderate and fragile.
4. *"Is it really about income?"* → Mostly not. Richer districts are smaller and have little public housing. Holding size fixed, the public-points link with income drops from +0.49 to +0.11. Smart bins follow public rental housing (+0.96), not income. Restricted estate points do follow private housing (+0.66), but income still matters after that (+0.60), probably because managed private estates run their own recycling and old tenement buildings don't.
5. *"Why does the 'why' matter for your question?"* → Because it tells us which gaps are unfair and fixable. Big districts are short-changed by a same-number-per-district rule (fix: scale to population). Wan Chai and Islands only look well served (fix: measure by type). And older private buildings without management fall between smart bins and estate bins (fix: target Stores there, as the Blueprint intends).
6. *"Why are Yuen Long, Sha Tin and Tuen Mun low?"* → Each district got a similar number of GREEN@COMMUNITY points (17–39), so the most populous districts get the fewest per resident (r = +0.92 with 1 ÷ population). It's an allocation issue, not neglect, which is why Recommendation 2 says scale to population.
7. *"Do more points reduce waste?"* → The landfill data gives the opposite sign but is indicative and unstable. District recycling volumes (Chan et al. 2024) point weakly the expected way (r = +0.47) but are from 2020–21. So we draw no firm conclusion.
8. *"How do you know access matters?"* → Residents say it does: in Ma et al. (2023), convenience is their main reason to recycle, and that is why we studied access. But our own test (RQ4) couldn't confirm that more points raise recycling, because district recycling data isn't published. That's one of our recommendations (Rec. 4). Outside Hong Kong, a randomised experiment in Vancouver found that moving bins closer raised recycling by about 140% (DiGiacomo et al. 2018), but a Shanghai study found distance mattered only a little (Li et al. 2020). So access helps, but it isn't the whole story.
9. *"Why residents, not daytime population?"* → Residents are the published official figure; we flag the bias for commercial districts.
10. *"Are those smart bins really public?"* → We used the EPD's official "For public use" definition rather than our own. Most public smart bins are at estate addresses and we did not check access on site, so we list it as a limitation: if some are gated, Solution C's coverage is overstated.
11. *"Which 8 sources?"* → We have 15 (report Table 1); each row has an extracted statistic and a standardised value.
12. *"Who did what?"* → Section 9.

### Submission Checklist
- [ ] ≥ 8 reports or papers in 3.2 with an extracted statistic, all opened and cited in Section 10
- [ ] ≥ 8 pages of body text (Times New Roman 12, single-spaced), excluding cover, references and appendix
- [x] 5 labelled charts, each with units, n and source
- [ ] Delete the report's draft-status box, the three WRITING GUIDE boxes and the *[Insert Chart …]* placeholders
- [x] All ✅ numbers re-run on 2025 population
- [ ] No [TODO] or [VERIFY] left
- [ ] Poster has: title, group number, names and IDs, course, problem and objectives, data sources, method, results charts, evaluation (5.5), limitations, conclusion and impact, references, responsibilities
- [ ] Files named `GroupXX_Report.pdf` and `GroupXX_Poster.pdf`
