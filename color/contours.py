import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread("D:/color/color_circle.png")

# BGR에서 HSV로 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

# 색상 범위 정의 - 예: 빨간색
lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([100, 100, 100])
upper_blue = np.array([140, 255, 255])

lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# HSV 이미지에서 빨간색만 추출하기 위한 임계값
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Find contours in the mask
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 각 외곽선에 대해
for cnt in contours_red:
    # 외곽선의 경계 사각형을 구함
    x, y, w, h = cv2.boundingRect(cnt)
    # 원본 이미지에 사각형을 그림
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # 해당 영역의 이미지를 잘라내고 확대
    roi_red = img[y:y+h, x:x+w]
    # roi_red = cv2.resize(roi_red, (200, 200))

for cnt in contours_blue:
    # 외곽선의 경계 사각형을 구함
    x, y, w, h = cv2.boundingRect(cnt)
    # 원본 이미지에 사각형을 그림
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # 해당 영역의 이미지를 잘라내고 확대
    roi_blue = img[y:y+h, x:x+w]
    # roi_blue = cv2.resize(roi_blue, (200, 200))

for cnt in contours_green:
    # 외곽선의 경계 사각형을 구함
    x, y, w, h = cv2.boundingRect(cnt)
    # 원본 이미지에 사각형을 그림
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # 해당 영역의 이미지를 잘라내고 확대
    roi_green = img[y:y+h, x:x+w]
    # roi_green = cv2.resize(roi_green, (200, 200))
# 결과 보기
cv2.imshow('img', img)
cv2.imshow('roi_red', roi_red)
cv2.imshow('roi_blue', roi_blue)
cv2.imshow('roi_green', roi_green)
cv2.waitKey(0)
cv2.destroyAllWindows()
