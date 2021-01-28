import PID
import pid_control
import RPi.GPIO as GPIO
import time
import gyro
import wifi
import tcpHandler
from motorControl import motorControl
import Echo
import Selfdriving


GPIO.setmode(GPIO.BOARD)
PinMotorlinksvorwaerts = 29
PinMotorrechtsvorwaerts = 31
PinMotorlinksrueckwaerts = 33
PinMotorrechtsrueckwaerts = 35
PinEnMotorLeft = 37
PinEnMotorRight = 38
PinEchoTrigger = 8
PinEchoEcho = 10
Kp = 0.0
Ki = 0.0
Kd = 0.0
Gyrokompensation = 0


#alles zu wifi
RcvWifiThread = wifi.RcvWifiModule()
#SendWifiThread = wifi.SendWifiModule()
#tcpHandlerClass = tcpHandler.tcpHandler()


motorcontrol = motorControl(PinEnMotorLeft, PinEnMotorRight, PinMotorlinksvorwaerts, PinMotorlinksrueckwaerts, PinMotorrechtsvorwaerts, PinMotorrechtsrueckwaerts)
EchoClass = Echo.Echo(PinEchoTrigger, PinEchoEcho)
GyroClass = gyro.gyro()

#Platzhalter für Klassen
PID_CONTROL_CLASS = None
SelfdrivingClass = None


print ("Main-Class INIT finished.")

try:
    while True:
        try:
            if(Kp == 0.0 and Ki == 0.0 and Kd == 0.0):
                if(RcvWifiThread.KonstantenReceived == True):
                    print("nKp: "+str(RcvWifiThread.Kp))
                    print("nKi: "+str(RcvWifiThread.Ki))
                    print("nKd: "+str(RcvWifiThread.Kd))
                    Kp = RcvWifiThread.Kp
                    Ki = RcvWifiThread.Ki
                    Kd = RcvWifiThread.Kd            
                  
                    #Klassen init
                    PID_CONTROL_CLASS = pid_control.pid_control(Kp, Ki, Kd, motorcontrol)
                    SelfdrivingClass = Selfdriving.selfdriving(GyroClass, Gyrokompensation, EchoClass, PID_CONTROL_CLASS)

                    print("Const. INIT finished.")

            if(RcvWifiThread.KonstantenReceived == True and Kp != 0.0 and Ki != 0.0 and Kd != 0.0):

                if(RcvWifiThread.neueDaten == True):
                    print("\nTargetSpeedFB: "+str(RcvWifiThread.targetSpeedFB)) #vorwaerts oder rueckwaerts je nach vorzeichen
                    print("\nRotateStrength: "+str(RcvWifiThread.rotateStrength)) #links oder rechts mit welcher Geschw. je nach Vorzeichen
                    #SendWifiThread.Smartphone_IP = RcvWifiThread.Smartphone_IP #IP setzen
                    RcvWifiThread.neueDaten = False #daten wurden verarbeitet, also kann RcvWifiThread wieder empfangen

                if(True):
                    #read gyroskop
                    GyroClass.read_gyro()

                    Distanz = EchoClass.Distanz #Debug
                    print("Debug Distanz: " + str(Distanz)) #Debug

                    speed = RcvWifiThread.targetSpeedFB
                    turn = RcvWifiThread.rotateStrength
                    PID_CONTROL_CLASS.reglung(GyroClass.x_rotation, speed, turn, Gyrokompensation)        

                else:
                    selfdrivingClass.drive()





        except Exception as e:
            print("Main-Error: "+str(e))
            GPIO.cleanup()
            break

except Exception as e:
    print("Main-Error: "+str(e))
    GPIO.cleanup()

finally:
    GPIO.cleanup()
        
