"""
AgriAssist AI - Database Migration Script
Phase 2: Advisory Engine + Dashboard Integration

This script initializes or updates the database schema using SQLAlchemy models.
"""

import logging
from backend.app import create_app
from backend.db import db
from backend.models import FarmProfile, AdvisoryLog

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_migrations():
    """
    Run database migrations: create tables if they don't exist.
    """
    app = create_app()
    with app.app_context():
        try:
            logging.info("Starting migrations...")
            db.create_all()
            logging.info("Migrations applied successfully.")
        except Exception as e:
            logging.error(f"Migration failed: {e}")

if __name__ == "__main__":
    run_migrations()
