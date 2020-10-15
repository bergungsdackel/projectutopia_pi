from picamera import PiCamera
from time import sleep

i=0
camera=PiCamera()

def Bild_machen():
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    i=i+1
