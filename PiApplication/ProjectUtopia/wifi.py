import threading
import socket


class WifiModule(threading.Thread):

    neueDaten = None
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = None
    data = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        neueDaten = False
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        self.start()

    def run(self):
        print("Warte auf Daten von Smartphone...")

        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            print("received message: %s" % data)
            print("received from: %s" % addr)
            #Connection Socket Funktion oder so was
            if(data != None):
                neueDaten = True
                if(data == "FORWARD"):
                    print(" ")

