import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)

# While loop
def abrir(self):
        # set GPIO15 pin to HIGH
        GPIO.output(15,GPIO.HIGH)
        # pause for one second
        time.sleep(3)
        # set GPIO15 pin to HIGH
        GPIO.output(15,GPIO.LOW)                                                                                                                       