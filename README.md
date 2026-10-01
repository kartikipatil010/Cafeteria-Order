# ☕ Cafeteria Order Data Analysis & Forecasting

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-yellow)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 Project Overview

**Cafeteria Order Data Analysis & Forecasting** is a data analytics project developed as part of an **internship evaluation challenge**.

The project focuses on analyzing cafeteria transaction data to understand **ordering patterns, peak business hours, branch performance, transaction behavior, and future order demand**.

The analysis combines **Python, Pandas, NumPy, Matplotlib, and MySQL** to convert raw transaction data into meaningful analytical insights.

---

# 🎯 Project Objectives

The main objectives of this project are:

- Import and analyze cafeteria transaction data
- Clean and prepare the dataset for analysis
- Perform Exploratory Data Analysis (EDA)
- Identify important ordering patterns
- Analyze peak ordering hours
- Compare branch-level performance
- Study transaction behavior
- Generate data visualizations
- Prepare analytical reports
- Estimate future order demand
- Provide business-oriented observations

---

# 📊 Dataset Overview

The analyzed dataset contains cafeteria order transactions covering:

| Metric | Value |
|---|---:|
| Total Transactions | **24,444** |
| Total Revenue | **₹15,81,186.20** |
| Average Order Value | **₹64.69** |
| Unique Customer IDs | **6,661** |
| Branches | **3** |
| Zero-Value Transactions | **435** |
| Negative-Value Transactions | **0** |
| Analysis Period | **1 Apr 2024 – 2 Apr 2024** |

> **Note:** The available dataset covers only two calendar days. Therefore, the forecasting results should be considered a baseline estimate rather than a long-term prediction.

---

# 🧹 Data Preparation

Before performing the analysis, the transaction data was checked and prepared.

### Data Preparation Steps

- Converted date and time fields
- Checked transaction values
- Standardized payment methods
- Identified zero-value transactions
- Checked negative-value transactions
- Investigated repeated order numbers
- Validated branch information
- Checked customer identifiers
- Prepared data for EDA and forecasting

---

# 🔎 Exploratory Data Analysis

The project performs analysis from multiple perspectives to understand cafeteria business activity.

## ⏰ Peak Ordering Hours

Hourly transaction activity was analyzed to identify periods with higher order volume.

| Hour | Orders |
|---|---:|
| 19:00 | **3,746** |
| 18:00 | **3,571** |
| 22:00 | **2,127** |
| 23:00 | **1,846** |
| 02:00 | **1,302** |

### Orders by Hour

![Orders by Hour](outputs/orders_by_hour.png)

### Revenue by Hour

![Revenue by Hour](outputs/revenue_by_hour.png)

### Observation

The highest recorded order activity occurred at **19:00**, followed by **18:00**.

The evening period shows strong ordering activity within the available two-day dataset.

---

# 🏢 Branch Analysis

Branch-level performance was compared using order volume, revenue, and Average Order Value.

| Branch | Orders | Revenue | AOV |
|---|---:|---:|---:|
| Branch 2 | 12,483 | ₹7,90,096.20 | ₹63.29 |
| Branch 1 | 10,326 | ₹7,06,472.00 | ₹68.42 |
| Branch 4 | 1,635 | ₹84,618.00 | ₹51.75 |

### Revenue by Branch

![Revenue by Branch](outputs/revenue_by_branch.png)

### Orders by Branch

![Orders by Branch](outputs/orders_by_branch.png)

### Observation

Branches 1 and 2 together account for approximately **94.65% of recorded revenue**.

Branch 2 recorded the highest order volume and total revenue, while Branch 1 had the higher Average Order Value.

---

# 💳 Payment Method Analysis

Payment methods were analyzed to understand transaction distribution and revenue contribution.

| Payment Method | Orders | Revenue | AOV | Revenue Share |
|---|---:|---:|---:|---:|
| Paytm | 10,109 | ₹6,05,197.70 | ₹59.87 | 38.27% |
| UPI | 5,591 | ₹4,36,978.00 | ₹78.16 | 27.64% |
| CCA | 2,823 | ₹1,94,752.00 | ₹68.99 | 12.32% |
| QR | 2,353 | ₹1,14,031.00 | ₹48.46 | 7.21% |
| Cash | 2,062 | ₹1,08,379.00 | ₹52.56 | 6.85% |
| Card | 1,210 | ₹1,02,551.00 | ₹84.75 | 6.49% |
| Unknown | 296 | ₹19,297.50 | ₹65.19 | 1.22% |

### Payment Revenue

![Payment Revenue](outputs/payment_revenue.png)

### Observation

Paytm contributed the largest recorded revenue share at **38.27%**.

Card transactions had the highest Average Order Value among the listed payment methods at **₹84.75**.

---

# 💰 Zero-Value Transaction Analysis

During data validation, **435 transactions** were found with:

`grand_total = ₹0`

These transactions were not automatically removed.

Further checks showed:

- Positive subtotal values
- Positive reward amounts
- No refund indicators
- No cancellation reasons
- No recorded discounts

