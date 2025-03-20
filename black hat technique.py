import cv2
import numpy as np

def apply_black_hat(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Define a kernel (structuring element)
    # A larger kernel will capture larger dark regions
    kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel

    # Apply the Black Hat operation
    black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

    # Display the original and Black Hat images
    cv2.imshow("Original Image", image)
    cv2.imshow("Black Hat Image", black_hat)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the Black Hat image (optional)
    output_path = "black_hat_image.jpg"
    cv2.imwrite(output_path, black_hat)
    print(f"Black Hat image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
apply_black_hat(image_path)
