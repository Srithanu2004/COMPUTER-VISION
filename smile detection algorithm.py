import cv2

def detect_smile(image_path):
    # Load the pre-trained Haar Cascade models for face and smile detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

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

    # Iterate over each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle with thickness 2

        # Extract the region of interest (ROI) for the face
        face_roi = gray_image[y:y + h, x:x + w]

        # Detect smiles within the face ROI
        smiles = smile_cascade.detectMultiScale(
            face_roi,
            scaleFactor=1.7,  # Scale factor for image pyramid
            minNeighbors=20,  # Minimum number of neighbors for a region to be considered a smile
            minSize=(25, 25)  # Minimum size of a smile
        )

        # Iterate over each detected smile
        for (sx, sy, sw, sh) in smiles:
            # Draw a rectangle around the smile
            cv2.rectangle(image, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 0, 255), 2)  # Red rectangle with thickness 2

    # Display the image with detected faces and smiles
    cv2.imshow("Smile Detection", image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the image with detected smiles (optional)
    output_path = "smile_detection.jpg"
    cv2.imwrite(output_path, image)
    print(f"Image saved as {output_path}")

# Example usage
image_path = "C:\\Users\\thanu\\Downloads\\IMG_0808.JPG"  # Replace with the path to your image
detect_smile(image_path)
