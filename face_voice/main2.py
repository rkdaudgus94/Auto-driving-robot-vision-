from multiprocessing import Process, Queue
import threading
from queue import Empty
from multi_face2 import Facerecognition, gstreamer_pipeline, face_confidence
from multi_voice import get_r_name_list

def main() :
    p0 = threading.Thread(target=mu_fa)
    p1 = threading.Thread(target=mu_fa)

    p0.start()
    p1.start()

    p0.join()
    p1.join()

def mu_fa():
    time = 0
    face_recognition = Facerecognition()
    face_recognition.video()
    """ for names in face_recognition.video() :
        if (names != []) & (time == 15) :
            print(names)
        time += 1 """
def mu_vo():
    r_name_list = get_r_name_list()

    print(r_name_list)

if __name__ == "__main__":
    main()