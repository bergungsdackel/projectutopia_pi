import time

from PID import PID
from MotorControl import MOTOR_CONTROL


class PID_CONTROL(object):

    def __init__(self, MotorControlClass: MOTOR_CONTROL, Kp, Ki, Kd):

        #übergebene Variablen
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.speedleft = 0
        self.speedright = 0

        #übergebene Klassen
        self.PID_CLASS = PID(self.Kp, self.Ki, self.Kd)
        self.MOTOR_CONTROL_CLASS = MotorControlClass
        
        #debug:
        print("Kp = {0}".format(self.Kp))
        print("Ki = {0}".format(self.Ki))
        print("Kd = {0}".format(self.Kd))
        print("pid_control iniziiert")


    def motor_adj(self, x_rotation, speed, turn, Gyrokompensation:float):
      
        #ich weiß nicht, ob das funktioniert, gegebenenfalls muss auch noch turn miteinbezogen werden
        #Der veränderte Sollwert soll dafür sorgen, das sich die Drohne nach vorne/hinten kippt, wenn man speed verwendet.
        #vielleicht würde es auch reichen, den Speed nur über den Sollwert für den Regler zu steuern, da er dadurch automatisch nach vorne/hinten fährt.
        sollwert = speed * 2

        geregelterWert = self.PID_CLASS.pid(x_rotation, sollwert, Gyrokompensation) #PID_CLASS.pid gibt Ausgang zurück
        return geregelterWert


    def selfrighting(self, x_rotation, Gyrokompensation: float):

        i=1000

        while (i != 0):
            self.MOTOR_CONTROL_CLASS.setSpeed(-15)
            i=i-1
        while (abs(x_rotation - Gyrokompensation) > 25):
            self.MOTOR_CONTROL_CLASS.setSpeed(15)

        if (abs(x_rotation - Gyrokompensation) < 30 ):
            self.PID_CLASS.regelerror = False
            

    def control(self, x_rotation, speed: int, turn: int, Gyrokompensation: float):

        if(self.PID_CLASS.controlError):
           print ("speed: %d" % speed)
           if (turn < 0 and speed > 0):
                self.speedleft = max(0, speed + turn)
                self.speedright = speed
           elif (turn > 0 and speed > 0):
                self.speedright = max(0, speed - turn)
                self.speedleft = speed
           elif (turn < 0 and speed < 0):
                self.speedleft = -max(0, abs(speed - turn))
                self.speedright = speed
           elif (turn > 0 and speed < 0):
                self.speedright = -max(0, abs(speed + turn))
                self.speedleft = speed
           elif (speed == 0 and turn != 0):
                self.speedleft = turn
                self.speedright = -turn
           elif (turn == 0 and speed != 0):
                self.speedleft = speed
                self.speedright = speed
           else:
                self.speedleft = 0
                self.speedright = 0


           motoranpassung = self.motor_adj(x_rotation, speed, turn, Gyrokompensation)
           #motoranpassung = 0
           print("Speedleft %d" % (self.speedleft + motoranpassung))
           print("Speedright %d" % (self.speedright + motoranpassung))

           self.MOTOR_CONTROL_CLASS.setSpeedL(self.speedleft + motoranpassung)
           self.MOTOR_CONTROL_CLASS.setSpeedR(self.speedright + motoranpassung)
            
        else:
           self.selfrighting(x_rotation, Gyrokompensation)
