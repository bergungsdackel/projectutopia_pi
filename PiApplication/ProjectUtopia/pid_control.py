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

    def vorwaerts():
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.HIGH)

    def rueckwaerts():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorrechtssrueckwaerts,GPIO.HIGH)

    def stopp():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)

    def links_vorwaerts():
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)

    def links_rueckwaerts():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)

    def rechts_vorwaerts():
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)

    def rechts_rueckwaerts():
        GPIO.output(Pinmotorrechtssrueckwaerts,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)

    def links_stopp():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)

    def rechts_stopp():
        GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)

    PID.PID.init(1,2,3)
    def reglung():
        PID.PID.pid(eingang)


 
