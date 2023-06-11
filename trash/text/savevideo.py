import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Unable to read camera")

else :
# 프레임 정보
    frame_width = int(cap.get(3))
    frame_heigt = int(cap.get(4))

# 캠에서 찍은 비디오 저장
out = cv2.VideoWriter('C:/Users/rkdau/OneDrive/사진/카메라 앨범/output.avi',
                cv2.VideoWriter_fourcc('D','I','V','X'),
                10,
                (frame_width, frame_heigt) )
time = 0
while True :
    ret, frame = cap.read()
    time += 1
    
    if ret == True :
        out.write(frame)
        cv2.imshow('frame', frame)
        if (time % 1) == 0 :   
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            imgchar = pytesseract.image_to_string(rgb_image, lang='kor')
            imgboxes = pytesseract.image_to_boxes(frame)
            print(imgchar)
        if cv2.waitKey(1) & 0xFF == 27 :
            break
    else :
        break