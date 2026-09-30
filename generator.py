import sys
import cv2
import numpy as np

import secret_reader
import noise_generator

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python generator.py <image>")

    print(f"Generating from: {sys.argv[1]}")

    # Create the "secret mask"
    secret_image = secret_reader.load(sys.argv[1])
    secret_mask = secret_reader.create_secret_mask(secret_image)

    # Crate the initial image
    noise_image = noise_generator.generate_noise(secret_image.shape[1], secret_image.shape[0])

    # Extract all elements from the noise image that are part of the secret mask
    pixel_secret_mask = cv2.cvtColor(noise_image, cv2.COLOR_BGR2BGRA)

    # Use the mask as alpha channel
    pixel_secret_mask[:, :, 3] = secret_mask
    
    
    secret_image_1 = secret_image.copy()
    # Translate mask upwards
    offset_y = -5

    M = np.float32([
        [1, 0, 0],
        [0, 1, offset_y]
    ])
    secret_image_1 = cv2.warpAffine(secret_mask, M, (secret_mask.shape[1], secret_mask.shape[0]))
    
    noise_image_2 = noise_image.copy()
    # Remove all pixels on noise_image_2 that are part of the translated secret mask
    noise_image_removed = noise_image_2.copy()
    noise_image_removed[secret_image_1 == 255] = [0, 0, 0]  # Set those pixels to black
    


    cv2.imwrite("images/mask.png", secret_mask)
    cv2.imwrite("images/noise1.png", noise_image)
    cv2.imwrite("images/noise2.png", noise_image_removed)
    cv2.imwrite("images/mask2.png", secret_image_1)
    cv2.imwrite("images/secret_masked.png", pixel_secret_mask)
if __name__ == "__main__":
    main()

