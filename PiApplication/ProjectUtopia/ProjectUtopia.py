import PID
import pid_control
import RPi.GPIO as GPIO
import time
import gyro
import wifi

#for x in range(0,10):

print ("Hello world")
PinMotorlinksvorwaerts = 5
PinMotorrechtsvorwaerts = 6
PinMotorlinksrueckwaerts = 13
PinMotorrechtsrueckwaerts = 19

while true:
    try:
        #read gyroskop
        gyro.read_gyro()
        #
        pid_control.pid_control.reglung(gyro.gyroskop_x_skaliert)
        Eingang=pin1 # keinen Schimmer
        Bewegung=Eingang*2 # keinen Schimmer


        #anderer thread für wifi cmds
        WifiThread = wifi.WifiModule()
        if(WifiThread.neueDaten == true):
            print("Penis")
