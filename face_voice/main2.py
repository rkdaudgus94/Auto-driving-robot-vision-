from multiprocessing import Process, Queue
from queue import Empty
from multi_face import Facerecognition
from multi_voice import get_r_name_list
import time

def main() :
    p0 = Process(target = mu_fa())
    p1 = Process(target = mu_vo())

    p0.start()
    p1.start()

    p0.join()
    p1.join()

def mu_fa():
    face_recognition = Facerecognition()
    for names in face_recognition.video() :
        time.sleep(2)
        print(names)

def mu_vo():
    r_name_list = get_r_name_list()

    print(r_name_list)

if __name__ == "__main__":
    main()