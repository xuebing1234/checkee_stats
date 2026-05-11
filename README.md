# Checkee.info 221(g) Processing Time Analysis — CS/AI Fields

Analysis of 221(g) administrative processing times for **Computer Science / AI related fields**, using self-reported case data from [checkee.info](https://www.checkee.info).

## Data Source

- **Raw data**: [xingyaoww/checkee-dashboard](https://github.com/xingyaoww/checkee-dashboard) — a project that scrapes checkee.info daily and stores cases as JSONL.
- **Dataset**: 46,712 total cases (all fields, all visa types, all time)
- **Last scraped**: 2026-03-31

## CS/AI Field Filter

Cases are included if the self-reported major matches any of:
- Exact: `CS`, `CSE`, `EECS`, `MSCS`, `CS/AI`, `AI`, `ML`, `EE/CS`
- Contains: `computer science`, `computer engineering`, `software engineer`, `artificial intelligence`, `machine learning`, `deep learning`, `data science`, `information technology`, `NLP`, `computer vision`

**9,776 total CS/AI cases** found across all time periods.

## Results (May 2025 – April 2026)

Only **resolved** cases (Clear or Reject) are included. Pending cases are shown for context but excluded from percentile calculations.

### All Visa Types (H1B, F1, J1, etc.)

| Month   | Total | Resolved | Pending | P25 | P50 | P75 | Mean | Max | Rej | Rej% |
|---------|-------|----------|---------|-----|-----|-----|------|-----|-----|------|
| 2025-05 | 80    | 54       | 26      | 55  | 61  | 72  | 63.4 | 112 | 0   | 0.0% |
| 2025-06 | 39    | 20       | 19      | 51  | 56  | 59  | 60.9 | 145 | 0   | 0.0% |
| 2025-07 | 39    | 26       | 13      | 38  | 43  | 50  | 45.2 | 154 | 1   | 3.8% |
| 2025-08 | 27    | 14       | 13      | 31  | 42  | 56  | 49.0 | 123 | 1   | 7.1% |
| 2025-09 | 31    | 20       | 11      | 54  | 72  | 77  | 63.8 | 104 | 0   | 0.0% |
| 2025-10 | 59    | 26       | 33      | 66  | 88  | 91  | 75.2 | 100 | 1   | 3.8% |
| 2025-11 | 57    | 5        | 52      | 14  | 25  | 52  | 29.2 | 54  | 0   | 0.0% |
| 2025-12 | 100   | 12       | 88      | 22  | 33  | 44  | 37.4 | 85  | 0   | 0.0% |
| 2026-01 | 62    | 33       | 29      | 34  | 56  | 63  | 47.1 | 77  | 1   | 3.0% |
| **OVERALL** | | **210** |         | **43** | **57** | **71** | **56.6** | **154** | **4** | **1.9%** |

### H1B Only

| Month   | Total | Resolved | Pending | P25 | P50 | P75 | Mean | Max | Rej | Rej% |
|---------|-------|----------|---------|-----|-----|-----|------|-----|-----|------|
| 2025-05 | 19    | 13       | 6       | 55  | 61  | 64  | 60.8 | 91  | 0   | 0.0% |
| 2025-06 | 14    | 7        | 7       | 49  | 50  | 56  | 53.3 | 72  | 0   | 0.0% |
| 2025-07 | 9     | 6        | 3       | 38  | 42  | 49  | 43.5 | 51  | 0   | 0.0% |
| 2025-08 | 9     | 6        | 3       | 40  | 42  | 62  | 57.3 | 123 | 0   | 0.0% |
| 2025-09 | 10    | 9        | 1       | 35  | 72  | 78  | 57.9 | 104 | 0   | 0.0% |
| 2025-10 | 20    | 12       | 8       | 68  | 87  | 93  | 80.7 | 93  | 0   | 0.0% |
| 2025-11 | 26    | 3        | 23      | 8   | 14  | 20  | 13.3 | 25  | 0   | 0.0% |
| 2025-12 | 56    | 9        | 47      | 22  | 31  | 47  | 38.1 | 85  | 0   | 0.0% |
| 2026-01 | 35    | 16       | 19      | 25  | 53  | 62  | 45.3 | 77  | 0   | 0.0% |
| **OVERALL** | | **81**  |         | **37** | **55** | **70** | **53.9** | **123** | **0** | **0.0%** |

### Key Findings

- **H1B CS/AI median wait: ~55 days** (P25=37, P75=70). Typical range is 5–10 weeks.
- **Zero H1B rejections** in CS/AI for the entire 12-month window.
- **Overall rejection rate: 1.9%** (4 out of 210 resolved cases, all F1/J1).
- Nov 2025–Jan 2026 show lower medians but high pending counts — these are **right-censored** (data scraped 2026-03-31, many cases still in progress).
- Feb–Apr 2026 show no data because those cases haven't resolved yet.

### Rejected Cases Detail

| Visa | Major | Month | Wait (days) | Consulate |
|------|-------|-------|-------------|-----------|
| J1   | Computer Science | 2026-01 | 5 | BeiJing |
| F1   | EECS | 2025-10 | 0 | ShangHai |
| F1   | CS | 2025-08 | 91 | BeiJing |
| F1   | CS | 2025-07 | 3 | ShangHai |

## Usage

```bash
python3 analyze.py
```

On first run, the script downloads the JSONL dataset (~14 MB) from GitHub into `data/`. Subsequent runs use the cached file. Output CSVs are written to `output/`.

## Caveats

1. **Self-reported data** — checkee.info is community-driven; there may be reporting bias (people with longer waits may be more likely to report).
2. **Right-censoring** — recent months show artificially low wait times because many cases are still pending.
3. **Field classification** — majors are free-text; our keyword filter catches common variants but may miss unusual phrasings.
4. **Scrape date** — the dataset was last scraped 2026-03-31. Cases filed after that date are not included.
