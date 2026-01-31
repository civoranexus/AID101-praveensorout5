"""
AgriAssist AI - File Paths Utility
Phase 2: Advisory Engine + Dashboard Integration

Centralized file and directory paths for datasets, uploads, and models.
"""

import os

# ---------- BASE DIRECTORY ----------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# ---------- DATA DIRECTORIES ----------
DATASET_DIR = os.path.join(BASE_DIR, "datasets")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
MODELS_DIR = os.path.join(BASE_DIR, "models_store")

# ---------- SPECIFIC FILES ----------
MARKET_DATA_FILE = os.path.join(DATASET_DIR, "market_prices.csv")
CROP_HEALTH_MODEL_FILE = os.path.join(MODELS_DIR, "crop_health_cnn.h5")

# ---------- ENSURE DIRECTORIES EXIST ----------
def ensure_directories():
    """
    Create required directories if they don't exist.
    """
    for path in [DATASET_DIR, UPLOAD_DIR, MODELS_DIR]:
        if not os.path.exists(path):
            os.makedirs(path)

# ---------- PATH HELPERS ----------
def get_dataset_path(filename: str) -> str:
    """Return full path for a dataset file."""
    return os.path.join(DATASET_DIR, filename)

def get_upload_path(filename: str) -> str:
    """Return full path for an uploaded file."""
    return os.path.join(UPLOAD_DIR, filename)

def get_model_path(filename: str) -> str:
    """Return full path for a model file."""
    return os.path.join(MODELS_DIR, filename)
