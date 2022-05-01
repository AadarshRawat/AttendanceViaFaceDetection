import json
import requests
from pydoc import classname
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from posixpath import splitext
presentlist=[]
# from PIL import ImageGrab
attendance=[]

path = "Images"
images = []
studentinfo={}
rollnumber=[]
myList = os.listdir(path)#path selected
# print(myList)
for i in myList:#browsing through the img list
    curImg = cv2.imread(f'{path}/{i}')
    images.append(curImg)
    x=splitext(i)[0]
    z=x.split('_')
    studentinfo[z[-2]]=z[:4]
    # attendance[z[-2]]=attendance.append(z[-1])
    rollnumber.append([z[-2]])

# print('-------------StudentInfo-------------',studentinfo)
# print()
# print('-------------RollNumber--------------',rollnumber)
# print()


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
# print('<----------------------ENCODINGS------------------------->')
# print(encodeListKnown)
# print('Number Of Students')
# print(len(encodeListKnown))
print('Encoding Complete')
cap = cv2.VideoCapture(0)

breaker=False
def detect(breaker,k):


    while True:
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    


        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            # print(matchIndex)
    
            if matches[matchIndex]:
                rolln = rollnumber[matchIndex]
                if rolln[0] not in presentlist:
                    presentlist.append(rolln[0])
                    # print(presentlist)
                    # print(rolln)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,f'{rolln}',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                cv2.imshow('Webcam',img)
                k=cv2.waitKey(1) & 0xff
            if k==27:
                cv2.destroyAllWindows()
                breaker=True
                break
        if breaker:
            return presentlist



#----------------------x----------------------------------------------------------
def call():

    # print('TEST FILE')
    URL="http://127.0.0.1:8000/create"
    breaker=False
    x=detect(breaker,0)
    # print('Present Students are:',x)
    # print('Studentinfo',studentinfo)
    l=[]
    for i in x:
        d={}
        d['rollnumber']=i
        d['name']=studentinfo[i][0]
        d['lname']=studentinfo[i][1]
        # print('dictionary',d)
        l.append(d)

    print('l->',l)

    for i in l:
        json_data=json.dumps(i)
        # print('This is Json Data',json_data)
        r=requests.put(url=URL,data=json_data)
        data=r.json()
        print(data)


