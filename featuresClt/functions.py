__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

import random
import hashlib

def getLoginOrPassword(choice):
    if choice == 0:
        return input("Saisir le login")
    elif choice == 1:
        return input("Saisir le mot de passe")



def randomLoginOrPassword(choice):

    loginOrPassword = ""
    length = 0
    #IL NE FAUT PAS OUBLIER D4AJOUTER LES SECURIT2 SUR LA TAILLE L4UTILISTATEUR NE PEUT ENTRER QUEUN ENTIER ...

    if choice == 0:
        length = int(input("Choisisez la taille de votre login: "))
    elif choice == 1:
        length = int(input("Choisisez la taille de votre mot de passe: "))

    while length > 0:
        loginOrPassword += random.choice('AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn123456789&é^$ù*,;:!?./§/*-+')
        length -= 1

    if choice == 0:
        message = "Votre login est : %s" % (loginOrPassword)
        print(message)

    elif choice == 1:
        message = "Votre mot de passe est : %s" % (loginOrPassword)
        print(message)

    return loginOrPassword