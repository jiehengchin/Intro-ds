# Q&A Prep: Who Gets a Recycling Point?

The brief: the professor and TA grade "your ability to defend your data", and **inability to explain your group's reasoning is penalised**. So every member must say every idea below in kids' words, without notes. Each answer ~20–30 seconds (2 minutes of Q&A).

Numbers match `GE1356 Report Draft.md` and `build_district_table.py`. Rewrite in your own words and put a [Name] on each section. Etiquette: rephrase the question, route it to the best-placed member, never bluff ("We did not test that, but here is how we would").

---

## Memorise these four (everyone)

**Story (30 s):** "Public points vary 3.2-fold between districts, but most of that is bins in parks and offices, not near homes. The three solutions follow different drivers: public-place bins follow land area, GREEN@COMMUNITY follows district size, smart bins follow public rental housing. So most income patterns are really size and housing, and only 3 of 20 tests are strong enough to trust. No solution wins on every measure, so we recommend measuring access by type."

**Data (30 s):** "We took the government's full list of recycling points (8,858 rows, 18 Sep 2025), dropped 2 rows with no type (8,856), and used the EPD's own note to keep the 5,301 public points and set aside the 3,555 restricted ones. We counted public points per district and type, divided by 2025 population per 10,000, and joined income and housing share. One script rebuilds every table."

**Method (30 s):** "For each district we asked: how different are they, do richer or more crowded districts have more of each type, and does that survive when we hold size or public housing fixed. With 18 districts and 20 tests, we tried to break every result six ways and only trust what survives."

**Takeaway:** "Hong Kong doesn't just need more recycling points; it needs to know who each type of point actually reaches, because the answer changes with what you count."

3-minute talk split (6 × ~30 s): problem → data and method → 3.2× gap and three solutions (Charts 6, 5) → why it's size and housing (Chart 7) → how far to trust it → recommendations.

---

## 0. Explain it like I'm 10  (everyone)

Say the kid version first; give the proper term only if pushed.

| Idea | Kid version | Proper |
|---|---|---|
| **Per 10,000 residents** | "A big town needs more bins than a small one, so we ask: bins for every 10,000 people?" | Population-standardised density |
| **Correlation (r)** | "From −1 to +1: do two things move together? +1 up together, −1 opposite, 0 no pattern." | Pearson's r |
| **Spearman** | "Same idea but using rankings (1st, 2nd…), so one odd district can't fool it." Pearson is our main number; Spearman is a double-check. | Rank correlation |
| **Held fixed (partial correlation)** | "Richer districts also have fewer people and less public housing. If two districts were the same size, would richer still mean more bins? Like runners starting at the same line." | Partial correlation |
| **Leave-one-out** | "Remove one district at a time. Does one odd kid change the class average?" | Influence check |
| **Evenness (CV)** | "How different districts are from each other. Low = similar; high = some have much more." | SD ÷ mean |
| **Ecological fallacy** | "Richer *districts* having more bins doesn't mean richer *people* recycle more." | Group ≠ individual |
| **Confounder** | "Something hiding behind the pattern, like size or public housing." | Confounding variable |
| **Snapshot** | "A photo of one day (18 Sep 2025); bins have been added since." | Cross-sectional |
| **Public / restricted** | "Public: anyone can use it. Restricted: only that estate's residents or that company's staff." | EPD access note |
| **Spot / Store / Station** | "Spot: booth open ~3 hours a week. Store: small shop. Station: big staffed centre." | GREEN@COMMUNITY tiers |
| **Smart bin** | "Bin in public housing estates, 90% food waste." | Public-use Smart Bin |
| **Why RQ4 is unanswered** | "We'd need recycling amounts per district; the government doesn't publish them." | Outcome data missing |

### Permutation test + Bonferroni (worked example: smart bins vs income, r = −0.67)

**Question:** could 18 random districts show r = −0.67 by luck?

1. Put each district's smart-bin number on one card, its income on another.
2. **Shuffle** the income cards so incomes are random. Bin numbers stay fixed. Any link is now pure luck.
3. Compute r for the shuffled pairing and write it down.
4. Repeat **10,000 times**: 10,000 luck-only r values.
5. **Count** how many are as strong as ours (|r| ≥ 0.67, either sign): about 24.
6. **p** = (count + 1) ÷ 10,001 ≈ 0.0024. "Only ~24 in 10,000 shuffles looked this strong by luck."

