import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# Function to load and preprocess an image
def load_and_preprocess_image(image_path):
    img = load_img(image_path, target_size=(160, 160))  # Adjust size as needed
    x = img_to_array(img)
    x = x / 255.0  # Normalize pixel values
    return x.reshape((1, x.shape[0], x.shape[1], x.shape[2]))

# Function to extract facial encodings (embeddings) using a pre-trained model
def get_face_encodings(model, image, face_locations):
    faces = []
    for (top, right, bottom, left) in face_locations:
        face_img = image[top:bottom, left:right]
        face_img = load_and_preprocess_image(face_img)
        face_embeddings = model.predict(face_img)[0]
        faces.append(face_embeddings)
    return faces

# Load MTCNN model for face detection
mtcnn_model = tf.keras.models.load_model('path/to/mtcnn_model.h5')  # Replace with your model path

# Load Facenet model for face recognition (e.g., keras-vggface2)
facenet_model = tf.keras.applications.VGGFace2(weights='imagenet', include_top=False)

# Load known face encodings from a dictionary or database
known_face_encodings = ...  # Load from your data source
known_face_names = ...  # Corresponding names for known encodings

# Process a test image
test_image = load_img('path/to/test_image.jpg', target_size=(160, 160))
test_image = img_to_array(test_image)
test_image = test_image / 255.0
test_image = np.expand_dims(test_image, axis=0)  # Add batch dimension

# Detect faces
face_locations = mtcnn_model.predict(test_image)[0]  # Adjust indexing as needed

# Extract face encodings
face_encodings = get_face_encodings(facenet_model, test_image, face_locations)

# Identify faces
for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
    matches = tf.reduce_sum(tf.math.abs(face_encoding - known_face_encodings), axis=1) <= 0.5  # Adjust threshold for distance metric
    name = "Unknown"

    if tf.math.reduce_any(matches):
        first_match_index = tf.math.argmin(matches)
        name = known_face_names[first_match_index]

    # Draw bounding boxes and labels (optional)
    cv2.rectangle(test_image, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.putText(test_image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display the processed image (optional)
cv2.imshow('Test Image', test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
