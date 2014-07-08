__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

HOST = '127.0.0.1'
PORT = 46000

from featuresClt.functions import *
from ftplib import FTP

import socket
import sys
import threading




class ThreadReception(threading.Thread):
    # objet thread gérant la reception des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):

        global syncinput

        while 1:

            message_recu = self.connexion.recv(1024).decode("Utf8")
            print("*" + message_recu + "*")
            #if not message_recu or message_recu.upper() == "FIN":

            syncinput = False

            if message_recu == "Bienvenu sur votre espace de stockage":


                ftp_host = '127.0.0.1'
                ftp_login = 'anonymous'
                ftp_password = 'Ls4z7B9t'

                ftp = FTP(ftp_host, ftp_login, ftp_password)
                print("#####  Listes de vos fichiers :  #####")
                ftp.dir()

                print("!!!! Transferer votre fichier qui est contenu dans votre dossier client FilesClients, pour le => a FilesServers: !!!!")
                varDir = "FilesClients\\"


                flush_input()
                varfichier = input("Entrer le nom du fichier à envoyer :\r")

                try:
                    file=open(varDir + varfichier, 'rb')
                    ftp.storbinary("STOR "+ varfichier +"", file)
                    file.close()
                except:
                    print("Le fichier n'existe pas")

                print("#####  Listes de vos nouveaux fichiers :  #####")
                ftp.dir()

                syncinput = True



        #Le thread <réception> se termine ici.
        #On force la fermeture du thread <émission> :
        #th_E._stop()
        print("Client arrêté. Connexion interrompue.")
        self.connexion.close()


class ThreadEmission(threading.Thread):
    # objet thread gérant l'émission des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):

        idForServerProcessing = "0"
        cptbruteforce = 1
        global syncinput

        syncinput = True
        while 1:

            if syncinput:
                menuPrincipal = input("---- Saisir le numero du menu ----\n" +
                                      "1: Administration login & mdp\n" +
                                      "2: Connexion a votre espace de stockage\n" +
                                      "3: Quitter le programme\n")

            if menuPrincipal == '1':

                while 1:

                        loginRoot = input("Entrer votre login administrateur")
                        passwordRoot = input("Entrer votre mot de passe administrateur")

                        if loginRoot == "mynameisroot" and passwordRoot == "7Wrf9y7L":
                            syncinput = True
                            print("Bienvenu sur votre espace de gestion administrateur")

                            menuAdministration = input("#####################  MENU 1: administration login & mdp  #####################\n" +
                                                           "----- Saisir le numero du menu -----\n" +
                                                           "1: Creer un login et un mot de pass random\n" +
                                                           "2: Creer un login et un mot de pass\n" +
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
                    syncinput = True
                    menuAuthentification = input("#####################  MENU 2: Authentification  #####################\n"+
                                               "----- Saisir le numero du menu -----\n" +
                                               "1: Connexion a votre compte\n" +
                                               "2: Retour au menu principal\n")
                    if cptbruteforce > 4:
                        print("vous avez essayé trop de codes. veuillez réessayer plus tard")
                        break

                    elif menuAuthentification == '1':
                        idForServerProcessing = "Sa8w94Tb"
                        self.connexion.send(idForServerProcessing.encode("Utf8"))

                        loginAuth = loginOrPassword(0)
                        passwordAuth = loginOrPassword(1)
                        cptbruteforce += 1

                        self.connexion.send(loginAuth.encode("Utf8"))
                        self.connexion.send(passwordAuth.encode("Utf8"))

                        break

                    elif menuAuthentification == '2':
                        print("Bonne journée, à bientôt")

                        break

            elif menuPrincipal == '3':
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