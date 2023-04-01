import multiprocessing
from face_recognition_process import Facerecognition
from speech_recognition_process import main as speech_main

def face_recognition_process():
    fr_instance = Facerecognition()
    fr_instance.video()

def speech_recognition_process():
    speech_main()

if __name__ == "__main__":
    face_process = multiprocessing.Process(target=face_recognition_process)
    speech_process = multiprocessing.Process(target=speech_recognition_process)

    face_process.start()
    speech_process.start()

    face_process.join()
    speech_process.join()
