# Presentation Outline — E-Commerce Retail Analytics

## Slide 1: Title
- **Project:** E-Commerce Retail Analytics Capstone
- **Team:** Team 01
- **Date:** April 2026
- **Tagline:** "Driving Revenue & Retention Through Data-Driven Insights"

---

## Slide 2: Problem Statement
- **Question:** How can an e-commerce business improve revenue and customer retention using transaction-level data?
- **Approach:** ETL → EDA → Statistical Analysis → Business Recommendations
- **Dataset:** 541,909 transactions | 8 columns | 38 countries | Dec 2010 – Dec 2011

---

## Slide 3: Data Pipeline
- Raw data: 541,909 rows
- Dropped missing CustomerID (135K rows, 24.9%)
- Removed cancellations & duplicates (14K rows)
- Engineered features: Revenue, Year, Month, DayOfWeek, Hour
- **Clean dataset: 392,732 rows × 13 columns**

---

## Slide 4: Key Performance Indicators

| KPI | Value |
|-----|-------|
| Total Revenue | £8,887,208.89 |
| Average Order Value | £479.46 |
| Total Customers | 4,339 |
| Repeat Customer Rate | 65.6% |
| Top Product Contribution | 1.9% |

---

## Slide 5: Revenue Trends
- **Monthly trend chart** showing Q4 2011 surge
- November peak driven by holiday/Christmas shopping
- Strong growth trajectory from August–November
- December incomplete (first week only)

---

## Slide 6: Geographic Analysis
- UK = 82% of revenue (£7.29M)
- Top international: Netherlands (£285K), EIRE (£265K), Germany (£229K), France (£209K)
- **Risk:** Heavy domestic concentration
- **Opportunity:** International market expansion

---

## Slide 7: Customer Analysis
- 65.6% repeat vs 34.4% one-time customers
- Repeat customers generate vast majority of revenue
- **Statistical proof:** Welch's t-test, p < 0.001
- High-value segment: 3–5x more orders than low-value

---

## Slide 8: Product Insights
- Top 10 products contribute significant revenue share
- "PAPER CRAFT, LITTLE BIRDIE" = £168K revenue
- Right-skewed order value distribution
- Median order: ~£300 | Mean order: ~£479

---

## Slide 9: Business Recommendations
1. **Retention First:** Loyalty programs & personalized engagement
2. **Diversify Markets:** Expand into Netherlands, Germany, France
3. **Seasonal Planning:** Prepare for Q4 surge (inventory + marketing)
4. **VIP Programs:** Premium service for high-value customers
5. **Better Data:** Mandate customer identification for all transactions

---

## Slide 10: Limitations & Next Steps
**Limitations:** Single year, no cost data, missing CustomerIDs, B2B/B2C ambiguity

**Next Steps:**
- Build Tableau dashboards for interactive exploration
- Implement RFM (Recency, Frequency, Monetary) segmentation
- Develop predictive models for churn and CLV
- A/B test retention campaign strategies

---

*Thank you — Questions?*
