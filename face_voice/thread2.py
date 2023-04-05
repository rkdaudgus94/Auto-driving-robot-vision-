import threading
import time
from multi_voice import get_r_name_list
import os
from multi_face2 import Facerecognition

# 공유 변수를 위한 스레드 락
lock = threading.Lock()

def compare_values(value1, value2):
    if value1 is not None and value2 is not None:
        if value1 == value2:
            print("The values match!")
        else:
            print("The values do not match!")

def func1(add):
    face_recognition = Facerecognition()
    time1 = 0
    for names in face_recognition.video():
        if time1 == 5:
            time1 += 1
            with lock:
                compare_values(names, r_name_list)

def func2(add):
    global r_name_list
    while True:
        r_name_list = get_r_name_list()
        with lock:
            compare_values(r_name_list, r_name_list)

def main():
    # 스레드 정의
    thread1 = threading.Thread(target=func2, args=('1',))
    thread2 = threading.Thread(target=func1, args=('2',))

    # 스레드 시작
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
