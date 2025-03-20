import cv2

# Load the image
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Get the original dimensions of the image
    original_height, original_width = image.shape[:2]

    # Resize the image to a smaller size (e.g., half the original size)
    scale_percent = 50  # Resize to 50% of the original size
    new_width = int(original_width * scale_percent / 100)
    new_height = int(original_height * scale_percent / 100)
    smaller_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Resize the image to a larger size (e.g., double the original size)
    scale_percent = 200  # Resize to 200% of the original size
    new_width = int(original_width * scale_percent / 100)
    new_height = int(original_height * scale_percent / 100)
    larger_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Display the original, smaller, and larger images
    cv2.imshow("Original Image", image)
    cv2.imshow("Smaller Image", smaller_image)
    cv2.imshow("Larger Image", larger_image)
    cv2.waitKey(0)  # Wait for a key press to close the windows
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the resized images
    cv2.imwrite("smaller_image.jpg", smaller_image)
    cv2.imwrite("larger_image.jpg", larger_image)
