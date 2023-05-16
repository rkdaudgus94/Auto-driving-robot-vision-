import easyocr
import cv2

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

cap = cv2.VideoCapture(gst_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
reader = easyocr.Reader(['ko','en'], gpu=False)

if cap.isOpened() :
    while True :
        ret, frame = cap.read()

        # Check if the frame is valid
        text = reader.readtext(frame, detail=0)
        print(text)
        if cv2.waitKey(1) & 0xFF == 27 :
                break
        cv2.imshow('frame', frame)

cv2.imshow()