from multiprocessing import Process, Queue
from queue import Empty
from multi_face import Facerecognition

def main():
    q = Queue()
    face_recognition = Facerecognition()

    # 별도의 프로세스에서 video 함수를 실행합니다.
    p = Process(target=face_recognition.video, args=(q,))
    p.start()

    try:
        while True:
            try:
                # 큐에서 이름을 가져와 처리합니다.
                name = q.get(timeout=1)
                print(f"Received name: {name}")
            except Empty:
                pass
    except KeyboardInterrupt:
        p.terminate()
        p.join()

if __name__ == "__main__":
    main()