**Bonferroni:** we ran 20 pairings (10 bin measures × income and crowdedness). Play 20 times and a 1-in-20 fluke is expected, so the pass mark is made 20× harder: **0.05 ÷ 20 = 0.0025**. Smart bins (0.0024) pass, just. Public bins vs income (0.018) pass a single test but fail here.

*Why not the textbook p-value?* It assumes bell-curve data; with 18 districts shuffling needs no assumption. *What it does not say:* nothing about cause, and a fail means "not strong enough with 18 districts", not "no effect".

---

## 1. Why it matters  [Name: ___]

- **Why?** Over 10,000 t of waste landfilled a day; households recycle 22% vs a ~55% target, rising ~0.75 points a year; residents *report* convenience is their main reason to recycle.
- **Who benefits?** Residents of the biggest districts (Yuen Long, Sha Tin, Tuen Mun) with the thinnest GREEN@COMMUNITY coverage; planners, since the government will run GREEN@COMMUNITY district by district (Table 7 is a ready baseline).
- **Did you prove more points → more recycling?** No. We study access because residents say it matters. Vancouver: closer bins raised recycling 137–147%; Nanjing: distance explained 3%; our own test (RQ4) was inconclusive.

---

## 2. Defending the data  [Name: ___]

| Challenge | Kid version | Full answer |
|---|---|---|
| **No data collected: OK?** | "We used the government's full list, not a few answers." | Option 2 allows official datasets plus ≥ 8 reports. Full register, so no sampling or non-response bias. Weakness: not checked on site. |
| **Trust the source?** | "The Environmental Protection Department keeps the list." | EPD "Waste Less" on DATA.GOV.HK; population and income from C&SD; all citable and re-downloadable. Limits: addresses not audited; EPD calls district *waste* figures "indicative only". |
| **What did you delete?** | "2 unlabelled rows, plus private bins the public can't use." | 2 rows with no type (8,858 → 8,856). Restricted points (3,177 private + 370 restricted smart bins + 8 NGO = 3,555) are excluded from the three solutions, kept as context for "restricted vs income". |
| **Why drop restricted?** | "A bin inside someone's estate doesn't help the neighbour." | Run by property managers, not government; public can't use them (EPD note). We rely on that label, not an on-site check. |
| **Duplicates?** | "Two bins at one place are two bins." | 120 rows share 58 coordinates; 246 addresses repeat. EPD lists each bin separately (e.g. paper and plastics). Kept all. *Not tested:* merging them; we'd dedupe by address + type and rerun. |
| **District labels right?** | "We used the EPD's label and checked it on a map." | One name mapped ("Central_Western"). A boundary check put every point in Hong Kong, but 189 (2%) sit in a neighbouring district, mostly near borders. Not re-run. |
| **Out of date?** | "A photo of one day; bins were added later." | 18 Sep 2025. LCQ2 (Jul 2026): ~600 Spots vs 398 in our data. We say so and don't mix years silently. |
| **Smart bins don't match the news (605 / 140)** | "Different kinds, different dates." | D1: 1,443 smart-bin rows (1,073 public; 962 accept food waste). 605 = food-waste bins in public estates, May 2024; 140+ = GREEN@COMMUNITY smart recycling bin sets. |
| **Which years?** | "Closest to our bin list." | 2025 population and income (2024 as a check); housing shares from 2021 Census, cross-checked with HA 2026 (r = 0.98). |
| **What is "income"?** | "The middle monthly income of a household." | C&SD median monthly household income of *all* households, incl. retired, so retiree-heavy districts look poorer; economically-active version gives a similar result. |
| **15 sources → one comparison?** | "Same units." | 55 t/day × 365 ≈ 20,000 t; HK$480M ÷ 47,500 t ≈ HK$10,100/t; tonnes → kg per resident. Where no figure exists, blank, not estimated. |
| **Can I rerun it?** | "One button, same tables." | Raw files untouched in `data/`; `build_district_table.py` checks totals and uses fixed seed 1. |
| **Why 15 sources, not 8?** | | The brief needs ≥ 8; each of our 15 has one extracted, standardised figure. Seven feed our tables; the rest are benchmarks. |

**Admit before they find it:** we trust the EPD "public" label (about 900 of 1,073 public smart bins are at estate addresses; access not verified on site); duplicates and border labels were reported but not stress-tested; housing is 2021 while income and population are 2025; a 3-hour Spot counts like a 7-day Station.

---

## 3. Defending the method  [Name: ___]

