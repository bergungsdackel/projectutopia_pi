import Echo
import pid_control
import gyro
import motorControl

class SELFDRIVING(object):
  
    def __init__(self, GyroClass: gyro, Gyrokompensation, EchoClass: Echo, PidClass: pid_control):
    
        #übergebene Klassen
        self.ECHO_CLASS = EchoClass
        self.PID_CONTROL_CLASS = PidClass
        self.GYRO_CLASS = GyroClass
    
        #übergebene Variablen
        self.gyrokompensation = Gyrokompensation


    def detect(self):

        if(self.ECHO_CLASS.Distanz < 40):
            return True
        else:
            return False
      

    def drive(self):

        if(self.detect()==False):
            self.PID_CONTROL_CLASS.reglung(self.GYRO_CLASS.x_rotation, 5, 0, self.gyrokompensation)
        else:
            self.PID_CONTROL_CLASS.reglung(self.GYRO_CLASS.x_rotation, 1, 1, self.gyrokompensation)
