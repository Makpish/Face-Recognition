import numpy as np
import cv2
import os
from PIL import Image
from store_users import Users

#using Local Binary Pattern Histogram algorithm to recognize face 
recognizer = cv2.face.createLBPHFaceRecognizer()

#using haarcascade for face detection
detector= cv2.CascadeClassifier('face.xml')

#folder where train data is present
path = "dataset"

#initialize database
users = Users()


def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    # print(imagePaths)
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=os.path.split(imagePath)[-1].split(".")[0]
        user = users.checkMember(Id)
        if not user:
            user = users.newMember(Id)
        # print(Id)
        # extract the face from the training image sample
        # print
        faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(user)
    return faceSamples,Ids

faces,Ids = getImagesAndLabels(path)
# print(Ids)
recognizer.train(faces, np.array(Ids))
recognizer.save('trainer.yml')
#cv2.destroyAllWindows()
