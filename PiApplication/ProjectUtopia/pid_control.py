import time
import RPi.GPIO as GPIO
import PID
import ProjectUtopia
class pid_control(object):
    def BasisKonfiguration():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PinMotorlinksvorwaerts, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PinMotorrechtsvorwaerts, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PinMotorlinksrueckwaerts, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PinMotorrechtsrueckwaerts, GPIO.OUT)

    def links_vorwaerts(sleepTime):
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)

    def links_rueckwaerts(sleepTime):
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)

    def rechts_vorwaerts(sleepTime):
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)

    def rechts_rueckwaerts(sleepTime):
        GPIO.output(Pinmotorrechtssrueckwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)

    PID.PID.init(1,2,3)
    def reglung():
        PID.PID.pid(eingang)


 
