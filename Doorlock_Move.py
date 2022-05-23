import RPi.GPIO as GPIO

import time


def Doorlock():
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(18,GPIO.OUT)
    
    time.sleep(0.5)
    
    GPIO.output(18,False)
    
    print('open')
    
    time.sleep(2)
    
    GPIO.cleanup()
    
    print('cleanup')
    
    time.sleep(0.5)
Doorlock()