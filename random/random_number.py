import random

random_number = random.randint(1, 6)
tentatives = 0
while True:
    joueur = int(input("deviner le nombre: "))
    if joueur == random_number:
        print("correct")
        break
    elif joueur < random_number:
        print("nombre inferieur")
    elif joueur > random_number:
        print("nombre superieur")
    tentatives += 1
    print(f"nombre de tentatives: {tentatives}")