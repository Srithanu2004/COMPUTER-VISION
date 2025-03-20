import cv2

def add_text_to_image(image_path, text):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Define the text properties
    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
    position = (50, 50)  # (x, y) coordinates of the bottom-left corner of the text
    font_scale = 1  # Font scale
    font_color = (0, 255, 0)  # Text color in BGR (green in this case)
    thickness = 2  # Thickness of the text

    # Add the text to the image
    cv2.putText(image, text, position, font, font_scale, font_color, thickness)

    # Display the image with the text
    cv2.imshow("Image with Text", image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the image with the text (optional)
    output_path = "image_with_text.jpg"
    cv2.imwrite(output_path, image)
    print(f"Image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
text = "DHANUSH SANAM"  # Text to display on the image
add_text_to_image(image_path, text)
