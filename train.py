import sys

sys.path.insert(0, "/home/vagno/Desktop/internship/ultralytics")

from ultralytics import YOLO

#Load pre-trained model
model = YOLO("YOLO11s-UAV.yml")

#Train model
results = model.train(
    data='/home/vagno/Desktop/internship/datasets/dataset.yml',
    epochs=10,
    imgsz=640,
    batch=16,
    device="cpu"
)