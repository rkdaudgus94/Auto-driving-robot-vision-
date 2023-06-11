
from face_win import Facerecognition, cog
from respeak3 import speak_jetson

import threading
import multiprocessing as Process

""" p0 = Process(target=star)
p1 = Process(target=speak_jetson)
p0.start()
p1.start()

p0.join()
p1.join() """


import multiprocessing

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=speak_jetson)
    p2 = multiprocessing.Process(target=cog)

    p1.start()
    p2.start()

    p1.join()
    p2.join()