import cv2
import torch
from facenet_pytorch import MTCNN

if torch.cuda.is_available():
    print("GPU is being used.")
else:
    print("CPU is being used.")
def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)
mtcnn = MTCNN(keep_all=True, device=device)

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method = 0), cv2.CAP_GSTREAMER)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    boxes, _ = mtcnn.detect(frame)

    """ if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = box.astype(int)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2) """

    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
