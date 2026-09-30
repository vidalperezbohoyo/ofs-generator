import sys
import cv2
import numpy as np

import secret_reader
import noise_generator

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python generator.py <image>")

    print(f"Generating from: {sys.argv[1]}")

    secret_image = secret_reader.load(sys.argv[1])
    secret_mask = secret_reader.create_secret_mask(secret_image)

    # Crate the initial image
    noise_image = noise_generator.generate_noise(secret_image.shape[1], secret_image.shape[0])

    # Extract the black pixels of the first image that satisfies the mask
    pixel_secret_mask = cv2.bitwise_and(noise_image, noise_image, mask=secret_mask)

    secret_image_1 = secret_image.copy()
    # Translate mask upwards
    offset_y = -5

    M = np.float32([
        [1, 0, 0],
        [0, 1, offset_y]
    ])
    secret_image_1 = cv2.warpAffine(secret_mask, M, (secret_mask.shape[1], secret_mask.shape[0]))
    
    # Translate mask upwards
    pixel_secret_mask_translated = cv2.warpAffine(pixel_secret_mask, M, (pixel_secret_mask.shape[1], pixel_secret_mask.shape[0]))

    noise_2 = noise_generator.generate_noise(secret_image.shape[1], secret_image.shape[0])
    # Remove from noise2 the secret_image_1
    noise_2 = noise_image.copy()

    # Combine pixel_secret_mask_translated to noise_2 
    noise_2 = cv2.bitwise_or(noise_2, pixel_secret_mask_translated)
    


    cv2.imwrite("mask.jpg", secret_mask)
    cv2.imwrite("noise1.jpg", noise_image)
    cv2.imwrite("mask2.jpg", secret_image_1)
    cv2.imwrite("secret_masked.jpg", pixel_secret_mask)
    cv2.imwrite("noise2.jpg", noise_2)
if __name__ == "__main__":
    main()

