import cv2
import numpy as np

# Load the image
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Define a kernel for the erosion operation
    # A larger kernel will result in more erosion
    kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel

    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display the original and eroded images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded_image)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the eroded image
    cv2.imwrite("eroded_image.jpg", eroded_image)
