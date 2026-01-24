"""
AgriAssist AI - Farm Profile Model
Phase 2: Advisory Engine + Dashboard Integration
"""

from backend.db import db, BaseModel

class FarmProfile(BaseModel):
    __tablename__ = "farm_profiles"

    id = db.Column(db.Integer, primary_key=True)
    farmer_name = db.Column(db.String(128), nullable=False)
    crop_type = db.Column(db.String(64), nullable=False)
    acreage = db.Column(db.Float, nullable=False)
    planting_date = db.Column(db.String(32), nullable=False)
    soil_type = db.Column(db.String(64))
    region = db.Column(db.String(128))

    def __repr__(self):
        return f"<FarmProfile {self.id} - {self.farmer_name}, {self.crop_type}>"

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
