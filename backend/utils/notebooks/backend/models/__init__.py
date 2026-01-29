"""
AgriAssist AI - Models Package
Phase 2: Advisory Engine + Dashboard Integration
"""

from backend.models.farm_profile import FarmProfile
from backend.models.advisory_log import AdvisoryLog

# Expose models for easy import
__all__ = ["FarmProfile", "AdvisoryLog"]
