import Echo
import pid_control
import gyro
import motorControl

class selfdriving(object):
  
  def __init__(self, motors: motorControl, gyroClass: gyro, Gyrokompensation, EchoClass: Echo, PID_CLASS: pid_control, Kp:float, Ki:float, Kd:float):
    self.Echo = EchoClass
    self.motors = motors
    self.PID_CONTROL_CLASS = PID_CLASS
    self.GYRO_CLASS = gyroClass

    self.Objdetectet = False
    self.Kp = Kp
    self.Ki = Ki
    self.Kd = Kd
    
  def detect(self):
    if(self.Echo.Distanz < 40):
      self.Objectdetectet = True
    else:
      self.Objectdetectet = False
      
  def drive(self, Kp, Ki, Kd):
    self.detect()
    if(self.Objectdetectet==False):
      PID_CONTROL_CLASS.reglung(self.GYRO_CLASS.x_rotation, 5, 0, Gyrokompensation, Kp, Ki, Kd)
    if(self.Objectdetectet==True):
      PID_CONTROL_CLASS.reglung(self.GYRO_CLASS.x_rotation, 1, 1, Gyrokompensation, Kp, Ki, Kd)
