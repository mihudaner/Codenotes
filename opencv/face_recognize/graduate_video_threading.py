import cv2
import os
from cv2 import imshow
import numpy as np
import sys
import time
from PIL import Image
import threading

cap=cv2.VideoCapture(r'C:\Users\wangkai\Desktop\pythonwork\data\big.mp4')

def face_detect_demo(img):
    img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    face_cascade = cv2.CascadeClassifier(r'C:\Users\wangkai\Desktop\pythonwork\data\haarcascade_frontalface_default.xml')
    #faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 10)
    for x,y,w,h in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    return img
        

def job1():
    global lock,frame_addface,frame,overflag
    flag,frame_addface=cap.read()
    overflag=0
    while True:
        lock1.acquire()
        print('lock1.acquire()')
        flag,frame=cap.read()
        if ord('q') == cv2.waitKey(1):
            overflag=1
            break
        if not flag:
            overflag=1
            break
        cv2,imshow('ok1',frame_addface)
        lock2.release()
        print('lock2.release()')
    cv2.destroyAllWindows()
    cap.release()    
        

def job2():
    global lock,frame_addface,frame,overflag
    while True:   
        lock2.acquire()#要等其他线程释放才能申请到所，会阻塞在这里
        print('lock2.acquire()')
        if overflag==1:
            break
        frame_addface=face_detect_demo(frame)
        lock1.release()
        print('lock1.release()')




if __name__=='__main__': 
        global lock1,lock2
        lock1=threading.Lock()
        lock2=threading.Lock()
        lock2.acquire()
        print('lock2.acquire()')
        t2 = threading.Thread(target=job2)
        t1 = threading.Thread(target=job1)
        #t3 = threading.Thread(target=job3)
        t1.start()
        t2.start()
        #t3.start()
        
