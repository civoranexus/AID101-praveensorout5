-- AgriAssist AI - Database Schema
-- Phase 2: Advisory Engine + Dashboard Integration

-- ---------- FARM PROFILES ----------
CREATE TABLE farm_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_name VARCHAR(128) NOT NULL,
    crop_type VARCHAR(64) NOT NULL,
    acreage FLOAT NOT NULL,
    planting_date VARCHAR(32) NOT NULL,
    soil_type VARCHAR(64),
    region VARCHAR(128)
);

-- ---------- ADVISORY LOGS ----------
CREATE TABLE advisory_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farm_id INTEGER NOT NULL,
    advisory_type VARCHAR(64) NOT NULL,
    message TEXT NOT NULL,
    FOREIGN KEY (farm_id) REFERENCES farm_profiles (id) ON DELETE CASCADE
);

-- ---------- INDEXES ----------
CREATE INDEX idx_farm_profiles_crop_type ON farm_profiles (crop_type);
CREATE INDEX idx_advisory_logs_farm_id ON advisory_logs (farm_id);
CREATE INDEX idx_advisory_logs_type ON advisory_logs (advisory_type);

-- ---------- SAMPLE DATA (Optional for testing) ----------
-- INSERT INTO farm_profiles (farmer_name, crop_type, acreage, planting_date, soil_type, region)
-- VALUES ('Praveen Kumar', 'Wheat', 10.5, '2026-01-15', 'Loamy', 'Haryana');

-- INSERT INTO advisory_logs (farm_id, advisory_type, message)
-- VALUES (1, 'weather', 'Low rainfall detected. Consider irrigation scheduling.');
