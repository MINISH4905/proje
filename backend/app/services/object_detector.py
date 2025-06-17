import cv2
import numpy as np

def detect_objects(image_bytes: bytes):
    # Dummy detection returning one "object" at a fixed location
    return [{"label": "object", "box": [50, 50, 100, 100]}]
