__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

HOST = '127.0.0.1'
PORT = 46000

from featuresClt.functions import *
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
        #test :     self.connexion.send(getLoginOrPassword(0).encode("Utf8"))
        #test :     self.connexion.send(getLoginOrPassword(1).encode("Utf8"))

        #definition du MENU PRINCIPALE
        # 1: Administration login & mdp FAIT
        # 2: Verifier l'utilisateur est bien dans le fichier de hash
        # 3: Brute force du programme de login & mot de passe
        # 4: Administration HIDS
        # 5: Quitter le programme
            # MENU 1: administration login & mdp
                # 1: Creer un login et un mdp random    (idForServerTreatement = 11) tretement in srv => she use bdd to log & mdp
                # 2: Creer un login et un mdp   (idForServerTreatement = 12)    tretement in srv => she use bdd to log & mdp
                # 3: Quitter le programme
            # MENU 2: Verifier l'utilisateur est bien dans le fichier ou bdd de hash
                # 1: Verification de l'utilisateur et du mot de passe   (idForServerTreatement = 21)
                # 2: Quitter le programme


        nameForServerTreatement = "Daoud"
        idForServerTreatement = 0

        while 1:

            menuPrincipal = input("---- Saisir le numero du menu ----\n"+
                                  "1: Administration login & mdp\n"+
                                  "2: Verifier l'utilisateur est bien dans le fichier de hash\n"+
                                  "3: Brute force du programme de login & mot de passe\n"+
                                  "4: Administration HIDS\n"+
                                  "5: Quitter le programme\n")

            if menuPrincipal == '1':
                while 1:
                    menuAdministration = input("#####################  MENU 1: administration login & mdp  #####################\n"+
                                               "----- Saisir le numero du menu -----\n"+
                                               "1: Creer un login et un mot de pass random\n"+
                                               "2: Creer un login et un mot de pass\n"+
                                               "3: Retour au menu principal\n")
                    if menuAdministration == '1':
                        idForServerTreatement = 11

                        print("menu administration 1")
                    elif menuAdministration == '2':
                        idForServerTreatement = 12

                        print("menu administration 2")
                    elif menuAdministration == '3':
                        print("Bonne journée, à bientôt")
                        break

            elif menuPrincipal == '2':
                print("menu 2")
            elif menuPrincipal == '3':
                print("menu 3")
            elif menuPrincipal == '4':
                print("menu 4")
            elif menuPrincipal == '5':
                exit()


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