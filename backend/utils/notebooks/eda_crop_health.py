"""
AgriAssist AI - Phase 1
Exploratory Data Analysis (EDA) - Crop Health Dataset (Large ~50k rows)
This script inspects crop disease dataset using pandas for efficiency.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- LOAD DATA ----------
DATA_PATH = os.path.join(os.path.dirname(__file__), "../datasets/crop_health.csv")

# Expect columns: image_id, file_path, class, width, height, (optional: avg_intensity)
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

# Class distribution
if "class" in df.columns:
    plt.figure(figsize=(12,6))
    sns.countplot(x="class", data=df, order=df["class"].value_counts().index, palette="Set2")
    plt.title("Distribution of Crop Health Classes")
    plt.xlabel("Class")
    plt.ylabel("Number of Images")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("eda_crop_health_class_distribution.png")
    plt.close()

# Image width and height distributions (sampled for efficiency)
if set(["width","height"]).issubset(df.columns):
    sample_df = df.sample(n=min(10000, len(df)), random_state=42)  # sample 10k rows for plotting
    plt.figure(figsize=(8,5))
    sns.histplot(sample_df["width"], bins=30, color="blue", kde=True)
    plt.title("Distribution of Image Widths (sampled)")
    plt.xlabel("Width (pixels)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("eda_crop_health_widths.png")
    plt.close()

    plt.figure(figsize=(8,5))
    sns.histplot(sample_df["height"], bins=30, color="green", kde=True)
    plt.title("Distribution of Image Heights (sampled)")
    plt.xlabel("Height (pixels)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("eda_crop_health_heights.png")
    plt.close()

# Average intensity distribution (if available)
if "avg_intensity" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df["avg_intensity"].sample(n=min(10000, len(df)), random_state=42), bins=50, color="purple")
    plt.title("Pixel Intensity Distribution (sampled)")
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("eda_crop_health_intensity.png")
    plt.close()

# Correlation heatmap (numeric features only)
num_cols = df.select_dtypes(include=["float64","int64"]).columns
if len(num_cols) > 1:
    corr_sample = df[num_cols].sample(n=min(10000, len(df)), random_state=42)
    plt.figure(figsize=(8,6))
    sns.heatmap(corr_sample.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Between Crop Health Variables (sampled)")
    plt.tight_layout()
    plt.savefig("eda_crop_health_correlation.png")
    plt.close()

print("EDA complete. Crop health plots saved as PNG files in current directory.")
