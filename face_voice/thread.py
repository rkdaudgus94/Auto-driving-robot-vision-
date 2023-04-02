import threading
import time

# 스레드 테스트를 위해 def 2개 생성
def func1(add):
    while(True):
        print("작업 1111", add)
        time.sleep(1)

def func2(add):
    while(True):
        print("작업 2222", add)
        time.sleep(1)

def main():
    #스레드 정의
    thread1 = threading.Thread(target=func1, args=('1'))
    thread2 = threading.Thread(target=func2, args=('2'))

    #스레드 시작
    thread1.start()
    thread2.start()
    print("done!")

if __name__ == "__main__":
    main()