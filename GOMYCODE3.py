# Fonction randint
from random import *

# EXERCICE PRATIQUE

# Invitation au jeu
print("Bienvenue dans le jeu Devinez le nombre !")
print("Je pense à un nombre compris entre 1 et 100. Pouvez-vous deviner ce que c’est ?")

# Entrée de la réponse

supposition= int(input("saisir votre supposition ?"))

nombre= randint(1, 100)

"""if supposition < nombre:
   print('nombre trop bas')

elif supposition > nombre:
    print('C_est trop grand !')

else:
    print("Félicitations ! Vous avez deviné le bon nombre !")"""

#Boucle while

while supposition != nombre:

    if supposition < nombre:
        print('nombre trop bas')

        print('Deviner encore SVP')

        supposition = int(input("saisir votre supposition ?"))

    elif supposition > nombre:
        print('C_est trop grand !')

        print('Deviner encore SVP')

        supposition = int(input("saisir votre supposition ?"))


print("Félicitations ! Vous avez deviné le bon nombre !",nombre)


print('Voulez vous continuer à jouer ?')

continuer= int(input("taper pour 1 continuer, 0 pour quitter:"))

while continuer==1:
    supposition = int(input("saisir votre supposition ?"))
    nombre = randint(1, 100)

    while supposition != nombre:

        if supposition < nombre:
            print('nombre trop bas')

            print('Deviner encore SVP')

            supposition = int(input("saisir votre supposition ?"))

        elif supposition > nombre:
            print('C_est trop grand !')

            print('Deviner encore SVP')

            supposition = int(input("saisir votre supposition ?"))

    print("Félicitations ! Vous avez deviné le bon nombre !", nombre)
    continuer = int(input("taper pour 1 continuer, 0 pour quitter:"))


