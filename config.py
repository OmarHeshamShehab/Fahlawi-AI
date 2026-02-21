"""
FAHLAWI AI - CONFIGURATION MODULE
Handles: GPU validation, Folder management, and Sequential naming.
"""
import os

import torch

# Directory for exports
EXPORT_DIR = "Generated_Ads"

def initialize_system():
    """Checks for RTX A5000 and prepares workspace."""
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)
        print(f"📁 Created export folder: {EXPORT_DIR}")
    
    device_name = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU"
    print(f"🚀 Production System Active on: {device_name}")
    return device_name

def get_unique_path(product_name):
    """Generates names like Ad_Pepsi_1.mp4 to prevent overwriting."""
    clean_name = product_name.replace(" ", "_")
    counter = 1
    while True:
        path = os.path.join(EXPORT_DIR, f"Ad_{clean_name}_{counter}.mp4")
        if not os.path.exists(path):
            return path
        counter += 1