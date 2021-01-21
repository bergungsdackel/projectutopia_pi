import time
import PID
import motorControl
import gyro


class pid_control(object):

    def __init__(self, Kp, Ki, Kd, motors : motorControl):
        self.Kp     =    Kp
        self.Ki     =    Ki
        self.Kd     =    Kd
        self.PID_CLASS = PID.PID(self.Kp, self.Ki, self.Kd)
        self.motors      =   motors
        self.speedlinks = 0
        self.speedrechts = 0
        print("Kp = {0}".format(self.Kp))
        print("Ki = {0}".format(self.Ki))
        print("Kd = {0}".format(self.Kd))
        print("pid_control iniziiert")

    def motoranpassung(self, x_rotation, speed, turn, Gyrokompensation:float, Kp: float, Ki: float, Kd: float):
        Sollwert = speed * 2
        #ich weiß nicht, ob das funktioniert, gegebenenfalls muss auch noch turn miteinbezogen werden
        #Der veränderte Sollwert soll dafür sorgen, das sich die Drohne nach vorne/hinten kippt, wenn man speed verwendet.
        #vielleicht würde es auch reichen, den Speed nur über den Sollwert für den Regler zu steuern, da er dadurch automatisch nach vorne/hinten fährt.

        
        self.PID_CLASS.pid(x_rotation, Sollwert, Gyrokompensation, Kp, Ki, Kd)
        geregelterWert = self.PID_CLASS.Ausgang
        return geregelterWert

    def selfrighting(self, x_rotation, Gyrokompensation: float):
        i=10000
        self.PID_CLASS.regelerror = True
        while (i != 0):
            self.motors.setSpeed(-15)
            i=i-1
        while (abs(x_rotation-Gyrokompensation) > 25):
            self.motors.setSpeed(15)
        if (abs(x_rotation-Gyrokompensation) < 30 ):
            self.PID_CLASS.regelerror = False
            

    def reglung(self, x_rotation, speed: int, turn: int, Gyrokompensation: float, Kp: float, Ki: float, Kd: float):

        #self.PID_CLASS.pid(x_rotation)

        #geregelterWert = self.PID_CLASS.Ausgang
        if(self.PID_CLASS.regelerror == False):
           print ("speed: %d" % speed)
           if (turn < 0 and speed > 0):
                self.speedlinks = max(0, speed + turn)
                self.speedrechts = speed
           elif (turn > 0 and speed > 0):
                self.speedrechts = max(0, speed - turn)
                self.speedlinks = speed
           elif (turn < 0 and speed < 0):
                self.speedlinks = -max(0, abs(speed - turn))
                self.speedrechts = speed
           elif (turn > 0 and speed < 0):
                self.speedrechts = -max(0, abs(speed + turn))
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


           motoranpassung = self.motoranpassung(x_rotation, speed, turn, Gyrokompensation, Kp, Ki, Kd)
           #motoranpassung = 0
           print("Speedlinks %d" % (self.speedlinks + motoranpassung))
           print("Speedrechts %d" % (self.speedrechts + motoranpassung))

           self.motors.setSpeedL(self.speedlinks + motoranpassung)
           self.motors.setSpeedR(self.speedrechts + motoranpassung)
            
        else:
           self.selfrighting(x_rotation, Gyrokompensation)


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
