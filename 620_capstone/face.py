import cv2

# 카메라 열기
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 의미합니다.

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # 프레임 표시
    cv2.imshow('Camera', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 리소스 해제
cap.release()
cv2.destroyAllWindows()