import cv2
import numpy as np

def create_image_with_rectangle():
    # Get the image size from the user
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # Create a white image of the specified size
    # np.ones() creates an array filled with ones, and multiplying by 255 makes it white
    white_image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Get the rectangle properties from the user
    top_left_x = int(input("Enter the x-coordinate of the top-left corner of the rectangle: "))
    top_left_y = int(input("Enter the y-coordinate of the top-left corner of the rectangle: "))
    bottom_right_x = int(input("Enter the x-coordinate of the bottom-right corner of the rectangle: "))
    bottom_right_y = int(input("Enter the y-coordinate of the bottom-right corner of the rectangle: "))

    # Define the rectangle color (BGR format) and thickness
    rectangle_color = (0, 0, 255)  # Red color
    thickness = 2  # Thickness of the rectangle outline

    # Draw the rectangle on the white image
    cv2.rectangle(white_image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), rectangle_color, thickness)

    # Display the image with the rectangle
    cv2.imshow("Image with Rectangle", white_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the image with the rectangle (optional)
    output_path = "image_with_rectangle.jpg"
    cv2.imwrite(output_path, white_image)
    print(f"Image saved as {output_path}")

# Example usage
create_image_with_rectangle()
