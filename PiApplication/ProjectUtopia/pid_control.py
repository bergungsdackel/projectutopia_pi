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
        print ("BasisKonfiguration")

    def vorwaerts():
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.HIGH)
        print ("vorwaerts")

    def rueckwaerts():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorrechtssrueckwaerts,GPIO.HIGH)
        print ("rueckwaerts")

    def stopp():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)
        print ("stopp")

    def links_vorwaerts():
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)
        print ("links vorwaerts")

    def links_rueckwaerts():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)
        print ("links rueckwaerts")

    def rechts_vorwaerts():
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)
        print ("rechts vorwaerts")

    def rechts_rueckwaerts():
        GPIO.output(Pinmotorrechtssrueckwaerts,GPIO.HIGH)
        GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)
        print ("rechts rueckwaerts")

    def links_stopp():
        GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)
        print ("links stopp")

    def rechts_stopp():
        GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)
        GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)
        print ("rechts stopp")

    PID.PID.init(1,2,3)
    def reglung(eingang1, eingang2):
        PID.PID.pid(eingang)
        geregelterWert = PID.PID.Ausgang
    #########################################################################################

   


 
