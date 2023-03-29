from multi_face import Facerecognition
from multi_voice import get_r_name_list

def process_names(names):
    # 이곳에서 names 변수를 사용하여 원하는 작업을 수행하세요.
    print(names)

def main():
    # voice_recognition.py의 get_r_name_list 함수를 호출하여 r_name_list 값을 가져옴
    r_name_list = get_r_name_list()

    print(r_name_list)

    # Facerecognition 클래스를 인스턴스화하고 video 메서드를 호출하며 process_names 함수를 전달합니다.
    run = Facerecognition()
    run.video(callback=process_names)

if __name__ == "__main__":
    main()