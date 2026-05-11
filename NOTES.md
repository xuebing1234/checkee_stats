# Session Notes — 2026-05-11

## What was done

### Goal
Analyze 221(g) administrative processing times for CS/AI-related fields from checkee.info, focusing on H1B visa cases over the past 12 months (May 2025 – April 2026).

### Approach
1. **Attempted direct scraping** of checkee.info detail pages (`main.php`). All automated attempts blocked by Cloudflare protection (added ~May 2026). The xingyaoww/checkee-dashboard scraper that previously worked has also been failing since May 6.
2. **Downloaded bulk historical data** from [xingyaoww/checkee-dashboard](https://github.com/xingyaoww/checkee-dashboard) JSONL (46,712 cases, last scraped 2026-03-31). Data only covered through 2026-01.
3. **Supplemented with fresh data** by manually saving checkee.info's "Last 90 Days' Complete Cases" page as MHTML. Parsed and merged: +319 new cases, +343 updated (Pending -> resolved). Final dataset: 47,031 cases.
4. **Built `analyze.py`** with filters for CS/AI (broad) and CS PhD (narrow), per-month percentile distributions, rejection rates, and CSV output.

### Key findings — CS/AI H1B
- **Median wait: ~66 days** (P25=38, P75=92)
- **1 rejection** out of 163 resolved (0.6%) — "Csai" major, Beijing, immediate 1-day turnaround
- Oct–Nov 2025 had longest waits (P50=89–106 days)

### Key findings — CS PhD (all visa types)
- **Only 24 resolved cases** — too sparse for reliable stats
- **Median wait: ~69 days** (P25=48, P75=99), zero rejections
- H1B CS PhD: only 3 resolved cases (median 92 days)

### Files
- `analyze.py` — analysis script with MHTML merge, CS/AI + CS PhD filters
- `data/checkee_data.jsonl` — merged dataset (47,031 cases)
- `data/Check Reporter.mhtml` — raw 90-day completed cases page
- `output/cs_ai_all_visas.csv` / `cs_ai_h1b_only.csv`
- `output/cs_phd_all_visas.csv` / `cs_phd_h1b_only.csv`

## To pick up next time
- **Refresh data**: save a new "Last 90 Days' Complete Cases" MHTML from checkee.info, replace `data/Check Reporter.mhtml`, re-run `python3 analyze.py`
- **Monthly pages**: if Cloudflare protection is lifted, download individual monthly pages for more complete data (the MHTML only covers completed cases, not pending ones)
- **Possible extensions**: filter by consulate, add EE/ECE comparison, visualizations
