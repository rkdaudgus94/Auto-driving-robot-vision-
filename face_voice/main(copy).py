import threading
import cv2
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
cap_name = None
shared_romanized_name = None
shared_camera_completion = None
korea_name = None
shared_place_list = None
voice_name_list = None
voice_place_list = None

def camera_mode ():
    global shared_romanized_name, shared_camera_completion, korea_name
    r = sr.Recognizer()
    s = sr.Recognizer()
                                    
    with sr.Microphone() as source :
                                                    
        audio_data = r.record(source, duration = 5)
                                        
    try:
        # 구글 API로 인식 (하루에 50회 제한)
        text = r.recognize_google(audio_data, language = 'ko')
                                                        
        # 인식된 음성에 대한 대답
        time.sleep(1.5)
        print('"' + text + '"' + "라고 말한 것이 맞습니까?")
        txt = text + "라고 말한 것이 맞습니까?"
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
        tts_kr.save(wav_path)
        playsound.playsound(wav_path)

        time.sleep(0.5)
        print("<네 / 아니요로 대답해주세요!")
        with sr.Microphone() as source :
            # 마이크로부터 오디오 읽기
            audio_data1 = s.record(source, duration = 3)
            text1 = s.recognize_google(audio_data1, language = 'ko')
                                    
        if (text1 == "네") :
            korea_name = text               
            # 로마자 변환을 위한 Transliter 클래스 객체 생성
            trans = Transliter(rule=academic)
            # 한글 이름을 로마자로 변환
            romanized_name = trans.translit(text)
            print(romanized_name)
                                                        
            print("이제 사진을 찍겠습니다.")
            print("카메라를 바라봐 주세요!")
            txt2 = "이제 사진을 찍겠습니다. 카메라를 바라봐 주세요!"
            tts_kr = gTTS(txt2, lang = 'ko', slow = False)
            wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
            tts_kr.save(wav_path)
            playsound.playsound(wav_path)
            time.sleep(2.5)
                                                                
            # 뚜뚜뚜 소리
            sound_path = os.path.join("/home/hyeun/ssun/620_capstone", "sound_effect.wav")
            playsound.playsound(sound_path)
                                                            
            time.sleep(1.5)
                
            # 뚜뚜뚜 소리
            sound_path = os.path.join("/home/hyeun/ssun/620_capstone", "sound_effect.wav")
            playsound.playsound(sound_path)
                
            time.sleep(2)
            shared_romanized_name = romanized_name
                                                            
        elif (text1 == "아니요") :
            # 인식된 음성에 대한 대답
            print("내용을 다시 한 번 말씀해주시겠어요?")
            txt = "내용을 다시 한 번 말씀해주시겠어요?"
            tts_kr = gTTS(txt, lang = 'ko', slow = False)
            wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
            tts_kr.save(wav_path)
            playsound.playsound(wav_path)
            return camera_mode()
            
        else : 
            print("내용을 다시 한 번 말씀해주시겠어요?")
            txt = "내용을 다시 한 번 말씀해주시겠어요?"
            tts_kr = gTTS(txt, lang = 'ko', slow = False)
            wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
            tts_kr.save(wav_path)
            playsound.playsound(wav_path)
            return camera_mode()
                                                            
    # 음성 인식 실패한 경우
    except sr.UnknownValueError:
        print("내용을 다시 한 번 말씀해주시겠어요?")
        txt = "내용을 다시 한 번 말씀해주시겠어요?"
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
        tts_kr.save(wav_path)
        playsound.playsound(wav_path)
        return camera_mode()
    
def camera_completion() :
    global korea_name
                                        
    # 찰칵 소리
    camera_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera_effect.wav")
    playsound.playsound(camera_path)
    
    time.sleep(1)
                    
    print("shared_romanized = ", shared_romanized_name)                                       
    print('"'+ korea_name +'"' + "님 데이터가 등록되었습니다.")
    txt = korea_name + "님 데이터가 등록되었습니다."
    tts_kr = gTTS(txt, lang = 'ko', slow = False)
    wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
    tts_kr.save(wav_path)
    playsound.playsound(wav_path)

