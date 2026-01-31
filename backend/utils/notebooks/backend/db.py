"""
AgriAssist AI - Database Setup
Phase 2: Advisory Engine + Dashboard Integration
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging

# ---------- INIT ----------
db = SQLAlchemy()

# ---------- DB INITIALIZATION ----------
def init_db(app):
    """
    Initialize SQLAlchemy with the Flask app and create tables.
    """
    db.init_app(app)
    with app.app_context():
        try:
            db.create_all()
            logging.info("Database initialized successfully.")
        except SQLAlchemyError as e:
            logging.error(f"Database initialization failed: {e}")

# ---------- SESSION HELPERS ----------
def commit_session():
    """
    Commit the current session with error handling.
    """
    try:
        db.session.commit()
        logging.info("Database session committed.")
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Commit failed, rolled back: {e}")
        raise

def add_instance(instance):
    """
    Add a new instance to the session and commit.
    """
    try:
        db.session.add(instance)
        commit_session()
        logging.info(f"Instance added: {instance}")
    except SQLAlchemyError as e:
        logging.error(f"Failed to add instance: {e}")
        raise

def delete_instance(instance):
    """
    Delete an instance from the session and commit.
    """
    try:
        db.session.delete(instance)
        commit_session()
        logging.info(f"Instance deleted: {instance}")
    except SQLAlchemyError as e:
        logging.error(f"Failed to delete instance: {e}")
        raise

# ---------- BASE MODEL ----------
class BaseModel(db.Model):
    """
    Base model with common methods for all tables.
    """
    __abstract__ = True

    def save(self):
        """
        Save the current instance to the database.
        """
        add_instance(self)

    def delete(self):
        """
        Delete the current instance from the database.
        """
        delete_instance(self)

    def to_dict(self):
        """
        Convert model instance to dictionary.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
