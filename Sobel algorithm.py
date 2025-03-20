import cv2
import numpy as np

def apply_sobel(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Sobel operator in the x and y directions
    # Parameters:
    # - gray_image: The grayscale image
    # - cv2.CV_64F: Output image depth (64-bit float)
    # - 1, 0: Compute gradient in the x direction
    # - 0, 1: Compute gradient in the y direction
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the magnitude of the gradients
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize the magnitude to the range [0, 255]
    sobel_magnitude = np.uint8(sobel_magnitude / sobel_magnitude.max() * 255)

    # Display the original and Sobel-filtered images
    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel Magnitude", sobel_magnitude)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the Sobel-filtered image (optional)
    output_path = "sobel_filtered_image.jpg"
    cv2.imwrite(output_path, sobel_magnitude)
    print(f"Sobel-filtered image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
apply_sobel(image_path)
