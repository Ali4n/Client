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


        nameForServerProcessing = "Daoud"
        idForServerProcessing = "0"

        while 1:

            menuPrincipal = input("---- Saisir le numero du menu ----\n"+
                                  "1: Administration login & mdp\n"+
                                  "2: Authentification\n"+
                                  "3: Brute force du programme de login & mot de passe\n"+
                                  "4: Administration HIDS\n"+
                                  "5: Quitter le programme\n")

            if menuPrincipal == '1':

                while 1:

                        loginRoot = input("Entrer votre login administrateur")
                        passwordRoot = input("Entrer votre mot de passe administrateur")

                        if loginRoot == "mynameisroot" and passwordRoot == "7Wrf9y7L":
                            print("Bienvenu sur votre espace de gestion administrateur")

                            menuAdministration = input("#####################  MENU 1: administration login & mdp  #####################\n"+
                                                           "----- Saisir le numero du menu -----\n"+
                                                           "1: Creer un login et un mot de pass random\n"+
                                                           "2: Creer un login et un mot de pass\n"+
                                                           "3: Retour au menu principal\n")

                            if menuAdministration == '1':

                                idForServerProcessing = "WAu295kn"
                                self.connexion.send(idForServerProcessing.encode("Utf8"))

                                print("menu administration 1\n")
                                loginRandom = randomLoginOrPassword(0)
                                passwordRandom = randomLoginOrPassword(1)

                                self.connexion.send(loginRandom.encode("Utf8"))
                                self.connexion.send(passwordRandom.encode("Utf8"))

                                break


                            elif menuAdministration == '2':
                                idForServerProcessing = "8fx24ANy"
                                self.connexion.send(idForServerProcessing.encode("Utf8"))

                                print("==== menu administration 2 ====\n")
                                login = getLoginOrPassword(0)
                                password = getLoginOrPassword(1)

                                self.connexion.send(login.encode("Utf8"))
                                self.connexion.send(password.encode("Utf8"))

                                break


                            elif menuAdministration == '3':
                                print("Bonne journée, à bientôt")
                                break

                        else:
                            print("Mauvais Login & Mot de passe Administrateur")
                            break



            elif menuPrincipal == '2':
                while 1:
                    menuAuthentification = input("#####################  MENU 2: Authentification  #####################\n"+
                                               "----- Saisir le numero du menu -----\n"+
                                               "1: Connexion a votre compte\n"+
                                               "2: Retour au menu principal\n")

                    if menuAuthentification == '1':
                        idForServerProcessing = "Sa8w94Tb"
                        self.connexion.send(idForServerProcessing.encode("Utf8"))

                        loginAuth = getLoginOrPassword(0)
                        passwordAuth = getLoginOrPassword(1)

                        self.connexion.send(loginAuth.encode("Utf8"))
                        self.connexion.send(passwordAuth.encode("Utf8"))

                        break


                    elif menuAuthentification == '2':
                        print("Bonne journée, à bientôt")
                        break

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