import cv2
import torch
from facenet_pytorch import MTCNN

if torch.cuda.is_available():
    print("GPU is being used.")
else:
    print("CPU is being used.")

# ... (생략) ...

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

# GPU를 사용하는 경우
if torch.cuda.is_available():
    gpu_frame = cv2.cuda_GpuMat()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if torch.cuda.is_available():
        gpu_frame.upload(frame)
        frame_gpu = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2RGB)
        boxes, _ = mtcnn.detect(frame_gpu.download())

        if boxes is not None:
            for box in boxes:
                x1, y1, x2, y2 = box.astype(int)
                cv2.cuda.rectangle(gpu_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        frame = gpu_frame.download()
    else:
        boxes, _ = mtcnn.detect(frame)

        if boxes is not None:
            for box in boxes:
                x1, y1, x2, y2 = box.astype(int)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()