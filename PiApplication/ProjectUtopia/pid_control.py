import time
import RPi.GPIO as GPIO
import PID
import ProjectUtopia
class pid_control(object):
    #def BasisKonfiguration():
    #    GPIO.setmode(GPIO.BCM)
    #    GPIO.setup(PinMotorlinksvorwaerts, GPIO.OUT)
    #    GPIO.setmode(GPIO.BCM)
    #    GPIO.setup(PinMotorrechtsvorwaerts, GPIO.OUT)
    #    GPIO.setmode(GPIO.BCM)
    #    GPIO.setup(PinMotorlinksrueckwaerts, GPIO.OUT)
    #    GPIO.setmode(GPIO.BCM)
    #    GPIO.setup(PinMotorrechtsrueckwaerts, GPIO.OUT)

    #def links_vorwaerts(sleepTime):
    #    GPIO.output(Pinmotorlinksvorwaerts,GPIO.HIGH)
    #    time.sleep(sleepTime)
    #    GPIO.output(Pinmotorlinksvorwaerts,GPIO.LOW)

    #def links_rueckwaerts(sleepTime):
    #    GPIO.output(Pinmotorlinksrueckwaerts,GPIO.HIGH)
    #    time.sleep(sleepTime)
    #    GPIO.output(Pinmotorlinksrueckwaerts,GPIO.LOW)

    #def rechts_vorwaerts(sleepTime):
    #    GPIO.output(Pinmotorrechtsvorwaerts,GPIO.HIGH)
    #    time.sleep(sleepTime)
    #    GPIO.output(Pinmotorrechtsvorwaerts,GPIO.LOW)

    #def rechts_rueckwaerts(sleepTime):
    #    GPIO.output(Pinmotorrechtssrueckwaerts,GPIO.HIGH)
    #    time.sleep(sleepTime)
    #    GPIO.output(Pinmotorrechtsrueckwaerts,GPIO.LOW)

    PID.PID.init(1,2,3)
    def reglung():
        PID.PID.pid(eingang)


 
    def __init__(self, enPin: int, inForewardPin: int, inBackwardPin: int):
        GPIO.setup(inForewardPin, GPIO.OUT)
        self.inForewardPin = inForewardPin
        GPIO.output(inForewardPin, False)
 
        self.inBackwardPin = inBackwardPin
        GPIO.setup(inBackwardPin, GPIO.OUT)
        GPIO.output(inBackwardPin, False)
 
        GPIO.setup(enPin, GPIO.OUT)
        self.pwm = GPIO.PWM(enPin, 100)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(0)
 
    def setSpeed(self, speed: int):
        """
            speed might be -3, -2, -1, 0, 1, 2, 3
        """
        force = min(3, abs(speed))
        isForewards = speed > 0
        if (isForewards):
            GPIO.output(self.inBackwardPin, False)
            GPIO.output(self.inForewardPin, True)
        else:
            GPIO.output(self.inForewardPin, False)
            GPIO.output(self.inBackwardPin, force > 0)
        if force > 0:
            self.pwm.ChangeDutyCycle(70 + (10 * force))
        else:
            self.pwm.ChangeDutyCycle(0)