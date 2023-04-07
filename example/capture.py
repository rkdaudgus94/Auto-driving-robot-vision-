import cv2
import time
import os
def capture_frame(frame, save_path):
    timestamp = int(time.time())
    file_name = f"{save_path}/frame_{timestamp}.png"
    success = cv2.imwrite(file_name, frame)
    if success:
        print(f"Saved frame as {file_name}")
    else:
        print(f"Failed to save frame as {file_name}")

def main():
    cap = cv2.VideoCapture(0)  # 기본 카메라를 사용합니다. 다른 카메라를 사용하려면 인덱스를 변경하세요.

    if not cap.isOpened():
        print("Unable to open camera")
        return

    save_path = r"C:/Users/rkdau/OneDrive/바탕 화면/album"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            capture_frame(frame, save_path)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
