import multiprocessing
from multi_face2 import Facerecognition
from multi_voice import get_r_name_list
import os
def face_recognition_process():
    fr_instance = Facerecognition()
    fr_instance.video()

def speech_recognition_process():
    r_name_list = get_r_name_list()

if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    face_process = multiprocessing.Process(target=face_recognition_process)
    speech_process = multiprocessing.Process(target=speech_recognition_process)

    face_process.start()
    speech_process.start()

    face_process.join()
    speech_process.join()
