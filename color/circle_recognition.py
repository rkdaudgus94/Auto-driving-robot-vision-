import cv2
import numpy as np

# 이미지를 불러옵니다.
image = cv2.imread("D:/color/CircleRed.png")

# 이미지를 그레이스케일로 변환합니다. 이렇게 하면 동그라미를 쉽게 감지할 수 있습니다.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지에서 원을 검색합니다.
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# 원이 감지되었는지 확인합니다.
if circles is not None:
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        # 동그라미의 중심을 추출합니다.
        center = (i[0], i[1])

        # 동그라미의 색상을 추출합니다.
        color = image[center[1], center[0]]

        # 색상이 존재하는지 확인합니다. 여기서는 빨간색을 기준으로 합니다.
        if np.all(color > [50, 50, 150]):  # BGR 순서로 색상을 확인하므로 빨간색은 [50, 50, 150] 이상입니다.
            print('Red circle detected at', center)
else:
    print('No circles detected')