from PIL import Image

# Escape backslashes in the file path
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Double backslashes

# Load the image
image = Image.open(image_path)

# Convert the image to grayscale
gray_image = image.convert("L")

# Save or display the grayscale image
gray_image.save("gray_image.jpg")  # Save the grayscale image
gray_image.show()  # Display the grayscale image
