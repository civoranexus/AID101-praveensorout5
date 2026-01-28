"""
AgriAssist AI - Resource Optimizer Service
Phase 2: Advisory Engine + Dashboard Integration

This module provides irrigation and fertilizer scheduling recommendations
based on farm profile, weather, and soil data.
"""

from backend.db import db
from backend.models import FarmProfile, AdvisoryLog

# ---------- IRRIGATION OPTIMIZER ----------
def optimize_irrigation(farm: FarmProfile, weather_data: dict):
    """
    Recommend irrigation schedule based on rainfall, temperature, and crop type.
    Example weather_data: {"rainfall": 8, "temperature": 34, "humidity": 65}
    """
    advisories = []
    rainfall = weather_data.get("rainfall", 0)
    temperature = weather_data.get("temperature", 0)

    if rainfall < 10:
        advisories.append("Rainfall is low. Schedule irrigation within 2 days.")
    if temperature > 35:
        advisories.append("High temperature stress. Increase irrigation frequency.")
    if farm.crop_type.lower() in ["wheat", "rice"]:
        advisories.append(f"{farm.crop_type} requires consistent moisture. Monitor soil regularly.")

    for msg in advisories:
        log = AdvisoryLog(farm_id=farm.id, advisory_type="irrigation", message=msg)
        db.session.add(log)
    db.session.commit()
    return advisories

# ---------- FERTILIZER OPTIMIZER ----------
def optimize_fertilizer(farm: FarmProfile, soil_data: dict):
    """
    Recommend fertilizer schedule based on soil nutrient levels and crop type.
    Example soil_data: {"nitrogen": 25, "phosphorus": 15, "potassium": 20, "ph": 5.8}
    """
    advisories = []
    nitrogen = soil_data.get("nitrogen", 0)
    phosphorus = soil_data.get("phosphorus", 0)
    potassium = soil_data.get("potassium", 0)
    ph = soil_data.get("ph", 7)

    if nitrogen < 30:
        advisories.append("Nitrogen deficiency detected. Apply urea or ammonium nitrate.")
    if phosphorus < 20:
        advisories.append("Phosphorus levels are low. Apply DAP or phosphate fertilizer.")
    if potassium < 25:
        advisories.append("Potassium deficiency detected. Apply MOP or potassium sulfate.")
    if ph < 6:
        advisories.append("Soil is acidic. Apply lime to balance pH.")

    for msg in advisories:
        log = AdvisoryLog(farm_id=farm.id, advisory_type="fertilizer", message=msg)
        db.session.add(log)
    db.session.commit()
    return advisories

# ---------- MASTER FUNCTION ----------
def optimize_resources(farm_id: int, weather_data=None, soil_data=None):
    """
    Generate irrigation and fertilizer advisories for a given farm.
    """
    farm = FarmProfile.query.get(farm_id)
    if not farm:
        return {"error": "Farm profile not found"}

    results = {}
    if weather_data:
        results["irrigation"] = optimize_irrigation(farm, weather_data)
    if soil_data:
        results["fertilizer"] = optimize_fertilizer(farm, soil_data)

    return results
