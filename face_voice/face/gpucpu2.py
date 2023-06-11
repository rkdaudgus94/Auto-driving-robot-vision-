import subprocess

def gpu_usage():
    try:
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv'])
        gpu_usage = [int(x) for x in output.decode().strip().split('\n')[1:]]
        return gpu_usage
    except subprocess.CalledProcessError as e:
        print("Error: ", e)