# 스레드 테스트를 위해 def 2개 생성
# 객체 인식
def func1(name):
    global shared_r_name_list, shared_romanized_name, cap_name, shared_camera_completion, shared_place_list
    face_recognition = Facerecognition()
    time1 = 0
    complete_count = 0
    
    for frame, names, location in face_recognition.video():
        str_names = ''.join(str(element) for element in names)
        str_location = ''.join(str(element1) for element1 in location)
        cap_name = str_names
        cap_frame = frame
        complete_count += 1
        
        if complete_count % 20 == 0 :
            print("location : ", str_location)
            
        if shared_r_name_list or shared_place_list:
            with lock:
                if (str_names == shared_r_name_list) and (complete_count % 20 == 0):
                    print('"' + str_names + '"' + "님을 찾았습니다.")
                if (str_location == shared_place_list) and (complete_count % 20 == 0) :
                    print("{0}에 도착했습니다. ".format(str_location))
                 
        if shared_romanized_name:
            print("camera_shared_romanized_name = ", shared_romanized_name)
            # 사진 찍는 코드 작성
            cv2.imwrite('/home/hyeun/face_img/{}.png'.format(shared_romanized_name), cap_frame) #  사진 기능 captured_frame : 저장할 이름
            print("사진찍기 완료!!")
            
            camera_completion()
            
            shared_romanized_name = None
                    
        elif time1 % 10 == 0 :
            print(str_names)
            
        time1 += 1

# 음성 인식
def func2(voice):
    global shared_r_name_list, cap_name, shared_place_list
    for r_name_list in main_voice() :
        if r_name_list != "사진" :
            voice_name_list = r_name_list[0]
            voice_place_list = r_name_list[1]
        
            # multi_voice 이름 반환값
            print ("메인 이름 :" , voice_name_list)
        
            # multi_voice 이름 반환값
            print ("메인 장소 :" , voice_place_list)

        with lock:
            if r_name_list != [] :
                if (voice_name_list or voice_place_list) :
                    shared_r_name_list = voice_name_list
                    shared_place_list = voice_place_list
                    print("공유 완료")
                
                if r_name_list == "사진" :
                    capture_mode = r_name_list
                    print("capture_mode : ", capture_mode)
                    
                    time.sleep(1)
                    
                    capname = cap_name
                    print("카메라를 바라봐 주세요")
                    txt = "카메라를 바라봐 주세요"
                    tts_kr = gTTS(txt, lang = 'ko', slow = False)
                    wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                    tts_kr.save(wav_path)
                    playsound.playsound(wav_path)
                    print("cap name = ", capname)
                    time.sleep(1)
                    
                    if capname != "???" :
                        print("등록된 사람입니다.")
                        txt = "등록된 사람입니다. 음성 인식 모드로 다시 전환하겠습니다."
                        tts_kr = gTTS(txt, lang = 'ko', slow = False)
                        wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                        tts_kr.save(wav_path)
                        playsound.playsound(wav_path)
                    
                    else :
                        print("등록되지 않은 사람입니다.") # 나중에 제거
                        txt = "등록되지 않은 사람입니다."
                        tts_kr = gTTS(txt, lang = 'ko', slow = False)
                        wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                        tts_kr.save(wav_path)
                        playsound.playsound(wav_path)
                        time.sleep(2)
                        
                        print("등록할 이름을 말해주세요!")
                        txt = "등록할 이름을 말해주세요!"
                        tts_kr = gTTS(txt, lang = 'ko', slow = False)
                        wav_path = os.path.join("/home/hyeun/ssun/620_capstone", "camera.wav")
                        tts_kr.save(wav_path)
                        playsound.playsound(wav_path)
                                                 
                        camera_mode()   
         
    time.sleep(1)


def main():
    #스레드 정의
    thread1 = threading.Thread(target=func2, args=(True,))
    thread2 = threading.Thread(target=func1, args=(True,))

    #스레드 시작
    thread1.start()
    thread2.start()
    print("done!")

    thread1.join()
    thread2.join()
    
if __name__ == "__main__":
    main()