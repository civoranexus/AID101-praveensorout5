"""
AgriAssist AI - API Routes
Phase 2: Advisory Engine + Dashboard Integration
"""

from flask import Blueprint, request, jsonify
from backend.db import db
from backend.app import FarmProfile, AdvisoryLog

# ---------- BLUEPRINT ----------
api_blueprint = Blueprint("api", __name__)

# ---------- FARM PROFILE ROUTES ----------
@api_blueprint.route("/farm-profiles", methods=["GET"])
def list_profiles():
    """List all farm profiles."""
    profiles = FarmProfile.query.all()
    return jsonify([p.to_dict() for p in profiles])

@api_blueprint.route("/farm-profiles/<int:farm_id>", methods=["GET"])
def get_profile(farm_id):
    """Get a single farm profile by ID."""
    profile = FarmProfile.query.get_or_404(farm_id)
    return jsonify(profile.to_dict())

@api_blueprint.route("/farm-profiles", methods=["POST"])
def add_profile():
    """Add a new farm profile."""
    data = request.json
    profile = FarmProfile(
        farmer_name=data.get("farmer_name"),
        crop_type=data.get("crop_type"),
        acreage=float(data.get("acreage", 0)),
        planting_date=data.get("planting_date"),
        soil_type=data.get("soil_type"),
        region=data.get("region"),
    )
    db.session.add(profile)
    db.session.commit()
    return jsonify({"status": "success", "profile": profile.to_dict()}), 201

@api_blueprint.route("/farm-profiles/<int:farm_id>", methods=["PUT"])
def update_profile(farm_id):
    """Update an existing farm profile."""
    profile = FarmProfile.query.get_or_404(farm_id)
    data = request.json
    for key, value in data.items():
        if hasattr(profile, key):
            setattr(profile, key, value)
    db.session.commit()
    return jsonify({"status": "updated", "profile": profile.to_dict()})

@api_blueprint.route("/farm-profiles/<int:farm_id>", methods=["DELETE"])
def delete_profile(farm_id):
    """Delete a farm profile."""
    profile = FarmProfile.query.get_or_404(farm_id)
    db.session.delete(profile)
    db.session.commit()
    return jsonify({"status": "deleted", "id": farm_id})

# ---------- ADVISORY ROUTES ----------
@api_blueprint.route("/advisory/<int:farm_id>", methods=["GET"])
def get_advisory(farm_id):
    """Fetch advisory logs for a farm."""
    logs = AdvisoryLog.query.filter_by(farm_id=farm_id).all()
    return jsonify([{"id": l.id, "type": l.advisory_type, "message": l.message} for l in logs])

@api_blueprint.route("/advisory/<int:farm_id>", methods=["POST"])
def add_advisory(farm_id):
    """Add a new advisory log for a farm."""
    data = request.json
    log = AdvisoryLog(
        farm_id=farm_id,
        advisory_type=data.get("advisory_type"),
        message=data.get("message"),
    )
    db.session.add(log)
    db.session.commit()
    return jsonify({"status": "success", "log_id": log.id}), 201

# ---------- CROP HEALTH ROUTE ----------
@api_blueprint.route("/crop-health/upload", methods=["POST"])
def upload_crop_health():
    """
    Upload crop health image metadata.
    (Actual CNN inference handled in services/crop_health_infer.py)
    """
    data = request.json
    # Example: store metadata in advisory log
    log = AdvisoryLog(
        farm_id=data.get("farm_id"),
        advisory_type="crop_health",
        message=f"Image uploaded: {data.get('file_name')}"
    )
    db.session.add(log)
    db.session.commit()
    return jsonify({"status": "success", "message": "Crop health image metadata stored."}), 201
