# 음성인식 텍스트 분활

import speech_recognition as sr
from gtts import gTTS
import playsound

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
    
    # 주어진 문자열과 위치 리스트
    location = ['으로', '로', '이에게', '에게', '을', '를', '이한테', '한테', '에']
    # 문자열을 띄어쓰기 기준으로 분리
    text = text.split()
    
    # 4 조사가 포함된 단어를 찾은 후 조사 제거 후 리스트로 저장
    # location 단어가 포함된 단어들을 저장할 리스트
    result = []
    
    # 문자열을 순회하면서 location이 포함된 단어를 찾음
    for word in text :
        for loc in location :
            if loc in word :
                # location의 단어를 제거한 후 저장
                result.append(word.replace(loc, ""))
                # 613으로 같은 경우 '으로'와 '로'가 포함되어 2번 결과가 나오게 됨
                # break문을 통해 겹치는 단어는 표시 X
                break

    # 결과 출력
    print(result)
    
# 음성 인식 실패한 경우
except sr.UnknownValueError:
    print("인식 실패")