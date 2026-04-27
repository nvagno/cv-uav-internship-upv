import sys
from pathlib import Path

pwd = Path.cwd()

# Add Ultralytics path
sys.path.insert(0, str(pwd / "ultralytics"))

from ultralytics import YOLO

# Load model
model = YOLO("YOLO11s-UAV.yml")

# Train model
results = model.train(
    data=str("/kaggle/input/datasets/vagnonyhasina/citrus-dataset/datasets/dataset.yml"),
    epochs=200,
    imgsz=640,
    batch=15,
    amp=False,
    patience=50,
    device=0
)