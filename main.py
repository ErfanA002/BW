from PIL import Image
import numpy as np

def rgb_to_grayscale_manual(image_path):

    img = Image.open(image_path)

    pixels = np.array(img)

    weights = [0.299, 0.587, 0.114]

    gray_pixels = np.zeros(pixels.shape[:2], dtype=np.uint8)

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            r, g, b = pixels[i, j]
            gray_pixels[i, j] = int(weights[0]*r + weights[1]*g + weights[2]*b)

    gray_img = Image.fromarray(gray_pixels)

    return gray_img

image_path = "MainAfter.jpg"

gray_image = rgb_to_grayscale_manual(image_path)

gray_image.save("gray_image_manual.jpg")

gray_image.show()