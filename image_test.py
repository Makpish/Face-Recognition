import cv2
import numpy as np
from store_users import Users

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer.yml')
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

users = Users()

# cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

path = input("Enter image name:")

# ret, im =cam.read()
im = cv2.imread("imageTest/"+path)
im = cv2.resize(im, (0,0), fx=0.5, fy=0.4)
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, 1.2,5)
for(x,y,w,h) in faces:
    cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
    Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
    print(Id," ",conf)
    if(conf<=50):
        Id = users.getMember(Id)
    else:
        Id="Unknown"
    # cv2.PutText(cv2.fromarray(im),str(Id), (x,y+h),font, 255)
    cv2.putText(im,str(Id),(x,y+h), font, 1, (200,255,155), 2, cv2.LINE_AA)
cv2.imshow('im',im)
cv2.waitKey(0) 
# if cv2.waitKey(100) & 0xFF==ord('q'):
    # break
# cam.release()
cv2.destroyAllWindows()
