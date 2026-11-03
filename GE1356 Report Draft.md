# Who Gets a Recycling Point? Comparing Collection-Point Types Across Hong Kong's 18 Districts

**DSC1001/GE1356 Introduction to Data Science — Group XX — Option 2: Analyse Data Solutions**

> **Draft status (3 Nov 2026).** Sections 3–7 are drafted from `GE1356 Project Draft v2.md`, `output/district_summary_2025.csv` and `output/charts/`. **Before submission: delete this box, the three WRITING GUIDE boxes and every *[Insert Chart …]* placeholder (replace with the image).** The group should write Sections 1, 2 and 8 in its own words and rewrite anything below it cannot explain in the Q&A. Format: Times New Roman 12, single spacing, at least 8 pages excluding cover, references and appendix.

---

## 1. Abstract

> **WRITING GUIDE: delete this box once the group has written the section.** About 150–200 words, one paragraph, written last. Five sentences, one per move. No citations, charts or new numbers in an abstract.
>
> | # | Move | What to say (facts to use) | Sentence starter |
> |---|---|---|---|
> | 1 | Problem | Hong Kong recycles only 22% of domestic waste against a 2035 target of about 55%; residents say convenience is their main reason to recycle | "Hong Kong's household recycling rate remains far below…" |
> | 2 | Aim and data | Compare three government solutions (public-place bins, GREEN@COMMUNITY, smart bins) across 18 districts, using 5,301 public points from the EPD's open data, C&SD population and income, and 15 official reports and papers | "This study compares three solutions…" |
> | 3 | Method | Points per 10,000 residents; correlation with income; robustness checks; literature figures standardised to tonnes and HK$ per tonne | "We standardised…" |
> | 4 | Findings | 3.2-fold gap between districts, driven mostly by public-place bins; most income patterns are really district size and housing type (smart bins follow public rental housing, r = +0.96; coverage is thinnest in the most populous districts); no solution is best on every measure; the waste link cannot be tested | "Access varies… However…" |
> | 5 | Recommendation | Measure access by type; scale GREEN@COMMUNITY to population (about 59 more Spots for Yuen Long, Sha Tin and Tuen Mun); publish output and cost for every solution | "We recommend…" |

## 2. Introduction

