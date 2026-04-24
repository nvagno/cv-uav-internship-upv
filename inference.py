import sys
from pathlib import Path
from PIL import Image

pwd = Path.cwd()
sys.path.insert(0, str(pwd / "ultralytics"))

from ultralytics import YOLO

model = YOLO("best.pt")

input_dir = pwd / "datasets/test"
output_dir = pwd / "predictions"
output_dir.mkdir(exist_ok=True)

# Loop through images
for img_path in input_dir.glob("*.*"):
    if img_path.suffix.lower() not in [".png", ".jpg", ".jpeg"]:
        continue

    results = model.predict(str(img_path))

    for r in results:
        boxes = r.boxes
        count = len(boxes) if boxes is not None else 0

        print(f"{img_path.name}: {count} objects detected")

        im_array = r.plot()
        im = Image.fromarray(im_array)

        # Save
        save_path = output_dir / img_path.name
        im.save(save_path)