import cv2
import numpy as np
from matplotlib import pyplot as plt

def analyze_histogram(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Split the image into its color channels (B, G, R)
    blue_channel, green_channel, red_channel = cv2.split(image)

    # Calculate the histogram for each channel
    blue_hist = cv2.calcHist([blue_channel], [0], None, [256], [0, 256])
    green_hist = cv2.calcHist([green_channel], [0], None, [256], [0, 256])
    red_hist = cv2.calcHist([red_channel], [0], None, [256], [0, 256])

    # Plot the histograms
    plt.figure(figsize=(10, 6))

    plt.plot(blue_hist, color='blue', label='Blue Channel')
    plt.plot(green_hist, color='green', label='Green Channel')
    plt.plot(red_hist, color='red', label='Red Channel')

    plt.title("Histogram of Color Levels")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
analyze_histogram(image_path)
