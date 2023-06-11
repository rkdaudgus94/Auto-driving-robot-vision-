import easyocr
import cv2

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

cap = cv2.VideoCapture(0)
reader = easyocr.Reader(['ko','en'], gpu = True)
count = 0
while True:
    ret, frame = cap.read()
    if ret:
        count += 1
        if count % 10 == 1 :
            image_path = "D:/text/saved_img.png"
            cv2.imwrite(image_path, frame)
            image = cv2.imread(image_path)
            text = reader.readtext(image, detail=0)
            print(text)
        cv2.imshow('frame', frame)
        # Check if the frame is valid
        if cv2.waitKey(1) & 0xFF == 27:
            break
