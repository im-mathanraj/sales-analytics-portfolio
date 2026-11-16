# Findings and business interpretation

All amounts below are INR from **synthetic practice data**, not a real business.

| Metric | Value |
|---|---:|
| Orders (one line per order) | 1,200 |
| Revenue after discount | 4,176,212 |
| Direct product cost | 3,341,466 |
| Gross profit | 834,746 |
| Gross margin | 19.99% |

## What the data shows
1. **Electronics leads revenue:** 2,459,235, or 58.9% of total revenue. Its gross profit is 280,659.
2. **Clothing leads gross profit:** 294,872 from 729,482 revenue. Its 40.4% gross margin exceeds Electronics' 11.4%. Revenue rank and profit rank differ.
3. **West leads regional revenue:** 1,118,836. This alone does not show greater efficiency; customer counts, operating expenses and acquisition costs are unavailable.

## Hypothetical next actions
- Investigate demand, stock availability and item-level profitability before changing the product mix.
- Review discount levels alongside margin; do not assume removing discounts will increase profit without measuring demand.
- Investigate regional customer counts and operating costs before reallocating budgets.
- Use monthly growth as a prompt for investigation, not proof of seasonality.

## Limits
The generator randomly samples months, regions, categories and quantities. Category prices and costs are fixed, with random discounts up to 15%. The resulting differences are partly built into the generation rules and are not independent market discoveries. No customer retention, causal impact, returns, overhead, tax, shipping or multi-year trends can be measured.
