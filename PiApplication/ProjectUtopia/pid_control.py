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
        print("Kp = {0}".format(self.Kp))
        print("Ki = {0}".format(self.Ki))
        print("Kd = {0}".format(self.Kd))
        print("pid_control iniziiert")


    def reglung (self, x_rotation) :

        self.PID_CLASS.pid(x_rotation)

        geregelterWert = self.PID_CLASS.Ausgang

        if(not self.motors.drivingForward and not self.motors.drivingBackward and not self.motors.drivingLeft and not self.motors.drivingRight) :
            print("balance mode")
            if(gergeregelterWert == 0):
                self.motors.setspeed(0)
            elif (geregelterWert > 1):
                self.motors.forward(2)
            elif (geregelterWert < 1):
                self.motors.backward(-2)

        elif(self.motors.drivingForward and not self.motors.drivingBackward and not self.motors.drivingLeft and not self.motors.drivingRight):
            #drive forward
            print("pid driving forward")

        elif(not self.motors.drivingForward and self.motors.drivingBackward and not self.motors.drivingLeft and not self.motors.drivingRight):
            #drive backward
            print("pid driving backward")

        elif(not self.motors.drivingForward and not self.motors.drivingBackward and not self.motors.drivingLeft and self.motors.drivingRight):
            #drive right
            print("pid driving right")

        elif(not self.motors.drivingForward and not self.motors.drivingBackward and self.motors.drivingLeft and not self.motors.drivingRight):
             #drive left
             print("pid driving left")

        else:
            #Balance
            print("balance mode")
            if(gergeregelterWert==0):
                self.motors.setspeed(0)
            elif (geregelterWert>1):
                self.motors.forward(2)
            elif (geregelterWert<1):
                self.motors.backward(-2)