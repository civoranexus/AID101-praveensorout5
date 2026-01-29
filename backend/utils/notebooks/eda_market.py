"""
AgriAssist AI - Phase 1
Exploratory Data Analysis (EDA) - Market Dataset
This script loads, cleans, and visualizes market price data using pandas.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------- LOAD DATA ----------
DATA_PATH = os.path.join(os.path.dirname(__file__), "../datasets/market_prices.csv")
df = pd.read_csv(DATA_PATH)

# ---------- BASIC INFO ----------
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# ---------- CLEANING ----------
# Drop duplicates and missing values
df = df.dropna().drop_duplicates()

# Convert date column to datetime if present
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

# ---------- SUMMARY STATISTICS ----------
print("\nSummary Statistics:\n", df.describe(include="all"))

# ---------- VISUALIZATIONS ----------

# Price trend over time for each crop
if set(["date", "price", "crop"]).issubset(df.columns):
    plt.figure(figsize=(12,6))
    sns.lineplot(x="date", y="price", hue="crop", data=df)
    plt.title("Crop Price Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend(title="Crop")
    plt.tight_layout()
    plt.savefig("eda_market_price_trends.png")
    plt.close()

# Distribution of crop prices
if "price" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df["price"], bins=30, kde=True, color="orange")
    plt.title("Distribution of Crop Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("eda_market_price_distribution.png")
    plt.close()

# Average price per crop
if set(["crop", "price"]).issubset(df.columns):
    plt.figure(figsize=(10,6))
    sns.boxplot(x="crop", y="price", data=df, palette="Set3")
    plt.title("Average Price per Crop")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("eda_market_avg_price_per_crop.png")
    plt.close()

# Correlation heatmap (numeric features only)
num_cols = df.select_dtypes(include=["float64","int64"]).columns
if len(num_cols) > 1:
    plt.figure(figsize=(8,6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Between Market Variables")
    plt.tight_layout()
    plt.savefig("eda_market_correlation.png")
    plt.close()

print("EDA complete. Market plots saved as PNG files in current directory.")
