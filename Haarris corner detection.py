import cv2
import numpy as np

def detect_corners(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Harris Corner Detection
    # Parameters:
    # - gray_image: The grayscale image
    # - blockSize: Neighborhood size for corner detection
    # - ksize: Aperture parameter for the Sobel operator
    # - k: Harris detector free parameter
    corners = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)

    # Dilate the corner points to make them more visible
    corners = cv2.dilate(corners, None)

    # Mark the detected corners on the original image
    image[corners > 0.01 * corners.max()] = [0, 0, 255]  # Mark corners in red

    # Display the original image with detected corners
    cv2.imshow("Corners Detected", image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the image with detected corners (optional)
    output_path = "corners_detected.jpg"
    cv2.imwrite(output_path, image)
    print(f"Image with detected corners saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
detect_corners(image_path)
