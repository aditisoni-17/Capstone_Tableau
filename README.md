# E-Commerce Retail Analytics — Capstone Project

> **Team 01** | April 2026

## 📌 Project Overview

This project analyzes the **Online Retail Dataset** (UCI/Kaggle) containing 541,909 e-commerce transactions to answer:

> *"How can an e-commerce business improve revenue and customer retention using transaction-level data?"*

We built a complete end-to-end analytics pipeline — from raw data extraction through cleaning, exploratory analysis, statistical testing, and Tableau-ready data preparation.

### Key Results
- **£8.89M** total revenue across **4,339 customers**
- **65.6%** repeat customer rate
- Repeat customers generate **statistically significantly** more revenue (p < 0.001)
- **United Kingdom** accounts for **82%** of revenue
- **Q4 (Nov)** is the peak revenue period

---

## 📁 Folder Structure

```
EcomAnalytics_Team01_Capstone/
│
├── README.md                          ← You are here
├── data/
│   ├── raw/                           ← Original dataset (never modified)
│   │   └── data.csv
│   └── processed/                     ← Cleaned & aggregated outputs
│       ├── cleaned_data.csv
│       ├── kpi_summary.csv
│       ├── monthly_revenue_summary.csv
│       ├── product_summary.csv
│       ├── country_summary.csv
│       ├── customer_summary.csv
│       └── day_hour_revenue.csv
│
├── notebooks/
│   ├── 01_extraction.ipynb            ← Data loading & inspection
│   ├── 02_cleaning.ipynb              ← Data cleaning & transformation
│   ├── 03_eda.ipynb                   ← Exploratory Data Analysis
│   ├── 04_statistical_analysis.ipynb  ← Hypothesis tests & segmentation
│   ├── 05_final_load_prep.ipynb       ← Tableau data preparation
│   └── 06_rfm_segmentation.ipynb      ← RFM customer segmentation analysis
│
├── scripts/
│   └── etl_pipeline.py                ← Modular, reusable ETL pipeline
│
├── tableau/
│   ├── screenshots/                   ← Dashboard screenshots
│   └── dashboard_links.md             ← Links to published dashboards
│
├── reports/
│   ├── project_report.md              ← Full project report
│   └── presentation.md                ← Presentation slide outline
│
└── docs/
    └── data_dictionary.md             ← Column definitions & metadata
```

---

## 📊 Dataset Information

| Attribute | Detail |
|-----------|--------|
| **Source** | [Kaggle — E-Commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data) |
| **Original Size** | 541,909 rows × 8 columns |
| **Cleaned Size** | 392,732 rows × 13 columns |
| **Period** | December 2010 – December 2011 |
| **Geography** | 38 countries |

### Columns
`InvoiceNo` · `StockCode` · `Description` · `Quantity` · `InvoiceDate` · `UnitPrice` · `CustomerID` · `Country`

See [`docs/data_dictionary.md`](docs/data_dictionary.md) for full column definitions.

---

## 🚀 Steps to Run

### Prerequisites
- Python 3.9+
- pip

### Setup

```bash
# Clone the repository
git clone <repo-url>
cd EcomAnalytics_Team01_Capstone

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pandas numpy matplotlib seaborn scipy jupyter kagglehub
```

### Option 1: Run ETL Pipeline (Command Line)

```bash
python scripts/etl_pipeline.py
```

This will:
- Load raw data from `data/raw/data.csv`
- Clean and transform the data
- Save all outputs to `data/processed/`
- Run RFM segmentation
- Print KPI summary

### Option 2: Run RFM Analysis Separately

```bash
python scripts/rfm_analysis.py
```

This will generate `data/processed/rfm_segments.csv`.

### Option 3: Run Notebooks (Interactive)

```bash
jupyter notebook notebooks/
```

Run notebooks in order: `01` → `02` → `03` → `04` → `05`

### Option 3: Download Dataset from Kaggle

```python
import kagglehub
path = kagglehub.dataset_download("carrie1/ecommerce-data")
# Copy data.csv to data/raw/
```

---

## 📈 Key Performance Indicators

| KPI | Value |
|-----|-------|
| Total Revenue | £8,887,208.89 |
| Average Order Value | £479.46 |
| Total Unique Customers | 4,339 |
| Repeat Customer Rate | 65.6% |
| Total Orders | 18,532 |
| **Champions (Top Segment)** | 647 customers (14.9%) |

---

## 📝 Reports

- **[Project Report](reports/project_report.md)** — Full analysis report with findings and recommendations
- **[Presentation](reports/presentation.md)** — Slide-by-slide presentation outline
- **[Data Dictionary](docs/data_dictionary.md)** — Column definitions and metadata

---

## ⚖️ License

This project uses the [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail) from the UCI Machine Learning Repository. The dataset is publicly available for academic and research purposes.

---

*Built with ❤️ by Team 01*
