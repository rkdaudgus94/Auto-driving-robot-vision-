import cv2
import dlib
import speech_recognition as sr
from multiprocessing import Process

def face_detection_function():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)

        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def voice_recognition_function():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("음성 인식을 시작합니다. 말하세요!")
        audio = recognizer.listen(source)

    try:
        print("음성 인식 중...")
        recognized_text = recognizer.recognize_google(audio, language="ko-KR")
        print("인식된 텍스트: " + recognized_text)
    except sr.UnknownValueError:
        print("음성 인식에 실패했습니다.")
    except sr.RequestError as e:
        print(f"구글 음성 인식 서비스에 요청하는 동안 오류 발생; {e}")

if __name__ == "__main__":
    face_detection_process = Process(target=face_detection_function)
    voice_recognition_process = Process(target=voice_recognition_function)

    face_detection_process.start()
    voice_recognition_process.start()

    face_detection_process.join()
    voice_recognition_process.join()
