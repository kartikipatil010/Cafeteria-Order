import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cleaned_orders.csv")

# Date conversion
df["created_at"] = pd.to_datetime(df["created_at"])

print("=" * 50)
print("CAFETERIA ORDER ANALYTICS")
print("=" * 50)

# -------------------------------------------------
# 1. BASIC SUMMARY
# -------------------------------------------------

orders = df.shape[0]
revenue = df["grand_total"].sum()
aov = revenue / orders if orders else 0
customers = df["customer_id"].nunique()

print("\n--- Overall Performance ---")
print("Total Orders      :", orders)
print(f"Total Revenue     : ₹{revenue:,.2f}")
print(f"Average Order     : ₹{aov:,.2f}")
print("Unique Customers  :", customers)

# -------------------------------------------------
# 2. BRANCH ANALYSIS
# -------------------------------------------------

branch = (
    df.groupby("branch")
      .agg(
          total_orders=("order_id", "count"),
          total_revenue=("grand_total", "sum")
      )
      .reset_index()
)

branch["average_order_value"] = (
    branch["total_revenue"] /
    branch["total_orders"]
)

branch = branch.sort_values(
    "total_revenue",
    ascending=False
)

branch.to_csv(
    "branch_analysis.csv",
    index=False
)

print("\n--- Branch Performance ---")
print(branch)

# -------------------------------------------------
# 3. HOURLY ANALYSIS
# -------------------------------------------------

df["hour"] = df["created_at"].dt.hour

hourly = (
    df.groupby("hour")
      .agg(
          orders=("order_id", "count"),
          revenue=("grand_total", "sum")
      )
      .reset_index()
)

hourly.to_csv(
    "hourly_analysis.csv",
    index=False
)

peak_hour = hourly.loc[
    hourly["orders"].idxmax()
]

print("\n--- Peak Hour ---")
print(
    f"Peak Hour: {int(peak_hour['hour']):02d}:00 "
    f"({int(peak_hour['orders'])} orders)"
)

# -------------------------------------------------
# 4. PAYMENT ANALYSIS
# -------------------------------------------------

payment = (
    df.groupby("payment_method")
      .agg(
          orders=("order_id", "count"),
          revenue=("grand_total", "sum")
      )
      .reset_index()
)

payment["aov"] = (
    payment["revenue"] /
    payment["orders"]
)

payment["revenue_share"] = (
    payment["revenue"] /
    revenue * 100
)

payment = payment.sort_values(
    "revenue",
    ascending=False
)

payment.to_csv(
    "payment_analysis.csv",
    index=False
)

# -------------------------------------------------
# 5. DAILY ANALYSIS
# -------------------------------------------------

daily = (
    df.groupby(df["created_at"].dt.date)
      .agg(
          orders=("order_id", "count"),
          revenue=("grand_total", "sum")
      )
      .reset_index()
)

daily.rename(
    columns={"created_at": "date"},
    inplace=True
)

daily["aov"] = (
    daily["revenue"] /
    daily["orders"]
)

daily.to_csv(
    "daily_analysis.csv",
    index=False
)

# -------------------------------------------------
# 6. DATA QUALITY
# -------------------------------------------------

zero_orders = df[
    df["grand_total"] == 0
]

negative_orders = df[
    df["grand_total"] < 0
]

quality = pd.DataFrame({
    "check": [
        "Total Records",
        "Zero Value Orders",
        "Negative Value Orders",
        "Missing Customer IDs",
        "Repeated Order Numbers"
    ],
    "count": [
        len(df),
        len(zero_orders),
        len(negative_orders),
        df["customer_id"].isna().sum(),
        df["order_id"].duplicated().sum()
    ]
})

quality.to_csv(
    "data_quality_summary.csv",
    index=False
)

print("\n--- Data Quality ---")
print(quality)

# -------------------------------------------------
# 7. CHARTS
# -------------------------------------------------

# Revenue by Branch
plt.figure(figsize=(8, 5))
plt.bar(
    branch["branch"].astype(str),
    branch["total_revenue"]
)
plt.title("Revenue by Branch")
plt.xlabel("Branch")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_branch.png")
plt.close()

# Orders by Hour
plt.figure(figsize=(10, 5))
plt.plot(
    hourly["hour"],
    hourly["orders"],
    marker="o"
)
plt.title("Orders by Hour")
plt.xlabel("Hour")
plt.ylabel("Orders")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("orders_by_hour.png")
plt.close()

# Payment Revenue
plt.figure(figsize=(10, 5))
plt.bar(
    payment["payment_method"].astype(str),
    payment["revenue"]
)
plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("payment_revenue.png")
plt.close()

# Daily Revenue
plt.figure(figsize=(8, 5))
plt.plot(
    daily["date"].astype(str),
    daily["revenue"],
    marker="o"
)
plt.title("Daily Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_revenue.png")
plt.close()

print("\nAnalysis completed successfully.")
