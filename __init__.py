__author__ = 'N3o'

from featuresClt.functions import *

HOST = '127.0.0.1'
PORT = 46000
print ("test")
import socket, sys, threading

class ThreadReception(threading.Thread):
    # objet thread gérant la reception des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024).decode("Utf8")
            print("*" + message_recu + "*")
            if not message_recu or message_recu.upper() =="FIN":
                break
        #Le thread <réception> se termine ici.
        #On force la fermeture du thread <émission> :
        th_E._stop()
        print("Client arrêté. Connexion interrompue.")
        self.connexion.close()

class ThreadEmission(threading.Thread):
    # objet thread gérant l'émission des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode("Utf8"))

# Programme principal - Etablissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    connexion.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec le serveur.")

#Dialogue avec le serveur : on lance deux threads pour gérer indépendamment l'émission et la réception des messages
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)

th_E.start()
th_R.start()