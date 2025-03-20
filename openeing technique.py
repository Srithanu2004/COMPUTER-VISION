import cv2
import numpy as np

def apply_opening(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Define a kernel (structuring element)
    # A larger kernel will remove larger noise
    kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel

    # Apply the Opening operation
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # Display the original and Opening images
    cv2.imshow("Original Image", image)
    cv2.imshow("Opening Image", opening)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the Opening image (optional)
    output_path = "opening_image.jpg"
    cv2.imwrite(output_path, opening)
    print(f"Opening image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
apply_opening(image_path)
