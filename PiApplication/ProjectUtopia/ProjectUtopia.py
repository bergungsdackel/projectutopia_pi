import PID
import pid_control
import RPi.GPIO as GPIO
import time
import gyro
import wifi
from motorControl import motorControl
import Echo
import Kamera

#for x in range(0,10):

print ("PI Lebt")
GPIO.setmode(GPIO.BOARD)
PinMotorlinksvorwaerts = 29
PinMotorrechtsvorwaerts = 31
PinMotorlinksrueckwaerts = 33
PinMotorrechtsrueckwaerts = 35
PinEnMotorLeft = 37
PinEnMotorRight = 38
PinEchoTrigger = 8
PinEchoEcho = 10
motorcontrol = motorControl(PinEnMotorLeft, PinEnMotorRight, PinMotorlinksvorwaerts, PinMotorlinksrueckwaerts, PinMotorrechtsvorwaerts, PinMotorrechtsrueckwaerts)
PID_CONTROL_CLASS = pid_control.pid_control(1,2,3,motorcontrol)

WifiThread = wifi.WifiModule()
EchoClass = Echo.Echo(PinEchoTrigger, PinEchoEcho)
GyroClass = gyro.gyro()

while True:
    try:
        #read gyroskop
        GyroClass.read_gyro()
        #
        Distanz = EchoClass.Distanz()
        speed = WifiThread.targetSpeedFB
        turn = WifiThread.rotateStrength
        PID_CONTROL_CLASS.reglung(GyroClass.gyroskop_x_skaliert, speed, turn)        
        

        #anderer thread für wifi cmds
        if(WifiThread.neueDaten == True):
                
            print(WifiThread.targetSpeedFB) #vorwaerts oder rueckwaerts je nach vorzeichen
            print(WifiThread.rotateStrength) #links oder rechts mit welcher Geschw. je nach Vorzeichen
            WifiThread.neueDaten = False #daten wurden verarbeitet, also kann WifiClass wieder empfangen
        #time.sleep(5)
    except Exception as e:
        print(str(e))
        GPIO.cleanup()
        break
        
