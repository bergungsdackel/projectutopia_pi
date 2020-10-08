print("HELLO WORimport PID
import pid_control
import RPi.GPIO as GPIO
import time

#for x in range(0,10):


PinMotorlinksvorwaerts = 1
PinMotorrechtsvorwaerts = 2
PinMotorlinksrueckwaerts = 3
PinMotorrechtsrueckwaerts = 4

while (1):
    pid_control.pid_control.reglung();
    Eingang=pin1 # keinen Schimmer
    Bewegung=Eingang*2 # keinen Schimmer

    pid.update(Bewegung)
    #Motor dreh dich

LD")