| Challenge | Kid version | Full answer |
|---|---|---|
| **Why per 10,000?** | "Fair between big and small districts." | Weakness: commercial districts (Wan Chai, Central) look over-served because workers and visitors aren't in the denominator. |
| **Why correlation, not regression/ML?** | "We wanted to see what moves together, not predict; 18 districts would make a fancy model guess." | Brief asks for descriptive statistics; 18 observations and correlated predictors make coefficients unstable. Partial correlations answer "does income still matter". |
| **Why these three solutions? Why not private estate points?** | | A, B, C are the government's programmes; private points are run by property managers, so context. |
| **Why district, not walking distance?** | | District counts are what the data supports; walking distance (Zhao et al. 2025) is future work. |
| **What does r = +0.49 mean?** | "Halfway between no link and perfect, with many exceptions." | r² = 0.24: a quarter of the variation, descriptively, not causally. |
| **What counts as reliable?** | "Holds when shaken, and not luck." | Sign stable in all checks **and** permutation p < 0.0025: only restricted (+0.79), private-estate (+0.77), smart bins (−0.67). The rest are "moderate and fragile", not disproven. |
| **Why 20 tests?** | "We checked 20 things." | 10 density measures (all public, restricted, private-estate, 6 point types, GREEN@COMMUNITY) × income and population density. 10,000 shuffles resolve p down to ~0.0001. |
| **Why income and density?** | "Do richer or more crowded places get more?" | The two easiest-to-cite district traits; housing and size added to explain "why". |
| **Median, not average income?** | "A few rich households drag the average up." | Median resists extremes. |
| **What does "size fixed" do?** | "Compare districts as if same population." | Partial correlation: (r_xy − r_xz·r_yz) ÷ √((1−r_xz²)(1−r_yz²)), for log population and for public-rental and private shares. |
| **Why public-rental share for smart bins?** | "Smart bins went into public housing." | +0.96 with public-rental share; income link −0.67 → +0.01 when fixed. |
| **Six robustness checks?** | "Six ways to break the answer." | Spearman; leave-one-out; excluding Wan Chai; 2024 population; alternative income; permutation + Bonferroni. |
| **The 59 Spots?** | "Lift the three thinnest big districts to the middle." | Median GREEN@COMMUNITY density 0.70 per 10k. Extra = (0.70 − density) × pop ÷ 10,000: Yuen Long +25, Sha Tin +22, Tuen Mun +12. Illustrative, not proven need. |
| **Chart 5 measures?** | | Coverage = public points ÷ HK population × 10,000 (B: 491 → 0.65). Evenness = SD ÷ mean of the 18 densities (A, B, C = 0.43–0.52). Materials = types accepted per point (A 2.6, B 8.4, C 1.2). Output and cost exist only for B, so we claim no winner on effectiveness. CV uses all districts, the best÷worst ratio only two, so C can be lowest on one and highest on the other. |
| **Density instead of size?** | | Partly, for public-place bins only (r = −0.53; density proxies land area). For GREEN@COMMUNITY, Spots, smart bins and restricted points it adds nothing once size is fixed. Holding density fixed barely moves the GREEN@COMMUNITY income link (+0.49 → +0.46); holding size fixed nearly removes it (+0.04). In `explanations.csv`, not in the report. |
| **How did you avoid bias?** | | Full official list, not a sample; EPD's own definitions of "public" and type; per-resident counts; we reported results against our guess (RQ4). Remaining: commercial districts, one-day snapshot. |
| **Did you use AI?** | | Agree one honest group sentence, e.g. "AI helped with grammar and scripting; question, method and interpretation are ours; every number rebuilds from `build_district_table.py`." |
| **No train/test? Baseline?** | "No practice test; instead we tried to break our answers." | No predictive model, so none applies. We compare against published benchmarks (Guo et al. 2018) and territory-wide recovery rates. |

**Never say:** "richer people recycle more" (say richer *districts*); "income causes…" (say "linked with"); "p = 0.039 is significant" (not after correcting for 20 tests); "smart bins are for poor people" (say "follow public rental housing").

---

## 4. Defending the findings  [Name: ___]

Rule: finding → number → what it does *not* show.

