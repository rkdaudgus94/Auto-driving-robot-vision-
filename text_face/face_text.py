import cv2
import face_recognition as fr
import os, sys
import numpy as np
import math
import glob
import pytesseract
import time
from multiprocessing import Process

def face_confidence(face_distance, face_match_threshold=0.6): # face_distance 값과 face_match 임계값을 설정한 사설함수
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'

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

image_path = r'/home/hyun/face_img/*.png'

#mser = cv2.MSER_create() # text를 bounding box로 표시하기 위한 MSER 알고리즘
#regions, _ = mser.detectRegions(src_transform)


class Facerecognition:
    face_location = []
    face_encoding = []
    face_names = []
    known_face_encoding = []
    known_face_names = []
    process_current_frame = True

    def __init__(self):
        self.encode_faces()

    def encode_faces(self):
        os.chdir('/home/hyun/face_img')
        file_names = os.listdir()
        for file_name in file_names :
            self.known_face_names.append(os.path.splitext(file_name)[0])
        for image in glob.glob(image_path):
            face_image = fr.load_image_file(image)
            face_encoding = fr.face_encodings(face_image)[0]
            self.known_face_encoding.append(face_encoding)
        print(self.known_face_names)
    
    def video(self):
        cap = cv2.VideoCapture(gstreamer_pipeline(flip_method = 0), cv2.CAP_GSTREAMER)
        time = 0
        if not cap.isOpened() :
            print('unable to open camera')
            sys.exit()

        while True :
            ret, frame = cap.read()
            time = time + 1
            if self.process_current_frame: # 인식처리를 더 빠르게 하기 위해 1/4 크기로 줄임
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1] # opencv의 bgr => rgb로 변경
                gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
                if time % 5 == 0 :
                    imgchar = pytesseract.image_to_string(gray, lang = 'eng', config= ' --oem 1 --psm 10 ')
                self.face_location = fr.face_locations(rgb_small_frame)
                self.face_encodings = fr.face_encodings(rgb_small_frame, self.face_location)

                self.face_names = []
                for face_encoding in self.face_encodings: # 저장된 얼굴과 캠에서 찍힌 얼굴과 비교
                    match = fr.compare_faces(self.known_face_encoding, face_encoding, 0.55)
                    name = "???"
                    match_percent = "??.?%"
                    face_distance = fr.face_distance(self.known_face_encoding, face_encoding) # 두 사진의 인코딩 거리 값을 비교

                    best_match_index = np.argmin(face_distance) # 최소 값을 가진 인덱스를 알려준다
                    if match[best_match_index] :
                        name = self.known_face_names[best_match_index]
                        match_percent = face_confidence(face_distance[best_match_index])
                    
                    self.face_names.append(f'{name} ({match_percent})')
            self.process_current_frame = not self.process_current_frame

            for (top, right, bottom, left), name in zip(self.face_location, self.face_names) : # 1/4로 축소된 얼굴 크기를 다시 되돌림
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 1)
                cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (0,255,0), cv2.FILLED)
                cv2.putText(frame, name, (left+ 10, bottom - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),1)
            print(imgchar)
            cv2.imshow('Face Recognition', frame)
            if cv2.waitKey(1) == ord('q'):
                    break

        cap.realease()
        cv2.destroyAllWindows()

if __name__ == '__main__' :
    run = Facerecognition()
    run.video()