__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

import random
import hashlib


def getLoginOrPassword(choice):
    if choice == 0:
        return input("Saisir votre login")
    elif choice == 1:
        return input("Saisir votre mot de passe")


def randomLoginOrPassword(choice):

    loginOrPassword = ""
    length = 0
    check = 1

    if choice == 0:
        while check == 1:
            try:
                length = int(input("Choisisez la taille de votre login: "))
                break
            except:
                print("Entrer un nombre")
                check == 1

    elif choice == 1:
        while check == 1:
            try:
                length = int(input("Choisisez la taille de votre login: "))
                break
            except:
                print("Entrer un nombre")
                check == 1

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