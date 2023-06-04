import threading
import time
from multi_voice import main_voice
import os
from multi_face import Facerecognition
import speech_recognition as sr
from gtts import gTTS
import playsound
from hangul_romanize import Transliter
from hangul_romanize.rule import academic

lock = threading.Lock() # 공유 변수
shared_r_name_list = None
shared_capture_mode = None
non_face = None
romanized_name = None
capture = None

# 스레드 테스트를 위해 def 2개 생성
# 객체 인식
def func1(add):
    global shared_r_name_list, shared_capture_mode, non_face, romanized_name, capture
    face_recognition = Facerecognition()
    time1 = 0
    for names in face_recognition.video():
        str_names = ''.join(str(element) for element in names)
        if shared_r_name_list:
            with lock:
                if str_names == shared_r_name_list:
                    print("일치합니다")
        
        elif shared_capture_mode :
            with lock:
                if str_names != "???":
                    print("등록된 사람입니다.") # 음성으로 나오게 확인
                    
                else :
                    print("등록되지 않은 사람입니다.") # 나중에 제거
                    non_face = "no"
                    print("카메라 non_face ", non_face) # 나중에 제거
 
                #cv2.imwrite('captured_frame.jpg', frame)  #  사진 기능 captured_frame : 저장할 이름

                    
        elif time1 % 10 == 0 :
            print(str_names)
        time1 += 1

# 음성 인식
def func2(add):
    global shared_r_name_list, shared_capture_mode, non_face, romanized_name, capture
    for r_name_list in main_voice() :
        capture_mode = r_name_list
        
        # 사진 모드 변경
        if capture_mode == "사진" :
            print("capture_mode : ", capture_mode) # 이부분 나중에 지우기
            with lock:
                shared_capture_mode = capture_mode
                
                print("카메라를 바라봐 주세요")
                txt = "카메라를 바라봐 주세요"
                tts_kr = gTTS(txt, lang = 'ko', slow = False)
                wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                tts_kr.save(wav_path)
                playsound.playsound(wav_path)
            
            if (non_face == "no") : # 인식되지 않았다는 데이터 받기
                print("음성인식 non_face ", non_face) # 나중에 제거
                print("등록할 이름을 말해주세요!")
                txt = "등록할 이름을 말해주세요!"
                tts_kr = gTTS(txt, lang = 'ko', slow = False)
                wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                tts_kr.save(wav_path)
                playsound.playsound(wav_path)
                    
                    
                """def camera_mode ():
                        r = sr.Recognizer()
                        s = sr.Recognizer()
            
                        with sr.Microphone() as source :
                            
                            audio_data = r.record(source, duration = 3)
                
                            try:
                                # 구글 API로 인식 (하루에 50회 제한)
                                text = r.recognize_google(audio_data, language = 'ko')
                                
                                # 인식된 음성에 대한 대답
                                print('"' + text + '"' + "라고 말한 것이 맞습니까?")
                                txt = text + "라고 말한 것이 맞습니까?"
                                tts_kr = gTTS(txt, lang = 'ko', slow = False)
                                wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                                tts_kr.save(wav_path)
                                playsound.playsound(wav_path)
        
                                print("<네 / 아니요로 대답해주세요!")
                                with sr.Microphone() as source :
                                    # 마이크로부터 오디오 읽기
                                    audio_data1 = s.record(source, duration = 3)
                                    text1 = s.recognize_google(audio_data1, language = 'ko')
            
                                if (text1 == "네") :
                                    
                                    # 로마자 변환을 위한 Transliter 클래스 객체 생성
                                    trans = Transliter(rule=academic)
                                    # 한글 이름을 로마자로 변환
                                    romanized_name = trans.translit(text)
                                    print(romanized_name)
                                
                                    # 이름 데이터 보내주기
                                
                                    print("사진 찍겠습니다.")
                                    print("카메라를 바라봐 주세요!")
                                    txt = "사진 찍겠습니다. 카메라를 바라봐 주세요!"
                                    tts_kr = gTTS(txt, lang = 'ko', slow = False)
                                    wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                                    tts_kr.save(wav_path)
                                    playsound.playsound(wav_path)
                                    # 뚜뚜뚜 소리
                                    sound_path = os.path.join("/home/hyeun/ssun/620_capstone", "sound_effect.wav")
                                    playsound.playsound(sound_path)
                                    
                                    global capture
                                    capture = "사진 찍기"
                                
                                    # 찰칵 소리
                                    camera_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera_effect.wav")
                                    playsound.playsound(camera_path)
                                
                                    print(text + "님 데이터가 등록되었습니다.")
                                    txt = text + "님 데이터가 등록되었습니다."
                                    tts_kr = gTTS(txt, lang = 'ko', slow = False)
                                    wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                                    tts_kr.save(wav_path)
                                    playsound.playsound(wav_path)
                                    yield func2()
                                
                                elif (text1 == "아니요") :
                                    # 인식된 음성에 대한 대답
                                    print("다시 한 번 말씀해주시겠어요?")
                                    txt = "다시 한 번 말씀해주시겠어요?"
                                    tts_kr = gTTS(txt, lang = 'ko', slow = False)
                                    wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "voice.wav")
                                    tts_kr.save(wav_path)
                                    playsound.playsound(wav_path)
                                    yield capture_mode()
                                
                            # 음성 인식 실패한 경우
                            except sr.UnknownValueError:
                                print("다시 말해주세요")
                                txt = "다시 말해주세요"
                                tts_kr = gTTS(txt, lang = 'ko', slow = False)
                                wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                                tts_kr.save(wav_path)
                                playsound.playsound(wav_path)
                                yield camera_mode()"""
                
        # multi_voice 이름 반환값
        else : 
            print ("r_name :" , r_name_list)

        with lock:
            if r_name_list != [] :
                shared_r_name_list = r_name_list
                
    time.sleep(1)

def main():
    #스레드 정의
    thread1 = threading.Thread(target=func2, args=('1',))
    thread2 = threading.Thread(target=func1, args=('2',))

    #스레드 시작
    thread1.start()
    thread2.start()
    print("done!")

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()