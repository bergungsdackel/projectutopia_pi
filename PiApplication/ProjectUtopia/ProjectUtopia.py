import PID
import pid_control
import RPi.GPIO as GPIO
import time
import gyro
import wifi
import motorControl

#for x in range(0,10):

print ('PI Lebt')
PinMotorlinksvorwaerts = 5
PinMotorrechtsvorwaerts = 6
PinMotorlinksrueckwaerts = 13
PinMotorrechtsrueckwaerts = 19
PinEnMotorLeft = 4 #Nicht festgelegt
PinEnMotorRight = 7 #Nicht festgelegt
motorcontrol = motorControl(PinEnMotorLeft, PinEnMotorRight, PinMotorlinksvorwaerts, PinMotorlinksrueckwaerts, PinMotorrechtsvorwaerts, PinMotorrechtsrueckwaerts)

while True:
    try:
        #read gyroskop
        gyro.read_gyro()
        #
        pid_control.pid_control.reglung(gyro.gyroskop_x_skaliert)


        #anderer thread für wifi cmds
        WifiThread = wifi.WifiModule()
        if(WifiThread.neueDaten == True):
            WifiThread.neueDaten = False
            print(WifiThread.data)
