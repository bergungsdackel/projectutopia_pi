import threading

class WifiModule(threading.Thread):

    neueDaten = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        neueDaten = false
        self.start()

    def run(self):
        print("Warte auf Daten von Smartphone...Penis!")
        #Connection Socket Funktion oder so was
        if(true):
            neueDaten = true

