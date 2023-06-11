import cv2

def show_webcam_video():
    cap = cv2.VideoCapture(0)  # 0: 기본 카메라를 사용

    if not cap.isOpened():
        print("Unable to open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        cv2.imshow('Webcam Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_webcam_video()
