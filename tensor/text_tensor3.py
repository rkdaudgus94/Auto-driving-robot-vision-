import cv2
import re
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img_path = 'D:/620/620(3).jpg'

img = cv2.imread(img_path)

if img is not None:
    print('Image is loaded.')
else:
    print('Failed to load the image.')

def convert_graystyle(img) :
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def blur(img, param) :
    img = cv2.medianBlur(img, param)
    return img

def threshold(img) :
    img = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img

h, w, c = img.shape

img = convert_graystyle(img)
img = blur(img, 5)
img = threshold(img)

boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines() :
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0),2)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows