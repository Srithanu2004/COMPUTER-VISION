import cv2
import numpy as np

def create_image_with_colored_boxes():
    # Get the image size from the user
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # Create a white image of the specified size
    # np.ones() creates an array filled with ones, and multiplying by 255 makes it white
    white_image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate the size of the boxes (1/10th of the image size)
    box_width = width // 10
    box_height = height // 10

    # Define the colors for the boxes (BGR format)
    colors = {
        "Black": (0, 0, 0),
        "Blue": (255, 0, 0),
        "Green": (0, 255, 0),
        "Red": (0, 0, 255)
    }

    # Draw the colored boxes at each corner
    # Top-left corner: Black
    white_image[:box_height, :box_width] = colors["Black"]

    # Top-right corner: Blue
    white_image[:box_height, -box_width:] = colors["Blue"]

    # Bottom-left corner: Green
    white_image[-box_height:, :box_width] = colors["Green"]

    # Bottom-right corner: Red
    white_image[-box_height:, -box_width:] = colors["Red"]

    # Display the image with the colored boxes
    cv2.imshow("Image with Colored Boxes", white_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the image with the colored boxes (optional)
    output_path = "image_with_colored_boxes.jpg"
    cv2.imwrite(output_path, white_image)
    print(f"Image saved as {output_path}")

# Example usage
create_image_with_colored_boxes()
