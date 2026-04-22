import cv2
import os

def mask_to_yolo(mask_dir, output_dir, class_id=0):
    os.makedirs(output_dir, exist_ok=True)

    for image_name in os.listdir(mask_dir):
        image_path = os.path.join(mask_dir, image_name)

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        h, w = img.shape

        _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        yolo_lines = []

        for contour in contours:
            x, y, bw, bh = cv2.boundingRect(contour)

            x_center = (x + bw / 2) / w
            y_center = (y + bh / 2) / h
            width = bw / w
            height = bh / h

            yolo_lines.append(f"{class_id} {x_center} {y_center} {width} {height}")

        txt_name = os.path.splitext(image_name.replace("tile_mask_", ""))[0] + ".txt"
        txt_path = os.path.join(output_dir, txt_name)

        with open(txt_path, "w") as f:
            f.write("\n".join(yolo_lines))

        print(f"Processed: {image_name}")


if __name__ == '__main__':
    mask_to_yolo(
        mask_dir="../annotation/22042026_130026/mask/",
        output_dir="../datasets/train/labels/",
        class_id=0
    )