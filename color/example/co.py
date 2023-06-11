import speech_recognition as sr

# 음성인식 객체 생성
r = sr.Recognizer()

with sr.Microphone() as source :
    
    # 마이크로부터 오디오 읽기
    print("음성을 말해주세요!")
    audio_data = r.record(source, duration = 5)
    
try:
    # 음성을 문자열로 전환
    # 구글 API로 인식 (하루에 50회 제한)
    text = r.recognize_google(audio_data, language = 'ko')
    print("<음성을 문자로 변환한 값을 아래에 표시했습니다.>")
    print(text)
    
# 음성 인식 실패한 경우
except sr.UnknownValueError:
    print("인식 실패")    
    
# Crtl + c 누르면 음성 인식 멈춤
#except KeyboardInterrupt: 
    #pass