| Finding | Number | Likely attack → reply |
|---|---|---|
| **Gap between districts** | 4.8 (Wong Tai Sin) to 15.2 (Wan Chai) per 10k, 3.2×; mean 7.9, median 7.3 | "Is it real?" Real in counts, but 68% of public points are public-place bins; Wan Chai is 81% bins (12.3 of 15.2), many in offices and hiking roads. Says little about home access. |
| **Ranking changes without park/office bins** | Range 1.5 (Sai Kung) to 3.6 (Islands); Kwai Tsing, Kwun Tong, Wong Tai Sin move bottom → top half | "Cherry-picking?" We show both. Park bins are real but don't serve people at home; which matters depends on the question (Guo et al. 2018). |
| **No solution wins everywhere** | A 4.79/10k, 6.0×, +0.55, 2.6 materials; B 0.65, 5.3×, +0.49, 8.4, 47,500 t, ~HK$10,100/t; C 1.43, 6.4×, −0.67, 1.2 | "Which is best?" Can't say on effectiveness (output and cost only for B); we compare reach and fairness. |
| **Public bins follow income** | +0.55 but p = 0.018 (fails); +0.38 without Wan Chai; +0.23 size fixed | "Richer get more bins?" Not reliably: moderate, fragile, pulled by Wan Chai and Central and Western. |
| **Smart bins follow public rental housing** | +0.96; income −0.67 → +0.01 fixed; p ≈ 0.0001 | "Then why −0.67 with income?" Poorer districts have more public housing; fix housing and income adds nothing. Strong. |
| **GREEN@COMMUNITY thins out in big districts** | +0.92 with 1 ÷ population; 17–39 points per district; income +0.49 → +0.04 size fixed | "Policy or accident?" Can't tell; consistent with an equal-number-per-district pattern, not tested. Allocation, not neglect. |
| **Restricted points follow income** | +0.79 (p = 0.0005); +0.69 size fixed; +0.60 private share fixed | "Why?" Likely managed private estates run their own bins, old tenements don't (Yau Tsim Mong: 89% private, 4.1 per 10k; Central and Western: 95%, 21.3). **Untested; say so.** |
| **Only 3 of 20 reliable** | The 3 above; all-public +0.49, p = 0.039, +0.29 without Wan Chai | "Bonferroni too harsh?" It is conservative, so the rest are "fragile", not zero. |
| **RQ4 inconclusive** | Public density vs domestic waste per person r = +0.35 / +0.40 / +0.48 (2022–24); recyclables vs facilities +0.47 (+0.34 without Islands) | "Opposite sign?" Reported anyway. EPD figures "indicative only"; Wan Chai +37% (188 → 258 t/day) with flat population; "Outlying Islands" row includes Ma Wan; workers create waste and bins; the recycling series is Facebook-derived, 2020–21, and its table (11.8 M kg) ≠ its text (~18 M kg). |
| **Rec 2: ~59 Spots** | Yuen Long 0.32, Sha Tin 0.38, Tuen Mun 0.47 vs median 0.70 | "Why not Wong Tai Sin (lowest overall)?" Its low total comes from few public-place bins; it has 8 Stations/Stores. "Will it raise recycling?" Unknown; illustrative. |
| **Rec 3: Stores in old private buildings** | Yau Tsim Mong: 89% private, 2 Stations/Stores, smart 0.4 per 10k | "Counted those buildings?" No ("3-nil" counts not in our data); Blueprint p. 8 already says Stores go there. |
| **"97 t per point" (B)** | 47,500 t ÷ 491 | Upper bound: the 47,500 t covers the whole network, not just 491 public points. Shows scale, not efficiency. |

**If the professor says…**
- *"Results are weak (3 of 20)."* → "That is a finding: most income stories dissolve once size and housing are accounted for."
- *"Correlation isn't causation."* → "Agreed; every finding is an association between 18 districts."
- *"n = 18, how do you generalise?"* → "We don't; the 18 are the whole population, and permutation tests suit small n."
- *"What surprised you?"* → "More points did not mean less waste, and housing and size explained most of the income pattern."
- *"More time?"* → "Walking distance (Zhao et al.), district recycling tonnage, on-site check of smart-bin access, counting 'no-management' buildings."

---

## 5. Limitations, ethics, teamwork  [Name: ___]

- **Biggest limitations:** counts ignore capacity and hours; one-day snapshot; n = 18 with Wan Chai influential; no distance measure; no reliable outcome data.
- **Ethics:** aggregated government data, no personal information; we don't call districts "good" or "bad" (low density may reflect where facilities were placed, not residents' failings).
- **Recommendations (none tested):** (1) measure access by type; (2) scale GREEN@COMMUNITY to population (~59 Spots, illustrative); (3) Stores near older unmanaged private buildings; (4) publish output and cost for every solution.
- **Who did what?** [Fill all 6 names and roles; make Report Section 9 and the poster match.]
