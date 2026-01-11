"""
AgriAssist AI - Phase 1
Exploratory Data Analysis (EDA) - Weather Dataset
This script loads, cleans, and visualizes weather data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------- LOAD DATA ----------
DATA_PATH = os.path.join(os.path.dirname(__file__), "../datasets/weather.csv")
df = pd.read_csv(DATA_PATH)

# ---------- BASIC INFO ----------
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# ---------- CLEANING ----------
# Convert date column to datetime
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

# Drop duplicates
df = df.drop_duplicates()

# ---------- SUMMARY STATISTICS ----------
print("\nSummary Statistics:\n", df.describe())

# ---------- VISUALIZATIONS ----------

# Temperature trend over time
plt.figure(figsize=(12,6))
plt.plot(df["date"], df["temperature"], color="red", label="Temperature (°C)")
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()
plt.tight_layout()
plt.savefig("eda_weather_temperature.png")
plt.close()

# Rainfall trend over time
plt.figure(figsize=(12,6))
plt.plot(df["date"], df["rainfall"], color="blue", label="Rainfall (mm)")
plt.title("Rainfall Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Rainfall")
plt.legend()
plt.tight_layout()
plt.savefig("eda_weather_rainfall.png")
plt.close()

# Humidity distribution
plt.figure(figsize=(8,5))
sns.histplot(df["humidity"], bins=30, kde=True, color="green")
plt.title("Humidity Distribution")
plt.xlabel("Humidity (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("eda_weather_humidity.png")
plt.close()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[["temperature","humidity","rainfall"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Weather Variables")
plt.tight_layout()
plt.savefig("eda_weather_correlation.png")
plt.close()

# ---------- FEATURE ENGINEERING ----------
# Example: Create a 'season' column based on month
df["month"] = df["date"].dt.month
df["season"] = df["month"].map({
    12:"Winter",1:"Winter",2:"Winter",
    3:"Spring",4:"Spring",5:"Spring",
    6:"Summer",7:"Summer",8:"Summer",
    9:"Autumn",10:"Autumn",11:"Autumn"
})

print("\nSeasonal distribution:\n", df["season"].value_counts())

# Average temperature by season
plt.figure(figsize=(8,5))
sns.boxplot(x="season", y="temperature", data=df, palette="Set2")
plt.title("Average Temperature by Season")
plt.tight_layout()
plt.savefig("eda_weather_seasonal_temp.png")
plt.close()

print("EDA complete. Plots saved as PNG files in current directory.")
