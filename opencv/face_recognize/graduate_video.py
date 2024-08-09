import cv2
import os
from cv2 import imshow
import numpy as np
import sys
import time
from PIL import Image
import threading

cap=cv2.VideoCapture(r'D:\Desktop\pythonwork\data\big.mp4')
face_cascade = cv2.CascadeClassifier(r'D:\Desktop\pythonwork\data\haarcascade_frontalface_default.xml')

def face_detect_demo(img):
    img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    face_cascade = cv2.CascadeClassifier(r'D:\Desktop\pythonwork\\data\haarcascade_frontalface_default.xml')
    #faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 10)
    for x,y,w,h in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    return img
    

flag,frame=cap.read()
while True:
    print("ing")
    flag,frame=cap.read()
    if ord('q') == cv2.waitKey(1):
        break
    if not flag:
        break
    frame=face_detect_demo(frame)
    cv2.imshow('ok1',frame)
cv2.destroyAllWindows()
cap.release()    
