import PID
import pid_control
import RPi.GPIO as GPIO
import time
import gyro
import wifi
import motorControl
import Echo
import Kamera

#for x in range(0,10):

print ("PI Lebt")
PinMotorlinksvorwaerts = 29
PinMotorrechtsvorwaerts = 31
PinMotorlinksrueckwaerts = 33
PinMotorrechtsrueckwaerts = 35
PinEnMotorLeft = 37
PinEnMotorRight = 38
motorcontrol = motorControl(PinEnMotorLeft, PinEnMotorRight, PinMotorlinksvorwaerts, PinMotorlinksrueckwaerts, PinMotorrechtsvorwaerts, PinMotorrechtsrueckwaerts)
PID_CONTROL_CLASS = pid_control.pid_control(1,2,3,motorcontrol)

WifiThread = wifi.WifiModule()
EchoClass = Echo.Echo()

while True:
    try:
        #read gyroskop
        gyro.read_gyro()
        #
        Distanz = EchoClass.Distanz()
        speed=wifi.speed()
        turn=wifi.turn()
        PID_CONTROL_CLASS.reglung(gyro.gyroskop_x_skaliert, speed, turn)

        #anderer thread für wifi cmds
        if(WifiThread.neueDaten == True):

            print(WifiThread.targetSpeed) #vorwärts oder rückwärts je nach vorzeichen
            print("Rotiere" + WifiThread.rotate + " mit Geschw. " + WifiThread.rotateStrength) #links oder rechts mit welcher Geschw.
            WifiThread.neueDaten = False #daten wurden verarbeitet, also kann WifiClass wieder empfangen

        #
        #time.sleep(5)
            
