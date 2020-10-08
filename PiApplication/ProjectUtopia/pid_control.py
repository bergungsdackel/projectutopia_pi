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

    def links_vorwaerts():
        time.sleep(5)
        GPIO.output(Pinmotorlinksvorwaerts,1)
        time.sleep(5)
        GPIO.output(Pinmotorlinksvorwaerts,0)

    def links_rueckwaerts():
        time.sleep(5)
        GPIO.output(Pinmotorlinksrueckwaerts,1)
        time.sleep(5)
        GPIO.output(Pinmotorlinksrueckwaerts,0)

    def rechts_vorwaerts():
        time.sleep(5)
        GPIO.output(Pinmotorrechtsvorwaerts,1)
        time.sleep(5)
        GPIO.output(Pinmotorrechtsvorwaerts,0)

    def rechts_rueckwaerts():
        time.sleep(5)
        GPIO.output(Pinmotorrechtssrueckwaerts,1)
        time.sleep(5)
        GPIO.output(Pinmotorrechtsrueckwaerts,0)

    PID.PID.init(1,2,3)
    def reglung():
        PID.PID.pid(eingang)