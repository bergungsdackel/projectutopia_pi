import time
import PID
import motorControl
import ProjectUtopia
import gyro


class pid_control(object):

    def __init__(self, Kp, Ki, Kd, motors : motorControl):#self am ende, damit man werte übergeben kann?
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

    def motoranpassung(self, x_rotation):
        self.PID_CLASS.pid(x_rotation)
        geregelterWert = self.PID_CLASS.Ausgang
        return geregelterWert



    def reglung (self, x_rotation, speed, turn) :

        #self.PID_CLASS.pid(x_rotation)

        #geregelterWert = self.PID_CLASS.Ausgang

       if (turn < 0 and speed > 0):
            self.speedlinks = max(0,speed + turn)
            self.speedrechts = speed
        elif (turn > 0 and speed > 0):
            self.speedrechts = max(0,speed - turn)
            self.speedlinks = speed
        elif (turn < 0 and speed < 0):
            self.speedlinks = min(0,speed - turn)
            self.speedrechts = speed
        elif (turn > 0 and speed < 0):
            self.speedrechts = min(0, speed + turn)
            self.speedlinks = speed
        elif (speed == 0 and turn != 0):
            self.speedlinks = turn
            self.speedrechts = -turn
        elif (turn == 0 and speed != 0):
            self.speedlinks = speed
            self.speedrechts = speed
        else:
            self.speedlinks = 0
            self.speedrechts = 0

        print("Speedlinks %d" % self.speedlinks)
        print("Speedrechts %d" % self.speedrechts)

        self.motors.motorControl.setSpeedL(self, self.speedlinks + self.motoranpassung(x_rotation))
        self.motors.motorControl.setSpeedR(self, self.speedrechts + self.motoranpassung(x_rotation))

       
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