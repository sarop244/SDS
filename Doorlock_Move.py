import RPi.GPIO as GPIO

import time


def Doorlock():
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(26,GPIO.OUT)
    
    time.sleep(1)


    for i in range(1,3):
        
        GPIO.output(26,True)
        
        print('true')
        
        time.sleep(1)
        
        GPIO.output(26,False)
        
        print('false')
        
        time.sleep(1)

    GPIO.cleanup()
    
    print('cleanup')
    
    time.sleep(1)
