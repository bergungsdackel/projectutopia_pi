import picamera
from time import sleep


class camera(object):
    
    def __init__(self):
        self.PiCamera = picamera.PiCamera()
        print("Kamera iniziiert")
        self.AufnahmezeitInSekunden = 5

    def Bild_machen():
        self.PiCamera.capture('/home/pi/Desktop/image%s.jpg' % i)
        i=i+1

    def Video_machen():
        #Video der Länge 5 Sekunden
        self.PiCamera.resolution = (1920, 1080)
        self.PiCamera.start_recording('test.h264')
        self.PiCamera.wait_recording(AufnahmezeitInSekunden)
        self.PiCamera.stop_recording()
