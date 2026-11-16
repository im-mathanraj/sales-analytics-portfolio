"""Run from any directory with Python 3.8+. Standard library only."""
from pathlib import Path
import csv
import datetime
import json
import sqlite3

ROOT = Path(__file__).resolve().parent
with (ROOT / "data/sales.csv").open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    expected = ["order_id", "order_date", "region", "category", "quantity", "revenue", "cost", "profit"]
    if reader.fieldnames != expected:
        raise ValueError("Unexpected CSV columns")
    rows = list(reader)
if not rows or len({r["order_id"] for r in rows}) != len(rows):
    raise ValueError("Empty data or duplicate order IDs")
for row in rows:
    if any(value is None or value == "" for value in row.values()):
        raise ValueError("Missing value")
    datetime.date.fromisoformat(row["order_date"])
    for key in ["quantity", "revenue", "cost", "profit"]:
        row[key] = int(row[key])
    if row["quantity"] <= 0 or row["revenue"] < 0 or row["cost"] < 0:
        raise ValueError("Invalid quantity or amount")
    if row["revenue"] - row["cost"] != row["profit"]:
        raise ValueError("Profit does not reconcile")
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE sales (order_id TEXT PRIMARY KEY, order_date TEXT, region TEXT, category TEXT, quantity INTEGER, revenue INTEGER, cost INTEGER, profit INTEGER)")
db.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?,?,?,?)", [tuple(r[k] for k in expected) for r in rows])
db.row_factory = sqlite3.Row
results = []
for statement in (ROOT / "analysis.sql").read_text(encoding="utf-8").split(";"):
    if statement.strip():
        results.append([dict(r) for r in db.execute(statement)])
# Reconcile independent Python aggregates with SQL output.
overall = results[0][0]
if overall["orders"] != len(rows) or overall["revenue"] != sum(r["revenue"] for r in rows) or overall["gross_profit"] != sum(r["profit"] for r in rows):
    raise ValueError("SQL and source totals differ")
for result in results[1:3]:
    if sum(r["revenue"] for r in result) != overall["revenue"]:
        raise ValueError("Segment totals differ")
if sum(r["revenue"] for r in results[3]) != overall["revenue"]:
    raise ValueError("Monthly totals differ")
print("PASS: unique IDs, required fields, dates, numeric values, profit and SQL totals.")
for title, result in zip(["Overview", "Categories", "Regions", "Monthly growth"], results):
    print("\n" + title)
    print(json.dumps(result, indent=2))
db.close()
