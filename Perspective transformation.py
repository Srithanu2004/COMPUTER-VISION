import cv2
import numpy as np

def apply_perspective_transformation(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Define the source points (coordinates of the 4 corners of the region to transform)
    # Example: A rectangle in the image
    height, width = image.shape[:2]
    src_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])

    # Define the destination points (coordinates of the 4 corners of the transformed region)
    # Example: A trapezoid to simulate perspective change
    dst_points = np.float32([[50, 50], [width - 100, 100], [50, height - 50], [width - 100, height - 100]])

    # Calculate the perspective transformation matrix
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply the perspective transformation
    transformed_image = cv2.warpPerspective(image, perspective_matrix, (width, height))

    # Display the original and transformed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the transformed image (optional)
    output_path = "transformed_image.jpg"
    cv2.imwrite(output_path, transformed_image)
    print(f"Transformed image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
apply_perspective_transformation(image_path)
