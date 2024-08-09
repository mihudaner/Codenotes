import cv2
r'''
img=cv2.imread(r'C:\Users\wangkai\Desktop\pythonwork\data\lenna.png',0)
print(img)
print(img.shape)
cv2.imshow('lenna',img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyWindow('lenna')
elif k==115:
    cv2.imwrite(r'C:\Users\wangkai\Desktop\pythonwork\data\lenna_gray.png',img)
    cv2.destroyWindow('lenna')
    

resize_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow('lenna_small',resize_img)
'''

img=cv2.imread(r'C:\Users\wangkai\Desktop\pythonwork\data\team.png')
img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray)

face_cascade = cv2.CascadeClassifier(r'C:\Users\wangkai\Desktop\pythonwork\data\haarcascade_frontalface_default.xml')
#创建一个级联分类器对象（CascadeClassifier）：

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.10, minNeighbors = 5)
print(faces)
#scaleFactor = 1.05 每次图像缩小的比例  minNeighbors = 5每一个目标至少被检测多少次

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('lenna',img)
#搭建环境
#Step one：载入图像，并创建一个级联分类器（包含人脸特征数据）
#Step two：  将 NumPy 数组中的数据与级联分类器的特征数据进行匹配，找到人脸
#Step three：在人脸位置画个框框标记一下
