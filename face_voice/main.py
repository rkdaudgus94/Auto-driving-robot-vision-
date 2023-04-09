import threading
import time
from multi_voice import main_voice
import os
from multi_face import Facerecognition

lock = threading.Lock() # 공유 변수
shared_r_name_list = None

# 스레드 테스트를 위해 def 2개 생성
def func1(name):
    global shared_r_name_list
    face_recognition = Facerecognition()
    
    for names in face_recognition.video():
        str_names = ''.join(str(element) for element in names)
        if shared_r_name_list:
            with lock:
                if str_names == shared_r_name_list:
                    print("일치합니다")
# 사진찍기 기능 추가
def func2(voice):
    global shared_r_name_list
    for r_name_list in main_voice() :
        print ("r_name :" , r_name_list)
        with lock:
            if r_name_list != [] :
                shared_r_name_list = r_name_list
    time.sleep(1)

def main():
    #스레드 정의
    thread1 = threading.Thread(target=func1, args=(True))
    thread2 = threading.Thread(target=func2, args=(True))

    #스레드 시작
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
