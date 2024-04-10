import cv2
import face_recognition

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load a sample image and learn how to recognize it
known_image = face_recognition.load_image_file("known_person.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize variables
face_names = []
face_encodings = []

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to RGB (required by face_recognition library)
    rgb_frame = frame[:, :, ::-1]

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Find face encodings for the detected faces
    for (x, y, w, h) in faces:
        face_encodings = face_recognition.face_encodings(rgb_frame, [(y, x+w, y+h, x)])[0]
        
        # Compare face encodings with the known face
        matches = face_recognition.compare_faces([known_encoding], face_encodings)
        
        name = "Unknown"
        if matches[0]:
            name = "Known Person"
        
        face_names.append(name)
    
    # Draw rectangles and labels for each face
    for (x, y, w, h), name in zip(faces, face_names):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Display the frame with detected faces
    cv2.imshow('Face Detection and Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
