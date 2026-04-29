"""
ETL Pipeline for Online Retail Dataset
========================================
This module contains modular, reusable functions for extracting,
transforming, and loading the Online Retail e-commerce dataset.

Usage:
    python etl_pipeline.py

Author: Team 01
Date: April 2026
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime


# ─────────────────────────────────────────────
# EXTRACTION
# ─────────────────────────────────────────────

def extract_data(filepath: str, encoding: str = "ISO-8859-1") -> pd.DataFrame:
    """
    Load raw CSV data into a pandas DataFrame.

    Parameters
    ----------
    filepath : str
        Path to the raw CSV file.
    encoding : str
        File encoding (default: ISO-8859-1 for this dataset).

    Returns
    -------
    pd.DataFrame
        Raw DataFrame as-is from the CSV.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at: {filepath}")

    df = pd.read_csv(filepath, encoding=encoding)
    print(f"[EXTRACT] Loaded {df.shape[0]:,} rows × {df.shape[1]} columns from {filepath}")
    return df


# ─────────────────────────────────────────────
# TRANSFORMATION / CLEANING
# ─────────────────────────────────────────────

def drop_missing_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows where CustomerID is missing."""
    before = len(df)
    df = df.dropna(subset=["CustomerID"])
    after = len(df)
    print(f"[CLEAN] Dropped {before - after:,} rows with missing CustomerID "
          f"({(before - after) / before * 100:.1f}%)")
    return df


def remove_negative_quantities(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows where Quantity is negative (cancellations/returns)."""
    before = len(df)
    df = df[df["Quantity"] > 0]
    after = len(df)
    print(f"[CLEAN] Removed {before - after:,} rows with non-positive Quantity")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove exact duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"[CLEAN] Removed {before - after:,} duplicate rows")
    return df


def convert_invoice_date(df: pd.DataFrame) -> pd.DataFrame:
    """Convert InvoiceDate column from string to datetime."""
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    print(f"[CLEAN] Converted InvoiceDate to datetime dtype")
    return df


def create_revenue_column(df: pd.DataFrame) -> pd.DataFrame:
    """Create Revenue column as Quantity × UnitPrice."""
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    print(f"[TRANSFORM] Created Revenue column — Total: £{df['Revenue'].sum():,.2f}")
    return df