Therefore, the records were retained and flagged for further analysis.

This demonstrates a validation-based approach to handling unusual transactions instead of deleting them without investigation.

---

# 🔁 Repeated Order Number Analysis

Repeated `order_number` values were also investigated.

A repeated order number was not automatically considered a duplicate because transactions could differ by:

- Date
- Customer
- Branch
- Order value
- Payment method

Therefore, repeated order-number values were **flagged rather than blindly deleted**.

---

# 📅 Daily Analysis

| Date | Orders | Revenue | AOV |
|---|---:|---:|---:|
| 2024-04-01 | 12,168 | ₹7,45,170.20 | ₹61.24 |
| 2024-04-02 | 12,276 | ₹8,36,016.00 | ₹68.10 |

### Daily Order Trend

![Daily Orders](outputs/daily_orders.png)

### Daily Revenue Trend

![Daily Revenue](outputs/daily_revenue.png)

### Observation

Across the two recorded days:

- Order volume changed by approximately **0.89%**
- Revenue changed by approximately **12.19%**
- Average Order Value changed by approximately **11.20%**

These values represent a **two-day comparison** and should not be interpreted as a long-term business trend.

---

# 🔮 Demand Forecasting

A baseline demand estimation approach was used because the available dataset contains only two days of historical transaction data.

The average daily order volume was calculated as:

**12,222 orders/day**

This value provides a simple reference point for expected daily demand.

### Forecast Visualization

![Demand Forecast](outputs/demand_forecast.png)

> **Note:** With only two days of historical data, advanced seasonal forecasting cannot be reliably validated. A larger historical dataset would be required for a production forecasting model.

---

# 📈 Key Findings

The analysis produced the following observations:

- **24,444** transactions were analyzed.
- Total recorded revenue was **₹15,81,186.20**.
- Average Order Value was **₹64.69**.
- Branch 2 recorded the highest order volume and revenue.
- Branches 1 and 2 contributed approximately **94.65%** of recorded revenue.
- **19:00** was the highest recorded order-volume hour.
- Paytm had the largest recorded revenue share.
- Card transactions had the highest listed AOV.
- **435 transactions** had a zero grand total.
- Repeated order numbers were investigated rather than automatically removed.
- The limited two-day history restricts long-term forecasting conclusions.

---

# 🛠️ Technology Stack

### Programming & Analysis

- **Python 3.x**
- **Pandas**
- **NumPy**
- **Matplotlib**

### Database

- **MySQL 8.0**

### Development Tools

- **Jupyter Notebook**
- **Git**
- **GitHub**

---

# 🔄 Project Workflow

```text
Raw Cafeteria Data
        ↓
Data Import
        ↓
Data Cleaning
        ↓
Data Validation
        ↓
Exploratory Data Analysis
        ↓
Branch & Hourly Analysis
        ↓
Payment Analysis
        ↓
Visualization
        ↓
Demand Estimation
        ↓
Business Insights
```

---

# 📂 Project Structure

```text
Cafeteria-Order/
│
├── README.md
├── forecast.py
├── eda_analysis.py
├── Cafeteria_Analysis_Report.md
├── forecast_results.csv
├── cafeteria_forecast_preview.png
└── requirements.txt
```

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/kartikipatil010/Cafeteria-Order.git
cd Cafeteria-Order
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run EDA

```bash
python eda_analysis.py
```

## 4. Run Forecasting

```bash
python forecast.py
```

The analysis generates the required analytical outputs and forecast results.

---

# ⚠️ Project Limitations

- The available transaction history covers only two days.
- Long-term weekly and monthly patterns cannot be established.
- Seasonal demand cannot be reliably measured.
- Forecast accuracy cannot be meaningfully evaluated with only two historical days.
- Repeated order numbers do not necessarily represent duplicate transactions.
- More historical data would be required for advanced forecasting models.

---

# 🚀 Future Enhancements

With additional historical data, this project can be extended with:

### Forecasting

- ARIMA
- Prophet
- XGBoost
- Random Forest
- LSTM
- MAE, RMSE and MAPE evaluation

### Analytics

- Weekly and monthly trend analysis
- Seasonal analysis
- Branch-level forecasting
- Product-level demand analysis
- Customer segmentation
- RFM analysis
- Anomaly detection

### Business Intelligence

- Power BI dashboard
- Tableau dashboard
- Interactive Plotly dashboard
- Automated KPI reporting

### Operations

- Inventory demand planning
- Staff scheduling based on peak hours
- Branch-specific planning
- Stock optimization

---

# 🎓 Internship Evaluation

This project was developed as part of an **internship evaluation challenge** focused on cafeteria order data analysis and forecasting.

The project demonstrates practical skills in:

**Python + SQL + Data Cleaning + EDA + Visualization + Forecasting + Business Analysis**

---

# 👩‍💻 Author

**Kartiki Patil**

Computer Engineering

GitHub: [@kartikipatil010](https://github.com/kartikipatil010)

---

⭐ **Thank you for reviewing this project!**
