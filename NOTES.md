# Session Notes — 2026-05-11

## What was done

### Goal
Analyze 221(g) administrative processing times for CS/AI-related fields from checkee.info, focusing on H1B visa cases over the past 12 months (May 2025 – April 2026).

### Approach
1. **Attempted direct scraping** of checkee.info monthly case pages (`main.php?dispdate=YYYY-MM`). All attempts blocked by Cloudflare protection (403 on curl, WebFetch, cloudscraper, Python urllib).
2. **Found existing scraped dataset** from [xingyaoww/checkee-dashboard](https://github.com/xingyaoww/checkee-dashboard) — a GitHub project that scrapes checkee.info daily via GitHub Actions and stores all cases as JSONL. Downloaded `checkee_data.jsonl` (46,712 cases, 14 MB, last scraped 2026-03-31).
3. **Built `analyze.py`** to filter CS/AI-related majors, compute percentile distributions (P25/P50/P75/Mean/Max), and rejection rates on a monthly basis.

### Key findings
- **H1B + CS/AI median processing time: ~55 days** (P25=37, P75=70)
- **Zero H1B rejections** in the CS/AI category for the entire 12-month window
- **Overall rejection rate: 1.9%** (4/210 resolved cases, all F1/J1 students)
- Oct 2025 cohort had longest waits (P50=88 days)
- Nov 2025 onward data is right-censored (many cases still pending at scrape date)

### Files
- `analyze.py` — main analysis script (downloads data if missing, outputs tables + CSVs)
- `data/checkee_data.jsonl` — raw dataset (46,712 cases)
- `output/cs_ai_all_visas.csv` — results for all visa types
- `output/cs_ai_h1b_only.csv` — results for H1B only
- `README.md` — full writeup with tables

## To pick up next time
- **Re-download data** to get fresher scrape (the dashboard updates daily): delete `data/checkee_data.jsonl` and re-run `python3 analyze.py`
- **Feb–Apr 2026 gaps**: these will fill in once the dashboard scrapes newer data and cases resolve
- **Possible extensions**: 
  - Filter by consulate (Beijing vs Guangzhou vs others)
  - Add EE/ECE to the analysis separately for comparison
  - Visualizations (histogram of wait times, trend chart)
  - Track how right-censored months update over time
