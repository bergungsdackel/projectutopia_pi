import RPi.GPIO as GPIO
import time

class Echo(object):
    


    def __init__(self, trigger, echo):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        self.trigger = trigger
        self.echo = echo
        GPIO.output(trigger,False)
        print("Ultraschall Messer iniziiert")
        print("test")

    def Distanz(self):
        GPIO.output(trigger,True)
        time.sleep(0.00001)
        GPIO.output(trigger,False)
        startzeit = time.time()
        stopzeit = time.time()
        while (GPIO.input(echo)==0):
            startzeit = time.time()
        while (GPIO.input(echo)==1):
            stopzeit = time.time()
        Dauer = stopzeit - startzeit
        distanz = (Dauer * 34300) / 2
        print("Gemessene Entfernung = %.1f cm" % distanz)
        return distanz
