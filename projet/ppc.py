import random 
choix = ['pierre', 'papier', 'ciseau']

victoire_cpu = 0
victoire_joueur = 0

while True:
    joueur = int(input("entrer une valeur (1=pierre, 2=papier, 3=ciseau) : "))
    random_number = random.randint(0, 2)
    ordi = choix[random_number]
    if joueur == 1 and ordi == 'pierre':
        print("egalite")
        victoire_cpu += 0
        victoire_joueur += 0
        continue
    elif joueur == 2 and ordi == 'pierre':
        print("l'ordinateur a perdu")
        victoire_joueur += 1
    elif joueur == 3 and ordi == 'pierre':
        print("l'ordinateur a gagne")
        victoire_cpu += 1
print(f"vous avez gagne {victoire_joueur} fois")
print(f";'ordinateur a gagne {victoire_cpu} fois")