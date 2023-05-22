import cv2

print('Is OpenCV built with CUDA:', cv2.ocl.haveOpenCL())

if cv2.ocl.haveOpenCL():
    cv2.ocl.setUseOpenCL(True)
    print('Using CUDA.')
else:
    print('Not using CUDA.')
