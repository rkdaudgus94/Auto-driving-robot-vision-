<div align="center">
  <h1>🚩 Capstone Design 🚩<br/>Autonomous Mobile Robot (🔭 Vision)</h1>
</div>

<div align="left">

## 🔓 사용 코드 파일
- `face_voice/main(tcp)3.py`
- `face_voice/multi_face0.py`
- `face_voice/multi_voice4.py`

## 🏳️ 프로젝트 목표
- 비대면 서비스 수요 증가 대응 **실내 자율주행 배달 로봇 구현**
- **2모터·4바퀴 구동 및 PID 제어 기반 목표 지점 이동**
- **LiDAR 기반 실내 지도 작성 및 장애물 회피 경로 계획**
- **객체 인식 기반 대상자 식별 및 음성 알림 제공**
- **모바일 앱 연동 기반 상태 모니터링·조작**

## 💭 프로젝트 내용

### 1) 주행·제어
- **PID 제어 기반 2모터·4바퀴 동시 구동**을 통한 목표 위치 이동
- **ROS 기반 주행 스택 구성** 및 센서 데이터 연동

### 2) 지도 작성·경로 계획
- **LiDAR 센서 기반 실내 구조 파악 및 SLAM 수행**
- **장애물(사물·사람) 회피 경로 탐색 및 최적 경로 계획**

### 3) 비전 인식
- **Jetson Nano 기반 객체·얼굴 인식 파이프라인 구성**
- **FaceRecognition + OpenCV 조합 기반 얼굴 임베딩 생성·매칭**
- **실시간 프레임 처리(해상도 축소 → RGB 변환 → 얼굴 탐지 → 인코딩 → 매칭)**
- **유클리드 거리 기반 유사도 판정 및 임계값 설정(0~1 스케일)**

#### 얼굴 인코딩
- 폴더 내 PNG 얼굴 이미지 로드 → **`face_recognition.face_encodings()`** 기반 특징 벡터 추출
- 인코딩 배열·이름 리스트 매핑 관리

#### 비디오 스트리밍
- OpenCV 캡처 입력 기반 **프레임 리사이즈(1/4) → RGB 변환 → 얼굴 위치 탐지 → 인코딩**
- 프레임 단위 실시간 식별 파이프라인 운영

#### 얼굴 비교·식별
- **`compare_faces()`** 및 **거리 계산** 기반 최근접 매칭
- **음성 명령 입력 이름 vs. 실영상 인식 이름 비교**를 통한 대상자 확인
- 일치 시 **“일치합니다” 출력** 처리

<div align="center">
  <img width="700" alt="face-match" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/a1d15d05-501a-457b-8d7f-49d97f12ac04">
</div>

### 4) 컬러 인식 (HSV)
- **HSV 색 공간 기반 색상 분류(빨강·파랑·하양·초록)**
- 색상 범위 마스크 적용 → **윤곽선 검출 및 노이즈 제거(영역 임계)** → **색상 픽셀 수 집계**
- 색상별 위치 매핑 반환: `{"not found", "620a", "elevator", "610a"}`

```python
# 예시 매핑 구조 (설명용)
color = {
    "not found": red_pixels,
    "620a": White_pixels,
    "elevator": green_pixels,
    "610a": blue_pixels
}
```

<div align="center">
  <img width="700" alt="color-detect" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/f49a0c3f-fdfb-4293-bc2c-77bce003fb2d">
</div>

### 5) 음성 입·출력
- **STT(Talk-to-Text)·TTS(Text-to-Speech) 파이프라인 구성**
- **대상자 이름 음성 입력 → 얼굴 인식 결과와 교차 확인 → 음성 알림 출력**
- **모바일 앱 연동** 기반 동작 상태·적재 물품 확인

## ✍️ 사용 라이브러리

### 음성
- **SpeechRecognition**: 음성 인식 처리
- **gTTS**: 텍스트 음성 변환(TTS)
- **PyAudio**: 오디오 입·출력 접근
- **playsound**: 사운드 파일 재생
- **hangul_romanize**: 한글 로마자 표기 변환

### 객체·비전
- **FaceRecognition**: 얼굴 탐지·인코딩·매칭
- **OpenCV**: 실시간 영상 처리·스트리밍

## ⏹️ 블록선도
<div align="center">
  <img width="500" alt="block" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/8499ec31-a0c2-4f44-9146-363f274d3fdf">
</div>

## 🧷 설계도
<div align="center">
  <img width="553" alt="design-1" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/c1cc75af-4090-472a-8be8-fc789f05aee0">
</div>
<div align="center">
  <img width="553" alt="design-2" src="https://github.com/rkdaudgus94/Auto-driving-robot-vision-/assets/76949032/97517b45-7c17-420e-8d67-1da773900a5b">
</div>

## 👥 팀원
| [양희웅](https://github.com/happybear98) (팀장) | [강명현](https://github.com/rkdaudgus94) | [이혜선](https://github.com/ssun0402) | [황태언](https://github.com/tae2on) |
| :---: | :---: | :---: | :---: |
| <a href="https://github.com/happybear98"><img src="https://github.com/happybear98.png" width="100px"></a> | <a href="https://github.com/rkdaudgus94"><img src="https://github.com/rkdaudgus94.png" width="100px"></a> | <a href="https://github.com/ssun0402"><img src="https://github.com/ssun0402.png" width="100px"></a> | <a href="https://github.com/tae2on"><img src="https://github.com/tae2on.png" width="100px"></a> |
| <div align="left">• LiDAR 기반 실내 지도 작성·SLAM<br/>• 경로 계획 및 장애물 회피</div> | <div align="left">• 얼굴·대상 인식 비전 모델 개발<br/>• 영상 처리 및 인식 정확도 개선</div> | <div align="left">• 음성 명령 인식(STT)·출력(TTS)<br/>• 사용자 시나리오·인터페이스 설계</div> | <div align="left">• 모터 PID 제어 및 속도 안정화<br/>• Dead Reckoning 기반 위치 추정</div> |

</div>

<hr/>

### 🔧 기술 스택 (요약)
- **플랫폼/보드**: Jetson Nano, ROS
- **센서**: LiDAR, 마이크, 스피커, 카메라
- **비전/AI**: FaceRecognition, OpenCV
- **음성**: SpeechRecognition, gTTS, PyAudio, playsound
- **앱 연동**: 모바일 앱 기반 상태 모니터링·제어

### 🧩 시스템 구성
- **지각(Perception)**: 카메라·LiDAR 데이터 수집 → 얼굴/객체 인식·지도 작성
- **계획(Planning)**: 목적지 설정 → 경로 계획 → 장애물 회피
- **제어(Control)**: PID 기반 구동 제어 → 속도·자세 안정화
- **상호작용(Interaction)**: 음성 명령 입력 → 대상자 확인 → 음성 알림 출력
- **운영(Operations)**: 모바일 앱 상태 확인·원격 조작

### 🔄 데이터 흐름
1. **음성 입력 수집** → 이름 인식(STT)  
2. **실시간 영상 처리** → 얼굴 인식·매칭  
3. **대상자 일치 판정** → 음성 알림(TTS) 출력  
4. **LiDAR 기반 위치 인식** → 경로 계획·회피 주행  
5. **모바일 앱 연동** → 동작 상태·적재 물품 확인
