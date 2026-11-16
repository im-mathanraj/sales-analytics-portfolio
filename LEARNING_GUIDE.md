# Learn this project before using it in interviews

1. Open data/sales.csv in Excel. Calculate total revenue using SUM and verify 4,176,212.
2. Create a PivotTable: category in Rows, revenue and profit in Values. Compare with FINDINGS.md.
3. Read the first query in analysis.sql. Explain COUNT(DISTINCT), SUM and NULLIF.
4. Run analyze.py. Check that all four result sections appear.
5. Explain why Clothing has more gross profit than Electronics despite lower revenue.
6. Change the regional query to rank by gross profit. Explain the difference.
7. Explain LAG and why January has no month-over-month growth rate.
8. Filter the dashboard to one region. Independently check those totals in Excel.
9. Add a new SQL question, such as revenue per order by category. Update the findings yourself.
10. Explain limitations: synthetic generation, one year, no returns or overhead, no customer identifiers.

## Interview explanation template
"I explored a synthetic retail dataset to compare revenue and gross profit across categories and regions. I used SQL aggregations and a window function for monthly growth, validated the totals, and explored the results in a filtered dashboard. Electronics led revenue, while Clothing led gross profit. Because the data is synthetic and excludes overhead, these are practice insights rather than real business recommendations."

Use this wording only after you understand the work. Be explicit about AI assistance and your own changes.
