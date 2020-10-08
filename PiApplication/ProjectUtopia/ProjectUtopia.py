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

PinMotorlinks = 1
PinMotorrechts = 2




def BasisKonfiguration():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinMotorlinks, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinMotorrechts, GPIO.OUT)

pid=PID.PID(P, I, D)

def Konfiguration():
    pid.setKp(Kp)
    pid.setKi(Ki)
    pid.setKd(Kd)

def links_vorwaerts():
    time.sleep(5)
    GPIO.output(Pinmotorlinks,1)
    time.sleep(5)
    GPIO.output(Pinmotorlinks,0)

def links_rueckwaerts():

def rechts_vorwaerts():
    time.sleep(5)
    GPIO.output(Pinmotorrechts,1)
    time.sleep(5)
    GPIO.output(Pinmotorrechts,0)

def rechts_rueckwaerts():


while (1):
    Konfiguration()
    Eingang=pin1 # keinen Schimmer
    Bewegung=Eingang*2 # keinen Schimmer

    pid.update(Bewegung)
    #Motor dreh dich

