from getpass import fallback_getpass

__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

import random
import hashlib
import sys

def getLoginOrPassword(choice):
    if choice == 0:
        doCondition = True
        while doCondition:
            login = input("Saisir votre login")
            controlLenght = len(login)
            if controlLenght < 6:
                print("Notre politique de mot de passe vous impose d'avoir un login plus grand que 6 caracteres")
            else:
                break
        return login
    elif choice == 1:
        doCondition = True
        while doCondition:
            password = input("Saisir votre mot de passe")
            controlLenght = len(password)
            if controlLenght < 6:
                print("Notre politique de mot de passe vous impose d'avoir un mot de passe plus grand que 6 caracteres")
            else:
                break
        return password


def loginOrPassword(choice):
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
                doCondition = True
                while doCondition:
                    length = int(input("Choisisez la taille de votre login: "))
                    if length < 6:
                        print("Notre politique de login vous impose d'avoir un login plus grand que 6 caracteres")
                    else:
                        break
                break
            except:
                print("Entrer un nombre")
                check == 1

    elif choice == 1:
        while check == 1:
            try:
                doCondition = True
                while doCondition:
                    length = int(input("Choisisez la taille de votre mot de passe: "))
                    if length < 6:
                        print("Notre politique de mot de passe vous impose d'avoir un login plus grand que 6 caracteres")
                    else:
                        break
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