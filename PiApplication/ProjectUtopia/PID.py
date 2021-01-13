import time

class PID(object):

    def __init__(self):
        self.Kp=Kp
        self.Ki=Ki
        self.Kd=Kd

        self.Buffer = 0.0
        self.Eingang_vorher = 0.0
        self.zeitfüreinendurchlauf = 0.00009
        self.Ausgang = 0.0
        self.Regeldifferenz = 0.0
        self.Regeldifferenz_vorher = 0.0
        self.maxBuffer = 100.0
        self.maxAusgang = 30.0
        self.regelerror = False

        print("PID iniziiert")
        
    def pid(self, Eingang, Sollwert, Gyrokompensation:float, Kp:float, Ki:float, Kd:float):
        kompEingang = Eingang-Gyrokompensation
        self.Regeldifferenz = Sollwert - self.Ausgang
        self.Buffer = self.Regeldifferenz * self.zeitfüreinendurchlauf + self.Buffer
        self.Ausgang = kompEingang + self.Ausgang + self.Kp * self.Regeldifferenz + self.Ki * self.Buffer  + self.Kd * ((self.Regeldifferenz - self.Regeldifferenz_vorher) / self.zeitfüreinendurchlauf)
        self.Regeldifferenz_vorher = self.Regeldifferenz
        print("Ausgang = %f" % self.Ausgang)
        if(Buffer > self.maxBuffer):
            Buffer = self.maxBuffer
        if(Buffer < -self.maxBuffer):
            Buffer = -self.maxBuffer
        if(abs(self.Ausgang) > abs(self.maxAusgang)):
            self.regelerror = True
