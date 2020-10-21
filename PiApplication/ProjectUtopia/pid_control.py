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


    def reglung(self, x_rotation):
        PID.PID.pid(x_rotation)
        geregelterWert = PID.PID.Ausgang
        if (geregelterWert>1):
            motorContol.forward(2)
        if (geregelterWert<1):
            motorContol.backward(-2)
