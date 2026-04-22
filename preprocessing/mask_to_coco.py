import os
import cv2
import json

def mask_to_coco(mask_dir, output_json, class_name="object"):
    images = []
    annotations = []
    categories = [{"id": 1, "name": class_name}]

    image_id = 0
    annotation_id = 0

    for file_name in os.listdir(mask_dir):
        image_path = os.path.join(mask_dir, file_name)

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        h, w = img.shape

        image_id += 1

        images.append({
            "id": image_id,
            "file_name": file_name.replace("tile_mask_",""),
            "height": h,
            "width": w
        })

        # Binarisation
        _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:
            if len(contour) < 3:
                continue

            annotation_id += 1

            # Bounding box
            x, y, bw, bh = cv2.boundingRect(contour)

            # Segmentation
            segmentation = contour.flatten().tolist()

            area = cv2.contourArea(contour)

            annotations.append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": 1,
                "bbox": [x, y, bw, bh],
                "area": float(area),
                "segmentation": [segmentation],
                "iscrowd": 0
            })

    coco_format = {
        "images": images,
        "annotations": annotations,
        "categories": categories
    }

    with open(output_json, "w") as f:
        json.dump(coco_format, f, indent=4)

    print(f"COCO file saved → {output_json}")


if __name__ == "__main__":
    mask_to_coco(
        mask_dir="../annotation/22042026_130026/mask/",
        output_json="../annotation/annotations.json",
        class_name="object"
    )