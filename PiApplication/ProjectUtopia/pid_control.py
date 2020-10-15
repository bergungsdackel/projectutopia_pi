import time
import PID
import motorControl
import ProjectUtopia


class pid_control(object):


    PID.PID.init(1,2,3)
    def reglung(eingang1, eingang2):
        PID.PID.pid(eingang)
        geregelterWert = PID.PID.Ausgang
        if (geregelterWert < 0.5 and geregelterWert > 0):
            motorContol.forward(1)
        if (geregelterWert > -0.5 and geregelterWert < 0):
            motorContol.backward(-1)
        if (geregelterWert < 1 and geregelterWert > 0.5):
            motorContol.forward(2)
        if (geregelterWert > -1 and geregelterWert < -0.5):
            motorContol.backward(-2)
        if (geregelterWert < 1.5 and geregelterWert > 1):
            motorContol.forward(3)
        if (geregelterWert > -1.5 and geregelterWert < -1):
            motorContol.backward(-3)
