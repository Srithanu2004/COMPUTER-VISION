from PIL import Image, ImageFilter

# Load the image
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
image = Image.open(image_path)

# Apply Gaussian Blur
# Parameter: radius (controls the intensity of the blur)
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))

# Save or display the blurred image
blurred_image.save("blurred_image.jpg")  # Save the blurred image
blurred_image.show()  # Display the blurred image
