import time
import PID
import motorControl
import gyro


class pid_control(object):

    def __init__(self, Kp, Ki, Kd, motors : motorControl):
        self.Kp     =    Kp
        self.Ki     =    Ki
        self.Kd     =    Kd
        self.PID_CLASS = PID.PID(Kp,Ki,Kd)
        self.motors      =   motors
        self.speedlinks = 0
        self.speedrechts = 0
        print("Kp = {0}".format(self.Kp))
        print("Ki = {0}".format(self.Ki))
        print("Kd = {0}".format(self.Kd))
        print("pid_control iniziiert")

    def motoranpassung(self, x_rotation, sollwert):
        #ich weiß nicht, ob das funktioniert, gegebenenfalls muss auch noch turn miteinbezogen werden
        #Der veränderte Sollwert soll dafür sorgen, das sich die Drohne nach vorne/hinten kippt, wenn man speed verwendet.
        #vielleicht würde es auch reichen, den Speed nur über den Sollwert für den Regler zu steuern, da er dadurch automatisch nach vorne/hinten fährt.

        
        self.PID_CLASS.pid(x_rotation, sollwert)
        geregelterWert = self.PID_CLASS.Ausgang
        return geregelterWert



    def reglung (self, x_rotation, speed: int, turn: int) :

        #self.PID_CLASS.pid(x_rotation)

        #geregelterWert = self.PID_CLASS.Ausgang
       Sollwert = speed * 3

       #print("Speedlinks %d" % self.speedlinks)
       #print("Speedrechts %d" % self.speedrechts)
       motoranpassung = self.motoranpassung(x_rotation, Sollwert)
       self.motors.setSpeedL(motoranpassung + turn/2)
       self.motors.setSpeedR(motoranpassung - turn/2)

       
#        if(not self.motors.drivingForward and not self.motors.drivingBackward and not self.motors.drivingLeft and not self.motors.drivingRight) :
#            print("balance mode")
#            if(gergeregelterWert == 0):
#                self.motors.setspeed(0)
#            elif (geregelterWert > 1):
#                self.motors.forward(2)
#            elif (geregelterWert < 1):
#                self.motors.backward(-2)
#
#        elif(self.motors.drivingForward and not self.motors.drivingBackward and not self.motors.drivingLeft and not self.motors.drivingRight):
#            #drive forward
#            print("pid driving forward")
#
#        elif(not self.motors.drivingForward and self.motors.drivingBackward and not self.motors.drivingLeft and not self.motors.drivingRight):
#            #drive backward
#            print("pid driving backward")
#
#        elif(not self.motors.drivingForward and not self.motors.drivingBackward and not self.motors.drivingLeft and self.motors.drivingRight):
#            #drive right
#            print("pid driving right")
#
#        elif(not self.motors.drivingForward and not self.motors.drivingBackward and self.motors.drivingLeft and not self.motors.drivingRight):
#             #drive left
#             print("pid driving left")
#
#        else:
#            #Balance
#            print("balance mode")
#            if(gergeregelterWert==0):
#                self.motors.setspeed(0)
#            elif (geregelterWert>1):
#                self.motors.forward(2)
#            elif (geregelterWert<1):
#                self.motors.backward(-2)
