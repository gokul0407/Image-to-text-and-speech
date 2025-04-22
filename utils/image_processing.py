# import cv2

# def preprocess_image(image_path):
    
#     image = cv2.imread(image_path)
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#     _, thresh_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY)
#     return thresh_image


import cv2
import logging

def preprocess_image(image_path):
    """
    Preprocesses the image by converting to grayscale, blurring, and applying thresholding.
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            logging.error(f"Failed to read image at {image_path}")
            return None

        # Convert image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Apply binary thresholding
        _, thresh_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY)

        logging.debug("Image preprocessing completed.")
        return thresh_image
    
    except Exception as e:
        logging.error(f"Error during image preprocessing: {e}")
        return None
