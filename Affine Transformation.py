import cv2
import numpy as np

def apply_affine_transformation(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Get the image dimensions
    height, width = image.shape[:2]

    # Define the transformation matrix for affine transformation
    # Example: Rotation by 45 degrees, scaling by 0.5, and translation by (100, 50)
    angle = 45  # Rotation angle in degrees
    scale = 0.5  # Scaling factor
    tx, ty = 100, 50  # Translation in x and y directions

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, scale)

    # Add translation to the rotation matrix
    rotation_matrix[0, 2] += tx  # Add translation in x direction
    rotation_matrix[1, 2] += ty  # Add translation in y direction

    # Apply the affine transformation
    transformed_image = cv2.warpAffine(image, rotation_matrix, (width, height))

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
apply_affine_transformation(image_path)
