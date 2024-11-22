from PIL import Image
import numpy as np

image_path = "myimage.jpg"

img = Image.open(image_path)

pixels = np.array(img)

weights = [0.3, 0.6, 0.1]

gray_pixels = np.zeros(pixels.shape[:2], dtype=np.uint8)

for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        r, g, b = pixels[i, j]
        gray_pixels[i, j] = int(weights[0]*r + weights[1]*g + weights[2]*b)

gray_img = Image.fromarray(gray_pixels)

gray_img.save("result.jpg")

gray_img.show()