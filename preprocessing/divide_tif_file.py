import cv2
import os

img = cv2.imread("valencia.tif")

h, w, _ = img.shape
tile_size = 1024

os.makedirs("tiles", exist_ok=True)

count = 0
for y in range(0, h, tile_size):
    for x in range(0, w, tile_size):
        tile = img[y:y+tile_size, x:x+tile_size]
        cv2.imwrite(f"tiles/tile_{count}.tif", tile)
        count += 1