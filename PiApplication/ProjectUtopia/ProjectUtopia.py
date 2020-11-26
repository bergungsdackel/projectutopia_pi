import PID
import pid_control
import RPi.GPIO as GPIO
import time
import gyro
import wifi
import tcpHandler
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

oldtime = 0

motorcontrol = motorControl(PinEnMotorLeft, PinEnMotorRight, PinMotorlinksvorwaerts, PinMotorlinksrueckwaerts, PinMotorrechtsvorwaerts, PinMotorrechtsrueckwaerts)
PID_CONTROL_CLASS = pid_control.pid_control(1,0.1,0,motorcontrol)
RcvWifiThread = wifi.RcvWifiModule()
SendWifiThread = wifi.SendWifiModule()
tcpHandlerClass = tcpHandler.tcpHandler()
EchoClass = Echo.Echo(PinEchoTrigger, PinEchoEcho)
GyroClass = gyro.gyro()

try:
    while True:
        try:

            print(time.clock() - oldtime)
            #read gyroskop
            GyroClass.read_gyro()
            #


            Distanz = EchoClass.Distanz()
            speed = RcvWifiThread.targetSpeedFB
            turn = RcvWifiThread.rotateStrength
            PID_CONTROL_CLASS.reglung(GyroClass.gyroskop_x_skaliert, speed, turn)        
            #PID_CONTROL_CLASS.reglung(0, speed, turn)
            #anderer thread für wifi cmds
            if(RcvWifiThread.neueDaten == True):
                
                print("\nTargetSpeedFB: "+str(RcvWifiThread.targetSpeedFB)) #vorwaerts oder rueckwaerts je nach vorzeichen
                print("\nRotateStrength: "+str(RcvWifiThread.rotateStrength)) #links oder rechts mit welcher Geschw. je nach Vorzeichen
                SendWifiThread.Smartphone_IP = RcvWifiThread.Smartphone_IP #IP setzen
                RcvWifiThread.neueDaten = False #daten wurden verarbeitet, also kann WifiClass wieder empfangen
            oldtime=time.clock()
        except Exception as e:
            print("Main-Error: "+str(e))
            GPIO.cleanup()
            break
except Exception as e:
    print("Main-Error: "+str(e))
    GPIO.cleanup()
finally:
    GPIO.cleanup()
        