> **WRITING GUIDE: delete this box once the group has written the section.** About 700–900 words (1.5–2 pages), six paragraphs. Every fact below is already checked and cited. Use the citation shown, put it in your own words, and don't add numbers that aren't here.
>
> **Paragraph 1: The waste problem (why it matters).**
> - Facts: 10,510 tonnes of MSW landfilled per day in 2024, or 1.40 kg per person (Environmental Protection Department [EPD], 2025b). Food waste 29%, paper 23%, plastics 18% (EPD, 2025b, Plate 2.8). Disposal per person fell only from 1.51 to 1.40 kg between 2022 and 2024 (EPD, 2023, 2025b). Define MSW (municipal solid waste: household plus commercial and industrial waste) here.
> - Starter: "Every day, Hong Kong sends more than 10,000 tonnes of municipal solid waste to its landfills…"
>
> **Paragraph 2: The recycling gap.**
> - Facts: overall recovery rose from 28% (2020) to 34% (2024), but domestic waste only from 19% to 22%, against 48% for commercial and industrial (C&I) waste (EPD, 2025b, Plate 3.2; "Plate" is the EPD's name for a figure or table). The Blueprint targets about 55% (Environment Bureau, 2021, p. 17), a gap of 21 points. Domestic recovery is rising only about 0.75 points a year.
> - Point to make: households are the weakest link, and residents report that nearby facilities matter (paragraph 3). Our study looks at access, not at whether access raises recycling.
> - Starter: "The gap is widest for households…"
>
> **Paragraph 3: Why access matters (literature).**
> - Facts:
>   - Ma et al. (2023) surveyed 100 residents and report that convenience is the main motivation to recycle; the authors argue that residents tend not to recycle when no bin is nearby. 50% said bins were insufficient. This is what residents **say**, not measured behaviour, so write "residents report" or "the authors argue", not "people recycle more when…".
>   - About 70% of Hong Kong's area has zero or low walking access to recycling (Zhao et al., 2025).
>   - Evidence that closer facilities **raise** recycling: in a Vancouver field experiment, moving bins closer raised recycling by 137–147% (DiGiacomo et al., 2018). But in Shanghai, distance explained only 3% of participation (Li et al., 2020), and in Hong Kong estates incentives mattered alongside facilities (Yau, 2012). So access likely helps, but is not the whole story.
>   - The government aims to "provide every district with more adequate recycling outlets" (Environment Bureau, 2021, p. 8).
>   - Yet by 2020 only 9 of 18 planned district Recycling Stations had been built (Audit Commission, 2020).
> - Starter: "Hong Kong residents say convenience matters…"
>
> **Paragraph 4: The three solutions being compared (Option 2).**
> - Describe A, B and C in one or two sentences each, using Table 2 and Section 4.1:
>   - **A. Public-place bins:** the oldest model, 3,588 public bins.
>   - **B. GREEN@COMMUNITY:** 12 Stations, 82 Stores and about 600 weekly Spots by 2026. Collection rose from 27,000 t (2023) to 47,500 t (2025) (HKSAR Government, 2026).
>   - **C. Smart bins:** mostly food-waste bins in public housing, 605 bins in 171 estates by May 2024 (Environment and Ecology Bureau, 2024).
> - Starter: "Hong Kong currently relies on three main solutions…"
>
> **Paragraph 5: The gap this project fills.**
> - Points:
>   - Official figures report network totals, not how fairly each solution reaches each district.
>   - Guo et al. (2018) showed that in Hong Kong, whether access looks "pro-rich" or "pro-poor" depends on how it is measured.
>   - The government now plans to run GREEN@COMMUNITY district by district (HKSAR Government, 2026), so a district comparison is timely.
> - Starter: "What is missing is a district-level comparison…"
>
> **Paragraph 6: Research question, objectives and roadmap.**
> - State the research question: *How evenly does Hong Kong's recycling network reach residents across the 18 districts, and how do its three main solutions compare?*
> - List RQ1–RQ4 (plan section 2.3): RQ1 spread between districts; RQ2 the three solutions on common measures; RQ3 equity (relation to income and density, and why); RQ4 whether access relates to waste or recycling.
> - List the four objectives (plan section 2.3): (1) measure how evenly public recycling points reach residents in each district; (2) compare the three solutions on common units of **access, equity and range**, plus output and cost where published; (3) test whether access is linked to district income and density, **explain why** (district size, land area, housing type), and test the link to waste or recycling; (4) recommend where and how access could be improved.
> - Say clearly that the solutions are compared on access and equity. Their effectiveness (recycling achieved) cannot be compared, because output data exist for only one of them.
> - Roadmap sentence: "Section 3 describes the data, Section 4 the method, Section 5 the results, followed by recommendations, limitations and conclusions."
> - Note: this is descriptive, exploratory analysis of 18 districts, not a test of cause and effect.

---

## 3. Data

### 3.1 Data sources

This project follows Option 2: we compare three existing recycling solutions (Section 4.1) using official open data and published reports, without collecting primary data. GREEN@COMMUNITY is the government's community recycling network of staffed **Recycling Stations** (large district centres), **Recycling Stores** (smaller shop-front sites) and **Recycling Spots** (street booths open at a fixed weekly time). MSW means municipal solid waste; C&I means commercial and industrial; PRH means public rental housing; LegCo is the Legislative Council, and an "LCQ" is a councillor's question with the government's written reply.

Our core data comes from three official datasets:

- **D1: Environmental Protection Department (EPD) *Waste Less – Recyclable Collection Points* dataset** (EPD, 2025a), downloaded as a snapshot dated 18 September 2025. It lists 8,858 collection points, each with its district, point type, an access note (for example "For public use" or "For residents of the estate only"), the materials accepted and the opening hours.
- **D2: Census and Statistics Department (C&SD) tables 110-02001 and 130-06806** (C&SD, 2026a, 2026b), giving mid-year land population, land area, population density and median monthly household income for each District Council district. We use 2025 figures, the year closest to the D1 snapshot, and 2024 as a check.
- **D3: EPD *Monitoring of Solid Waste in Hong Kong* reports for 2022, 2023 and 2024**, which give district-level domestic waste disposal (Plate 2.6) and territory-wide recovery rates (Plate 3.2).
- **D4: C&SD *2021 Population Census, statistics by District Council district*** (C&SD, 2022): the share of each district's residents living in **public rental housing**, **subsidised home ownership housing** and **private permanent housing**. We use these shares to explain our results (Section 5.5). As a cross-check, the Housing Authority's September 2026 public rental figures (Housing Authority, 2026) give almost the same public-rental shares (*r* = 0.98).

We also extracted a statistic from each of **15** reports and papers and converted it to a common unit (Table 1). Of the seven academic papers, five study Hong Kong; two (from Vancouver and Shanghai) were added because no Hong Kong study measures whether nearer facilities raise recycling. The "Used in" column shows where each feeds the analysis: seven supply numbers used directly in our tables and charts (sources 1–4, 7, 10, 11), and the rest provide benchmarks we compare our results against.

Raw figures from each source were converted to common units where possible: tonnes per year, HK$ per tonne, kg per resident, or share of districts.

**Table 1. Reports and papers used: statistic extracted, standardised value and where it is used**

| # | Source | Statistic extracted | Standardised value | Used in |
|---|---|---|---|---|
| 1–3 | Environmental Protection Department [EPD] (2023, 2024b, 2025b), *Waste Statistics for 2022, 2023, 2024* | Disposal 1.51 → 1.44 → 1.40 kg/person/day; recovery 32% → 33% → 34%; district domestic waste (Plate 2.6) | Disposal −7% in 2 years; recovery +1 point a year | 5.6 test 1; Chart 4 |
| 4 | Environment Bureau (2021), *Waste Blueprint for Hong Kong 2035* | Target recovery rate about 55%; cut per-capita disposal by 40–45% | Gap to target: 21 points (55% vs 34% in 2024) | Chart 4 target line (p. 17); 5.4; 5.5 and Rec. 3 ("3-nil" buildings, p. 8) |
| 5 | Audit Commission (2020), Report No. 74, Ch. 8 | Goal of one Recycling Station per district; 9 of 18 built by February 2020 | 50% of districts had a Station | Benchmark for 5.2 |
| 6 | Zhao et al. (2025) | Walking access index on a 0.25 km² grid | About 70% of area with zero or low walking access; 50% of districts (9 of 18) low | Benchmark for Rec. 2; Limitations |
| 7 | Chan et al. (2024) | Recyclables collected by GREEN@COMMUNITY in each district, Sep 2020–Aug 2021 | 0.80–2.47 kg per resident per year by district | 5.6 test 2 (district data) |
| 8 | Ma et al. (2023) | Survey of 100 residents on recycling bins | 50% say bins are insufficient vs 26% sufficient | Introduction (why access matters) |
| 9 | Guo et al. (2018) | 28 services across 1,620 neighbourhoods | Per-population measures make access look pro-rich; distance measures make it look pro-poor | Benchmark for 5.1–5.2 interpretation |
| 10 | LegCo LCQ2 (8 July 2026) | GREEN@COMMUNITY: about 27,000 t (2023) and 47,500 t (2025) collected; operating cost HK$313M (2023-24) and HK$480M (2025-26) | **HK$11,600 → HK$10,100 per tonne**; 6.3 kg per resident per year; +76% tonnage in 2 years | Table 6; Rec. 1–2 |
| 11 | LegCo Panel paper CB(1)606/2024(01) (27 May 2024) | 605 food-waste smart bins in 171 public-housing estates; domestic food waste recycled rose from 1.4 to about 55 t/day; GREEN@COMMUNITY collected "over 26,000 t" in 2023 (20,300 t in 2022; LCQ2 later gives about 27,000 t for 2023) | At most about 20,000 t/year of domestic food waste, or ≤33 t per smart bin per year (upper bound: the 55 t/day covers all domestic channels) | Table 6 |
| 12 | EPD (2024a), press release (16 April 2024), *EPD responds to concerns regarding food waste recycling services* | About 530 food-waste smart bins in about 150 of 213 public-housing estates (70%); target of 700+ bins in all estates by August 2024 | Combined with source 11: 530 → 605 smart bins in about six weeks (mid-April to late May 2024) | Background to solution C |
| 13 | DiGiacomo et al. (2018) | Two randomised field experiments in high-density residences, Vancouver | Moving bins closer: composting +70% (+27 kg per unit per year) and +139%; recycling +147% (containers) and +137% (paper) | Introduction; Limitations |
| 14 | Li et al. (2020) | Smart-card logs of food-waste deposits, 1,200 households, Shanghai | Distance explained only 3% of the variation in participation; no effect on frequency among participants | Introduction; Limitations |
| 15 | Yau (2012) | Recyclables collected in 122 private high-rise estates, Hong Kong | Income, age and reward schemes were linked to more recycling; floor-based facilities alone unlikely to raise it | Introduction; 5.5; Limitations |

### 3.2 Data cleaning

All raw files were kept unchanged in a `data/` folder. Everything we computed is stored separately in `output/`, so any member can rebuild our results from the original downloads. The cleaning steps were:

1. **Removing unusable rows.** Two of the 8,858 points have no point type and no access note, so we excluded them, leaving 8,856 points. No coordinates were missing and every point fell inside one of the 18 districts.
2. **Duplicates.** 120 rows share 58 sets of coordinates, and 246 addresses appear more than once. We kept these rows because the EPD lists each bin or set of bins separately, for example a paper bin and a plastics bin at the same refuse collection point.
3. **Matching district names.** The dataset's district codes were matched to the C&SD names. Only one needed changing ("Central_Western" to "Central and Western").
4. **Classifying access.** We used the EPD's own access note to separate **public-use** points (5,301) from **restricted** points (3,555), which are limited to estate residents, staff, members, students or tenants.
5. **Classifying type.** We used the EPD's own point-type field rather than inventing categories (Table 2).

**Table 2. Collection points by type and access (D1, September 2025)**

| Point type | All points | Public-use | Description |
|---|---|---|---|
| Recycling Bins at Public Place | 3,588 | 3,588 | Bins in parks, playgrounds, beaches, refuse collection points, villages, government buildings and hiking roads |
| Private Collection Points | 3,177 | 0 | Bins in housing estates, malls and companies, for their own users only |
| Smart Bin | 1,443 | 1,073 | Mostly food-waste bins (1,288 accept food waste); 925 of the public ones are at housing-estate addresses. D1 (Sep 2025) has more than the 605 food-waste smart bins counted in May 2024 because the programme kept growing and D1 also includes other smart bins |
| Recycling Spots (GREEN@COMMUNITY) | 398 | 398 | Fixed street booths, each with one session of about 3 hours a week |
| Recycling Stations/Stores (GREEN@COMMUNITY) | 93 | 93 | Staffed facilities open most days |
| Street Corner Recycling Shops | 106 | 106 | |
| NGO Collection Points | 51 | 43 | |
| **Total** | **8,856** | **5,301** | |

---

## 4. Methodology

### 4.1 Approach and metric

We compare **three solutions** that the government uses to get households recycling: **(A) passive public-place bins**, the oldest model; **(B) the staffed GREEN@COMMUNITY network** of Recycling Stations, Stores and weekly Spots; and **(C) smart bins**, mostly food-waste bins in public-housing estates. Private estate points are run by property managers, not the government, so we treat them as context rather than a solution. We compare the solutions on **access, equity and range**, measured the same way for all three from the dataset. Output and cost are added where published, which is only for B, so this is a comparison of where and how the solutions reach residents, not of how much recycling each achieves.

We used descriptive statistics only. There was no survey and no model fitting. The unit of analysis is the district (n = 18). To compare districts of very different sizes fairly, we standardised every count by population:

> **Point density = (number of points of a given type in the district ÷ district population) × 10,000**

This gives "points per 10,000 residents", which is calculated separately for public points, restricted points and each point type.

### 4.2 Analysis steps

1. Count points in each district by access (public or restricted) and by type.
2. Divide by the 2025 mid-year population (D2).
3. Describe the spread of each density: mean, median, standard deviation and range.
4. Measure how each density relates to two district characteristics, **median monthly household income** and **population density** (persons per km²), using Pearson's correlation coefficient *r*.
5. Test whether access relates to outcomes (RQ4) in two ways: against domestic waste landfilled per person (D3, Plate 2.6), and against GREEN@COMMUNITY recyclables collected per resident (Chan et al., 2024, Table 2).
6. Check the robustness of every correlation (Section 5.5): Spearman rank correlation, leave-one-out, excluding Wan Chai, 2024 population, an alternative income measure, and a permutation p-value with a correction for the number of tests.
7. Compare solutions A, B and C on common units (Section 5.7). From the dataset: coverage per 10,000 residents, unevenness across districts (coefficient of variation: standard deviation ÷ mean of the 18 district densities; and highest ÷ lowest district), equity (r with income), materials accepted per point, and opening hours. From the literature: tonnes collected per year, per point and per resident, and HK$ per tonne, after converting tonnes per day into tonnes per year and total budgets into cost per tonne.
8. Look for explanations (Section 5.5): correlate each density with **district population**, **land area**, and the **public-rental** and **private-housing** shares of residents (D4), and use **partial correlations**, the link between two things that remains after holding a third fixed, to see whether income still matters once size or housing type is taken into account.

The calculations were done in a short Python script (`build_district_table.py`, Appendix A), which also checks its totals against the raw counts and writes every figure in Tables 3–6. The descriptive results can be reproduced in Excel with COUNTIFS, division and CORREL.

### 4.3 Avoiding bias

- **Definitions taken from the data provider.** "Public" and "type" come from the EPD's own fields rather than our own judgement, which limits the room to choose definitions that favour a result. The trade-off is that we inherit the EPD's labels (see Limitations).
- **Official sources only.** Each source is cited, and each extracted figure can be traced to a page or table.
- **Reporting results against our hypothesis.** Our first idea was that more recycling points would mean less waste. The data did not support it, and we report that result rather than dropping it (Section 5.6).
- **Robustness checks** guard against results that depend on a single district, year or chance (Section 5.5).

### 4.4 Data ethics

All data is aggregated and published by the government, and no personal information is involved. Because our analysis is at district level, it cannot say anything about individual households. For example, a correlation between district income and recycling points does not mean that richer *people* recycle more (the ecological fallacy). We also avoid ranking districts as "good" or "bad": a low density may reflect where the government placed facilities, not any failing by residents.

---

## 5. Analysis and Results

### 5.1 How unevenly are public points spread? (RQ1)

*[Insert Chart 1: `output/charts/chart1_public_points_by_type.png`]*

Public-use points per 10,000 residents vary **3.2-fold** across the 18 districts: from **4.8 in Wong Tai Sin to 15.2 in Wan Chai** (mean 7.9, median 7.3, standard deviation 3.0). Populous or dense districts such as Kwun Tong and Tuen Mun (both 5.4), Sham Shui Po (5.5) and Sha Tin (5.6) are near the bottom.

Chart 1 shows that this ranking is driven almost entirely by **public-place bins** (blue), which make up 68% of all public points. In Wan Chai they account for 12.3 of its 15.2 points per 10,000 residents (81%). Their addresses suggest that some are not near homes, for example Revenue Tower and Immigration Tower (government offices) and country-park roads such as Tai Tam Reservoir Road and Black's Link. Islands ranks second for a similar reason: many of its bins are at village refuse points, beaches and country parks.

If public-place bins are removed, the range shrinks to between **1.5 (Sai Kung) and 3.6 (Islands)** points per 10,000. Kwai Tsing, Kwun Tong and Wong Tai Sin then rise into the top half, mainly because they have many smart bins. **So "which district has the best access" depends on which kind of point is counted.** District size also matters: the most populous districts have the lowest public density (r = −0.81 with log population), consistent with facilities not being added in proportion to residents (Section 5.5).

### 5.2 Do different point types favour different districts? (RQ3)

*[Insert Chart 2: `output/charts/chart2_income_vs_type.png`]*

**Table 3. Correlation of point density (per 10,000 residents) with district characteristics, 2025, n = 18**

| Point type | r with median household income | r with population density |
|---|---|---|
| All restricted points | +0.79 | −0.07 |
| Private estate (restricted) | +0.77 | −0.04 |
| Public-place bins | +0.55 | −0.53 |
| Recycling Spots | +0.53 | −0.21 |
| Stations/Stores | −0.10 | −0.01 |
| Stations/Stores + Spots (GREEN@COMMUNITY) | +0.49 | −0.20 |
| Public smart bins | −0.67 | +0.23 |
| All public points | +0.49 | −0.48 |

Chart 2 plots the two types with the strongest opposite patterns. Taken together, public points look "pro-rich": districts with higher median income have more points per resident (r = +0.49), and denser districts have fewer (r = −0.48). Table 3 shows that this overall pattern hides **types that pull in opposite directions**:

- **Public-place bins (+0.55) and Recycling Spots (+0.53)** are denser in richer districts. The public-place-bin result needs caution, because it is pulled up by Wan Chai and Central and Western, where many bins serve office workers and visitors and the resident population is small.
- **Recycling Stations and Stores show no pattern** (−0.10). This is consistent with them being spread across districts, as policy intends; the original plan was one Station in each district (Audit Commission, 2020).
- **Public smart bins are denser in lower-income districts (−0.67)**: Kwai Tsing (2.5 per 10,000), Kwun Tong (2.3) and Wong Tai Sin (1.9) lead, while Central and Western and Yau Tsim Mong have only 0.4. Most are food-waste bins at public housing estates, in line with the government's focus on public rental housing (HKSAR Government, 2026). Section 5.5 shows that public rental housing, not income itself, is the better explanation (*r* = +0.96).

This matches the finding of Guo et al. (2018) for 28 other public services in Hong Kong: whether access looks "pro-rich" or "pro-poor" depends on the indicator chosen. For recycling, it also depends on which *type* of point is counted. Section 5.5 shows that most of these income patterns are better explained by district size and housing type than by income itself.

### 5.3 Public versus restricted points

*[Insert Chart 3: `output/charts/chart3_public_vs_restricted.png`]*

When restricted points are added (Chart 3), the gap between districts widens sharply. Restricted points per 10,000 residents range from **2.4 in Kwai Tsing to 21.3 in Central and Western**, and are closely associated with median household income (**r = +0.79**). For all points combined, the correlation is +0.83. Richer districts therefore *have* many more restricted points, mostly bins in private housing estates that only their residents can use.

This is a district-level association, and it does not show that wealthier households recycle more. Section 5.5 shows that restricted points follow private housing, but that income still matters after allowing for it, probably because higher-income districts have more managed private estates that run their own recycling. It does show that residents of districts with little private housing depend more heavily on the public network.

### 5.4 The territory-wide context

*[Insert Chart 4: `output/charts/chart4_recovery_rates.png`]*

Hong Kong's overall MSW recovery rate rose from 28% in 2020 to 34% in 2024 (Chart 4; EPD, 2025b, Plate 3.2). Domestic waste, the part that household collection points affect, is far lower: from 19% to 22%, about 0.75 percentage points a year. Commercial and industrial waste reached 48%. At the current pace, the Blueprint's target of about 55% overall (Environment Bureau, 2021) is far off. Household collection points are one lever aimed at the domestic gap, although our data cannot show how much they raise recycling (Section 5.6).

### 5.5 Evaluation: how robust are the results?

With only 18 districts, one unusual district can change a correlation a great deal. We therefore checked every correlation in Table 3 in six ways:

- **Spearman rank correlation:** the same idea as *r*, but based on the districts' rank order, so it is less affected by extreme values.
- **Leave-one-out:** we recalculated *r* 18 times, each time leaving out one district, and report the lowest and highest result.
- **Excluding Wan Chai**, the most extreme district.
- **2024 population** instead of 2025.
- **Alternative income measure:** median income of economically active households only.
- **Permutation p-value:** we shuffled the income values across districts 10,000 times and counted how often a correlation at least as strong appeared by chance. Because we ran 20 tests (10 point types × 2 district variables), we only call a result reliable if *p* < 0.05 ÷ 20 = 0.0025 (a Bonferroni correction).

**Table 4. Robustness of the main correlations with district median income (full results for all 20 tests: Appendix B)**

| Point density per 10,000 | Pearson *r* | Spearman | Leave-one-out range | Excluding Wan Chai | 2024 population | Alt. income | Permutation *p* | Passes correction? |
|---|---|---|---|---|---|---|---|---|
| All restricted points | +0.79 | +0.73 | +0.73 to +0.87 | +0.74 | +0.78 | +0.86 | 0.0005 | Yes |
| Private-estate points (restricted) | +0.77 | +0.65 | +0.68 to +0.86 | +0.71 | +0.76 | +0.85 | 0.0006 | Yes |
| Public smart bins (C) | −0.67 | −0.64 | −0.76 to −0.60 | −0.65 | −0.68 | −0.68 | 0.0024 | Yes, just |
| Public-place bins (A) | +0.55 | +0.63 | +0.38 to +0.65 | +0.38 | +0.55 | +0.50 | 0.018 | No |
| Recycling Spots | +0.53 | +0.36 | +0.35 to +0.64 | +0.35 | +0.53 | +0.55 | 0.024 | No |
| GREEN@COMMUNITY (B) | +0.49 | +0.27 | +0.29 to +0.59 | +0.29 | +0.48 | +0.51 | 0.039 | No |
| All public points | +0.49 | +0.62 | +0.29 to +0.60 | +0.29 | +0.49 | +0.44 | 0.039 | No |

The **direction** of every result in Table 4 holds in all checks, but only three of our 20 tests are strong enough to be called reliable. Restricted points (and the private-estate points that make up most of them) are denser in richer districts, and public smart bins in lower-income ones (the latter only just passes; Section 5.5 shows it reflects public rental housing). The pro-rich patterns for public-place bins, Spots and all public points are moderate and fragile. For example, the all-public correlation drops from +0.49 to +0.29 without Wan Chai, so we describe these as patterns, not proven relationships.

The same checks on population density gave a stable negative link for public points (−0.48; −0.56 without Wan Chai; *p* = 0.037), which also does not pass the correction. Income and population density are themselves correlated (*r* = −0.38), so with 18 districts we cannot separate their effects. Overall, **this analysis is exploratory.**

**What else explains the patterns?** A correlation with income does not mean income is the reason. We tested other district features: population size, land area, and the share of residents in public rental housing and in private housing (D4, 2021 Census). Income is strongly linked to housing mix (*r* = +0.72 with private-housing share, −0.71 with public-rental share; C&SD, 2022, 2026b), and richer districts in our data also tend to be smaller (*r* = −0.54 with log population), so income can stand in for any of these.

**Table 5. What best explains each pattern (n = 18; "…fixed" is a partial correlation: the link with income that remains after holding that feature constant)**

| Point density per 10,000 | r with income | …size fixed | r with public-rental share | …public-rental fixed | r with private share | …private fixed | Best explanation |
|---|---|---|---|---|---|---|---|
| All public points | +0.49 | +0.11 | −0.42 | +0.30 | +0.47 | +0.25 | District size (r = +0.87 with 1 ÷ population) |
| Public-place bins (A) | +0.55 | +0.23 | −0.57 | +0.25 | +0.56 | +0.26 | District size; bin counts follow land area (+0.74), not population (+0.22) |
| Recycling Spots | +0.53 | +0.13 | −0.35 | +0.43 | +0.49 | +0.29 | District size (+0.94 with 1 ÷ population) |
| GREEN@COMMUNITY (B) | +0.49 | +0.04 | −0.29 | +0.42 | +0.44 | +0.28 | District size (+0.92 with 1 ÷ population) |
| Public smart bins (C) | −0.67 | −0.56 | **+0.96** | +0.01 | −0.82 | −0.21 | **Public rental housing** |
| All restricted points | +0.79 | **+0.69** | −0.56 | **+0.67** | +0.66 | **+0.60** | **Income** (remains after size and housing) |

*Source: our calculations from D1, D2 and D4 (Appendix B).*

- **District size explains coverage.** Each district has a similar number of GREEN@COMMUNITY points (17–39), so per-resident coverage is lowest where most people live: Yuen Long, Sha Tin and Tuen Mun. Once size is held fixed, the link with income almost disappears (+0.04).
- **Land area and countryside explain public-place bins.** Their counts follow land area, not population, because many sit in country parks, villages and beaches (Islands, North, Tai Po). Wan Chai looks over-served because its bins are in parks, on hillside roads and at offices, but we divide by only 163,000 residents.
- **Public rental housing explains smart bins.** Smart-bin density follows the public-rental share almost exactly (*r* = +0.96, permutation *p* ≈ 0.0001), and the link with income disappears once that share is held fixed (+0.01). Kwun Tong (58% of residents in public rental housing), Kwai Tsing (56%) and Wong Tai Sin (49%) lead; Central and Western (4%), Wan Chai (4%) and Yau Tsim Mong (3%) trail (C&SD, 2022). This matches the policy of placing smart bins in public estates.
- **Restricted points follow income more than private housing.** They are denser where more people live in private housing (+0.66), but income matters more: holding private share fixed, income still gives +0.60, while holding income fixed, private share gives only +0.23. For example, Yau Tsim Mong is 89% private housing but has only 4.1 restricted points per 10,000, against 21.3 in Central and Western (95% private; housing shares from C&SD, 2022). A likely reason, which we did not test, is that much private housing in older districts is in tenement buildings, often without property management, which rarely run their own recycling. Higher-income managed estates do. Yau (2012) similarly found more recycling in higher-income private estates.

These are associations among 18 districts. Housing shares are from 2021, against 2025 points and population.

**What this means for our research question.** Our question asks how *evenly* the network reaches residents, which is a question about fairness. Knowing **why** a gap exists tells us whether it is unfair and whether it can be fixed:

- **Gaps caused by district size are an allocation problem.** Residents of the biggest districts get the least GREEN@COMMUNITY coverage, consistent with each district having a similar number of points (17–39). This is an unequal outcome that could be corrected by allocating in proportion to population (Recommendation 2).
- **Gaps caused by countryside and offices are a measurement problem.** Wan Chai and Islands only *look* well served; their extra bins are not near homes. This is why access should be measured by type (Recommendation 1).
- **Housing type plausibly decides which solution reaches whom.** Smart bins (C) serve public rental estates, and residents-only bins appear to serve mainly managed private estates. If so, residents of **older private buildings without management** are reached by neither and rely on public-place bins and GREEN@COMMUNITY. We could not count such buildings, so this is a likely explanation rather than a tested one. The government recognises this gap: the Blueprint says Recycling Stores should be placed especially where single-block and "3-nil" buildings are, meaning buildings with no owners' corporation, residents' association or property management (Environment Bureau, 2021, p. 8). Yau Tsim Mong illustrates it: 89% of residents live in private housing (C&SD, 2022), yet it has few smart bins (0.4 per 10,000), few restricted bins (4.1) and only two Stations or Stores. This would also explain why the three solutions **complement each other** (RQ2): each appears to reach a different kind of home (Recommendation 3).

### 5.6 Does access relate to waste or recycling? (RQ4)

**Test 1: landfilled waste.** Our original hypothesis was that districts with more public points would landfill less domestic waste per person. The data shows the **opposite sign**: r = +0.35 (2022), +0.40 (2023) and +0.48 (2024), falling to 0.25–0.29 in each year once Wan Chai is removed. We do not trust this result, for four reasons:

1. The EPD says its district figures "should be regarded as indicative reference only", because they are estimated from intake records at waste facilities (EPD, 2025b, Plate 2.6, note 1).
2. Wan Chai's domestic waste rose from 188 to 258 tonnes per day (+37%) between 2022 and 2024 while its population barely changed.
3. The "Outlying Islands" row includes Ma Wan (part of Tsuen Wan district) and Hei Ling Chau, so it does not match the Islands district boundary.
4. Districts with many workers and visitors, such as Wan Chai and Yau Tsim Mong, both generate more waste and have more public-place bins. Their high values come from the same cause and are not evidence that bins create waste.

**Test 2: recyclables collected.** Using Chan et al.'s (2024) district figures for GREEN@COMMUNITY, recyclables collected per resident (September 2020 to August 2021) ranged from 0.80 kg (Tsuen Wan) to 2.47 kg (Kowloon City and Islands). Districts with more Stations, Stores and Spots per 10,000 residents today collected more: **r = +0.47** (+0.34 without Islands). This is the expected direction. However, the figures were compiled from Facebook posts, they cover 2020–21, when the network had about 130 facilities against about 490 in our 2025 data, and the paper's table totals 11.8 million kg while its text gives about 18 million kg.

**Conclusion for RQ4:** neither test can confirm whether more access reduces waste or increases recycling. Answering that would require official district-level recycling data, which the EPD does not publish. The wider evidence is also limited: Hong Kong studies show that residents *say* nearby facilities matter (Ma et al., 2023), but not that more points raise recycling (see Limitations).

### 5.7 Comparing the three solutions (RQ2)

*[Insert Chart 5: `output/charts/chart5_solutions_compared.png`]*

**Table 6. Three recycling solutions on common measures**

| Measure (unit) | A. Public-place bins | B. GREEN@COMMUNITY | C. Smart bins | Source |
|---|---|---|---|---|
| Public points | 3,588 | 491 | 1,073 | D1 |
| Coverage (points per 10,000 residents) | 4.79 | 0.65 | 1.43 | D1, D2 |
| Unevenness: coefficient of variation across districts | 0.52 | 0.50 | 0.43 | D1, D2 |
| Unevenness: highest ÷ lowest district | 6.0× | 5.3× | 6.4× | D1, D2 |
| Equity (r with district median income; Table 4) | +0.55 (not reliable; mainly district size) | +0.49 (not reliable; mainly district size) | −0.67 (reliable; follows public rental housing) | D1, D2, D4 |
| Range (materials accepted per point) | 2.6 | 8.4 | 1.2 (90% accept food waste) | D1 |
| Opening hours | Not stated for 96% (open-air) | Stores 10–13 h a day in D1 (Sep 2025), all extended to 13 h by 2026 (LCQ2); each Spot one session of about 3 hours a week | 80% open 7 am – midnight | D1, LCQ2 |
| Tonnes collected per year | Not published | 47,500 (2025) | ≤ about 20,000 food waste (mid-2024 rate) | LCQ2; LegCo paper 2024 |
| Tonnes per point per year | Not published | ≤ about 97 (÷ 491 public points, Sep 2025) | ≤ 33 (÷ 605 bins, May 2024) | Derived (script) |
| Kg per resident per year (all HK residents) | Not published | 6.3 | ≤ 2.7 | Derived (script) |
| Operating cost (HK$ per tonne) | Not published | About 10,100 (2025-26) | Not published | LCQ2 |

All three are spread unevenly across districts to a similar degree (coefficient of variation 0.43–0.52). **No solution is best on every measure; they complement each other.**

- **A (public-place bins)** gives the widest coverage, 4.8 points per 10,000 residents, but each bin accepts only about 2.6 materials. Their density is higher in richer districts (r = +0.55), but this does not pass our reliability check (Table 4), and we found **no published output or cost figures** for them. This is the oldest solution and the least measured.
- **B (GREEN@COMMUNITY)** accepts the widest range of materials (8.4 per point) and is the only solution with published output and cost. Its tonnage rose 76% in two years while the cost per tonne fell from about HK$11,600 to HK$10,100. But its coverage is the thinnest (0.65 per 10,000), and 398 of its 491 points are Spots, each open for one session of about 3 hours a week. Because only B has a cost figure, Table 6 does not compare cost-effectiveness across all three.
- **C (smart bins)** is the only solution that reaches **public rental estates** most: its density follows the public-rental share (*r* = +0.96), which is why it is also denser in lower-income districts (*r* = −0.67), consistent with the government's policy of placing smart bins in public estates. However, it is almost entirely for food waste, and its cost is not published.

Caveats:
- **Years and denominators differ.** Point counts are from September 2025; B's tonnage is for 2025 and its cost for financial year 2025-26; C's tonnage is a mid-2024 rate divided by the 605 bins installed at that time.
- **Upper bounds.** B's 47,500 t covers the whole network, including Stores in public-housing estates and smart recycling devices, not only the 491 public points, so about 97 t per point is an overestimate. C's tonnage includes all domestic food-waste channels, not only smart bins.
- **Different populations.** Per-resident figures use Hong Kong's whole population, although smart bins serve mainly public-housing residents.
- **Different materials.** Food waste and dry recyclables differ in weight and value, so tonnes per point shows scale, not efficiency.

### 5.8 District summary

**Table 7. District summary, sorted by public points per 10,000 residents (2025)**

| District | Population | Public points | Public /10k | Public-place bins /10k | Spots /10k | Stations/Stores (count) | Public smart bins /10k | Restricted /10k | Median income (HK$) |
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

Sources: EPD collection points (September 2025); C&SD 2025 population and income. Full table with all columns: Appendix B.

---

## 6. Recommendations

1. **Measure access by type, not by total point count.** The EPD and district planners should report Station, Store and Spot coverage separately from public-place bins, because a bin in an office lobby or on a hiking road is not household access. This is timely: the government plans to reorganise GREEN@COMMUNITY district by district, with one operator per district (HKSAR Government, 2026). A per-district, per-type baseline like Table 7 could be used directly.

2. **Scale GREEN@COMMUNITY to population, starting where coverage is thinnest.** Because each district has a similar number of points, coverage per resident is lowest in the most populous districts (Section 5.5). On Stations, Stores and Spots per 10,000 residents, the lowest districts are **Yuen Long (0.32), Sha Tin (0.38) and Tuen Mun (0.47)**, against a median of about 0.70. Using the median as an illustrative target, bringing them up to it would need about **59 more Spots** (Yuen Long 25, Sha Tin 22, Tuen Mun 12). That is around 15% of the 398 Spots in our data, and the network had already grown to about 600 Spots by mid-2026 (HKSAR Government, 2026), so the scale is realistic. We cannot say how much extra recycling this would bring (Section 5.6). Since most Spots open only about 3 hours a week, longer opening hours are an alternative. Zhao et al. (2025) find 9 of 18 districts low on walking access, which could be cross-checked against this list.

3. **Target Recycling Stores at older private housing without management.** Smart bins reach public rental estates, and managed private estates have their own bins, but older private buildings without management get neither (Section 5.5). The Blueprint already says Stores should go where "3-nil" buildings are (Environment Bureau, 2021, p. 8). Districts with much private housing but few managed-estate bins, such as Yau Tsim Mong (89% private housing, C&SD, 2022; only two Stations or Stores, D1), are a starting point. We could not count 3-nil buildings directly, so this needs checking with building-level data.

4. **Publish output and cost data for every solution, by district.** Only GREEN@COMMUNITY has published tonnage and cost (about HK$10,100 per tonne). Public-place bins and smart bins have none (Table 6), and researchers had to rebuild district figures from Facebook posts (Chan et al., 2024). With official data, the three solutions could be compared on cost-effectiveness, and RQ4 could be tested properly.

*These are proposals based on descriptive evidence. None has been tested, and the effect on recycling volumes is unknown.*

---

## 7. Limitations

- **Counts ignore capacity and opening hours.** A Recycling Spot open about 3 hours a week counts the same as a Station open most days, and a single bin counts the same as a staffed Store.
- **Residents as the denominator.** Commercial districts (Wan Chai, Central and Western, Yau Tsim Mong) look over-served because their points also serve workers and visitors, who are not counted in the resident population.
- **"Public" is the EPD's label (assumption).** We rely on the EPD's "For public use" label to decide what counts as public access, rather than inventing our own definition. 925 of the 1,073 public smart bins are at housing-estate addresses, and we did not verify on site whether non-residents can reach them. If some are inside residents-only areas, smart-bin coverage (Solution C) is overstated, and the −0.67 result shows where bins are placed rather than who can use them.
- **One snapshot.** D1 shows a single day (18 September 2025). The network kept growing; there were about 600 Spots by July 2026 against 398 in our data.
- **No distance measure.** We count points per district rather than walking distance to the nearest point. Guo et al. (2018) show that distance-based measures can reverse the conclusion, and Zhao et al. (2025) measure walking access directly.
- **Access is not the same as use.** Evidence that nearby points make people recycle more is limited. Ma et al. (2023) report what residents **say** (convenience is their main reason to recycle). Chan et al. (2024) find that people who visited a Recycling Store recycle more, which is an association, not proof. Zhao et al. (2025) measure walking access, not behaviour. Outside Hong Kong, a randomised experiment in Vancouver found that moving bins closer raised recycling by 137–147% (DiGiacomo et al., 2018). However, in Shanghai distance explained only 3% of the variation in participation (Li et al., 2020), and in Hong Kong private estates floor-level facilities alone were unlikely to raise recycling without incentives (Yau, 2012). Our own test (RQ4) could not confirm the link either. We therefore study access because residents say it matters, not because it is proven to raise recycling.
- **Small sample and confounding.** With 18 districts, one district (Wan Chai) moves several results noticeably. Income is linked to district size, population density and housing mix (public rental and private shares). Partial correlations (Table 5) help, but with 18 districts they cannot fully separate these effects.
- **Uneven solution data.** Output and cost are published only for GREEN@COMMUNITY, so Table 6 cannot compare cost-effectiveness across all three solutions.
- **Weak outcome data.** District waste figures are indicative and do not exactly match district boundaries. The only district recycling figures are from 2020–21, unofficial, and inconsistent with the paper's own total.
- **Mixed years.** Points are from 2025; population and income from 2025 (2024 as a check); waste from 2022–2024; recycling volumes from 2020–21.

---

## 8. Conclusion

> **WRITING GUIDE: delete this box once the group has written the section.** About 400–500 words (just under one page), four paragraphs. Answer the research questions directly. No new numbers or sources.
>
> **Paragraph 1: Answer each research question in one or two sentences.**
> - **RQ1:** Public access varies 3.2-fold (4.8 in Wong Tai Sin to 15.2 in Wan Chai per 10,000 residents), but mostly because of public-place bins in parks, offices and on hiking roads. Without them the range narrows to 1.5–3.6 (Section 5.1).
> - **RQ2:** No solution is best on every measure, so they complement each other (Section 5.7). A has the widest coverage but few materials and no published output or cost. B accepts the most materials and is the only one with published cost (about HK$10,100 per tonne), but has the thinnest coverage. C reaches public rental estates but is mostly for food waste.
> - **RQ3:** Most of the apparent income patterns are really about **district size and housing type** (Section 5.5, Table 5). Coverage is thinnest in the most populous districts; smart bins follow public rental housing (+0.96); public-place bins follow land area. Only restricted estate points still follow income, even after allowing for private-housing share, probably because managed private estates (not old tenement buildings) run their own recycling. Whether the network looks fair depends on what is counted, and on what you compare it with.
> - **RQ4:** Cannot be answered with current data. The landfill figures are indicative, and the only district recycling figures are from 2020–21 (Section 5.6).
>
> **Paragraph 2: What we learned about data (data thinking).**
> - Definitions drive conclusions: counting all points, public points or one type gives different answers, as Guo et al. (2018) also found.
> - Official data still needs checking: blank rows, a one-day snapshot, the EPD's own "indicative" warning, and the "public" label we had to assume.
> - Robustness checks showed that the direction of every result holds, but only three of 20 tests pass a correction for running 20 tests (restricted points, private-estate points and smart bins). Several depend on one district (Wan Chai), so the results are exploratory.
>
> **Link to the question:** explain that the "why" in Section 5.5 decides whether each gap is unfair and fixable. Size gaps are an allocation problem (fix: scale to population); countryside and office bins are a measurement problem (fix: measure by type); housing type decides which solution reaches whom, leaving older private buildings without management in a gap (fix: target Stores there).
>
> **Paragraph 3: Impact.**
> - Who benefits: residents of districts with thin coverage (Yuen Long, Sha Tin, Tuen Mun), and planners reorganising GREEN@COMMUNITY district by district.
> - The practical changes:
>   - measure access by type;
>   - scale GREEN@COMMUNITY to population, for example about 59 more Spots to bring the three most populous low-coverage districts up to the median (an illustrative target);
>   - publish output and cost for all three solutions.
> - Link back to the 55% target: improving household access targets the weakest part of recycling (22%).
>
> **Paragraph 4: Future work and final takeaway.**
> - Next steps: walking-distance measures (as in Zhao et al., 2025); official district recycling tonnage; an on-site check of smart-bin access.
> - Close with one memorable sentence, the same take-away as the presentation. Starter: "Hong Kong does not simply need more recycling points; it needs…" 

## 9. Member Responsibilities

*[Group to complete: name, student ID and responsibilities for each of the 6 members.]*

## References

*APA 7. In tables, "LCQ2" refers to HKSAR Government (2026), and "LegCo paper 2024" refers to Environment and Ecology Bureau (2024). In-text, C&SD = Census and Statistics Department.*

**Datasets**

Census and Statistics Department. (2022). *2021 Population Census statistics (by District Council district)* [Data set]. DATA.GOV.HK. Retrieved November 3, 2026, from https://www.census2021.gov.hk/doc/DC_21C.zip

Census and Statistics Department. (2026a). *Land area, land population and population density by District Council district* (Table 110-02001) [Data set]. DATA.GOV.HK. Retrieved November 3, 2026, from https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-02001

Census and Statistics Department. (2026b). *Average household size and median monthly household income of households by District Council district* (Table 130-06806) [Data set]. DATA.GOV.HK. Retrieved November 3, 2026, from https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-130-06806

Environmental Protection Department. (2025a). *Waste Less – Recyclable collection points data* [Data set]. DATA.GOV.HK. Retrieved September 18, 2025, from https://data.gov.hk/en-data/dataset/hk-epd-recycteam-waste-less-recyclable-collection-points-data

Housing Authority. (2026). *Report on population and households in Housing Authority public rental housing (September 2026)* [Data set]. Retrieved November 3, 2026, from https://www.housingauthority.gov.hk/en/common/pdf/about-us/publications-and-statistics/PopulationReport.pdf

**Reports, papers and government documents**

Audit Commission. (2020). *Provision and management of Community Green Stations* (Director of Audit's Report No. 74, Chapter 8). https://www.aud.gov.hk/pdf_e/e74ch08.pdf

Chan, T. H. C., Hui, T. Y., & Chan, J. K. Y. (2024). From trash to treasure: Assessing the effectiveness of the Green@Community recycling network in Hong Kong. *Recycling, 9*(6), Article 110. https://doi.org/10.3390/recycling9060110

DiGiacomo, A., Wu, D. W.-L., Lenkic, P., Fraser, B., Zhao, J., & Kingstone, A. (2018). Convenience improves composting and recycling rates in high-density residential buildings. *Journal of Environmental Planning and Management, 61*(2), 309–331. https://doi.org/10.1080/09640568.2017.1305332

Environment and Ecology Bureau. (2024). *Report on the Municipal Solid Waste Charging Demonstration Scheme* (LC Paper No. CB(1)606/2024(01)). Legislative Council Panel on Environmental Affairs and Panel on Food Safety and Environmental Hygiene. https://legco.gov.hk/yr2024/english/panels/ea/papers/eafseh20240527cb1-606-1-e.pdf

Environment Bureau. (2021). *Waste blueprint for Hong Kong 2035*. https://www.eeb.gov.hk/sites/default/files/pdf/waste_blueprint_2035_eng.pdf

Environmental Protection Department. (2023). *Monitoring of solid waste in Hong Kong: Waste statistics for 2022*. https://www.wastereduction.gov.hk/sites/default/files/resources_centre/waste_statistics/msw2022_eng.pdf

Environmental Protection Department. (2024a). *EPD responds to concerns regarding food waste recycling services* [Press release]. https://www.info.gov.hk/gia/general/202404/16/P2024041600707.htm

Environmental Protection Department. (2024b). *Monitoring of solid waste in Hong Kong: Waste statistics for 2023*. https://www.wastereduction.gov.hk/sites/default/files/resources_centre/waste_statistics/msw2023_eng.pdf

Environmental Protection Department. (2025b). *Monitoring of solid waste in Hong Kong: Waste statistics for 2024*. https://www.wastereduction.gov.hk/sites/default/files/resources_centre/waste_statistics/msw2024_eng.pdf

Guo, Y., Chang, S.-S., Chen, M., & Yip, P. S. F. (2018). Do poorer areas have poorer access to services in Hong Kong? A small-area analysis based on multiple spatial accessibility indicators. *Social Indicators Research, 138*(1), 1–21. https://doi.org/10.1007/s11205-017-1658-5

HKSAR Government. (2026, July 8). *LCQ2: Operation of GREEN@COMMUNITY* [Press release]. https://www.info.gov.hk/gia/general/202607/08/P2026070800357.htm

Li, C. J., Zhang, Y., Nouvellet, P., Okoro, J. O., Wang, X., & Harder, M. K. (2020). Distance is a barrier to recycling – or is it? Surprises from a clean test. *Waste Management, 108*, 183–188. https://doi.org/10.1016/j.wasman.2020.04.022

Ma, F. C., Wong, T. L., Chan, C. N., & Ran, L. (2023). Revising the effectiveness of municipal waste management in Hong Kong. *Frontiers in Environmental Science, 11*, Article 1178363. https://doi.org/10.3389/fenvs.2023.1178363

Yau, Y. (2012). Stakeholder engagement in waste recycling in a high-rise setting. *Sustainable Development, 20*(2), 115–127. https://doi.org/10.1002/sd.468

Zhao, T., Shang, X., Li, L., Li, W., Li, Y., Guan, M., Ding, A., Zhang, J., & Tian, Y. (2025). Measuring walking convenience of Hong Kong resource recycling services: Utilizing a spatially refined model framework of multiple recyclable wastes. *Resources, Conservation and Recycling, 215*, Article 108153. https://doi.org/10.1016/j.resconrec.2025.108153

*All links were checked on 3 November 2026; the three waste-statistics PDFs at these links are identical to the copies in `data/`.*

## Appendix

- **A.** Cleaning and download log (dates, URLs, file names); analysis script `build_district_table.py` and its outputs (`output/district_summary_2025.csv`, `output/solutions_comparison.csv`, `output/robustness_by_type.csv`, `output/explanations.csv`, `output/housing_mix.csv`)
- **B.** Full district table (`output/district_summary_2025.csv`) and full robustness results (`output/robustness_by_type.csv`)
- **C.** Chart code (`make_charts.py`) or Excel formulas; solutions table (`output/solutions_comparison.csv`)
