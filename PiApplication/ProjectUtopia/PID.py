import time

class PID(object):

    def __init__(self, Kp:float, Ki:float, Kd:float):
        self.Kp=Kp
        self.Ki=Ki
        self.Kd=Kd

        self.Buffer = 0.0
        self.Eingang_vorher = 0.0
        self.zeitfüreinendurchlauf = 0.00009
        self.Ausgang = 0.0
        self.Regeldifferenz = 0.0
        self.Regeldifferenz_vorher = 0.0


        print("PID iniziiert")
        
    def pid(self,Eingang):
        self.Regeldifferenz = Eingang - self.Ausgang
        self.Buffer = self.Regeldifferenz * self.zeitfüreinendurchlauf + self.Buffer
        self.Ausgang = self.Kp * self.Regeldifferenz + self.Ki * self.Buffer  + self.Kd * ((self.Regeldifferenz - self.Regeldifferenz_vorher) / self.zeitfüreinendurchlauf)
        self.Regeldifferenz_vorher = self.Regeldifferenz
        print("Ausgang = %f" % self.Ausgang)

