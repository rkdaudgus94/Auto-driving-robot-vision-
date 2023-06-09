import cv2

def gstreamer_pipeline(sensor_id=0):
    return (
        f"nvarguscamerasrc sensor-id={sensor_id} ! "
        "video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)NV12, framerate=(fraction)15/1 ! "
        "nvvidconv flip-method=0 ! "
        "video/x-raw, width=(int)640, height=(int)360, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
    )

# 카메라 0
cap0 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=0), cv2.CAP_GSTREAMER)
# 카메라 1
cap1 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=1), cv2.CAP_GSTREAMER)

while True:
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    if ret0 and ret1:
        cv2.imshow('Camera 0', frame0)
        cv2.imshow('Camera 1', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cap1.release()
cv2.destroyAllWindows()
