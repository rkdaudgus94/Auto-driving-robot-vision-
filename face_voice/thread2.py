import threading
import time
from multi_voice import get_r_name_list
import os
from multi_face2 import Facerecognition

# 공유 변수를 위한 스레드 락
lock = threading.Lock()

# 결과를 저장할 공유 변수
shared_results = {"func1": None, "func2": None}

def func1(add):
    face_recognition = Facerecognition()
    time1 = 0
    while True:
        for names in face_recognition.video():
            if time1 == 15:
                time1 += 1
                with lock:
                    shared_results["func1"] = names

def func2(add):
    while True:
        r_name_list = get_r_name_list()
        time.sleep(1)
        with lock:
            shared_results["func2"] = r_name_list

def main():
    # 스레드 정의
    thread1 = threading.Thread(target=func2, args=('1',))
    thread2 = threading.Thread(target=func1, args=('2',))

    # 스레드 시작
    thread1.start()
    thread2.start()

    while True:
        # 공유 변수를 사용하여 값이 일치하는지 확인
        with lock:
            if shared_results["func1"] is not None and shared_results["func2"] is not None:
                if shared_results["func1"] == shared_results["func2"]:
                    print("The values match!")
                else:
                    print("The values do not match!")

        # 필요한 경우 검사 간격을 조절할 수 있습니다.
        time.sleep(1)

if __name__ == "__main__":
    main()