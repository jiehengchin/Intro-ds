# Q&A Prep: Who Gets a Recycling Point?

2 minutes of Q&A means each answer is ~20–30 seconds. These are **drafts**: rewrite in your own words and assign a [Name] to each section. Every number matches `GE1356 Report Draft.md` and the output of `build_district_table.py`.

Etiquette: rephrase the question first, route it to the best-placed member, don't interrupt, and say "We did not test that, but here is how we would approach it" rather than bluff.

---

## 1. Why it matters, who benefits  [Name: ___]

**Why does this problem matter?**
Hong Kong landfills over 10,000 tonnes of waste a day. Households recycle only 22% against a ~55% target, and the rate rises only ~0.75 points a year. Households are the weakest link, and residents *report* convenience is their main reason to recycle.

**Who benefits?**
- Residents of the most populous districts (Yuen Long, Sha Tin, Tuen Mun), who have the thinnest GREEN@COMMUNITY coverage.
- Planners: the government is reorganising GREEN@COMMUNITY district by district, and our per-type table (Table 7) is a ready baseline.

**Did you prove more recycling points increase recycling?**
No. We study access because residents say it matters.
- Vancouver experiment: moving bins closer raised recycling 137–147%.
- Shanghai: distance explained only 3% of participation.
- Our own test (RQ4) was inconclusive.

## 2. Data  [Name: ___]

**Sources, and can you trust them?**
- EPD collection-point dataset (8,858 points, snapshot 18 Sep 2025).
- C&SD population and income tables; EPD waste statistics 2022–24; 2021 Census housing shares; statistics from 15 reports and papers.
- Weak spot: the EPD itself says its district waste figures are "indicative reference only".

**Missing data, duplicates, cleaning?**
- Removed 2 rows with no point type and no access note → 8,856 points.
- No coordinates missing; every point fell in one of 18 districts.
- Kept duplicates (120 rows share 58 coordinates) because the EPD lists each bin separately, e.g. a paper bin and a plastics bin at one site.
- Renamed one district ("Central_Western" → "Central and Western").

**Sampling and bias?**
It is the full EPD list, not a sample, covering all 18 districts. Risks: one-day snapshot (the network has since grown, ~600 Spots by 2026 vs 398 in our data). We used the EPD's own "public" and "type" fields so we could not pick definitions that favour a result.

**How did you decide what counts as "public"?**
The EPD note "For public use". This is an assumption: 925 of 1,073 public smart bins are at housing-estate addresses and we did not verify on site that non-residents can use them. If they can't, smart-bin coverage is overstated.

## 3. Method choices  [Name: ___]

**Why points per 10,000 residents?**
Raw counts reward big districts. Dividing by population makes districts comparable. Weakness: commercial districts (Wan Chai, Central) look over-served because workers and visitors use the bins but aren't in the denominator.

**Why correlation, not regression?**
The brief asks for descriptive statistics, and the unit is only 18 districts, so we avoided fitting a model. Partial correlations (holding size or housing fixed) let us ask whether income still matters. Limit: with 18 points we cannot fully separate income, density and housing effects.

**Why these three solutions? Why not private estate points?**
A, B and C are the government's own programmes. Private estate points (3,177) are run by property managers, so we treat them as context.

**Why district level, not walking distance?**
District counts are what the data supports. Walking distance would be better (Zhao et al., 2025 do it); it is our main future work.

**Ecological fallacy?**
A district-level link between income and points does not mean richer *people* recycle more. We claim only district-level associations.

## 4. Validation  [Name: ___]  (expect the hardest questions here)

**How did you validate? There's no train/test.**
We built no predictive model, so train/test doesn't apply. We stress-tested every correlation six ways: Spearman, leave-one-out, excluding Wan Chai, 2024 population, an alternative income measure, and a permutation test with a Bonferroni correction.

**What is your baseline?**
No predictive baseline. We compare against published benchmarks (e.g. Guo et al. 2018) and territory-wide recovery rates.

