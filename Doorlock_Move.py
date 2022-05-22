import RPi.GPIO as GPIO

import time


def Doorlock():
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(18,GPIO.OUT)
    
    time.sleep(1)
    
    GPIO.output(18,False)
    
    print('open')
    
    time.sleep(3)
    
    GPIO.cleanup()
    
    print('cleanup')
    
    time.sleep(1)
