import cv2

def detect_faces(image_path):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,  # Scale factor for image pyramid
        minNeighbors=5,   # Minimum number of neighbors for a region to be considered a face
        minSize=(30, 30)  # Minimum size of a face
    )

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle with thickness 2

    # Display the image with detected faces
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the image with detected faces (optional)
    output_path = "faces_detected.jpg"
    cv2.imwrite(output_path, image)
    print(f"Image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
detect_faces(image_path)
