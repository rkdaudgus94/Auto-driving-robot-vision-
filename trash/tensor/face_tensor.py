import cv2
import numpy as np
import tensorflow as tf
from mtcnn import MTCNN
from scipy.spatial.distance import cosine
from tensorflow.keras.models import load_model

def preprocess_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (160, 160))
    img = img.astype("float32")
    img = (img - 128) / 128
    return img

def get_face_embeddings(model, face):
    face = preprocess_image(face)
    face = np.expand_dims(face, axis=0)
    embedding = model.predict(face)[0]
    return embedding

def compare_faces(embedding1, embedding2, threshold=0.5):
    distance = cosine(embedding1, embedding2)
    return distance < threshold

# Load the FaceNet model
facenet_model = load_model("facenet_keras.h5")

# Initialize the MTCNN face detector
detector = MTCNN()

# Load the known faces and their names
known_faces = np.load("known_faces.npy")
known_names = np.load("known_names.npy")

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect faces
    faces = detector.detect_faces(frame)

    for face in faces:
        x, y, w, h = face["box"]
        face_img = frame[y:y+h, x:x+w]

        # Get the face embedding
        face_embedding = get_face_embeddings(facenet_model, face_img)

        # Compare the face with known faces
        min_distance = 10000
        min_index = -1
        for i, known_face in enumerate(known_faces):
            distance = cosine(face_embedding, known_face)
            if distance < min_distance:
                min_distance = distance
                min_index = i

        # If a match is found, display the name
        if min_distance < 0.5:
            name = known_names[min_index]
        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
