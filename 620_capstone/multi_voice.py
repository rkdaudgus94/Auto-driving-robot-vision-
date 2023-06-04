import speech_recognition as sr
from gtts import gTTS
import playsound
import os
from hangul_romanize import Transliter
from hangul_romanize.rule import academic

def recognition_rate(text, place, tae_eon, myung_hyun):
    for word in place + tae_eon + myung_hyun:
        if word in text:
            if word in place:
                text = text.replace(word, '620호')
            elif word in tae_eon:
                text = text.replace(word, '태언')
            elif word in myung_hyun :
                text = text.replace(word, '명현')
    return text

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
            
            # 음성인식 시 오류나는 단어
            jetson = ["잭슨", "넥슨", "넥센"]
            
            # 오류나는 젯슨 단어를 젯슨으로 바꿔주는 코드
            for i in jetson :
                if i in text :
                    text = text.replace(i, '젯슨')

            # 이름 인식 -> 음성 인식 코드로 넘어감
            if(text == "젯슨") :
                print("네! 부르셨나요?")
                txt = "네! 부르셨나요?"
                tts_kr = gTTS(txt, lang = 'ko', slow = False)
                wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "voice.wav")
                tts_kr.save(wav_path)
                playsound.playsound(wav_path)
                print("모드 변경 OR 내용을 말씀해주세요!")
                
                return respeak()
                    
            # 다른 단어 인식 -> 다시 이름 부르는 코드로 돌아감
            else:
                return speak_jetson()
            
        # 음성 인식 실패한 경우
        except sr.UnknownValueError:
            return speak_jetson()

# 음성 인식    
def respeak():
    global r_name
    
    # 음성인식 시 오류나는 단어
    place = ['620 4', '20%', '625']
    tae_eon = ['태연', '태현']
    myung_hyun = ['명 현', '영현', '영 현', '영영', '영 영', '명 연']
            
    # 음성인식 객체 생성
    r = sr.Recognizer()
    s = sr.Recognizer()
    m = sr.Recognizer()

    with sr.Microphone() as source :
        # 마이크로부터 오디오 읽기
        audio_data = r.record(source, duration = 5)
                
    try:
        # 음성을 문자열로 전환
        # 구글 API로 인식 (하루에 50회 제한)
        text = r.recognize_google(audio_data, language = 'ko')
        #테스트 후 이 위치로 변경
        #text = recognition_rate(text, place, tae_eon, myung_hyun)
        
        if(text == "사진"):
            mode_capture = []
            mode_capture = "사진"
            print("사진 데이터 등록 모드로 변경하겠습니다.")
            text = "사진 데이터 등록 모드로 변경하겠습니다."
            tts_kr = gTTS(text, lang = 'ko', slow = False)
            wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "voice.wav")
            tts_kr.save(wav_path)
            playsound.playsound(wav_path)
                    
            # mode_capture에 단어가 있으면 객체 인식 코드로 이동
            return mode_capture if mode_capture else respeak()
            
        # 오류난 단어를 원하는 단어로 변경(위치는 나중에 변경해야 함 !)
        text = recognition_rate(text, place, tae_eon, myung_hyun)
        
        # 인식된 음성에 대한 대답
        print('"' + text + '"' + "라고 말한 것이 맞습니까?")
        txt = text + "라고 말한 것이 맞습니까?"
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "voice.wav")
        tts_kr.save(wav_path)
        playsound.playsound(wav_path)
        
        print("<네 / 아니요로 대답해주세요!")
        with sr.Microphone() as source :
            # 마이크로부터 오디오 읽기
            audio_data1 = s.record(source, duration = 3)
            text1 = s.recognize_google(audio_data1, language = 'ko')
            
        if (text1 == "네") :
            # 분리할 조사
            location = ['으로', '로', '이에게', '에게', '을', '를', '이한테', '한테', '에', '이']
                
            # 문자열을 띄어쓰기 기준으로 분리
            text = text.split()
            
            v_name = []
            v_place = []
                
            # 문자열을 순회하면서 location이 포함된 단어를 찾고 제거하여 이름과 장소 분리
            for word in text :
                for loc in location :
                    if loc in word :
                        # location의 단어를 제거한 후 이름 저장
                        if loc in ['이에게', '에게', '이한테', '한테', '이']:
                            v_name = word.replace(loc, '')
                        # location의 단어를 제거한 후 장소 저장
                        elif loc in ['으로', '로', '에']:
                            v_place = word.replace(loc, '')
                        # 613으로 같은 경우 '으로'와 '로'가 포함되어 2번 결과가 나오게 됨
                        # break문을 통해 겹치는 단어는 표시 X
                        break
            print(v_name)
            print(v_place)
            
            # 로마자 변환을 위한 Transliter 클래스 객체 생성
            trans = Transliter(rule=academic)
            # 한글 이름을 로마자로 변환
            romanized_name = trans.translit(v_name)
            print(romanized_name)
                
            r_name = []
            r_place = []
            
            r_name = romanized_name
            r_place = v_place
                
            print('이름은', r_name)
            print('장소는', r_place)
                
            # r_name에 단어가 있으면 객체 인식 코드로 이동
            return r_name if r_name else respeak()
        
        elif (text1 == "아니요") :
            # 인식된 음성에 대한 대답
            print("다시 한 번 말씀해주시겠어요?")
            txt = "다시 한 번 말씀해주시겠어요?"
            tts_kr = gTTS(txt, lang = 'ko', slow = False)
            wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "voice.wav")
            tts_kr.save(wav_path)
            playsound.playsound(wav_path)
            return respeak()
    
    # 음성 인식 실패한 경우
    except sr.UnknownValueError:
        print("다시 한 번 말씀해주시겠어요?")
        txt = "다시 한 번 말씀해주시겠어요?"
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        wav_path = os.path.join("/home/hyeun/ssun", "voice.wav")
        tts_kr.save(wav_path)
        playsound.playsound(wav_path)
        return respeak()

    
def main_voice(): 
    while True:
        name = []
        name = speak_jetson()
        if name != [] :
            r_name_list = name
            if (name == "사진") :
                capture_mode = name
                #print("capture_mode: ", capture_mode)
                yield capture_mode
            else :
                r_name_list = name
                print("r_name: ", r_name_list)
                yield r_name_list
        else:
            break
        
""" def get_r_name_list():
    r_name_list = main()  
    return r_name_list """

if __name__ == "__main__" :
    main_voice()