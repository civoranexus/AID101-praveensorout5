"""
AgriAssist AI - Phase 1
Exploratory Data Analysis (EDA) - Soil Dataset
This script loads, cleans, and visualizes soil data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------- LOAD DATA ----------
DATA_PATH = os.path.join(os.path.dirname(__file__), "../datasets/soil.csv")
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

# Soil type distribution
if "soil_type" in df.columns:
    plt.figure(figsize=(8,5))
    sns.countplot(x="soil_type", data=df, palette="Set2")
    plt.title("Distribution of Soil Types")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("eda_soil_types.png")
    plt.close()

# Nitrogen levels distribution
if "nitrogen" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df["nitrogen"], bins=20, kde=True, color="green")
    plt.title("Nitrogen Level Distribution")
    plt.xlabel("Nitrogen Level")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("eda_soil_nitrogen.png")
    plt.close()

# pH distribution
if "ph" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df["ph"], bins=20, kde=True, color="blue")
    plt.title("Soil pH Distribution")
    plt.xlabel("pH Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("eda_soil_ph.png")
    plt.close()

# Correlation heatmap (numeric features only)
num_cols = df.select_dtypes(include=["float64","int64"]).columns
if len(num_cols) > 1:
    plt.figure(figsize=(8,6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Between Soil Variables")
    plt.tight_layout()
    plt.savefig("eda_soil_correlation.png")
    plt.close()

print("EDA complete. Soil plots saved as PNG files in current directory.")
