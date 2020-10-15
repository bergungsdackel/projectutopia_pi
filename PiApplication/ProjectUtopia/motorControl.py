import RPi.GPIO as GPIO

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

    def setSpeedL(self, speed: int):
        """
            speed might be -3, -2, -1, 0, 1, 2, 3
        """
        force = min(3, abs(speed))
        isForewards = speed > 0
        if (isForewards):
            GPIO.output(self.inBackwardPinL, False)
            GPIO.output(self.inForewardPinL, True)
        else:
            GPIO.output(self.inForewardPinL, False)
            GPIO.output(self.inBackwardPinL, force > 0)
        if force > 0:
            self.pwmL.ChangeDutyCycle(70 + (10 * force))
        else:
            self.pwmL.ChangeDutyCycle(0)
        
    def setSpeedR(self, speed: int):
        """
            speed might be -3, -2, -1, 0, 1, 2, 3
        """
        force = min(3, abs(speed))
        isForewards = speed > 0
        if (isForewards):
            GPIO.output(self.inBackwardPinR, False)
            GPIO.output(self.inForewardPinR, True)
        else:
            GPIO.output(self.inForewardPinR, False)
            GPIO.output(self.inBackwardPinR, force > 0)
        if force > 0:
            self.pwmR.ChangeDutyCycle(70 + (10 * force))
        else:
            self.pwmR.ChangeDutyCycle(0)

    def setSpeed(speed: int):
        setSpeedL(speed)
        setSpeedR(speed)

    def turnLeft(speed: int):
        setSpeedL(0)
        setSpeedR(speed)

    def turnRight(speed: int):
        setSpeedR(0)
        setSpeedL(speed)

    def forward(speed):
        if(speed > 0):
            setSpeed(speed)

    def backward(speed):
        if(speed < 0):
            setSpeed(speed)

    def stopp():
        setSpeed(0)