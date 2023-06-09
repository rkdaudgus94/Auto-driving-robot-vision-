import cv2
import numpy as np
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# 이미지 불러오기
img = cv2.imread("D:/color/color_circle.png")

# BGR에서 HSV로 변환
# cv2.cvtColor 함수는 이미지의 색 공간을 변환합니다. 
# 여기서는 이미지를 BGR 색 공간(OpenCV의 기본 색 공간)에서 HSV 색 공간으로 변환합니다. HSV 색 공간은 색상을 인식하는 데 더 적합합니다.

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

# 색상 범위 정의 - 예: 녹색
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

lower_blue = np.array([100, 100, 100])
upper_blue = np.array([140, 255, 255])

lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])

#lower_red2 = np.array([170, 70, 50])
#upper_red2 = np.array([180, 255, 255])

# HSV 이미지에서 녹색만 추출하기 위한 임계값
mask_red = cv2.inRange(hsv, lower_red1, upper_red1)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# 마스크 이미지를 원본 이미지에 적용
res_red = cv2.bitwise_and(img, img, mask=mask_red)
res_blue = cv2.bitwise_and(img, img, mask=mask_blue)
res_green = cv2.bitwise_and(img, img, mask=mask_green)

# 빨간색 픽셀의 수 세기
red_pixels = cv2.countNonZero(mask_red)
blue_pixels = cv2.countNonZero(mask_blue)
green_pixels = cv2.countNonZero(mask_green)

print("red_pixels = ", red_pixels)
print("blue_pixels = ", blue_pixels)
print("green_pixels = ", green_pixels)

if red_pixels > blue_pixels :
    print("620호 입니다.")
else :
    print("619호 입니다.")

circles = cv2.HoughCircles(mask_red, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    # 원이 발견되었다면, 원의 정보를 정수형으로 변환
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        # 원의 중심점 좌표와 반지름을 구하기
        center_x, center_y, radius = i[0], i[1], i[2]
        
        # 원을 둘러싸는 사각형의 좌측 상단과 우측 하단 좌표를 계산
        top_left = (center_x - radius, center_y - radius)
        bottom_right = (center_x + radius, center_y + radius)
        
        # 이미지에 사각형 그리기
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
else :
    print("not found")

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('mask_red', res_red)
cv2.imshow('mask_blue', res_blue)
cv2.imshow('mask_green', res_green)
cv2.waitKey(0)
cv2.destroyAllWindows()
