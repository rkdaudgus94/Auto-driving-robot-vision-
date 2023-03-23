import cv2
import numpy as np
import os
def detect_faces(image, net, conf_threshold=0.5):
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    faces = []

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > conf_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            faces.append((start_x, start_y, end_x, end_y))

    return faces

# 모델 파일 경로 설정

current_directory = os.path.dirname(os.path.abspath(__file__))
prototxt_path = os.path.join(current_directory, 'deploy.prototxt.txt')
caffemodel_path = os.path.join(current_directory, 'res10_300x300_ssd_iter_140000.caffemodel')

# 모델 로드
net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# GPU 사용 설정
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# 카메라 모듈 초기화
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    faces = detect_faces(frame, net)

    for (start_x, start_y, end_x, end_y) in faces:
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
