import cv2
from multiprocessing import Process
import multiprocessing
import time
def video_cap():

    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        try :
            while True :
                ret, frame = cap.read()
                if ret == True :
                    cv2.imshow('frame', frame)
                keycode = cv2.waitKey(10) & 0xFF
                
                if keycode == 27 or keycode == ord('q'):
                    break

        finally :
            cap.release()
            cv2.destroyAllWindows()

def prt():

       # a = input("글자를 입력하세요")
        print(1)
        #return a
            



if __name__ == '__main__' :
    p0 = Process(target = video_cap)
    p1 = Process(target = prt)
    
    p0.start()
    p1.start()
    p0.join()
    p1.join()
    print("main process done?")