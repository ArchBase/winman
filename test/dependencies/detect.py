import cv2
import time
from deepface import DeepFace


color = (0, 0, 255)
# Load the pre-trained face detection model
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

reference_img = cv2.imread("test/dependencies/r.jpg")
# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    #time.sleep(2)
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    #faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    try:
        if DeepFace.verify(frame, reference_img)['verified']:
            print("yes" + time.strftime("%H:%M:%S", time.localtime()))
            color = (0, 255, 0)
        else:
            print("no" + time.strftime("%H:%M:%S", time.localtime()))
            color = (0, 0, 255)
    except ValueError:
        print("invalid" + time.strftime("%H:%M:%S", time.localtime()))
        color = (255, 0, 0)
    
    # Draw rectangles around the detected faces
    #for (x, y, w, h) in faces:
    #    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
    
    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()