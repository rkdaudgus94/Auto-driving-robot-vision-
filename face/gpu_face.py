import cv2

def gstreamer_pipeline(
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink drop=True"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
# GPU를 사용하여 비디오 캡처 초기화
cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# GPU를 사용하여 얼굴 감지기 초기화
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # GPU를 사용하여 프레임 읽기
    ret, frame = cap.read()

    # GPU를 사용하여 얼굴 감지 수행
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

    # 감지된 얼굴에 대해 작업 수행
    for (x, y, w, h) in faces:
        # 얼굴 영역에 대해 특정 작업 수행
        # 예: perform_action(frame[y:y+h, x:x+w])

        # 얼굴 영역에 박스 그리기
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # GPU를 사용하여 프레임 출력
    cv2.imshow('frame', frame)

    # 종료 조건 설정
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()