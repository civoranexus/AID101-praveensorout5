"""
AgriAssist AI - Backend Configuration
Phase 2: Advisory Engine + Dashboard Integration
"""

import os

class Config:
    # ---------- DATABASE ----------
    # Default: SQLite (development). Override with PostgreSQL/MySQL via env var.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///agriassist.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---------- SECURITY ----------
    SECRET_KEY = os.getenv("SECRET_KEY", "change_me")  # Replace in production

    # ---------- FILE PATHS ----------
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATASET_FOLDER = os.getenv("DATASET_FOLDER", os.path.join(BASE_DIR, "../datasets"))
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(BASE_DIR, "../uploads"))
    MODELS_FOLDER = os.getenv("MODELS_FOLDER", os.path.join(BASE_DIR, "../models_store"))

    # ---------- APP SETTINGS ----------
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
    PORT = int(os.getenv("PORT", 5000))
    HOST = os.getenv("HOST", "0.0.0.0")

    # ---------- LOGGING ----------
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # ---------- CUSTOM SETTINGS ----------
    # Advisory thresholds (example values, adjust as needed)
    IRRIGATION_THRESHOLD = float(os.getenv("IRRIGATION_THRESHOLD", 0.6))
    YIELD_MODEL_ENABLED = os.getenv("YIELD_MODEL_ENABLED", "True").lower() in ("true", "1", "yes")
    MARKET_ALERT_ENABLED = os.getenv("MARKET_ALERT_ENABLED", "True").lower() in ("true", "1", "yes")
