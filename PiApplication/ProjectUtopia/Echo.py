import RPi.GPIO as GPIO
import time
import threading

class Echo(threading.Thread):
    
    def __init__(self, trigger, echo):

        threading.Thread.__init__(self)
        self.daemon = True

        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        self.trigger = trigger
        self.echo = echo
        GPIO.output(trigger,False)

        self.Distanz = 0.0

        self.start()

        print("Ultraschall-Messer iniziiert")

    def run(self):

        while True:

            GPIO.output(self.trigger,True)
            time.sleep(0.00001)
            GPIO.output(self.trigger,False)
            startzeit = time.time()
            stopzeit = time.time()
            while (GPIO.input(self.echo)==0):

                startzeit = time.time()

            while (GPIO.input(self.echo)==1):

                stopzeit = time.time()

            Dauer = stopzeit - startzeit
            self.Distanz = (Dauer * 34300) / 2

            time.sleep(0.5)