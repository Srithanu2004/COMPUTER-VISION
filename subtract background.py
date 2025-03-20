import cv2
import numpy as np

def subtract_background(image_path, lower_color, upper_color):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the background color in HSV
    # Example: lower_color = np.array([0, 0, 0])  # Black background
    #          upper_color = np.array([180, 255, 50])  # Dark colors
    lower_bound = np.array(lower_color)
    upper_bound = np.array(upper_color)

    # Create a mask for the background
    background_mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Invert the mask to get the foreground
    foreground_mask = cv2.bitwise_not(background_mask)

    # Extract the foreground from the original image
    foreground = cv2.bitwise_and(image, image, mask=foreground_mask)

    # Display the original image, background mask, and extracted foreground
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Mask", background_mask)
    cv2.imshow("Extracted Foreground", foreground)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the results (optional)
    cv2.imwrite("background_mask.jpg", background_mask)
    cv2.imwrite("extracted_foreground.jpg", foreground)

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
lower_color = [0, 0, 0]  # Lower bound of the background color in HSV (e.g., black)
upper_color = [180, 255, 50]  # Upper bound of the background color in HSV (e.g., dark colors)
subtract_background(image_path, lower_color, upper_color)
