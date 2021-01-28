import Echo
import pid_control
import gyro
import motorControl

class selfdriving(object):
  
  def __init__(self, gyroClass: gyro, Gyrokompensation, EchoClass: Echo, PidClass: pid_control, Kp:float, Ki:float, Kd:float):
    
    #übergebene Klassen
    self.ECHO_CLASS = EchoClass
    self.PID_CONTROL_CLASS = PidClass
    self.GYRO_CLASS = gyroClass
    
    #übergebene Variablen
    self.gyrokompensation = Gyrokompensation
    self.Kp = Kp
    self.Ki = Ki
    self.Kd = Kd

    #neue Variablen
    self.objdetectet = False

  def detect(self):
    if(self.ECHO_CLASS.Distanz < 40):
      self.objectdetected = True
    else:
      self.objectdetected = False
      
  def drive(self, Kp, Ki, Kd):
    self.detect()
    if(self.objectdetectet==False):
      self.PID_CONTROL_CLASS.reglung(self.GYRO_CLASS.x_rotation, 5, 0, self.gyrokompensation, Kp, Ki, Kd)
    if(self.objectdetectet==True):
      self.PID_CONTROL_CLASS.reglung(self.GYRO_CLASS.x_rotation, 1, 1, self.gyrokompensation, Kp, Ki, Kd)
