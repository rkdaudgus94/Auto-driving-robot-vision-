import cv2
import pytesseract
import threading
import face_recognition
# 비디오 스트림을 초기화합니다.
time = 0
# pytesseract OCR 엔진을 초기화합니다.
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
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
cap = cv2.VideoCapture(gstreamer_pipeline(flip_method = 0), cv2.CAP_GSTREAMER)
# 텍스트 인식을 처리하는 함수를 정의합니다.
def recognize_text(frame):
    # 이미지에서 텍스트를 추출합니다.
    text = pytesseract.image_to_string(frame, lang = 'kor')
    if time % 10 == 0 :
        print(text)

def detect_faces(frame):
    # 이미지에서 얼굴을 검출합니다.
    face_locations = face_recognition.face_locations(frame)
    # 각 얼굴의 경계선 좌표를 출력합니다.
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

# 비디오를 촬영하고 텍스트를 인식하는 함수를 정의합니다.
def capture_video():
    while True:
        # 비디오 프레임을 캡처합니다.
        ret, frame = cap.read()
        if ret:
            # 이미지를 회색조로 변환합니다.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 이미지에서 경계선을 검출합니다.
            edges = cv2.Canny(gray, 50, 150)
            # 경계선을 감지하고 텍스트를 추출합니다.
            recognize_thread = threading.Thread(target=recognize_text, args=(edges,))
            recognize_thread.start()
            # 얼굴인식
            detect_thread = threading.Thread(target=detect_faces, args=(frame,))
            detect_thread.start()
            # 원본 이미지에 경계선을 그립니다.
            cv2.imshow('Video', frame)
        # ESC 키를 누르면 종료합니다.
        if cv2.waitKey(1) == 27:
            break

# 비디오 캡처 및 텍스트 인식 스레드를 시작합니다.
video_thread = threading.Thread(target=capture_video)
video_thread.start()

# 모든 스레드가 종료될 때까지 대기합니다.
video_thread.join()

# 비디오 스트림을 종료합니다.
cap.release()
cv2.destroyAllWindows()