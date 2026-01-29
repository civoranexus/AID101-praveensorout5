"""
AgriAssist AI - Phase 1
Exploratory Data Analysis (EDA) - Crop Yield Dataset
This script loads, cleans, and visualizes crop yield data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------- LOAD DATA ----------
DATA_PATH = os.path.join(os.path.dirname(__file__), "../datasets/crop_yield.csv")
df = pd.read_csv(DATA_PATH)

# ---------- BASIC INFO ----------
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# ---------- CLEANING ----------
# Drop duplicates and missing values
df = df.dropna().drop_duplicates()

# ---------- SUMMARY STATISTICS ----------
print("\nSummary Statistics:\n", df.describe(include="all"))

# ---------- VISUALIZATIONS ----------

# Yield distribution
if "yield" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df["yield"], bins=30, kde=True, color="purple")
    plt.title("Crop Yield Distribution")
    plt.xlabel("Yield")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("eda_crop_yield_distribution.png")
    plt.close()

# Rainfall vs Yield
if set(["rainfall", "yield"]).issubset(df.columns):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x="rainfall", y="yield", data=df, hue=df.get("crop_type", None))
    plt.title("Rainfall vs Crop Yield")
    plt.xlabel("Rainfall (mm)")
    plt.ylabel("Yield")
    plt.tight_layout()
    plt.savefig("eda_crop_yield_rainfall.png")
    plt.close()

# Acreage vs Yield
if set(["acreage", "yield"]).issubset(df.columns):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x="acreage", y="yield", data=df, hue=df.get("crop_type", None))
    plt.title("Acreage vs Crop Yield")
    plt.xlabel("Acreage (acres)")
    plt.ylabel("Yield")
    plt.tight_layout()
    plt.savefig("eda_crop_yield_acreage.png")
    plt.close()

# Correlation heatmap
num_cols = df.select_dtypes(include=["float64","int64"]).columns
if len(num_cols) > 1:
    plt.figure(figsize=(8,6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Between Crop Yield Variables")
    plt.tight_layout()
    plt.savefig("eda_crop_yield_correlation.png")
    plt.close()

print("EDA complete. Crop yield plots saved as PNG files in current directory.")
