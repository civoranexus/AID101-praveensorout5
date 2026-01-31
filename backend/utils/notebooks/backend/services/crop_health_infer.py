"""
AgriAssist AI - Crop Health Inference Service
Phase 2: Advisory Engine + Dashboard Integration

This module loads a trained CNN model and performs crop health classification
on uploaded images. Results are passed to advisory_engine for recommendations.
"""

import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# ---------- MODEL LOADING ----------
MODEL_PATH = os.getenv("CROP_HEALTH_MODEL", "models_store/crop_health_cnn.h5")
model = load_model(MODEL_PATH)

# Class labels (adjust based on your dataset)
CLASS_LABELS = ["Healthy", "Rust", "Leaf Blight"]

def preprocess_image(img_path, target_size=(224, 224)):
    """
    Load and preprocess image for CNN inference.
    """
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def predict_crop_health(img_path):
    """
    Predict crop health status using CNN model.
    """
    processed = preprocess_image(img_path)
    preds = model.predict(processed)
    class_idx = np.argmax(preds, axis=1)[0]
    confidence = float(np.max(preds))
    return {"status": CLASS_LABELS[class_idx], "confidence": confidence}
