import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)

def abrir(self):
        # set GPIO10 pin to HIGH
        GPIO.output(10,GPIO.HIGH)
        # pause for one second
        time.sleep(3)
        # set GPIO10 pin to LOW
        GPIO.output(10,GPIO.LOW)
