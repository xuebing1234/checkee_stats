#!/usr/bin/env python3
"""
Analyze 221(g) administrative processing times for CS/AI-related fields
using data from checkee.info (via xingyaoww/checkee-dashboard).

Data source: https://github.com/xingyaoww/checkee-dashboard
"""

import json
import re
import csv
import sys
import os
from collections import defaultdict
from urllib.request import urlretrieve

DATA_URL = "https://raw.githubusercontent.com/xingyaoww/checkee-dashboard/main/public/data/checkee_data.jsonl"
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "checkee_data.jsonl")


def is_cs_ai(major: str) -> bool:
    m = major.strip().lower()
    if m in ("cs", "cse", "eecs", "mscs", "cs/ai", "ai", "ml", "cs phd", "ee/cs"):
        return True
    keywords = [
        "computer science",
        "computer engineering",
        "software engineer",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "data science",
        "information technology",
        "natural language processing",
        "nlp",
        "computer vision",
        "software development",
    ]
    for kw in keywords:
        if kw in m:
            return True
    if re.match(r"^cs\b", m):
        return True
    if m == "computer":
        return True
    return False


def percentile(data: list[float], p: float) -> float:
    data_sorted = sorted(data)
    n = len(data_sorted)
    k = (n - 1) * p / 100
    f = int(k)
    c = k - f
    if f + 1 < n:
        return data_sorted[f] + c * (data_sorted[f + 1] - data_sorted[f])
    return data_sorted[f]


def download_data():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        print(f"Downloading data from {DATA_URL} ...")
        urlretrieve(DATA_URL, DATA_FILE)
        print(f"Saved to {DATA_FILE}")
    else:
        print(f"Using cached data: {DATA_FILE}")


def load_cases():
    cases = []
    with open(DATA_FILE) as f:
        for line in f:
            cases.append(json.loads(line))
    return cases


def analyze(cases, target_months, visa_filter=None):
    monthly_clear = defaultdict(list)
    monthly_reject = defaultdict(list)
    monthly_pending = defaultdict(int)
    monthly_total = defaultdict(int)

    for rec in cases:
        if not is_cs_ai(rec.get("major", "")):
            continue
        month = rec.get("month", "")
        if month not in target_months:
            continue
        if visa_filter and rec.get("visa_type", "") != visa_filter:
            continue

        status = rec.get("status", "")
        try:
            days = int(rec.get("waiting_days", 0))
        except (ValueError, TypeError):
            days = 0

        monthly_total[month] += 1
        if status == "Clear":
            monthly_clear[month].append(days)
        elif status == "Reject":
            monthly_reject[month].append(days)
        else:
            monthly_pending[month] += 1

    return monthly_clear, monthly_reject, monthly_pending, monthly_total


