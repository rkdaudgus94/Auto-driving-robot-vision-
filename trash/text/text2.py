import cv2
import pytesseract
import numpy as np
 # pytesseract.pytesseract.tesseract_cmd = "/home/hyun/tesseract.exe"
def gst_pipeline(
    sensor_id = 0,
    capture_width = 1920,
    capture_height = 1080,
    display_width = 960,
    display_height = 540,
    framerate = 30,
    flip_method = 0,
) :
    return (
        sensor_id,
        capture_width,
        capture_height,
        framerate,
        flip_method,
        display_width,
        display_height,
    )

time = 0

window_title = "CSI Camera"
print(gst_pipeline(flip_method=0))
video_capture = cv2.VideoCapture(gst_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

if video_capture.isOpened():
    frame_width = int(video_capture.get(3)) 
    frame_height = int(video_capture.get(4))
    out = cv2.VideoWriter('/home/hyun/video/output.avi',
                        cv2.VideoWriter_fourcc('D','I','V','X'),
                        10,
                        (frame_width,frame_height) )
    try : # error code가 발생할 것 같은 곳에서 쓰임
        # window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE) # 창을 띄우는데 사용
        while True :
            ret, frame =video_capture.read()
            time += 1
            
            if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
        
        #윈도우의 파라미터를 취득하는 함수로, 제 2의 인수에 
        #cv2.WND_PROP_ASPECT_RATIO를 지정함으로써 창의 aspect비를 리턴값으로 취득하는 것이 가능하다.
        #닫기 버튼을 누르면 -1.0이 반환된다.
        #WND_PROP_AUTOSIZE => 0 : 최대화 , 1 : 전체 화면으로 표시
                out.write(frame)
                cv2.imshow('frame', frame)
                if (time % 5) == 0 :
                    rgb_image = cv2.cvtColor(frame, cv2.CoLOR_BGR2RGB)
                    imgchar = pytesseract.image_to_string(rgb_image, lang='kor')
                    imgboxes = pytesseract.image_to_boxes(frame)
                    print(imgchar)
            else :
                break
            keyCode = cv2.waitKey(10) & 0xFF
            # 멈추려면 ESC or 'q'
            if keyCode == 27 or keyCode == ord('q'):
                break
    finally :
        video_capture.release()
        cv2.destroyAllWindows()
else :
    print("Unable to open camera")