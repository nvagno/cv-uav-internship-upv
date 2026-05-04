from ultralytics import YOLO

# Load model
model = YOLO("yolo11n.pt")

# Train model
results = model.train(
    data=str("/kaggle/input/datasets/vagnonyhasina/citrus-dataset/datasets/dataset.yml"),
    epochs=200,
    imgsz=1024,
    batch=8,
    amp=True,
    patience=10,
    device=0
)