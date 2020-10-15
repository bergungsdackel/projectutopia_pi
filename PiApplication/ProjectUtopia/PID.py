import time

class PID(object):
    Kp = 0
    Ki = 0
    Kd = 0
    Buffer = 0
    Eingang_vorher = 0
    zeitfüreinendurchlauf = 2
    Ausgang = 0
    Regeldifferenz = 0
    Regeldifferenz_vorher = 0

    def init(Kp,Ki,Kd):
        Kp=Kp
        Ki=Ki
        Kd=Kd
    def pid(Eingang):
        Regeldifferenz = Eingang-Ausgang
        Buffer = Regeldifferenz+Buffer
        Ausgang = Kp*Regeldifferenz+Ki*Buffer+Kd*((Regeldifferenz-Regeldifferenz_vorher)/2)
        Regeldifferenz_vorher = Regeldifferenz

