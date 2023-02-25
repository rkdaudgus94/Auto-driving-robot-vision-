import cv2
import pytesseract
from multiprocessing import Process
import time

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

cap = cv2.VideoCapture(0)
def video_cap():
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

def text():
    while True :
        ret, frame = cap.read()
        if ret == True :
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            imgchar = pytesseract.image_to_string(gray, lang='eng')
            print(imgchar)
            
if __name__ == '__main__' :
    p0 = Process(target=video_cap)
    p1 = Process(target=text)
    p0.start()
    p1.start()
    p0.join()
    p1.join()
    print("main process done")
