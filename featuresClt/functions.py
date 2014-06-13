__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

def getLoginOrPassword(choice):
    if choice == 0:
        return input("Saisir le login")
    elif choice == 1:
        return input("Saisir le mot de passe")
