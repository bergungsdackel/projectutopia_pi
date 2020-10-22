import threading
import socket
import time


class WifiModule(threading.Thread):

    neueDaten = None
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = None
    data = None
    targetSpeedFB = None
    rotateStrength = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        neueDaten = False
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))
        self.start()
        print("Wifi iniziiert")

    def run(self):
        print("Warte auf Daten von Smartphone...")
        while True:

            if(neueDaten == False):

                self.data, self.addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
                print("received message: %s" % self.data)
                print("received from: %s" % self.addr)

                if(self.data != None):
                    lesbarerString = self.data.decode("utf-8")
                    strengthL, directionL, strengthR, directionR = lesbarerString.split("|")

                    if(directionL == "F"):
                        targetSpeedFB = strengthL
                    elif(directionL == "B"):
                        targetSpeedFB = -(strengthL)
                    if(directionR == "L"):
                        rotateStrength = strengthR #-10 ist links
                    elif(directionR == "R"):
                        rotateStrength = -(strengthR)

                    neueDaten = True

                time.sleep(0.005) #kurz warten bis neue Daten ankommen
               