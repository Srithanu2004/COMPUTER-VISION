import cv2
import numpy as np

def subtract_foreground(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Create a background subtractor object
    # You can use either MOG2 or KNN
    bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
    # bg_subtractor = cv2.createBackgroundSubtractorKNN(history=500, dist2Threshold=400, detectShadows=True)

    # Apply the background subtractor to get the foreground mask
    fg_mask = bg_subtractor.apply(image)

    # Refine the mask using morphological operations (optional)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)  # Remove noise
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)  # Fill holes

    # Extract the foreground from the original image
    foreground = cv2.bitwise_and(image, image, mask=fg_mask)

    # Display the original image, foreground mask, and extracted foreground
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Mask", fg_mask)
    cv2.imshow("Extracted Foreground", foreground)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the results (optional)
    cv2.imwrite("foreground_mask.jpg", fg_mask)
    cv2.imwrite("extracted_foreground.jpg", foreground)

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
subtract_foreground(image_path)
