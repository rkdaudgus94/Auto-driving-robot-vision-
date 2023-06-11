import cv2
import numpy as np
import tensorflow as tf

# 모델 불러오기
new_model = tf.keras.models.load_model('C:/Users/rkdau/OneDrive/바탕 화면/Coding/2023-1-Capstone-/tensor/model.h5')

# 웹캠 접근
img = cv2.imread('D:/620/620(2).jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

def index_to_char(index):
    return '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[index]


lower_blue = np.array([100, 100, 100])
upper_blue = np.array([140, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

mask = cv2.resize(mask, (28, 28))  # 이미지 크기 조정
mask = mask / 255.0  # 이미지 정규화
mask = mask.reshape(-1, 28, 28, 1)  # 배치 차원을 추가

prediction = new_model.predict(mask)    
    # 예측 결과를 출력
index = np.argmax(prediction)
print(index_to_char(index))  # 가장 높은 확률을 가진 클래스에 해당하는 문자 출력

    # 'q'를 누르면 종료
cv2.waitKey(0)
cv2.imshow()
cv2.destroyAllWindows()