import cv2
import numpy as np

def apply_dilation(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Define a kernel (structuring element)
    # A larger kernel will result in more dilation
    kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel

    # Apply the dilation operation
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display the original and dilated images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated_image)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the dilated image (optional)
    output_path = "dilated_image.jpg"
    cv2.imwrite(output_path, dilated_image)
    print(f"Dilated image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
apply_dilation(image_path)
