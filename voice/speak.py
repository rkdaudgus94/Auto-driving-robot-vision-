from gtts import gTTS
import playsound

def speak_ko():
    print("음성을 말해주세요!")
    txt = "음성을 말해주세요!"
    tts_kr = gTTS(text = txt, lang = 'ko', slow = False)
    tts_kr.save("voice.wav")
    playsound.playsound("voice.wav")
    
def speak_en():
    print("hello! nice to meet you!")
    txt = "hello! nice to meet you!"
    tts_kr = gTTS(text = txt, lang = 'en', slow = False)
    tts_kr.save("voice.wav")
    playsound.playsound("voice.wav")
    
if __name__ == "__main__" :
    speak_ko()
    speak_en()