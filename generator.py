import sys, os
import cv2
import numpy as np

import secret_reader
import noise_generator

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python generator.py <image>")

    print(f"Generating from: {sys.argv[1]}")
        # create directory if it doesn't exist
  
    if not os.path.exists("output"):
        os.makedirs("output")
    else:
        for f in os.listdir("output"):
            os.remove(os.path.join("output", f))
            
    # Create the "secret mask"
    secret_image = secret_reader.load(sys.argv[1])
    secret_mask = secret_reader.create_secret_mask(secret_image)

    # Crate the initial image
    noise_image = noise_generator.generate_noise(secret_image.shape[1], secret_image.shape[0])

    # Extract all elements from the noise image that are part of the secret mask
    pixel_secret_mask = cv2.cvtColor(noise_image, cv2.COLOR_BGR2BGRA)
    pixel_secret_mask[:, :, 3] = secret_mask # Use the mask as alpha channel

    # Save it
    cv2.imwrite("output/1.png", noise_image)

    # Loop for every image to generate
    for i in range(4):

        # Translation
        offset_y = -1

        M = np.float32([
            [1, 0, 0],
            [0, 1, offset_y]
        ])
        secret_mask = cv2.warpAffine(secret_mask, M, (secret_mask.shape[1], secret_mask.shape[0]))
        pixel_secret_mask = cv2.warpAffine(pixel_secret_mask, M, (pixel_secret_mask.shape[1], pixel_secret_mask.shape[0]))

        # Remove all pixels on "noise_image_copy" that are part of the translated secret mask
        noise_image_copy = noise_image.copy()
        noise_image_copy[secret_mask == 255] = [0, 0, 0]  # Set those pixels to black
    
        # Combine the "noise_image_copy" and the translated secret mask
        combined_image = noise_image_copy.copy()
        opaque_pixels = pixel_secret_mask[:, :, 3] > 0
        combined_image[opaque_pixels] = pixel_secret_mask[opaque_pixels, :3]
        
        # Save the combined image
        cv2.imwrite(f"output/{i + 2}.png", combined_image)

   
if __name__ == "__main__":
    main()

