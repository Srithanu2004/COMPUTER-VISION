import cv2

def segment_image(image_path, threshold_value):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, segmented_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the original and segmented images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented_image)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the segmented image (optional)
    output_path = "segmented_image.jpg"
    cv2.imwrite(output_path, segmented_image)
    print(f"Segmented image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
threshold_value = 127  # Replace with the desired threshold value (0 to 255)
segment_image(image_path, threshold_value)
