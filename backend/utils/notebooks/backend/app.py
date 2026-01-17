"""
AgriAssist AI - Backend Entry Point
Efficient Flask App (~75 lines)
Phase 2: Advisory Engine + Dashboard Integration
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# ---------- CONFIG ----------
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///agriassist.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "change_me")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    MODELS_FOLDER = os.getenv("MODELS_FOLDER", "models_store")

# ---------- DB INIT ----------
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# ---------- MODELS ----------
class FarmProfile(db.Model):
    __tablename__ = "farm_profiles"
    id = db.Column(db.Integer, primary_key=True)
    farmer_name = db.Column(db.String(128), nullable=False)
    crop_type = db.Column(db.String(64), nullable=False)
    acreage = db.Column(db.Float, nullable=False)
    planting_date = db.Column(db.String(32), nullable=False)
    soil_type = db.Column(db.String(64))
    region = db.Column(db.String(128))

    def to_dict(self):
        return {
            "id": self.id,
            "farmer_name": self.farmer_name,
            "crop_type": self.crop_type,
            "acreage": self.acreage,
            "planting_date": self.planting_date,
            "soil_type": self.soil_type,
            "region": self.region,
        }

class AdvisoryLog(db.Model):
    __tablename__ = "advisory_logs"
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm_profiles.id"), nullable=False)
    advisory_type = db.Column(db.String(64), nullable=False)
    message = db.Column(db.Text, nullable=False)

# ---------- APP FACTORY ----------
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    init_db(app)

    # Health check
    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "ok", "message": "AgriAssist backend running"})

    # Example route: list farm profiles
    @app.route("/api/farm-profiles", methods=["GET"])
    def list_profiles():
        profiles = FarmProfile.query.all()
        return jsonify([p.to_dict() for p in profiles])

    # Example route: add farm profile
    @app.route("/api/farm-profiles", methods=["POST"])
    def add_profile():
        from flask import request
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

    return app

# ---------- MAIN ----------
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
