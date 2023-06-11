import speech_recognition as sr

# 음성인식 객체 생성
r = sr.Recognizer()

with sr.Microphone() as source :
    
    # 마이크로부터 오디오 읽기
    print("인식중.......")
    audio_data = r.record(source, duration = 5)
    
    
    # 음성을 문자열로 전환
    text = r.recognize_google(audio_data)
    print("....음성 데이터 -> 텍스트....")
    print(text)