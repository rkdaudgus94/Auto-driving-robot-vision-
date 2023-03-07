# 완성된 음성인식에 텍스트 분리

import speech_recognition as sr
from gtts import gTTS
import playsound

# 이름 인식 코드
def speak_jetson():
    
    # 음성인식 객체 생성
    r = sr.Recognizer()
    
    with sr.Microphone() as source :
        
        # 마이크로부터 오디오 읽기
        print('"젯슨"을 불러주세요!')
        audio_data = r.record(source, duration = 3)
        
        try:
            # 구글 API로 인식 (하루에 50회 제한)
            text = r.recognize_google(audio_data, language = 'ko')
            
            # 이름 인식 -> 음성 인식 코드로 넘어감
            if(text == "태형") :
                print("네! 부르셨나요?")
                txt = "네! 부르셨나요?"
                tts_kr = gTTS(txt, lang = 'ko', slow = False)
                tts_kr.save("voice.wav")
                playsound.playsound("voice.wav")
                return respeak()
            
            # 다른 단어 인식 -> 다시 이름 부르는 코드로 돌아감
            else:
                return speak_jetson()
            
        # 음성 인식 실패한 경우
        except sr.UnknownValueError:
            return speak_jetson()

# 음성 인식    
def respeak():
    
    # 음성인식 객체 생성
    r = sr.Recognizer()

    with sr.Microphone() as source :
    
        # 마이크로부터 오디오 읽기
        audio_data = r.record(source, duration = 5)
        
    try:
        # 음성을 문자열로 전환
        # 구글 API로 인식 (하루에 50회 제한)
        text = r.recognize_google(audio_data, language = 'ko')
        print("<음성을 문자로 변환한 값을 아래에 표시했습니다.>")
        print(text)
    
        # 인식된 음성에 대한 대답
        print(text + "라고 말했습니다.")
        txt = text + "라고 말했습니다."
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        tts_kr.save("voice.wav")
        playsound.playsound("voice.wav")

        # 분리할 조사
        location = ['으로', '로', '이에게', '에게', '을', '를', '이한테', '한테', '에']
        
        # 문자열을 띄어쓰기 기준으로 분리
        text = text.split()
        
        # 조사가 포함된 단어를 찾은 후 조사 제거 후 리스트로 저장
        # location 단어가 포함된 단어들을 저장할 리스트
        text_division = []
        
        # 문자열을 순회하면서 location이 포함된 단어를 찾음
        for word in text :
            for loc in location :
                if loc in word :
                    # location의 단어를 제거한 후 저장
                    text_division.append(word.replace(loc, ""))
                    # 613으로 같은 경우 '으로'와 '로'가 포함되어 2번 결과가 나오게 됨
                    # break문을 통해 겹치는 단어는 표시 X
                    break
        name = ['Myung Hyun', 'Siwon', 'Hye seon', 'Tae eon']
        place = ['613', '620', '랩실']
        # 결과 출력
        print(text_division)
        for text in text_division :
            for names in name :
                if names == text :
                    r_name = names
            for places in place :
                if places == text :
                    r_place = places
        print(r_name)
        print(r_place)
        return speak_jetson()
    
    # 음성 인식 실패한 경우
    except sr.UnknownValueError:
        print("다시 한 번 말씀해주시겠어요?")
        txt = "다시 한 번 말씀해주시겠어요?"
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        tts_kr.save("voice.wav")
        playsound.playsound("voice.wav")
        return respeak()

try:  
    while True :
        speak_jetson()
        respeak()
        
# Crtl + c 누르면 음성 인식 멈춤
except KeyboardInterrupt: 
    pass