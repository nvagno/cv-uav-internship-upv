if __name__ == '__main__':
    import os

    labels_dir = "datasets/train/labels"
    images_dir = "datasets/train/images"

    # Extensions
    image_extensions = [".jpg", ".jpeg", ".png"]

    # List images without extension
    images_base = set()
    for img_file in os.listdir(images_dir):
        name, ext = os.path.splitext(img_file)
        if ext.lower() in image_extensions:
            images_base.add(name)

    for label_file in os.listdir(labels_dir):
        label_name, ext = os.path.splitext(label_file)

        if label_name not in images_base:
            label_path = os.path.join(labels_dir, label_file)
            os.remove(label_path)
            print(f"Delete : {label_path}")