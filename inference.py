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
    results = model.predict(str(img_path))

    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array)

        # Save
        save_path = output_dir / img_path.name
        im.save(save_path)