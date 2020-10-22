import time
import PID
import motorControl
import ProjectUtopia
import gyro


class pid_control(object):

    def init(Kp, Ki, Kd, motors : motorControl, self):#self am ende, damit man werte übergeben kann?
        self.Kp     =    Kp
        self.Ki     =    Ki
        self.kd     =    Kd
        PID.PID.init(Kp,Ki,Kd)
        motors      =   motors
        print("Kp = ")
        print("Ki = ")
        print("Kd = ")
        print("pid_control iniziiert")


    def reglung (self, x_rotation) :
        PID.PID.pid(x_rotation)
        geregelterWert = PID.PID.Ausgang

        if(not motors.drivingForward and not motors.drivingBackward and not motors.drivingLeft and not motors.drivingRight) :
            print('balance mode')
            if(gergeregelterWert==0):
                motors.setspeed(0)
            elif (geregelterWert>1):
                motors.forward(2)
            elif (geregelterWert<1):
                motors.backward(-2)
        elif(motors.drivingForward and not motors.drivingBackward and not motors.drivingLeft and not motors.drivingRight):
            #drive forward
            print('pid driving forward')
        elif(not motors.drivingForward and motors.drivingBackward and not motors.drivingLeft and not motors.drivingRight):
            #drive backward
            print('pid driving backward')
        elif(not motors.drivingForward and not motors.drivingBackward and not motors.drivingLeft and motors.drivingRight):
            #drive right
            print('pid driving right')
        elif(not motors.drivingForward and not motors.drivingBackward and motors.drivingLeft and not motors.drivingRight):
             #drive left
             print('pid driving left')
        else:
            #Balance
            print('balance mode')
            if(gergeregelterWert==0):
                motors.setspeed(0)
            elif (geregelterWert>1):
                motors.forward(2)
            elif (geregelterWert<1):
                motors.backward(-2)