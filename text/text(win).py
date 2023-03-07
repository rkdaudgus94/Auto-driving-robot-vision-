import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd += ' --oem 1 --psm 10'  # CUDA 가속 사용을 위한 추가 옵션입니다.

def process_frame(frame):
    text = pytesseract.image_to_string(frame)
    print(text)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    process_frame(frame)

cap.release()
cv2.destroyAllWindows()