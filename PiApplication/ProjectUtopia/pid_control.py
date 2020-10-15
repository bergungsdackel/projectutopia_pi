import time
import PID
import motorControl
import ProjectUtopia


class pid_control(object):


    PID.PID.init(1,2,3)
    def reglung(eingang1, eingang2):
        PID.PID.pid(eingang)
        geregelterWert = PID.PID.Ausgang
        if (geregelterWert>1):
            motorContol.forward(2)
        if (geregelterWert<1):
            motorContol.backward(-2)
