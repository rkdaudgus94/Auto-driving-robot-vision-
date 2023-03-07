import cv2
import pytesseract
import torch
import torchvision.transforms as transforms

# GPU를 사용하여 모델을 실행합니다.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 모델을 로드합니다.
model = torch.load("C:/Users/rkdau/OneDrive/바탕 화면/코딩/2023-1-Capstone-/example/model.pt").to(device)
model.eval()

# 이미지 전처리를 위한 함수를 정의합니다.
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 텍스트 인식을 위한 OCR 엔진을 초기화합니다.
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# 카메라를 엽니다.
cap = cv2.VideoCapture(0)

while True:
    # 프레임을 읽어옵니다.
    ret, frame = cap.read()

    # 이미지 전처리를 수행합니다.
    img = transform(frame).to(device)

    # 모델을 사용하여 텍스트 영역을 탐지합니다.
    with torch.no_grad():
        output = model(img)
        bboxes = output["boxes"].cpu().numpy()

    # 추출된 텍스트 영역을 OCR 엔진을 사용하여 인식합니다.
    for bbox in bboxes:
        x, y, w, h = bbox
        text_img = frame[y:y+h, x:x+w]
        text = pytesseract.image_to_string(text_img)

        # 인식된 텍스트를 화면에 출력합니다.
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 화면에 프레임을 출력합니다.
    cv2.imshow("Text Recognition", frame)

    # 'q' 키를 누르면 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라를 닫습니다.
cap.release()

# 윈도우를 닫습니다.
cv2.destroyAllWindows()