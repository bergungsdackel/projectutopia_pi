import RPi.GPIO as GPIO
import time

class Echo(object):
    


    def __init__(self, trigger, echo):
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        self.trigger = trigger
        self.echo = echo
        GPIO.output(trigger,False)
        print("Ultraschall-Messer iniziiert")


    def Distanz(self):
        GPIO.output(self.trigger,True)
        time.sleep(0.00001)
        GPIO.output(self.trigger,False)
        startzeit = time.time()
        stopzeit = time.time()
        #while (GPIO.input(self.echo)==0):
        startzeit = time.time()
        #while (GPIO.input(self.echo)==1):
        stopzeit = time.time()
        Dauer = stopzeit - startzeit
        distanz = (Dauer * 34300) / 2
        return distanz
