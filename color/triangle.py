import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 이진화
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

# 외곽선 찾기
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # 근사화
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    # 꼭지점이 3개인 경우 세모로 판단
    if len(approx) == 3:
        cv2.drawContours(img, [approx], 0, (0), 5)

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
