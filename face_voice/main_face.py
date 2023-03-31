from multiprocessing import Process, Queue
from queue import Empty
from multi_face import Facerecognition

def main():
    face_recognition = Facerecognition()

    for names in face_recognition.video() :
        print(names)
if __name__ == "__main__":
    main()