def print_table(monthly_clear, monthly_reject, monthly_pending, monthly_total, target_months, label):
    print()
    print("=" * 120)
    print(label)
    print("=" * 120)
    header = f"{'Month':<10} {'Total':>6} {'Resolved':>9} {'Pending':>8} {'P25':>5} {'P50':>5} {'P75':>5} {'Mean':>6} {'Max':>5} {'Rej':>4} {'Rej%':>6}"
    print(header)
    print("-" * 120)

    all_resolved_days = []
    total_rej = 0
    rows = []

    for month in sorted(target_months):
        clears = monthly_clear.get(month, [])
        rejects = monthly_reject.get(month, [])
        pending = monthly_pending.get(month, 0)
        total = monthly_total.get(month, 0)
        resolved = clears + rejects
        n_res = len(resolved)
        n_rej = len(rejects)
        total_rej += n_rej
        all_resolved_days.extend(resolved)

        if n_res >= 3:
            p25 = percentile(resolved, 25)
            p50 = percentile(resolved, 50)
            p75 = percentile(resolved, 75)
            mean_d = sum(resolved) / len(resolved)
            max_d = max(resolved)
            rej_pct = n_rej / n_res * 100
            print(f"{month:<10} {total:>6} {n_res:>9} {pending:>8} {p25:>5.0f} {p50:>5.0f} {p75:>5.0f} {mean_d:>6.1f} {max_d:>5} {n_rej:>4} {rej_pct:>5.1f}%")
            rows.append([month, total, n_res, pending, f"{p25:.0f}", f"{p50:.0f}", f"{p75:.0f}", f"{mean_d:.1f}", max_d, n_rej, f"{rej_pct:.1f}%"])
        elif n_res > 0:
            mean_d = sum(resolved) / len(resolved)
            max_d = max(resolved)
            rej_pct = n_rej / n_res * 100
            print(f"{month:<10} {total:>6} {n_res:>9} {pending:>8}   n/a   n/a   n/a {mean_d:>6.1f} {max_d:>5} {n_rej:>4} {rej_pct:>5.1f}%")
            rows.append([month, total, n_res, pending, "n/a", "n/a", "n/a", f"{mean_d:.1f}", max_d, n_rej, f"{rej_pct:.1f}%"])
        else:
            print(f"{month:<10} {total:>6} {0:>9} {pending:>8}     -     -     -      -     -    -      -")
            rows.append([month, total, 0, pending, "-", "-", "-", "-", "-", "-", "-"])

    print("-" * 120)
    if all_resolved_days:
        op25 = percentile(all_resolved_days, 25)
        op50 = percentile(all_resolved_days, 50)
        op75 = percentile(all_resolved_days, 75)
        omean = sum(all_resolved_days) / len(all_resolved_days)
        omax = max(all_resolved_days)
        orej = total_rej / len(all_resolved_days) * 100
        print(f"{'OVERALL':<10} {'':>6} {len(all_resolved_days):>9} {'':>8} {op25:>5.0f} {op50:>5.0f} {op75:>5.0f} {omean:>6.1f} {omax:>5} {total_rej:>4} {orej:>5.1f}%")
        rows.append(["OVERALL", "", len(all_resolved_days), "", f"{op25:.0f}", f"{op50:.0f}", f"{op75:.0f}", f"{omean:.1f}", omax, total_rej, f"{orej:.1f}%"])

    return rows


def write_csv(rows, filename, header):
    path = os.path.join(os.path.dirname(__file__), "output", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"\nWritten to {path}")


def main():
    download_data()
    cases = load_cases()
    print(f"Loaded {len(cases)} total cases")

    target_months = []
    for y in range(2025, 2027):
        for m in range(1, 13):
            ms = f"{y}-{m:02d}"
            if "2025-05" <= ms <= "2026-04":
                target_months.append(ms)

    csv_header = ["Month", "Total", "Resolved", "Pending", "P25", "P50", "P75", "Mean", "Max", "Rejected", "Rej%"]

    # All visa types
    mc, mr, mp, mt = analyze(cases, target_months)
    rows_all = print_table(mc, mr, mp, mt, target_months,
                           "CS/AI FIELD — ALL VISA TYPES (data: checkee.info)")
    write_csv(rows_all, "cs_ai_all_visas.csv", csv_header)

    # H1B only
    mc, mr, mp, mt = analyze(cases, target_months, visa_filter="H1")
    rows_h1 = print_table(mc, mr, mp, mt, target_months,
                           "CS/AI FIELD — H1B VISA ONLY")
    write_csv(rows_h1, "cs_ai_h1b_only.csv", csv_header)

    # Print rejected cases
    print("\n--- Rejected CS/AI Cases (all visa types, past 12 months) ---")
    for rec in cases:
        if not is_cs_ai(rec.get("major", "")):
            continue
        if rec.get("month", "") not in target_months:
            continue
        if rec.get("status") == "Reject":
            print(f"  Visa={rec['visa_type']}, Major={rec['major']}, Month={rec['month']}, "
                  f"Wait={rec['waiting_days']}d, Consulate={rec['us_consulate']}")


if __name__ == "__main__":
    main()
