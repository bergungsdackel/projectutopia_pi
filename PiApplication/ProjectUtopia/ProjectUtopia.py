import PID
import RPi.GPIO as GPIO
import time

#for x in range(0,10):


P = 5
I = 5
D = 5
Kp = 1
Ki = 1
Kd = 1

PinMotorlinksvorwaerts = 1
PinMotorrechtsvorwaerts = 2
PinMotorlinksrueckwaerts = 3
PinMotorrechtsrueckwaerts = 4


def BasisKonfiguration():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinMotorlinksvorwaerts, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinMotorrechtsvorwaerts, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinMotorlinksrueckwaerts, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinMotorrechtsrueckwaerts, GPIO.OUT)

pid=PID.PID(P, I, D)

def Konfiguration():
    pid.setKp(Kp)
    pid.setKi(Ki)
    pid.setKd(Kd)

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

while (1):
    Konfiguration()
    Eingang=pin1 # keinen Schimmer
    Bewegung=Eingang*2 # keinen Schimmer

    pid.update(Bewegung)
    #Motor dreh dich

