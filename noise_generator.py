import cv2
import numpy as np

def generate_noise(width: int, height: int) -> cv2.Mat:
    """
    Generate a noise image of the specified width and height.

    Args:
        width (int): The width of the noise image.
        height (int): The height of the noise image.

    Returns:
        cv2.Mat: The generated noise image.
    """
    # Generate binary black-and-white noise, then replicate it across BGR channels.
    noise = np.random.randint(0, 2, (height, width), dtype=np.uint8) * 255
    return cv2.cvtColor(noise, cv2.COLOR_GRAY2BGR)