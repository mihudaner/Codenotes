import cv2
import os
import numpy as np
import sys
from PIL import Image
#加载训练集数据文件
recogenizer=cv2.face.LBPHFaceRecognizer_create()
recogenizer.read(r'C:\Users\wangkai\Desktop\pythonwork\opencv\face_recognize\facetrainer.yml')
#准备要识别的图片
#img=cv2.imread('./face/dlrb1/9.png')
img=cv2.imread(r'C:\Users\wangkai\Desktop\ss.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(r'C:\Users\wangkai\Desktop\pythonwork\data\haarcascade_frontalface_default.xml')
#创建一个级联分类器对象（CascadeClassifier）：
faces = face_detector.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 10)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    id,confidence=recogenizer.predict(gray[y:y+h,x:x+h])
    print('标签id:',id,'置信评分',confidence)
    cv2.imshow('img_find',img)
    path_result='./face/1/'+str(id)+'.png'
    img_result=cv2.imread(path_result)
    cv2.imshow('img_result',img_result)
while True:
    if ord('q') == cv2.waitKey(1): 
        break
cv2.destroyALLWindows()


