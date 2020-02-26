import numpy as np
import atexit
import cv2
import time
from timeit import timeit
import json
from time import sleep

cap = cv2.VideoCapture(0)

def scaleImg(img, targetDims):
    x0, y0, _ = img.shape
    x1, y1 = targetDims
    return cv2.resize(img, None, fx=x1/x0, fy=y1/y0, interpolation=cv2.INTER_AREA)

translate = np.vectorize(lambda x: colorMap[x])
def imgToAscii(img, colorMap):
    n = len(colorMap)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = (img.astype('float32') * (n/256.0)).astype(int)
    ret = translate(img)
    return '\n'.join(map(lambda x: ''.join(x), ret))

def clearScreen():
    print('\33[2J',)

@atexit.register
def cleanup():
    print("cleanup")
    cap.release()
    cv2.destroyAllWindows() 

colorMap = {int(k) : v for k, v in json.load(open('./charBrightness.json')).items()}

while(True):
    ret, frame = cap.read()
    frame = scaleImg(frame, (80, 60))
    clearScreen()
    print(imgToAscii(frame, colorMap))
