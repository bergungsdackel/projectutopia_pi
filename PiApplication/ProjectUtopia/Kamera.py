import picamera
from time import sleep


class camera(object):
    
    def __init__(self):
        self.PiCamera = picamera.PiCamera()
        print("Kamera iniziiert")
        self.i = 0

    def Bild_machen(self):
        self.PiCamera.capture('/home/pi/Desktop/image%s.jpg' % self.i)
        self.i = self.i + 1

    def Video_machen(self, AufnahmezeitInSekunden):
        #Video der Länge 5 Sekunden
        self.PiCamera.resolution = (1920, 1080)
        self.PiCamera.start_recording('test%s.h264' % self.i)
        self.PiCamera.wait_recording(AufnahmezeitInSekunden)
        self.PiCamera.stop_recording()
        self.i = self.i+1