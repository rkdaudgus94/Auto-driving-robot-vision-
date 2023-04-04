import threading
import time
from multi_voice import get_r_name_list
import os
from multi_face2 import Facerecognition

def func1(add, func1_result):
    face_recognition = Facerecognition()
    time1 = 0
    for names in face_recognition.video():
        if time1 == 15:
            time1 += 1
            func1_result.append(names)

def func2(add, func2_result):
    r_name_list = get_r_name_list()
    time.sleep(1)
    func2_result.append(r_name_list)

def main():
    while True:
        # 반환 값을 저장할 리스트
        func1_result = []
        func2_result = []

        # 스레드 정의
        thread1 = threading.Thread(target=func2, args=('1', func2_result))
        thread2 = threading.Thread(target=func1, args=('2', func1_result))

        # 스레드 시작
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        # 반환 값이 일치하는지 확인
        if set(func1_result) == set(func2_result):
            print("The values match!")
        else:
            print("The values do not match.")

        # 반복 주기를 설정하려면 다음 코드의 주석을 해제하십시오.
        # time.sleep(10)

if __name__ == "__main__":
    main()