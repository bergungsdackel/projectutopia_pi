import time

class PID(object):

    def __init__(self, Kp:float, Ki:float, Kd:float):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

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
        
    def pid(self, Eingang, Sollwert, Gyrokompensation:float):

        kompEingang = Eingang - Gyrokompensation
        self.Regeldifferenz = Sollwert - self.Ausgang
        self.Buffer = self.Regeldifferenz * self.zeitfüreinendurchlauf + self.Buffer
        self.Ausgang = kompEingang + self.Ausgang + self.Kp * self.Regeldifferenz + self.Ki * self.Buffer  + self.Kd * ((self.Regeldifferenz - self.Regeldifferenz_vorher) / self.zeitfüreinendurchlauf)
        self.Regeldifferenz_vorher = self.Regeldifferenz
        print("Ausgang = %f" % self.Ausgang)
        if(self.Buffer > self.maxBuffer):
            self.Buffer = self.maxBuffer
        if(self.Buffer < -self.maxBuffer):
            self.Buffer = -self.maxBuffer
        if(self.Ausgang > self.maxAusgang):
            self.Ausgang = self.maxAusgang
            self.regelerror = True
        if(self.Ausgang < -self.maxAusgang):
            self.Ausgang = -self.maxAusgang
            self.regelerror = True

        return self.Ausgang
