"""
AgriAssist AI - Input Validators
Phase 2: Advisory Engine + Dashboard Integration

Reusable validation functions for API inputs.
"""

import re
from datetime import datetime

# ---------- FARM PROFILE VALIDATION ----------
def validate_farm_profile(data: dict):
    """
    Validate farm profile input data.
    Required: farmer_name, crop_type, acreage, planting_date
    """
    errors = []

    if not data.get("farmer_name"):
        errors.append("Farmer name is required.")
    if not data.get("crop_type"):
        errors.append("Crop type is required.")
    try:
        acreage = float(data.get("acreage", 0))
        if acreage <= 0:
            errors.append("Acreage must be greater than zero.")
    except ValueError:
        errors.append("Acreage must be a number.")

    # Validate planting date format (YYYY-MM-DD)
    planting_date = data.get("planting_date")
    if planting_date:
        try:
            datetime.strptime(planting_date, "%Y-%m-%d")
        except ValueError:
            errors.append("Planting date must be in YYYY-MM-DD format.")
    else:
        errors.append("Planting date is required.")

    return errors

# ---------- ADVISORY VALIDATION ----------
def validate_advisory(data: dict):
    """
    Validate advisory log input data.
    Required: advisory_type, message
    """
    errors = []
    if not data.get("advisory_type"):
        errors.append("Advisory type is required.")
    if not data.get("message"):
        errors.append("Advisory message is required.")
    return errors

# ---------- CROP HEALTH VALIDATION ----------
def validate_crop_health_upload(data: dict):
    """
    Validate crop health upload metadata.
    Required: farm_id, file_name
    """
    errors = []
    if not data.get("farm_id"):
        errors.append("Farm ID is required.")
    if not data.get("file_name"):
        errors.append("File name is required.")
    else:
        # Basic file name check
        if not re.match(r"^[\w,\s-]+\.[A-Za-z]{3,4}$", data["file_name"]):
            errors.append("Invalid file name format.")
    return errors
