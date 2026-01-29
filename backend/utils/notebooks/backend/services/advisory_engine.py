"""
AgriAssist AI - Advisory Engine Service
Phase 2: Advisory Engine + Dashboard Integration

This module generates advisories for farms based on weather, soil, yield, market,
and crop health data. It stores advisories in the database for dashboard display.
"""

import datetime
from backend.db import db
from backend.models import FarmProfile, AdvisoryLog

# ---------- WEATHER ADVISORY ----------
def generate_weather_advisory(farm: FarmProfile, weather_data: dict):
    """
    Generate irrigation/fertilizer advisories based on weather data.
    Example weather_data: {"temperature": 32, "rainfall": 5, "humidity": 70}
    """
    advisories = []

    if weather_data.get("rainfall", 0) < 10:
        advisories.append("Low rainfall detected. Consider irrigation scheduling.")
    if weather_data.get("temperature", 0) > 35:
        advisories.append("High temperature stress. Mulching recommended to retain soil moisture.")
    if weather_data.get("humidity", 0) > 80:
        advisories.append("High humidity may increase fungal risk. Monitor crop health closely.")

    for msg in advisories:
        log = AdvisoryLog(
            farm_id=farm.id,
            advisory_type="weather",
            message=msg
        )
        db.session.add(log)
    db.session.commit()
    return advisories

# ---------- SOIL ADVISORY ----------
def generate_soil_advisory(farm: FarmProfile, soil_data: dict):
    """
    Generate fertilizer advisories based on soil nutrient levels.
    Example soil_data: {"nitrogen": 20, "ph": 5.5}
    """
    advisories = []

    if soil_data.get("nitrogen", 0) < 30:
        advisories.append("Nitrogen deficiency detected. Apply nitrogen-rich fertilizer.")
    if soil_data.get("ph", 7) < 6:
        advisories.append("Soil is acidic. Consider liming to balance pH.")

    for msg in advisories:
        log = AdvisoryLog(
            farm_id=farm.id,
            advisory_type="soil",
            message=msg
        )
        db.session.add(log)
    db.session.commit()
    return advisories

# ---------- YIELD ADVISORY ----------
def generate_yield_forecast(farm: FarmProfile, yield_model_output: float):
    """
    Generate yield forecast advisories.
    yield_model_output: predicted yield value (e.g., tons per hectare).
    """
    msg = f"Predicted yield for {farm.crop_type}: {yield_model_output:.2f} tons/hectare."
    log = AdvisoryLog(
        farm_id=farm.id,
        advisory_type="yield",
        message=msg
    )
    db.session.add(log)
    db.session.commit()
    return [msg]

# ---------- MARKET ADVISORY ----------
def generate_market_insight(farm: FarmProfile, market_data: dict):
    """
    Generate market advisories based on crop price trends.
    Example market_data: {"crop": "Wheat", "avg_price": 1800, "trend": "rising"}
    """
    advisories = []
    crop = market_data.get("crop", farm.crop_type)
    price = market_data.get("avg_price", 0)
    trend = market_data.get("trend", "stable")

    advisories.append(f"Market price for {crop} is {price} INR/quintal, trend: {trend}.")
    if trend == "rising":
        advisories.append(f"Consider delaying sale of {crop} to benefit from rising prices.")
    elif trend == "falling":
        advisories.append(f"Consider early sale of {crop} before prices drop further.")

    for msg in advisories:
        log = AdvisoryLog(
            farm_id=farm.id,
            advisory_type="market",
            message=msg
        )
        db.session.add(log)
    db.session.commit()
    return advisories

# ---------- CROP HEALTH ADVISORY ----------
def generate_crop_health_advisory(farm: FarmProfile, health_status: str):
    """
    Generate advisories based on crop health detection (CNN output).
    health_status: e.g., "Healthy", "Rust", "Leaf Blight"
    """
    advisories = []

    if health_status.lower() == "healthy":
        advisories.append("Crop health is good. Continue regular monitoring.")
    elif health_status.lower() == "rust":
        advisories.append("Rust detected. Apply fungicide treatment promptly.")
    elif health_status.lower() == "leaf blight":
        advisories.append("Leaf blight detected. Remove infected leaves and apply fungicide.")

    for msg in advisories:
        log = AdvisoryLog(
            farm_id=farm.id,
            advisory_type="crop_health",
            message=msg
        )
        db.session.add(log)
    db.session.commit()
    return advisories

# ---------- MASTER FUNCTION ----------
def generate_all_advisories(farm_id: int, weather_data=None, soil_data=None,
                            yield_model_output=None, market_data=None, health_status=None):
    """
    Generate all advisories for a given farm in one call.
    """
    farm = FarmProfile.query.get(farm_id)
    if not farm:
        return {"error": "Farm profile not found"}

    results = {}
    if weather_data:
        results["weather"] = generate_weather_advisory(farm, weather_data)
    if soil_data:
        results["soil"] = generate_soil_advisory(farm, soil_data)
    if yield_model_output is not None:
        results["yield"] = generate_yield_forecast(farm, yield_model_output)
    if market_data:
        results["market"] = generate_market_insight(farm, market_data)
    if health_status:
        results["crop_health"] = generate_crop_health_advisory(farm, health_status)

    return results
