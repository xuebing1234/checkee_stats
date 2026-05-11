# Checkee.info 221(g) Processing Time Analysis — CS/AI Fields

Analysis of 221(g) administrative processing times for **Computer Science / AI related fields**, using self-reported case data from [checkee.info](https://www.checkee.info).

## Data Sources

1. **Bulk historical data**: [xingyaoww/checkee-dashboard](https://github.com/xingyaoww/checkee-dashboard) JSONL (46,712 cases, last scraped 2026-03-31).
2. **Fresh completed cases**: checkee.info "Last 90 Days' Complete Cases" page, saved as MHTML on 2026-05-11. Added 319 new cases and updated 343 pending-to-resolved.
3. **Merged dataset**: 47,031 total cases across all fields, all visa types, all time.

## CS/AI Field Filter

Cases are included if the self-reported major matches any of:
- Exact: `CS`, `CSE`, `EECS`, `MSCS`, `CS/AI`, `CSAI`, `AI`, `ML`, `EE/CS`
- Contains: `computer science`, `computer engineering`, `software engineer`, `artificial intelligence`, `machine learning`, `deep learning`, `data science`, `information technology`, `NLP`, `computer vision`

## Results (May 2025 – April 2026)

Only **resolved** cases (Clear or Reject) are included. Pending cases are shown for context but excluded from percentile calculations.

### All Visa Types (H1B, F1, J1, etc.)

| Month   | Total | Resolved | Pending | P25 | P50 | P75 | Mean | Max | Rej | Rej% |
|---------|-------|----------|---------|-----|-----|-----|------|-----|-----|------|
| 2025-05 | 80    | 55       | 25      | 56  | 61  | 72  | 67.7 | 301 | 0   | 0.0% |
| 2025-06 | 39    | 21       | 18      | 51  | 56  | 61  | 70.0 | 253 | 0   | 0.0% |
| 2025-07 | 39    | 26       | 13      | 38  | 43  | 50  | 45.2 | 154 | 1   | 3.8% |
| 2025-08 | 27    | 16       | 11      | 36  | 44  | 74  | 67.7 | 205 | 1   | 6.2% |
| 2025-09 | 30    | 20       | 10      | 54  | 72  | 77  | 63.8 | 104 | 0   | 0.0% |
| 2025-10 | 61    | 38       | 23      | 84  | 91  | 119 | 91.3 | 138 | 1   | 2.6% |
| 2025-11 | 70    | 46       | 24      | 97  | 106 | 112 | 99.9 | 146 | 0   | 0.0% |
| 2025-12 | 117   | 78       | 39      | 72  | 88  | 92  | 79.1 | 110 | 1   | 1.3% |
| 2026-01 | 63    | 40       | 23      | 46  | 58  | 70  | 52.0 | 84  | 1   | 2.5% |
| 2026-02 | 20    | 20       | 0       | 26  | 41  | 50  | 36.9 | 73  | 0   | 0.0% |
| 2026-03 | 32    | 32       | 0       | 19  | 29  | 34  | 25.7 | 51  | 0   | 0.0% |
| 2026-04 | 5     | 5        | 0       | 5   | 6   | 12  | 10.4 | 28  | 1   | 20.0% |
| **OVERALL** | | **397** |         | **43** | **65** | **91** | **67.2** | **301** | **6** | **1.5%** |

### H1B Only

| Month   | Total | Resolved | Pending | P25 | P50 | P75 | Mean | Max | Rej | Rej% |
|---------|-------|----------|---------|-----|-----|-----|------|-----|-----|------|
| 2025-05 | 19    | 14       | 5       | 55  | 62  | 66  | 78.0 | 301 | 0   | 0.0% |
| 2025-06 | 14    | 7        | 7       | 49  | 50  | 56  | 53.3 | 72  | 0   | 0.0% |
| 2025-07 | 9     | 6        | 3       | 38  | 42  | 49  | 43.5 | 51  | 0   | 0.0% |
| 2025-08 | 9     | 6        | 3       | 40  | 42  | 62  | 57.3 | 123 | 0   | 0.0% |
| 2025-09 | 10    | 9        | 1       | 35  | 72  | 78  | 57.9 | 104 | 0   | 0.0% |
| 2025-10 | 20    | 14       | 6       | 72  | 89  | 93  | 86.5 | 125 | 0   | 0.0% |
| 2025-11 | 33    | 23       | 10      | 104 | 106 | 112 | 99.2 | 146 | 0   | 0.0% |
| 2025-12 | 61    | 40       | 21      | 67  | 86  | 92  | 75.4 | 105 | 0   | 0.0% |
| 2026-01 | 35    | 19       | 16      | 31  | 56  | 66  | 49.8 | 84  | 0   | 0.0% |
| 2026-02 | 11    | 11       | 0       | 14  | 38  | 48  | 33.9 | 73  | 0   | 0.0% |
| 2026-03 | 9     | 9        | 0       | 14  | 31  | 31  | 23.7 | 39  | 0   | 0.0% |
| 2026-04 | 5     | 5        | 0       | 5   | 6   | 12  | 10.4 | 28  | 1   | 20.0% |
| **OVERALL** | | **163** |         | **38** | **66** | **92** | **65.6** | **301** | **1** | **0.6%** |

### Key Findings

- **H1B CS/AI median wait: ~66 days** (P25=38, P75=92). Most cases resolve in 5–13 weeks.
- **1 H1B rejection** in CS/AI (Major="Csai", Beijing, Apr 2026 — cleared in 1 day, likely an immediate refusal rather than processing).
- **Overall rejection rate: 1.5%** (6 out of 397 resolved cases).
- Oct–Nov 2025 cohort had the longest waits (P50=91–106 days), likely seasonal backlog.
- Feb–Apr 2026 show shorter waits but these are early resolvers — longer cases from those months are still pending.

### Rejected Cases Detail

| Visa | Major | Check Date | Complete Date | Wait (days) | Consulate |
|------|-------|------------|---------------|-------------|-----------|
| H1   | Csai  | 2026-04-23 | 2026-04-24    | 1           | BeiJing   |
| J1   | Computer Science | 2026-01-02 | 2026-01-07 | 5 | BeiJing |
| J1   | Computer Science | 2025-12-12 | 2026-03-09 | 87 | ShangHai |
| F1   | EECS  | 2025-10-22 | 2025-10-22    | 0           | ShangHai  |
| F1   | CS    | 2025-08-14 | 2025-11-13    | 91          | BeiJing   |
| F1   | CS    | 2025-07-06 | 2025-07-09    | 3           | ShangHai  |

## Usage

```bash
python3 analyze.py
```

On first run, the script downloads the JSONL dataset (~14 MB) from GitHub into `data/`. Subsequent runs use the cached file. Output CSVs are written to `output/`.

To refresh with the latest completed cases, save checkee.info's "Last 90 Days' Complete Cases" page as `data/Check Reporter.mhtml` and re-run — the script will automatically merge it.

## Caveats

1. **Self-reported data** — checkee.info is community-driven; there may be reporting bias.
2. **Right-censoring** — recent months' stats skew low because only fast-resolving cases are counted; slow ones are still pending.
3. **Field classification** — majors are free-text; our keyword filter catches common variants but may miss unusual phrasings.
4. **Cloudflare** — checkee.info added Cloudflare protection in ~May 2026, blocking automated scraping of detail pages. The MHTML approach (manual save) is a workaround.
