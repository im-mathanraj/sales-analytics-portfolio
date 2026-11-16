# Retail Sales Analytics Portfolio

A beginner-friendly analytics project answering: **Which categories and regions drive revenue and gross profit, and how does revenue change month to month?**

**Tools:** SQL (SQLite), Python standard library, CSV/Excel, and an offline HTML dashboard.

> Uses 1,200 synthetic orders for 2025, not actual customer or company data. Created with AI assistance as a learning project.

## Results
- Revenue: **INR 4,176,212**
- Gross profit: **INR 834,746**
- Gross margin: **19.99%**
- Electronics leads revenue; Clothing leads gross profit.

Read [findings and limitations](FINDINGS.md).

## View the dashboard
1. Click **Code → Download ZIP** on this repository.
2. Extract the ZIP.
3. Open **dashboard.html** in Chrome, Edge or Firefox.
4. Filter by region or category; reset to see all orders.

The HTML works offline and embeds the same dataset as the CSV. GitHub displays HTML source rather than running it; download it to view the dashboard. This is an HTML dashboard, not a Power BI report.

## Run the SQL analysis
Install Python 3.8 or later, then run from the extracted folder:

```bash
python analyze.py
```

On Windows, `py analyze.py` may also work. No third-party packages are needed. The script imports the CSV into an in-memory SQLite database, validates records and executes all queries in analysis.sql. It prints overall, category, regional and monthly results.

## Files
| File | Purpose |
|---|---|
| [data/sales.csv](data/sales.csv) | 1,200 synthetic order records |
| [analysis.sql](analysis.sql) | Aggregations, CTE and LAG for monthly growth |
| [analyze.py](analyze.py) | Load, validate and analyse the data |
| [dashboard.html](dashboard.html) | Offline dashboard with filters |
| [FINDINGS.md](FINDINGS.md) | Results, recommendations and limitations |
| [LEARNING_GUIDE.md](LEARNING_GUIDE.md) | Exercises and interview preparation |

## Data dictionary
| Field | Meaning |
|---|---|
| order_id | Unique identifier; each order has exactly one line |
| order_date | Order date in 2025 |
| region | North, South, East or West |
| category | Electronics, Home or Clothing |
| quantity | Units sold, 1–5 |
| revenue | Sales after discount, rounded to whole INR |
| cost | Direct product cost, whole INR |
| profit | revenue minus cost |

## Method
Generated deterministically using seed 42 and a 32-bit linear congruential generator (multiplier 1664525, increment 1013904223). For each order, draws select month, category, region, quantity, discount and day, in that order. List prices are 2400/900/600 for Electronics/Home/Clothing; cost rates are 82%/68%/55%. Discounts are sampled from 0–15%, with dates limited to days 1–28. Regions and months are sampled uniformly. This creates a clean learning dataset; it does not demonstrate cleaning real-world messy records.

Gross margin = SUM(profit) / SUM(revenue), not average row margin. Gross profit excludes overhead, tax, shipping and returns.

## Validation
Checks cover unique order IDs, required values, dates, numeric values, profit reconciliation and Python-versus-SQL aggregate totals. The dashboard and CSV share the same source records. Runtime validation can be reproduced using analyze.py.

## Portfolio use
Study and rebuild the analysis before presenting these skills in an interview. Describe it as a synthetic, AI-assisted personal project and explain your own contributions accurately.
