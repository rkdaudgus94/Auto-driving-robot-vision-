import psutil
import GPUtil
import time

while True:
    # CPU 사용량 출력
    cpu_percent = psutil.cpu_percent()
    print(f"CPU Usage: {cpu_percent}%")

    # GPU 사용량 출력
    gpus = GPUtil.getGPUs()
    for i, gpu in enumerate(gpus):
        print(f"GPU {i} Usage: {gpu.load * 100}%")
        print(f"GPU {i} Memory Usage: {gpu.memoryUsed}MB / {gpu.memoryTotal}MB ({gpu.memoryUtil * 100}%)")

    time.sleep(1)