**What did the checks show?**
The direction of every result held. Only 3 of 20 tests pass the correction (p < 0.0025):
- restricted points vs income (+0.79)
- private-estate points vs income (+0.77)
- smart bins vs income (−0.67; p = 0.0024, just passes)

Others, including "pro-rich" public points, are fragile: all-public drops from +0.49 to +0.29 without Wan Chai.

**Why Bonferroni? Isn't it too strict?**
We ran 20 tests, so some would look significant by chance. It is conservative, so we call the rest "moderate and fragile patterns", not disproven.

**Are your "why" explanations proven?**
- Smart bins follow public rental housing: r = +0.96, income link falls to +0.01 once held fixed. Strong.
- Size explains GREEN@COMMUNITY coverage: r = +0.92 with 1/population, income link falls to +0.04. Strong.
- Our reason why restricted points follow income (older private buildings without management) is a **likely explanation we did not test**.

## 5. Surprises and honesty  [Name: ___]

**You expected more points → less waste. What happened?**
The sign was opposite (r = +0.35 to +0.48). We don't trust it:
- the EPD calls its district figures indicative only
- Wan Chai's domestic waste rose 37% (188 → 258 t/day) while population barely changed
- the "Outlying Islands" row includes Ma Wan, so it doesn't match the Islands district
- districts with many workers and visitors produce more waste *and* have more bins

We reported it anyway (Section 4.3).

**Why not compare cost-effectiveness of all three?**
Only GREEN@COMMUNITY publishes output and cost (~HK$10,100 per tonne). We found none for public bins or smart bins, so we say so rather than invent one.

**Is "97 tonnes per point" reliable?**
No, it's an upper bound: the 47,500 t covers the whole network (including Stores in public housing estates and smart recycling devices), not just the 491 public points. It shows scale, not efficiency.

**Chan et al. (2024) numbers look odd.**
Correct: compiled from Facebook posts, covers 2020–21 (~130 facilities vs ~490 now), and the paper's table totals 11.8 million kg while its text says ~18 million. We used it only as a weak check (r = +0.47; +0.34 without Islands).

## 6. Limitations, reproducibility, ethics  [Name: ___]

**Biggest limitations?**
- Counts ignore capacity and opening hours (a 3-hours-a-week Spot counts like a Station).
- One-day snapshot.
- n = 18, and Wan Chai is influential.
- No distance measure.
- No reliable outcome data.

**Reproducible?**
Yes. Raw files are untouched in `data/`; `build_district_table.py` rebuilds every table (stdlib only, fixed seed 1) and `make_charts.py` redraws the charts. Descriptive results also work in Excel (COUNTIFS, CORREL).

**Ethics and privacy?**
All data is aggregated, government-published, with no personal information. We avoid calling districts "good" or "bad": low density may reflect where the government placed facilities, not any failing by residents.

## 7. Recommendations and teamwork  [Name: ___]

**Recommendations?**
1. Measure access by type, not total count.
2. Scale GREEN@COMMUNITY to population (~59 more Spots to lift Yuen Long, Sha Tin, Tuen Mun to the median; an *illustrative* target).
3. Put Stores near older private buildings without management (the Blueprint already says this).
4. Publish output and cost for every solution.

None is tested; the effect on recycling volumes is unknown.

**What did each member contribute?**
[Fill in all 6 names and roles. Report Section 9 is still blank; make the two match.]

---

## "We did not test that, but…" lines

- 3-nil / unmanaged buildings: we'd use building-level data to count them.
- Access vs use: we'd need official district recycling tonnage.
- Smart-bin access: we'd check on site whether non-residents can use them.
- Walking distance: we'd replicate Zhao et al.'s method.

## Everyone should be able to explain

- Table 5 (partial correlations) in plain words: "the link with income that remains after holding size/housing fixed".
- Why Wan Chai and Islands only *look* well served.
- Why RQ4 is unanswered.
