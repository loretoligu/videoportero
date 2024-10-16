import cv2
import numpy as np
import os
import imutils
import time
from apertura import *
from  pymdb import *
from telegram import *

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/log/FacialRecognitionProject/trainer/trainer.yml')
# Load the classifier
cascadePath = "/home/log/FacialRecognitionProject/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

confidence =200 #Initialize confidence
id = 0 # Initialize id counter
names = ['None', 'Loreto'] # Names related to ids

# Initialize and start realtime video capture
cam = cv2.VideoCapture('/dev/video0')

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

ini_time=time.time()
end_time=ini_time + 30
while True:
    ret, img =cam.read()
    img =imutils.resize(img,width=480)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # Detect faces on the image
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
       
    # Mark rectangle in the faces   
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        # Analyze face and return owner
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less than 100."0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidencep = "  {0}%".format(round(100 - confidence))
            
        else:
            id = "Desconocido"
            confidencep = "  {0}%".format(round(100 - confidence))
            #lanzar notificacion
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidencep), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img)
    
    if (confidence < 30):
        abrir(id) # Open the door (turn on LED)
        percent = 100 - confidence
        success = 1
        passdata(success,id)
        break
    else:
        if (time.time() > end_time):
            percent = 100 - confidence
            success = 0
            passdata(success,id)
            chat_id = "458778819"
            api_key = "6355325056:AAHwqlZPHhrq41iwAhVye7Kw_91yWPktF5c"
            send_telegram_message("Hay alguien en la puerta!",chat_id,api_key)
            send_telegram_message("http://192.168.1.100/catalog/",chat_id,api_key)
            break
        
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Cleanup
cam.release()
cv2.destroyAllWindows()
