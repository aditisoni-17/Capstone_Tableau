# Project Report — E-Commerce Retail Analytics

## 1. Executive Summary

This capstone project analyzes a year's worth of transactional data from an online retail company to uncover actionable insights for improving revenue and customer retention. Using 541,909 raw transaction records, we cleaned, explored, and statistically analyzed the data to identify key revenue drivers, customer behavior patterns, and growth opportunities.

**Key findings:**
- Total revenue of **£8.89M** across **4,339 unique customers** and **18,532 orders**.
- **65.6% of customers are repeat buyers**, generating the vast majority of revenue.
- The **United Kingdom accounts for 82%** of total revenue, with Netherlands, Ireland, Germany, and France as top international markets.
- Revenue peaks during **November** (holiday season) and during **mid-week business hours** (10 AM – 3 PM).
- Statistical testing confirms repeat customers generate **significantly more revenue** than one-time buyers (p < 0.001).

---

## 2. Problem Statement

> *"How can an e-commerce business improve revenue and customer retention using transaction-level data?"*

This project addresses this question by:
1. Building a robust ETL pipeline for data quality
2. Performing exploratory analysis to identify revenue patterns
3. Conducting statistical tests to validate business hypotheses
4. Segmenting customers for targeted strategies
5. Preparing Tableau-ready datasets for dashboard visualization

---

## 3. Dataset Description

| Attribute | Detail |
|-----------|--------|
| **Source** | UCI Machine Learning Repository / Kaggle |
| **Name** | Online Retail Dataset |
| **Records** | 541,909 transactions |
| **Period** | December 2010 – December 2011 |
| **Columns** | 8 (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) |
| **Geography** | 38 countries (predominantly UK) |
| **Business Type** | Online retail / wholesale (B2B + B2C) |

---

## 4. Cleaning Methodology

| Step | Action | Impact |
|------|--------|--------|
| 1 | Drop rows with missing CustomerID | Removed 135,080 rows (24.9%) |
| 2 | Remove negative/zero Quantity | Removed 8,905 cancellation/return rows |
| 3 | Remove exact duplicates | Removed 5,192 duplicate records |
| 4 | Convert InvoiceDate to datetime | Enabled time-series analysis |
| 5 | Convert CustomerID to integer | Standardized data type |
| 6 | Create Revenue column (Qty × Price) | Enabled revenue analysis |
| 7 | Extract time features (Year, Month, Day, Hour) | Enabled temporal analysis |

**Final cleaned dataset:** 392,732 rows × 13 columns

---

## 5. EDA Insights

1. **Seasonal Revenue Surge:** Revenue increases dramatically from August to November 2011, peaking in November — driven by pre-Christmas/holiday purchasing.

2. **Product Concentration:** The top 10 products generate a disproportionate share of revenue. "PAPER CRAFT, LITTLE BIRDIE" leads with ~£168K in revenue.

3. **UK Dominance:** United Kingdom accounts for ~82% of total revenue. The business is heavily dependent on a single domestic market.

4. **International Opportunities:** Netherlands (£285K), Ireland (£265K), Germany (£229K), and France (£209K) represent significant international growth opportunities.

5. **Right-Skewed Orders:** Order value distribution is heavily right-skewed — median ~£300 vs mean ~£479 — indicating a small number of high-value orders.

6. **Repeat Customer Power:** 65.6% of customers are repeat buyers, and they drive the overwhelming majority of revenue.

7. **Mid-Week Peak:** Thursday generates the highest revenue. No Saturday transactions occur, suggesting a B2B-oriented business model.

8. **Business Hours Activity:** Peak ordering occurs between 10 AM – 3 PM, consistent with B2B purchasing behavior during working hours.

9. **Customer Lifetime Value Variance:** High-value customers (above median revenue) have 3–5x higher order frequency than low-value customers.

10. **Data Quality Gap:** 24.9% of transactions lack CustomerID, representing a significant data collection improvement opportunity.

---

## 6. Statistical Findings

### 6.1 Correlation Analysis
- **Quantity ↔ Revenue:** Strong positive correlation — higher quantities drive higher revenue.
- **OrderCount ↔ TotalRevenue (customer level):** Strong positive correlation — frequent buyers are the highest-value customers.
- **UnitPrice ↔ Quantity:** Weak negative correlation — bulk orders tend to have lower unit prices (volume discounts).

### 6.2 Hypothesis Test
- **H₀:** No significant difference in revenue between repeat and one-time customers.
- **H₁:** Repeat customers generate significantly more revenue.
- **Result:** H₀ rejected (p < 0.001, Welch's t-test). Repeat customers generate statistically and practically significantly more revenue.
- **Cohen's d:** Indicates a meaningful practical effect size.

### 6.3 Customer Segmentation
- **High-Value Customers:** Higher repeat rates, higher order frequency, and contribute disproportionately more revenue.
- **Low-Value Customers:** Primarily one-time buyers with low engagement — candidates for re-engagement campaigns.

---

## 7. Business Recommendations

### 7.1 Invest in Customer Retention Programs
With 65.6% repeat rate and statistical proof that repeat customers drive significantly more revenue, implement loyalty programs, personalized email campaigns, and tiered rewards to nurture existing customers.

### 7.2 Reduce UK Revenue Dependency
82% UK concentration creates market risk. Develop targeted marketing campaigns for top international markets (Netherlands, Ireland, Germany, France) to diversify the revenue base.

### 7.3 Capitalize on Seasonal Peaks
Revenue surges 2–3x in Q4 (October–November). Plan inventory, marketing, and staffing well in advance of the holiday season to maximize peak-period revenue capture.

### 7.4 Focus on High-Value Customer Segment
Implement VIP/premium service tiers for high-value customers. These customers have 3–5x higher order frequency — even small improvements in their retention or average order value yield outsized revenue gains.

### 7.5 Improve Data Collection Practices
24.9% of transactions lack CustomerID. Implement mandatory customer identification (accounts, loyalty cards) to enable better analytics, personalization, and customer relationship management.

---

## 8. Limitations

1. **Missing CustomerID:** 24.9% of transactions could not be used for customer-level analysis, potentially biasing customer behavior insights.

2. **Single Year of Data:** The dataset covers approximately 12 months (Dec 2010 – Dec 2011). Year-over-year trend analysis is not possible.

3. **No Cost/Profit Data:** Revenue analysis only — without cost-of-goods data, profitability analysis is not feasible.

4. **No Marketing Data:** Cannot correlate revenue trends with marketing campaigns, promotions, or advertising spend.

5. **Geographic Bias:** Heavy UK concentration means international insights are based on smaller sample sizes.

6. **Product Description Quality:** Some product descriptions are inconsistent or missing, limiting product-level analysis accuracy.

7. **B2B vs B2C Ambiguity:** The dataset likely contains a mix of wholesale (B2B) and retail (B2C) transactions that cannot be reliably distinguished.

---

## 9. Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.x | Primary analysis language |
| pandas | Data manipulation and aggregation |
| NumPy | Numerical computations |
| Matplotlib | Static visualizations |
| Seaborn | Statistical visualizations |
| SciPy | Statistical testing |
| Jupyter Notebook | Interactive analysis environment |
| Tableau | Dashboard visualization (data prep only) |
| Git/GitHub | Version control and collaboration |

---

*Report prepared by Team 01 — April 2026*
