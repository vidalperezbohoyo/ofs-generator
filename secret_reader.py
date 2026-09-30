import cv2

def load(path : str) -> cv2.Mat:
    """
    Load an image from the specified path.

    Args:
        path (str): The path to the image file.
    """
    image = cv2.imread(path)

    # Check if the image was loaded successfully
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {path}")

    return image

def create_secret_mask(image : cv2.Mat) -> cv2.Mat:
    """
    Create a mask for the secret color in the image.

    Args:
        image (cv2.Mat): The input image.

    Returns:
        cv2.Mat: The mask where the secret color is present.
    """
    
    # Black in image will be considered as the secret color and will be the mask
    # Consider a range of black colors to account for variations in the image
    mask = cv2.inRange(image, (0, 0, 0), (50, 50, 50))
    return mask