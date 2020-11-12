import threading
import socket
import time

class WifiModule(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

        #VAR INIT
        self.UDP_IP = ""
        self.UDP_PORT = 12345
        self.sock = None
        self.data = None
        self.targetSpeedFB = 0
        self.rotateStrength = 0

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP,self.UDP_PORT))
        self.start()

        print("Wifi iniziiert")

    def run(self):

        global neueDaten
        neueDaten = False

        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print("Eigene IP: " + local_ip)
        print("Warte auf Daten von Smartphone...")
        while True:

            if(neueDaten == False):

                self.data, (self.ip, self.port) = self.sock.recvfrom(1024) # buffer size is 1024 bytes
                print("received message: %s" % self.data)
                print("received from: {0}:{1}".format(str(self.ip), str(self.port)))

                if(self.data != None):
                    length = len(self.data)

                    if(length == 4 or length == 8):
                        print("Schicke {0} Bytes zurück an {1}:{2}".format(length, self.ip, self.port))
                        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        sock.sendto(self.data, (self.ip, self.port))
                        neueDaten = True
                    elif(self.data.decode("utf-8").count("|") == 3):

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
                    else:
                        error = True;
               