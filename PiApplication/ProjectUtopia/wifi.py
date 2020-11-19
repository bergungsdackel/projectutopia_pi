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
        self.PING_PORT = 12346
        self.sock = None
        self.data = None
        self.targetSpeedFB = 0
        self.rotateStrength = 0
        self.neueDaten = False
        self.error = False

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP,self.UDP_PORT))
        self.start()

        print("\nWifi iniziiert")

    def run(self):

        #global neueDaten
        #neueDaten = False

        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print("\nEigene IP: " + local_ip)
        print("\nWarte auf erste Daten von Smartphone...")
        while True:

            if(self.neueDaten == False):

                #start = float(time.process_time()) #debug zeitmessung

                self.data, (self.ip, self.port) = self.sock.recvfrom(1024) # buffer size is 1024 bytes

                #print("received message: %s" % self.data)
                #print("received from: {0}:{1}".format(str(self.ip), str(self.port)))

                if(self.data != None):
                    length = len(self.data)

                    try:

                        if(length == 4 or length == 6):
                            print("\nSchicke {0} Bytes zurück an {1}:{2}".format(length, self.ip, self.PING_PORT))
                            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            sock.sendto(self.data, (self.ip, self.PING_PORT))
                            self.neueDaten = False
                        elif(self.data.decode("utf-8").count("|") == 3):

                            lesbarerString = self.data.decode("utf-8")
                            strengthL, directionL, strengthR, directionR = lesbarerString.split("|")

                            #print("stengthL: " + strengthL + ", directionL: " + directionL + ", strengthR: " + strengthR + ", directionR: " + directionR)

                            self.targetSpeedFB = int(strengthL)
                            self.rotateStrength = int(strengthR)

                            #if(directionL == "F"):
                            #    self.targetSpeedFB = int(strengthL)
                            #elif(directionL == "B"):
                            #    self.targetSpeedFB = int(strengthL)
                            #if(directionR == "L"):
                            #    self.rotateStrength = int(strengthR) #-10 ist links
                            #elif(directionR == "R"):
                            #    self.rotateStrength = int(strengthR)

                            #print("\nDurchlaufdauer: " + str(float(float(time.process_time()) - float(start)))) #debug zeitmessung
                            
                            self.neueDaten = True
                        else:
                            self.error = True;
                    except Exception as e:
                        print("Wifi Error: "+ str(e))
               