import Echo
import pid_control
import gyro

class selfdriving(object):
  
  def __init__(self, motors: motorcontrol, gyro: gyro, Gyrokompensation, Kp:float, Ki:float, Kd:float,):
    self.Echo = Echo.Echo()
    self.motors = motors
    self.PID_CONTROL_CLASS = pid_control.pid_control(Kp,Ki,Kd,motors)
    
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
      PID_CONTROL_CLASS.reglung(gyro.x_rotation, 5, 0, Gyrokompensation, Kp, Ki, Kd)
    if(self.Objectdetectet==True):
      PID_CONTROL_CLASS.reglung(gyro.x_rotation, 1, 1, Gyrokompensation, Kp, Ki, Kd)
