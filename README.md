# ☕ Cafeteria Sales Analysis & Demand Forecasting

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-yellow)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 About the Project

This project focuses on analyzing cafeteria order data to understand **sales performance, customer ordering patterns, peak demand periods, and payment behavior**.

The analysis was performed using **Python, Pandas, MySQL, and data visualization techniques**.

The project was developed as part of the **Kanishka Software Pvt. Ltd. Internship Evaluation Challenge**.

---

## 🎯 Project Goals

The main objectives of this project are:

- Understand overall cafeteria sales performance
- Analyze order and revenue patterns
- Identify high-demand hours
- Compare branch-level performance
- Study payment method usage
- Perform data cleaning and validation
- Identify unusual or zero-value transactions
- Generate useful visualizations
- Create a baseline demand forecast
- Convert raw transaction data into business insights

---

## 📊 Dataset Overview

The dataset contains cafeteria transaction records with information related to:

- Order details
- Customer information
- Branch
- Order amount
- Payment method
- Date and time
- Rewards
- Discounts
- Transaction status

### Key Metrics

| Metric | Result |
|---|---:|
| Total Transactions | **24,444** |
| Total Revenue | **₹15,81,186.20** |
| Average Order Value | **₹64.69** |
| Unique Customers | **6,661** |
| Branches | **3** |
| Zero-Value Orders | **435** |

> The current dataset covers **1 April 2024 to 2 April 2024**, so the forecasting results are treated as a baseline rather than a long-term prediction.

---

# 🔍 Analysis Performed

## 1. Sales & Revenue Analysis

The project calculates important business KPIs such as:

- Total orders
- Total revenue
- Average Order Value
- Daily revenue
- Daily order volume
- Branch-wise revenue

---

## 2. Branch Analysis

Branch performance was compared using order count, revenue, and AOV.

| Branch | Orders | Revenue | AOV |
|---|---:|---:|---:|
| Branch 2 | 12,483 | ₹7,90,096.20 | ₹63.29 |
| Branch 1 | 10,326 | ₹7,06,472.00 | ₹68.42 |
| Branch 4 | 1,635 | ₹84,618.00 | ₹51.75 |

### Revenue by Branch

![Branch Revenue](outputs/revenue_by_branch.png)

---

## 3. Peak Hour Analysis

Hourly order data was analyzed to identify periods of high cafeteria activity.

### Highest Recorded Hours

| Time | Orders |
|---|---:|
| 19:00 | 3,746 |
| 18:00 | 3,571 |
| 22:00 | 2,127 |
| 23:00 | 1,846 |
| 02:00 | 1,302 |

### Order Volume by Hour

![Hourly Orders](outputs/orders_by_hour.png)

This analysis can help with operational planning such as **staff allocation and inventory preparation**.

---

## 4. Payment Method Analysis

Different payment methods were compared based on transaction count and revenue.

| Payment Method | Orders | Revenue |
|---|---:|---:|
| Paytm | 10,109 | ₹6,05,197.70 |
| UPI | 5,591 | ₹4,36,978.00 |
| CCA | 2,823 | ₹1,94,752.00 |
| QR | 2,353 | ₹1,14,031.00 |
| Cash | 2,062 | ₹1,08,379.00 |
| Card | 1,210 | ₹1,02,551.00 |

### Payment Revenue Distribution

![Payment Revenue](outputs/payment_revenue.png)

---

# 🧹 Data Quality Analysis

Before generating insights, the dataset was checked for potential data-quality problems.

### Checks Included

- Missing values
- Zero-value transactions
- Negative transaction values
- Payment method inconsistencies
- Repeated order numbers
- Invalid or unusual records
- Date and time formatting

### Zero-Value Transactions

There were **435 transactions with a grand total of ₹0**.

These records were investigated instead of being automatically removed.

The analysis found that these records contained other transaction information such as positive subtotal/reward values, so they were retained and flagged for further review.

---

# 📈 Daily Analysis

| Date | Orders | Revenue | AOV |
|---|---:|---:|---:|
| 01-Apr-2024 | 12,168 | ₹7,45,170.20 | ₹61.24 |
| 02-Apr-2024 | 12,276 | ₹8,36,016.00 | ₹68.10 |

### Daily Revenue

![Daily Revenue](outputs/daily_revenue.png)

### Daily Orders

![Daily Orders](outputs/daily_orders.png)

---

# 🔮 Demand Forecasting

A simple baseline method was used to estimate future daily order demand.

### Baseline Demand

**Average Daily Orders: 12,222**

The calculated average was used as a reference point for demand estimation.

![Demand Forecast](outputs/demand_forecast.png)

> Since only two days of historical data are available, the result should not be considered a production-level forecasting model.

---

# 💡 Key Findings

The analysis highlighted several useful patterns:

- Branch 2 recorded the largest order volume.
- Branches 1 and 2 contributed most of the recorded revenue.
- The highest order activity occurred around **18:00–19:00**.
- Paytm represented the largest share of recorded revenue.
- UPI showed a relatively higher average transaction value.
- Zero-value transactions were present and required separate investigation.
- The short historical period limits long-term forecasting.

---

# 🛠️ Tools & Technologies

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Database
- MySQL

### Visualization
- Matplotlib

### Development Tools
- Git
- GitHub

---

# 🔄 Data Analysis Pipeline

```text
Transaction Dataset
        ↓
MySQL Database
        ↓
Data Extraction
        ↓
Data Cleaning
        ↓
Quality Validation
        ↓
Exploratory Analysis
        ↓
KPI Calculation
        ↓
Visualization
        ↓
Demand Baseline
        ↓
Business Insights
