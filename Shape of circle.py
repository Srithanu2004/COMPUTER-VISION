import cv2
import numpy as np

def create_image_with_circle():
    # Get the image size from the user
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # Create a white image of the specified size
    # np.ones() creates an array filled with ones, and multiplying by 255 makes it white
    white_image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Get the circle properties from the user
    center_x = int(input("Enter the x-coordinate of the circle center: "))
    center_y = int(input("Enter the y-coordinate of the circle center: "))
    radius = int(input("Enter the radius of the circle: "))

    # Define the circle color (BGR format) and thickness
    circle_color = (0, 0, 255)  # Red color
    thickness = 2  # Thickness of the circle outline

    # Draw the circle on the white image
    cv2.circle(white_image, (center_x, center_y), radius, circle_color, thickness)

    # Display the image with the circle
    cv2.imshow("Image with Circle", white_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the image with the circle (optional)
    output_path = "image_with_circle.jpg"
    cv2.imwrite(output_path, white_image)
    print(f"Image saved as {output_path}")

# Example usage
create_image_with_circle()