def convert_customer_id(df: pd.DataFrame) -> pd.DataFrame:
    """Convert CustomerID from float to integer."""
    df["CustomerID"] = df["CustomerID"].astype(int)
    print(f"[CLEAN] Converted CustomerID to integer type")
    return df


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add Year, Month, DayOfWeek, and Hour columns derived from InvoiceDate."""
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()
    df["Hour"] = df["InvoiceDate"].dt.hour
    print(f"[TRANSFORM] Added time features: Year, Month, DayOfWeek, Hour")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run the full cleaning pipeline in sequence.

    Steps:
        1. Drop rows with missing CustomerID
        2. Remove negative/zero Quantity rows
        3. Remove duplicate rows
        4. Convert InvoiceDate to datetime
        5. Convert CustomerID to int
        6. Create Revenue column
        7. Add time features

    Parameters
    ----------
    df : pd.DataFrame
        Raw dataframe.

    Returns
    -------
    pd.DataFrame
        Cleaned and transformed dataframe.
    """
    print("\n" + "=" * 60)
    print("  ETL PIPELINE — CLEANING & TRANSFORMATION")
    print("=" * 60)

    df = drop_missing_customers(df)
    df = remove_negative_quantities(df)
    df = remove_duplicates(df)
    df = convert_invoice_date(df)
    df = convert_customer_id(df)
    df = create_revenue_column(df)
    df = add_time_features(df)

    print(f"\n[RESULT] Final dataset: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print("=" * 60 + "\n")
    return df


# ─────────────────────────────────────────────
# KPI COMPUTATION
# ─────────────────────────────────────────────

def compute_kpis(df: pd.DataFrame) -> dict:
    """
    Compute key performance indicators from cleaned data.

    Returns
    -------
    dict
        Dictionary of KPI names and values.
    """
    total_revenue = df["Revenue"].sum()

    # Average Order Value (per invoice)
    order_values = df.groupby("InvoiceNo")["Revenue"].sum()
    avg_order_value = order_values.mean()

    # Repeat Customer Rate
    customer_orders = df.groupby("CustomerID")["InvoiceNo"].nunique()
    repeat_customers = (customer_orders > 1).sum()
    total_customers = customer_orders.shape[0]
    repeat_rate = repeat_customers / total_customers * 100

    # Top Product Contribution
    product_revenue = df.groupby("Description")["Revenue"].sum()
    top_product = product_revenue.idxmax()
    top_product_revenue = product_revenue.max()
    top_product_pct = top_product_revenue / total_revenue * 100

    # Revenue by Country (top 5)
    country_revenue = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(5)

    kpis = {
        "Total Revenue (£)": round(total_revenue, 2),
        "Average Order Value (£)": round(avg_order_value, 2),
        "Total Unique Customers": total_customers,
        "Repeat Customers": repeat_customers,
        "Repeat Customer Rate (%)": round(repeat_rate, 2),
        "Top Product": top_product,
        "Top Product Revenue (£)": round(top_product_revenue, 2),
        "Top Product Contribution (%)": round(top_product_pct, 2),
        "Top 5 Countries by Revenue": country_revenue.to_dict(),
    }

    return kpis


# ─────────────────────────────────────────────
# AGGREGATION FOR TABLEAU
# ─────────────────────────────────────────────

def create_monthly_revenue_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate revenue by year-month."""
    df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    monthly = df.groupby("YearMonth").agg(
        TotalRevenue=("Revenue", "sum"),
        TotalOrders=("InvoiceNo", "nunique"),
        TotalCustomers=("CustomerID", "nunique"),
        TotalQuantity=("Quantity", "sum"),
    ).reset_index()
    monthly["AvgOrderValue"] = monthly["TotalRevenue"] / monthly["TotalOrders"]
    return monthly


def create_product_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate revenue and quantity by product."""
    product = df.groupby(["StockCode", "Description"]).agg(
        TotalRevenue=("Revenue", "sum"),
        TotalQuantity=("Quantity", "sum"),
        OrderCount=("InvoiceNo", "nunique"),
    ).reset_index().sort_values("TotalRevenue", ascending=False)
    return product


def create_country_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate revenue and customer count by country."""
    country = df.groupby("Country").agg(
        TotalRevenue=("Revenue", "sum"),
        TotalCustomers=("CustomerID", "nunique"),
        TotalOrders=("InvoiceNo", "nunique"),
        TotalQuantity=("Quantity", "sum"),
    ).reset_index().sort_values("TotalRevenue", ascending=False)
    return country


def create_customer_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate metrics per customer for segmentation."""
    customer = df.groupby("CustomerID").agg(
        TotalRevenue=("Revenue", "sum"),
        OrderCount=("InvoiceNo", "nunique"),
        TotalQuantity=("Quantity", "sum"),
        AvgOrderValue=("Revenue", "mean"),
        FirstPurchase=("InvoiceDate", "min"),
        LastPurchase=("InvoiceDate", "max"),
        Country=("Country", "first"),
    ).reset_index()
    customer["IsRepeat"] = (customer["OrderCount"] > 1).astype(int)
    return customer


# ─────────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────────

def save_processed_data(df: pd.DataFrame, output_dir: str) -> None:
    """Save cleaned dataset and summary tables as CSVs."""
    os.makedirs(output_dir, exist_ok=True)

    # Save main cleaned dataset
    main_path = os.path.join(output_dir, "cleaned_data.csv")
    df.to_csv(main_path, index=False)
    print(f"[LOAD] Saved cleaned dataset → {main_path}")

    # Save summary tables for Tableau
    monthly = create_monthly_revenue_summary(df)
    monthly.to_csv(os.path.join(output_dir, "monthly_revenue_summary.csv"), index=False)
    print(f"[LOAD] Saved monthly_revenue_summary.csv")

    product = create_product_summary(df)
    product.to_csv(os.path.join(output_dir, "product_summary.csv"), index=False)
    print(f"[LOAD] Saved product_summary.csv")

    country = create_country_summary(df)
    country.to_csv(os.path.join(output_dir, "country_summary.csv"), index=False)
    print(f"[LOAD] Saved country_summary.csv")

    customer = create_customer_summary(df)
    customer.to_csv(os.path.join(output_dir, "customer_summary.csv"), index=False)
    print(f"[LOAD] Saved customer_summary.csv")


# ─────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────

def run_pipeline(raw_path: str, processed_dir: str) -> pd.DataFrame:
    """
    Execute the full ETL pipeline: Extract → Transform → Load.

    Parameters
    ----------
    raw_path : str
        Path to the raw CSV file.
    processed_dir : str
        Directory to save processed outputs.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame.
    """
    # Extract
    df = extract_data(raw_path)

    # Transform
    df = clean_data(df)

    # Load
    save_processed_data(df, processed_dir)

    # Compute & display KPIs
    kpis = compute_kpis(df)
    print("\n" + "=" * 60)
    print("  KEY PERFORMANCE INDICATORS")
    print("=" * 60)
    for key, value in kpis.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for k, v in value.items():
                print(f"    {k}: £{v:,.2f}")
        else:
            print(f"  {key}: {value}")
    print("=" * 60 + "\n")

    return df


if __name__ == "__main__":
    # Resolve paths relative to this script
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

    RAW_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "data.csv")
    PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

    df = run_pipeline(RAW_PATH, PROCESSED_DIR)
    print("✅ ETL Pipeline completed successfully.")
