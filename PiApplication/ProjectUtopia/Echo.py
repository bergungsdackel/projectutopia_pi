import RPi.GPIO as GPIO
import time

class Echo(object):
    trigger = 8
    echo = 10

    def Distanz(self):

        GPIO.output(trigger,True)
        sleep(0.00001)
        GPIO.output(trigger,False)
        startzeit = time.time()
        stopzeit = time.time()
        while (GPIO.input(echo)==0):
            startzeit = time.time()
        while (GPIO.input(echo)==1):
            stopzeit = time.time()
        Dauer = stopzeit - startzeit
        distanz = (TimeElapsed * 34300) / 2
        print("Gemessene Entfernung = %.1f cm" % distanz)
        return distanz

    def __init__(self):
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        GPIO.output(trigger,False)
        print("Ultraschall Messer iniziiert")