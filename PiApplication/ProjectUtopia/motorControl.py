

class motorControl(object):

    inForewardPinL = None
    inForewardPinR = None
    inBackwardPinL = None
    inBackwardPinR = None
    enPinR = None
    enPinL = None
    pwmL = None
    pwmR = None

    def __init__(self, enPinL: int,enPinR: int, inForewardPinL: int, inBackwardPinL: int,inForewardPinR: int, inBackwardPinR: int):
        GPIO.setup(inForewardPinL, GPIO.OUT)
        self.inForewardPinL = inForewardPinL
        GPIO.output(inForewardPinL, False)
 
        self.inBackwardPinL = inBackwardPinL
        GPIO.setup(inBackwardPinL, GPIO.OUT)
        GPIO.output(inBackwardPinL, False)
 
        GPIO.setup(enPinL, GPIO.OUT)

        GPIO.setup(inForewardPinR, GPIO.OUT)
        self.inForewardPinR = inForewardPinR
        GPIO.output(inForewardPinL, False)
 
        self.inBackwardPinR = inBackwardPinR
        GPIO.setup(inBackwardPinR, GPIO.OUT)
        GPIO.output(inBackwardPinR, False)
 
        GPIO.setup(enPinR, GPIO.OUT)

        self.pwmL = GPIO.PWM(enPinL, 100)
        self.pwmR = GPIO.PWM(enPinR, 100)
        self.pwmL.start(0)
        self.pwmR.start(0)
        self.pwmL.ChangeDutyCycle(0)
        self.pwmR.ChangeDutyCycle(0)

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

