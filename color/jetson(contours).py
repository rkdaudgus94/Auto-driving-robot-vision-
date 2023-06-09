import cv2
import numpy as np
import os, sys
import time

count = 0
MIN_CONTOUR_AREA = 3500
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

def color_recognition(frame) :
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([170, 70, 50])
    upper_red = np.array([180, 255, 255])
    #lower_red = np.array([0, 90, 80])
    #upper_red = np.array([10, 255, 255])

    #lower_red1 = np.array([130, 50, 50])
    #upper_red1 = np.array([160, 255, 255])
    
    lower_purple = np.array([130, 50, 50])
    upper_purple = np.array([160, 255, 255])


    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_purple, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    roi_red = None
    roi_purple = None
    roi_green = None
    
    #for cnt_red in contours_red :
    #    x_r, y_r, w_r, h_r = cv2.boundingRect(cnt_red) # 외곽선 경계 사각형 구함 
    #    cv2.rectangle(frame, (x_r, y_r), (x_r + w_r, y_r + h_r), (0, 0, 255), 2) # w는 너비 h는 높이, 녹색, 두께
    #    roi_red = mask_red[y_r : y_r + h_r, x_r : x_r + w_r] # 해당 영역 이미지 잘라내고 확대`1`

    for cnt_red in contours_red:
        if cv2.contourArea(cnt_red) > MIN_CONTOUR_AREA:
            x_r, y_r, w_r, h_r = cv2.boundingRect(cnt_red)
            if abs(w_r - h_r) <= 5:
                cv2.rectangle(frame, (x_r, y_r), (x_r + w_r, y_r + h_r), (0, 0, 255), 2)
                roi_red = mask_red[y_r : y_r + h_r, x_r : x_r + w_r]

    for cnt_purple in contours_purple :
        if cv2.contourArea(cnt_purple) > MIN_CONTOUR_AREA:
            x_b, y_b, w_b, h_b = cv2.boundingRect(cnt_purple)
            if abs(w_b - h_b) <= 5:
                cv2.rectangle(frame, (x_b, y_b), (x_b + w_b, y_b + h_b), (128, 0, 128), 2)
                roi_purple = mask_purple[y_b:y_b + h_b, x_b:x_b + w_b]

    for cnt_green in contours_green :
        if cv2.contourArea(cnt_green) > MIN_CONTOUR_AREA:
            x_g, y_g, w_g, h_g = cv2.boundingRect(cnt_green)
            if abs(w_g - h_g) <= 5:
                cv2.rectangle(frame, (x_g, y_g), (x_g + w_g, y_g + h_g), (0, 255, 0), 2)
                roi_green = mask_green[y_g:y_g + h_g, x_g:x_g + w_g]

    #remask_red = cv2.inRange(roi_red, lower_red,upper_red)
    #remask_purple = cv2.inRange(roi_purple, lower_purple,upper_purple)
    #remask_green = cv2.inRange(roi_green, lower_green,upper_green)

    red_pixels = cv2.countNonZero(roi_red) 
    purple_pixels = cv2.countNonZero(roi_purple) 
    green_pixels = cv2.countNonZero(roi_green) 
    
    return frame, red_pixels, purple_pixels, green_pixels



cap = cv2.VideoCapture(gstreamer_pipeline(flip_method = 0), cv2.CAP_GSTREAMER)

if not cap.isOpened() :
        print('unable to open camera')
        sys.exit()

while True :
        # 이미지 불러오기
    count += 1
    ret, frame = cap.read()
    
    if not ret:
        print('Error reading video stream')
        break

    color_frame, r_pix, p_pix, g_pix  = color_recognition(frame)

    if count % 20 == 0 :
        colors = {1: r_pix, 2: p_pix, 3: g_pix}
        max_color = max(colors, key=colors.get)
        print(max_color)
        if max_color == 1 :
            print("620호 입니다.")
        elif max_color == 2 :
            print("619호 입니다. ")
        elif max_color == 3 :
            print("610호 입니다.")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('frame', color_frame)

cap.release()
cv2.destroyAllWindows()

