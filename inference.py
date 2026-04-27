from ultralytics import YOLO

# Load best trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Run prediction on test images
results = model.predict(
    source="/kaggle/input/datasets/vagnonyhasina/citrus-dataset/datasets/test/images",
    save=True,
    conf=0.5
)