from multi_face import Facerecognition
from multi_voice import get_r_name_list
from multiprocessing import Process, Queue

def process_names(names):
    # 이곳에서 names 변수를 사용하여 원하는 작업을 수행하세요.
    print(names)

def main():
    queue = Queue()
    face_recognition_process = Process(target=mul_fa, args=(queue,))
    speech_recognition_process = Process(target=mul_vo)

    face_recognition_process.start()
    speech_recognition_process.start()

    while True:
        names = queue.get()
        process_names(names)

    face_recognition_process.join()
    speech_recognition_process.join()

def mul_vo():
    r_name_list = get_r_name_list()

    print(r_name_list)

def mul_fa(queue):
    face_recog = Facerecognition()

    for names in face_recog.video():
        queue.put(names)

if __name__ == "__main__":
    main()