import cv2
import multiprocessing as mp
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
def text_recognition(frame):
    # 이미지에서 텍스트를 추출합니다.
        text = pytesseract.image_to_string(frame, lang = 'kor')
        print(text)

def video_capture():
    cv2.cuda.setDevice(0)
    stream = cv2.cuda_Stream()

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

    # CPU에서 GPU로 이미지 전송
        img = cv2.cuda_GpuMat(frame, stream=stream)

    # GPU에서 색상 변환 수행
        img = cv2.cuda.cvtColor(img, cv2.COLOR_BGR2GRAY, dst=None, stream=stream)

    # GPU에서 CPU로 이미지 전송
        frame = img.download(stream=stream)

    # 이미지 출력
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # 텍스트인식을 처리할 프로세스 생성
    p1 = mp.Process(target=text_recognition)

    # 비디오 캡처를 처리할 프로세스 생성
    p2 = mp.Process(target=video_capture)

    # 프로세스 실행
    p1.start()
    p2.start()

    # 프로세스 종료 대기
    p1.join()
    p2.join()