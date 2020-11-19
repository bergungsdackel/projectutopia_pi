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
    drivingForward = False
    drivingBackward = False
    drivingLeft = False
    drivingRight = False

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
        print("motorcontrol iniziiert")


    def setSpeedL(self, speed: int):
        """
            speed might be -15...+15
        """
        print("linksspeed:%d" % speed)
        force = min(15, abs(speed))
        if (speed > 0):
            GPIO.output(self.inBackwardPinL, False)
            print("inBackwardspinL:False")
            GPIO.output(self.inForewardPinL, True)
            print("inForewardspinL:True")
        elif (speed < 0):
            GPIO.output(self.inForewardPinL, False)
            print("inForewardspinL:False")
            GPIO.output(self.inBackwardPinL, True)
            print("inBackwardspinL:True")
        else:
            GPIO.output(self.inForewardPinL, False)
            print("inForewardspinL:False")
            GPIO.output(self.inBackwardPinL, False)
            print("inBackwardspinL:False")

        if force > 0:
            self.pwmL.ChangeDutyCycle(10 + 6 * force)
            print("pwm")
            print(10+6*force)
        else:
            self.pwmL.ChangeDutyCycle(0)
        
    def setSpeedR(self, speed: int):
        """
            speed might be -15...+15
        """
        print("rechtsspeed:%d" % speed)
        force = min(15, abs(speed))

        if (speed > 0):
            GPIO.output(self.inBackwardPinR, False)
            print("inBackwardspinR:False")
            GPIO.output(self.inForewardPinR, True)
            print("inForewardspinR:True")
        elif (speed < 0):
            GPIO.output(self.inForewardPinR, False)
            print("inForewardspinR:False")
            GPIO.output(self.inBackwardPinR, True)
            print("inBackwardspinR:True")
        else:
            GPIO.output(self.inForewardPinR, False)
            print("inForewardspinR:False")
            GPIO.output(self.inBackwardPinR, False)
            print("inBackwardspinR:False")

        if force > 0:
            self.pwmR.ChangeDutyCycle(10 + 6 * force)
            print("pwm")
            print(10+6*force)
        else:
            self.pwmR.ChangeDutyCycle(0)

    def setSpeed(speed: int):
        setSpeedL(speed)
        setSpeedR(speed)
        print("Geschwindigkeit auf %f" % speed)


    def turnLeft(speed: int):
        drivingForward = False
        drivingBackward = False
        drivingLeft = True
        drivingRight = False
        setSpeedL(0)
        setSpeedR(speed)
        print("links drehen")


    def turnRight(speed: int):
        drivingForward = False
        drivingBackward = False
        drivingLeft = False
        drivingRight = True
        setSpeedR(0)
        setSpeedL(speed)
        print("rechts drehen")

    def forward(speed: int):
        if(speed > 0):
            drivingForward = True
            drivingBackward = False
            drivingLeft = False
            drivingRight = False
            setSpeed(speed)
            print("Vorwaerts")

    def backward(speed: int):
        if(speed < 0):
            drivingForward = False
            drivingBackward = True
            drivingLeft = False
            drivingRight = False
            setSpeed(speed)
            print("Rueckwaerts")

    def stopp():
        setSpeed(0)
