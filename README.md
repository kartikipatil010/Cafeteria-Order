# ☕ Cafeteria Analytics

> **Turning cafeteria transaction data into meaningful business insights.**

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)](https://www.mysql.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Analytics-green)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-yellow)](https://matplotlib.org/)

---

## 📍 Project Snapshot

| | |
|---|---|
| **Project Type** | Data Analytics & Forecasting |
| **Domain** | Cafeteria / Food Service |
| **Dataset Size** | 24,444 Transactions |
| **Analysis Period** | 1–2 April 2024 |
| **Database** | MySQL |
| **Analysis Tool** | Python |
| **Developed For** | Kanishka Software Pvt. Ltd. Internship Evaluation Challenge |

---

## 🧾 What is this project?

Cafeterias generate a large amount of transaction data every day.

This project uses that data to answer practical questions such as:

- How much revenue was generated?
- Which branch handled more orders?
- When is the cafeteria busiest?
- Which payment methods are commonly used?
- Are there unusual transactions?
- What can the available data tell us about future demand?

The objective is to convert raw transaction records into **clear, measurable and business-oriented insights**.

---

# 📊 At a Glance

### 💰 Revenue
**₹15,81,186.20**

### 🛒 Orders
**24,444**

### 👥 Customers
**6,661**

### 🏢 Branches
**3**

### 💳 Average Order Value
**₹64.69**

### ⚠️ Zero-Value Orders
**435**

---

# 🔎 Analysis Areas

```text
                 CAFETERIA DATA
                       │
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
   Sales Analysis   Branch Analysis   Time Analysis
       │               │               │
       ↓               ↓               ↓
    Revenue          Revenue          Peak Hours
    Orders           Orders           Daily Trends
    AOV              AOV              Demand
       │               │               │
       └───────────────┼───────────────┘
                       ↓
                Payment Analysis
                       ↓
                Data Quality Checks
                       ↓
                Demand Baseline
```

---

# 🏢 Branch Performance

The transaction data was compared across the available branches.

| Branch | Total Orders | Revenue | Average Order |
|:------:|-------------:|--------:|--------------:|
| Branch 1 | 10,326 | ₹7,06,472.00 | ₹68.42 |
| Branch 2 | 12,483 | ₹7,90,096.20 | ₹63.29 |
| Branch 4 | 1,635 | ₹84,618.00 | ₹51.75 |

### Revenue Distribution

![Revenue by Branch](outputs/revenue_by_branch.png)

### Order Distribution

![Orders by Branch](outputs/orders_by_branch.png)

---

# ⏱️ When Do Customers Order?

Hourly transaction data was examined to understand cafeteria activity throughout the day.

### Top Recorded Hours

| Time | Number of Orders |
|:----:|-----------------:|
| **19:00** | **3,746** |
| **18:00** | **3,571** |
| **22:00** | **2,127** |
| **23:00** | **1,846** |
| **02:00** | **1,302** |

### Hourly Order Pattern

![Orders by Hour](outputs/orders_by_hour.png)

### Hourly Revenue Pattern

![Revenue by Hour](outputs/revenue_by_hour.png)

**Insight:** The strongest recorded activity occurs during the evening period, particularly around **18:00–19:00**.

---

# 💳 Payment Behaviour

Payment methods were grouped and analyzed to understand transaction distribution.

| Payment Method | Orders | Revenue | AOV |
|---|---:|---:|---:|
| Paytm | 10,109 | ₹6,05,197.70 | ₹59.87 |
| UPI | 5,591 | ₹4,36,978.00 | ₹78.16 |
| CCA | 2,823 | ₹1,94,752.00 | ₹68.99 |
| QR | 2,353 | ₹1,14,031.00 | ₹48.46 |
| Cash | 2,062 | ₹1,08,379.00 | ₹52.56 |
| Card | 1,210 | ₹1,02,551.00 | ₹84.75 |

![Payment Revenue](outputs/payment_revenue.png)

---

# 📅 Two-Day Sales View

| Date | Orders | Revenue | AOV |
|---|---:|---:|---:|
| 01-Apr-2024 | 12,168 | ₹7,45,170.20 | ₹61.24 |
| 02-Apr-2024 | 12,276 | ₹8,36,016.00 | ₹68.10 |

![Daily Revenue](outputs/daily_revenue.png)

![Daily Orders](outputs/daily_orders.png)

> The dataset contains only two days of transactions, so daily changes should not be treated as long-term business trends.

---

# 🧹 Data Quality Review

Data quality checks were performed before interpreting the results.

### Checks included

- Zero-value transactions
- Negative values
- Repeated order numbers
- Payment method consistency
- Date/time formatting
- Branch values
- Customer identifiers
- Transaction-level records

---

## ⚠️ Zero-Value Transactions

**435 transactions** were recorded with:

`grand_total = ₹0`

These transactions were investigated instead of being removed automatically.

The records contained other transaction information, including positive subtotal/reward values, and therefore were retained and flagged for further analysis.

---

## 🔁 Repeated Order Numbers

Some `order_number` values appeared more than once.

A repeated order number was **not automatically considered a duplicate transaction** because the associated records could differ in:

- Customer
- Date
- Branch
- Order value
- Payment method

Therefore, such records were flagged for investigation rather than blindly deleted.

---

# 🔮 Demand Estimation

A simple baseline was created from the available daily transaction history.

### Baseline

**12,222 orders/day**

This value represents the average recorded daily order volume.

![Demand Forecast](outputs/demand_forecast.png)

### Why a baseline?

The available dataset contains only two calendar days. A longer historical dataset would be required to build and properly evaluate a seasonal forecasting model.

---

# 💡 Insights From the Data

### 🏢 Branches
Branches 1 and 2 together account for approximately **94.65% of recorded revenue**.

### 🕖 Peak Period
The highest recorded order volume occurs at **19:00**.

### 💳 Payments
Paytm contributes the largest recorded revenue share, while Card transactions show the highest AOV among the listed payment methods.

### ⚠️ Data Quality
Zero-value transactions and repeated order numbers require separate validation instead of automatic deletion.

### 📈 Forecasting
The current forecast should be treated as a **baseline reference**, not a production forecasting model.

---

# 🧰 Technology Used

| Technology | Purpose |
|---|---|
| **Python** | Data processing & analysis |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical operations |
| **Matplotlib** | Charts & visualization |
| **MySQL** | Database & SQL analysis |
| **Git** | Version control |
| **GitHub** | Project hosting |

---

# 📂 Repository Layout

```text
Cafeteria-Order/
│
├── forecast.py
├── eda_analysis.py
│
├── Cafeteria_Analysis_Report.md
├── forecast_results.csv
├── cafeteria_forecast_preview.png
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Getting Started

### 1. Clone the project

```bash
git clone https://github.com/kartikipatil010/Cafeteria-Order.git
```

### 2. Open the project

```bash
cd Cafeteria-Order
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python eda_analysis.py
```

### 5. Run forecasting

```bash
python forecast.py
```

---

# 📌 Limitations

The current analysis has some important limitations:

- Only two days of historical data are available.
- Long-term trends cannot be established.
- Seasonal behaviour cannot be reliably measured.
- Forecast accuracy cannot be properly evaluated.
- Product-level forecasting is not included.
- More historical data would be required for advanced forecasting.

---

# 🚀 Possible Extensions

With additional historical data, this project could be extended to include:

```text
More Historical Data
        ↓
Weekly / Monthly Analysis
        ↓
Seasonality Detection
        ↓
Product-Level Analysis
        ↓
Machine Learning Forecasting
        ↓
Inventory Prediction
        ↓
Staff Planning
        ↓
Interactive Dashboard
```

Possible technologies/models:

- Power BI
- Plotly
- ARIMA
- Prophet
- XGBoost
- Random Forest
- LSTM

---

# 🎓 Skills Demonstrated

**Programming**
- Python
- SQL

**Analytics**
- Data Cleaning
- EDA
- KPI Analysis
- Business Analytics
- Data Quality Analysis

**Visualization**
- Matplotlib
- Data-driven reporting

**Database**
- MySQL

**Development**
- Git
- GitHub

---

# 👩‍💻 Author

### Kartiki Patil

Computer Engineering Student

[GitHub Profile](https://github.com/kartikipatil010)

---

## 📌 Internship Evaluation

This project was developed as part of the

**Kanishka Software Pvt. Ltd. Internship Evaluation Challenge**

### Project Flow

**Raw Data → Cleaning → Analysis → Visualization → Forecasting → Insights**

---

> *Data becomes valuable when it helps us understand what is happening and why.*
