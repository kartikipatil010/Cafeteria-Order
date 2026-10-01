import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_orders.csv")

df["created_at"] = pd.to_datetime(
    df["created_at"]
)

# -------------------------------------------------
# DAILY DEMAND
# -------------------------------------------------

daily_orders = (
    df.groupby(df["created_at"].dt.date)
      .size()
      .reset_index(name="orders")
)

daily_orders["date"] = pd.to_datetime(
    daily_orders["created_at"]
)

daily_orders.drop(
    columns=["created_at"],
    inplace=True
)

print("\nDaily Order History")
print(daily_orders)

# -------------------------------------------------
# BASELINE DEMAND
# -------------------------------------------------

baseline = daily_orders["orders"].mean()

print(
    f"\nAverage Daily Demand: "
    f"{baseline:.0f} orders"
)

# -------------------------------------------------
# FUTURE DATES
# -------------------------------------------------

last_day = daily_orders["date"].max()

future_days = pd.date_range(
    start=last_day + pd.Timedelta(days=1),
    periods=7,
    freq="D"
)

# -------------------------------------------------
# FORECAST
# -------------------------------------------------

forecast = pd.DataFrame({
    "date": future_days,
    "predicted_orders": round(baseline)
})

forecast.to_csv(
    "forecast_results.csv",
    index=False
)

print("\nForecast Results")
print(forecast)

# -------------------------------------------------
# VISUALIZATION
# -------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    daily_orders["date"],
    daily_orders["orders"],
    marker="o",
    label="Actual Orders"
)

plt.plot(
    forecast["date"],
    forecast["predicted_orders"],
    marker="o",
    linestyle="--",
    label="Baseline Forecast"
)

plt.axhline(
    baseline,
    linestyle=":"
)

plt.title(
    "Cafeteria Order Demand Forecast"
)

plt.xlabel("Date")
plt.ylabel("Number of Orders")

plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "cafeteria_forecast_preview.png"
)

plt.show()

print("\nForecast generated successfully.")
