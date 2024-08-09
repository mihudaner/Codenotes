import cv2
import os
from cv2 import imshow
import numpy as np
import sys
import time
from PIL import Image



def getImageAndLabels(path):
    facesSamples=[]
    ids=[]
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]

    #检测人类、脸
    face_cascade = cv2.CascadeClassifier\
    (r'C:\Users\wangkai\Desktop\pythonwork\data\haarcascade_frontalface_default.xml')
    
    
    #遍历所有图片
    for imagePath in imagePaths:
        #打开图片
        PIL_img = Image.open(imagePath).convert('L')
        #将图片转换为数组
        img_numpy = np.array(PIL_img,'uint8')
        #获取图片id
        print(os.path.split(imagePath))
        id_=int(os.path.split(imagePath)[1].split('.')[0])
        faces = face_cascade.detectMultiScale(img_numpy)
        #cv2.imshow('VIDIO',img_numpy)
        for x,y,w,h in faces:
            facesSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id_)

            
    return facesSamples,ids
if __name__ == '__main__':
    path='./face/1/'
    #获取图像数组和id标签
    faces,ids=getImageAndLabels(path)
    recogenizer=cv2.face.LBPHFaceRecognizer_create()
    recogenizer.train(faces,np.array(ids))
    #保存文件
    recogenizer.write('./face/trainer.yml')
