import cv2
import numpy as np
import tensorflow as tf

# 모델 불러오기
new_model = tf.keras.models.load_model('C:/Users/rkdau/OneDrive/바탕 화면/Coding/2023-1-Capstone-/tensor/model.h5')
# EMNIST bymerge 데이터셋의 클래스를 나타내는 리스트
class_names = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# 웹캠 접근
cap = cv2.VideoCapture(0)

while True:
    # 웹캠에서 프레임을 읽음
    ret, frame = cap.read()

    # 임의로 이미지를 여러 부분으로 분할
    # 이 부분에서는 실제 이미지 내의 문자 위치와 크기에 맞게 분할해야 합니다
    parts = [frame[:, i*28:(i+1)*28] for i in range(frame.shape[1] // 28)]

    predictions = []
    for part in parts:
        # 프레임을 모델이 받아들일 수 있는 형태로 변환
        part = cv2.cvtColor(part, cv2.COLOR_BGR2GRAY)  # 모델이 흑백 이미지를 사용한다면
        part = cv2.resize(part, (28, 28))  # 이미지 크기 조정
        part = part / 255.0  # 이미지 정규화
        part = part.reshape(-1, 28, 28, 1)  # 배치 차원을 추가

        # 이미지를 모델에 넣고 예측
        prediction = new_model.predict(part)
        
        # 예측 결과를 저장
        predictions.append(np.argmax(prediction))

    # 예측 결과를 출력
    print(''.join(class_names[prediction] for prediction in predictions))  # 가장 높은 확률을 가진 클래스 출력

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
