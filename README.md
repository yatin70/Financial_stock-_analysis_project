# S\&P 500 Financial Analytics Dashboard

End-to-end data analytics project on real S\&P 500 daily stock price data (2014–2017), covering data cleaning, feature engineering, sector-level analysis, anomaly detection, and an interactive Power BI dashboard.

## Project Overview

This project analyzes \~497,000 rows of daily stock price data across 505 S\&P 500 companies to answer three questions:

* Which sectors showed the strongest momentum (consistent upward movement)?
* Which stocks were the most volatile / risky?
* Which trading days showed statistically unusual volume activity?

## Dataset

* **Source:** Kaggle — S\&P 500 Stock Prices (2014–2017)
* **Size:** \~497,000 rows, 505 unique companies
* **Columns:** `symbol`, `date`, `open`, `high`, `low`, `close`, `volume`

## Tools Used

* **Python (Pandas, NumPy)** — data cleaning, feature engineering, anomaly detection
* **Power BI** — interactive dashboard, KPI cards, sector comparison
* **Excel** — quick validation checks

## Steps

### 1\. Data Cleaning

* Converted `date` from text to proper datetime format
* Dropped 11 rows (out of \~497,000) with missing OHLC values — a negligible fraction, so rows were dropped rather than imputed, to avoid introducing artificial patterns into financial calculations
* Sorted data chronologically per company, since all downstream time-series calculations depend on row order

### 2\. Sector Mapping

* The raw dataset had no sector labels, so a curated set of \~22 well-known companies was manually mapped to their real sectors (Technology, Financials, Energy, Healthcare, Consumer Staples, Consumer Discretionary)

### 3\. Feature Engineering

* **Daily return** — percentage change in closing price vs. the previous trading day
* **20-day rolling average** — smooths short-term noise to reveal the underlying trend (20 trading days ≈ 1 calendar month)
* **20-day rolling volatility** — standard deviation of daily returns, used as a risk indicator

### 4\. Anomaly Detection

* Calculated a z-score for daily trading volume, relative to each stock's own historical average
* Flagged trading days with a z-score above 3 as statistically significant volume anomalies

### 5\. Sector-Level KPIs

* Aggregated average return, volatility, and volume by sector to compare performance and identify high-momentum sectors

### 6\. Power BI Dashboard

* KPI cards: average daily return, average volatility, total volume, anomaly day count
* Trend line chart: closing price over time by company
* Sector comparison bar chart: average daily return by sector
* Volume anomaly table: flagged outlier trading days

## Key Insights

* **Energy was the only sector with a negative average daily return** across the full period — this aligns with the real, well-documented 2014–2016 oil price crash, serving as an independent validation that the analysis correctly reflects real market behavior.
* **ADBE and AMZN** were the strongest growth stocks in the sample, each growing roughly 190%+ over the period.
* **COP (ConocoPhillips)** showed the highest volatility overall, consistent with an oil company during a period of major price disruption.

## Author

Yatin Pal — [GitHub](https://github.com/yatin70) | [LinkedIn](https://linkedin.com/in/yatinpal)

