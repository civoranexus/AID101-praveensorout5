"""
AgriAssist AI - Advisory Log Model
Phase 2: Advisory Engine + Dashboard Integration
"""

from backend.db import db, BaseModel

class AdvisoryLog(BaseModel):
    __tablename__ = "advisory_logs"

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm_profiles.id"), nullable=False)
    advisory_type = db.Column(db.String(64), nullable=False)   # e.g., irrigation, fertilizer, market, crop_health
    message = db.Column(db.Text, nullable=False)

    # Relationship back to FarmProfile
    farm_profile = db.relationship("FarmProfile", backref=db.backref("advisories", lazy=True))

    def __repr__(self):
        return f"<AdvisoryLog {self.id} - Farm {self.farm_id}, Type {self.advisory_type}>"

    def to_dict(self):
        return {
            "id": self.id,
            "farm_id": self.farm_id,
            "advisory_type": self.advisory_type,
            "message": self.message,
        }
