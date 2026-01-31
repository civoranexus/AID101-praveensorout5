"""
AgriAssist AI - Market Insight Service
Phase 2: Advisory Engine + Dashboard Integration

This module analyzes market price data and generates insights for advisories.
"""

import pandas as pd

def analyze_market_data(csv_path="datasets/market_prices.csv"):
    """
    Analyze market dataset and return average prices and trends.
    """
    df = pd.read_csv(csv_path)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])

    insights = {}
    for crop in df["crop"].unique():
        crop_df = df[df["crop"] == crop].sort_values("date")
        avg_price = crop_df["price"].mean()
        trend = "stable"
        if len(crop_df) > 5:
            recent = crop_df.tail(5)["price"].values
            if recent[-1] > recent[0]:
                trend = "rising"
            elif recent[-1] < recent[0]:
                trend = "falling"
        insights[crop] = {"avg_price": round(avg_price, 2), "trend": trend}
    return insights

def get_crop_insight(crop_name, csv_path="datasets/market_prices.csv"):
    """
    Get market insight for a specific crop.
    """
    insights = analyze_market_data(csv_path)
    return insights.get(crop_name, {"avg_price": None, "trend": "unknown"})
