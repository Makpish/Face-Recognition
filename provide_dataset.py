import numpy as np
import cv2
import os
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('face.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# eye_cascade = cv2.CascadeClassifier('eye.xml')

# cap = cv2.VideoCapture(0)

#enter folder name which u want to provide to as dataset
path = input("enter folder name:")
# if not os.path.exists(path):
# 	os.mkdir(path)

c=1
imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
for imagePath in imagePaths:
    #loading the image and converting it to gray scale
    img = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
# ret, img = cap.read()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_gray = img[y:y+h, x:x+w]
        cv2.imwrite("dataset/"+path+"."+str(c)+".jpg",roi_gray)
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # roi_color = img[y:y+h, x:x+w]
        c+=1
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # cv2.imshow('img',img)
    # os.remove(imagePath)
        

# cap.release()
cv2.destroyAllWindows()
