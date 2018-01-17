import cv2
import numpy as np
from store_users import Users

#using local binary pattern histograms for face recognizion
recognizer = cv2.face.createLBPHFaceRecognizer()

#loading trained model
recognizer.load('trainer.yml')

#using haarcascade to detect faces in a image
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

users = Users()

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(Id," ",conf)
        #if the confidence of face recognision is to certain threshold then find the member
        if(conf<=50):
            Id = users.getMember(Id)
        else:
            Id="Unknown"
        # cv2.PutText(cv2.fromarray(im),str(Id), (x,y+h),font, 255)
        cv2.putText(im,str(Id),(x,y+h), font, 1, (200,255,155), 2, cv2.LINE_AA)
    cv2.imshow('im',im) 
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
