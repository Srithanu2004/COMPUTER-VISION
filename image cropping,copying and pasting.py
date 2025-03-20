import cv2

def crop_copy_paste(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Define the region of interest (ROI) to crop
    # Example: Crop a rectangle from (x1, y1) to (x2, y2)
    x1, y1, x2, y2 = 100, 100, 300, 300  # Coordinates of the ROI
    cropped_roi = image[y1:y2, x1:x2]  # Crop the ROI using array slicing

    # Create a copy of the cropped ROI
    copied_roi = cropped_roi.copy()

    # Paste the copied ROI into another part of the image
    # Example: Paste the ROI at (x3, y3)
    x3, y3 = 400, 100  # Coordinates where the ROI will be pasted
    image[y3:y3 + (y2 - y1), x3:x3 + (x2 - x1)] = copied_roi

    # Display the original image with the pasted ROI
    cv2.imshow("Original Image with Pasted ROI", image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the modified image (optional)
    output_path = "modified_image.jpg"
    cv2.imwrite(output_path, image)
    print(f"Modified image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
crop_copy_paste(image_path)
