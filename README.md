<div align="center">
    <h1>  🚩Capstone Design🚩 <br>
            Autonomous Mobile Robot(🔭Vision)(미완성) </h1>
</div>

<div align="left">
    
## 🔓 : 사용한 코드 파일

- main(tcp)3.py
- multi_face0.py
- multi_voice4.py
    
## 🏳️ : 프로젝트 목표

사람들은 비대면 접촉을 선호하기 시작했고 비대면 접촉을 위한 방법을 발전시켜왔다. 하지만 일부분에서는 사람이 직접 배달해야 한다. </br>
우리는 현재 자율주행 자동차가 상용화되고 있다는 걸 알고 실생활에 적용하면 사람들이 편리할 수 있겠다는 생각을 시작으로 2개의 모터와 4개의 바퀴를 이용하여 원하는 위치로 이동하고 라이다 센서를 통해 건물 안 구조를 파악한 후 목적지까지 장애물(사람, 사물)을 피해 최적의 길을 찾아 이동한다.</br>
객체 인식을 통해 목표로 하는 사람을 구별하여 음성인식으로 배달 알림을 음성으로 알려주는 로봇을 개발한다.

## 💭 : 프로젝트 내용

-  PID 제어를 통해 2개의 모터를 포함하여 4개의 바퀴를 동시에 구동시켜 원하는 위치로 이동할 수 있도록 사용했다.
-  ROS 기반으로 라이다 센서를 이용해 건물 안 구조를 파악한 후 목적지까지 장애물(사물, 사람)을 피해 최적의 길을 찾을 수 있도록 한다.
-  Jetson nano 보드를 이용하여 객체를 인식하여 사람을 구별하여 목표로 하는 사람을 인식할 수 있게 한다.
-  Jetson nano 보드에 마이크와 스피커를 연결하여 음성을 인식하고 목표로 하는 사람에게 배달 알림을 음성으로 알려준다.
-  이 모든 기능을 휴대폰 앱을 통해 확인하여 작동과 물건 여부를 쉽게 할 수 있다.
-  이러한 기능들을 합쳐 자율 주행 로봇이 설계가 되고 이에 따라 사람들이 직접 움직이지 않아도 손쉽게 물건을 배달하고 그 자리에서 확인까지 할 수 있어 편리함과 안전 예방까지 할 수 있다.

## ✍️ : 사용한 라이브러리
&nbsp;&nbsp;&nbsp;**음성**
- **SpeechRecognition :** 파이썬에서 음성 인식을 수행하기 위한 라이브러리
- **gTTs :** 파이썬에서 텍스트를 음성으로 변환하는 라이브러리
- **pyaudio :** 파이썬에서 오디오 입출력 기능을 사용할 수 있도록 해주는 라이브러리
- **playsound :** 파이썬에서 간단하게 사운드 파일을 재생하기 위한 라이브러리
- **hangul_romanize :** 한글을 로마자(영문)로 변환하기 위한 파이썬 라이브러리

&nbsp;&nbsp;&nbsp;**객체**
- **FaceRecognition :** 파이썬에서 얼굴 인식을 수행하기 위한 라이브러리
- **OpenCV :** 실시간 컴퓨터 비전을 목적으로 한 프로그래밍 라이브러리

  **👩얼굴 인코딩👩 :** 폴더에 png 파일로 저장된 얼굴의 이미지가 로드되고, 그 얼굴들의 특징은 Face Recognition 라이브러리의 face_encodings함수를 사용하여 추출됩니다. </br>
  추출된 각 얼굴 인코딩은 배열에 저장됩니다. 또한, 각 얼굴의 이름 또한 따로 리스트에 저장됩니다.</br>

  **📺비디오 스트리밍📺 :** OpenCV를 사용하여 실시간 프레임을 제공 받습니다. 각 프레임은 처리하기 위해 1/4로 크기가 조정되고, 그 다음 RGB로 변환됩니다.</br>
  이 변환된 이미지에서 Face Recognition 라이브러리의 face_locations함수를 사용하여 얼굴의 위치를 찾고, face_encodings함수를 사용하여 그 얼굴의 특징을 추출합니다.</br>

  **👬얼굴 비교 및 식별👬 :** 각 비디오 프레임에서 얻은 얼굴 인코딩은 알려진 얼굴 인코딩들과 비교됩니다. 이 비교는 Face Recognition 라이브러리의 compare_faces함수를 사용하여 수행되며, 인식된 얼굴이 알려진 얼굴 중 어느 것과 가장 유사한지를 결정합니다.</br>
   compare_faces함수에는 얼만큼 유사한지 기준을 정할 수 있는데 0~1까지 값을 설정할 수 있으며 이 값은 유클라디안의 거리를 나타냅니다. </br>
   즉, 유클라디안 거리값을 작게 설정할수록 보다 엄격한 기준으로 비교합니다.</br>
   그런 다음, 얼굴 인코딩 간의 거리를 계산하여 가장 가까운 인코딩(즉, 가장 유사한 얼굴)을 찾습니다.</br>
   이 얼굴이 알려진 얼굴 목록의 어떤 얼굴과 일치하는지를 결정하고, 해당 얼굴의 이름을 얻을 수 있습니다.</br></br>
   ex) 음성 명령을 통해 받은 이름 데이터와 비디오를 통해 인식되는 얼굴의 데이터 네임과 일치하는지 확인한 후 일치하면 “일치합니다” 출력 
  <div align="center">
    <img width="700" alt="image" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/a1d15d05-501a-457b-8d7f-49d97f12ac04">
  </div>
  </br>  
  <div align="left">
  
  **🔸컬러 인식🔸 :** RGB(Red, Green, Blue) 색 공간보다 더 정확하게 색상을 구분할 수 있는 HSV(Hue, Saturation, Value) 색 공간을 이용하여 색상을 구분합니다.</br>
  먼저 특정 색상(빨강, 파랑, 하양, 초록)의 범위를 설정합니다. 정의된 색상 범위를 사용하여 원본 이미지에 마스크를 적용합니다. </br>
  마스크는 특정 색상 범위 내의 픽셀만을 유지하고 나머지 픽셀을 모두 제거합니다. 마스크된 이미지에서 윤곽선을 검출한 후 윤곽선 안에 있는 이미지의 색을 분석합니다.</br>
  이 때 윤곽선 중 일정 크기 이상의 영역만 추출하여 작은 노이즈를 제거합니다. 이후 이미지에 나타나 있는 색의 픽셀 수를 계산하여 색상을 결정합니다. 이후 그 색상에 연결된 장소값(“not found”, “620a”, “elevator”, “610a”)을 반환합니다.
</div>

  ```

  color= {"not found":red_pixels, "620a": White_pixels, "elevator": green_pixels, "610a": blue_pixels}

  ```
<div align="center">
  <img width="700" alt="image" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/f49a0c3f-fdfb-4293-bc2c-77bce003fb2d">
</div>

## ⏹️ : 블록선도
<div align="center">
    <img width="500" alt="image" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/8499ec31-a0c2-4f44-9146-363f274d3fdf">
</div>

## 🧷 : 설계도 사진
<div align="center">
    <img width="553" alt="image" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/c1cc75af-4090-472a-8be8-fc789f05aee0">
</div>
<div align="center">
    <img width="553" alt="image" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/97517b45-7c17-420e-8d67-1da773900a5b">
</div>
