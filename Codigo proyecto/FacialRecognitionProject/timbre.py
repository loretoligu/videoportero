import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        
while(True):        
    status=GPIO.input(24)
    if status == False:
        exec(open("/home/log/FacialRecognitionProject/FaceRecognition.py").read())
    
