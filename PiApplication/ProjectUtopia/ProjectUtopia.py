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
import Selfdriving

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
Kp = 0
Ki = 0
Kd = 0
Gyrokompensation = 0
#sprung = 0
#i=0

motorcontrol = motorControl(PinEnMotorLeft, PinEnMotorRight, PinMotorlinksvorwaerts, PinMotorlinksrueckwaerts, PinMotorrechtsvorwaerts, PinMotorrechtsrueckwaerts)
PID_CONTROL_CLASS = pid_control.pid_control(1,1,0,motorcontrol)
RcvWifiThread = wifi.RcvWifiModule()
#SendWifiThread = wifi.SendWifiModule()
#tcpHandlerClass = tcpHandler.tcpHandler()
EchoClass = Echo.Echo(PinEchoTrigger, PinEchoEcho)
GyroClass = gyro.gyro()
SelfdrivingClass = Selfdriving.selfdriving(motorcontrol, GyroClass, Gyrokompensation, EchoClass, Kp, Ki, Kd)

try:
    while True:
        try:
            if(Kp == 0 and Ki == 0 and Kd == 0):
                if(RcvWifiThread.KonstantenReceived == True):
                    print("nKp: "+str(RcvWifiThread.Kp))
                    print("nKi: "+str(RcvWifiThread.Ki))
                    print("nKd: "+str(RcvWifiThread.Kd))
                    Kp = RcvWifiThread.Kp
                    Ki = RcvWifiThread.Ki
                    Kd = RcvWifiThread.Kd            
                  

            if(RcvWifiThread.KonstantenReceived == True):

                if(RcvWifiThread.neueDaten == True):
                    print("\nTargetSpeedFB: "+str(RcvWifiThread.targetSpeedFB)) #vorwaerts oder rueckwaerts je nach vorzeichen
                    print("\nRotateStrength: "+str(RcvWifiThread.rotateStrength)) #links oder rechts mit welcher Geschw. je nach Vorzeichen
                    #SendWifiThread.Smartphone_IP = RcvWifiThread.Smartphone_IP #IP setzen
                    RcvWifiThread.neueDaten = False #daten wurden verarbeitet, also kann WifiClass wieder empfangen


                if(True):
                    #read gyroskop
                    GyroClass.read_gyro()
                    #
                    #if (i == 30):
                    #    sprung = 90

                    Distanz = EchoClass.Distanz()
                    print("Debug Distanz: " + str(Distanz)) #Debug

                    speed = RcvWifiThread.targetSpeedFB
                    turn = RcvWifiThread.rotateStrength
                    PID_CONTROL_CLASS.reglung(GyroClass.x_rotation, speed, turn, Gyrokompensation, Kp, Ki, Kd)        
                    #PID_CONTROL_CLASS.reglung(sprung, speed, turn)
                    #i = i + 1
                    #anderer thread für wifi cmds

                else:
                    selfdrivingClass.drive(Kp, Ki, Kd)





        except Exception as e:
            print("Main-Error: "+str(e))
            GPIO.cleanup()
            break
except Exception as e:
    print("Main-Error: "+str(e))
    GPIO.cleanup()
finally:
    GPIO.cleanup()
        
