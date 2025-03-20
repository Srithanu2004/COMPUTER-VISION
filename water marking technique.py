import cv2
import numpy as np

def add_watermark(original_image_path, watermark_image_path, position, alpha=0.5):
    # Load the original image and watermark image
    original_image = cv2.imread(original_image_path)
    watermark_image = cv2.imread(watermark_image_path, cv2.IMREAD_UNCHANGED)  # Load with alpha channel if available

    # Check if the images were loaded successfully
    if original_image is None or watermark_image is None:
        print("Error: Unable to load images.")
        return

    # Resize the watermark to fit the desired size
    watermark_height, watermark_width = watermark_image.shape[:2]
    resized_watermark = cv2.resize(watermark_image, (watermark_width, watermark_height))

    # Get the region of interest (ROI) from the original image where the watermark will be placed
    x, y = position  # Position of the watermark (top-left corner)
    roi = original_image[y:y + watermark_height, x:x + watermark_width]

    # Blend the watermark with the ROI using transparency
    blended_roi = cv2.addWeighted(roi, 1, resized_watermark, alpha, 0)

    # Place the blended ROI back into the original image
    original_image[y:y + watermark_height, x:x + watermark_width] = blended_roi

    # Display the watermarked image
    cv2.imshow("Watermarked Image", original_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the watermarked image (optional)
    output_path = "watermarked_image.jpg"
    cv2.imwrite(output_path, original_image)
    print(f"Watermarked image saved as {output_path}")

# Example usage
original_image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your original image
watermark_image_path = "watermark.png"  # Replace with the path to your watermark image
position = (50, 50)  # Position of the watermark (top-left corner)
alpha = 0.5  # Transparency of the watermark (0 = fully transparent, 1 = fully opaque)
add_watermark(original_image_path, watermark_image_path, position, alpha)
