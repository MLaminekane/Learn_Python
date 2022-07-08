# Écrire un programme qui permet de saisir une suite de nombre entier. 
# Le programme affiche tous les nombres saisis ainsi que la somme des nombres pairs.
# la saisie s arrête lorsque le gas saisie 0

# Ecrire u programme qui permet de saisir 275345 réél.
# Le programme affiche les 10000 premiers réels saisis et les 10000 derniers

# sup = 0
# inf = 0
# for reel in range(0, 5):
#     x = float(input("entrer les reels: "))
#     x += 1
#     inf = [reel< 3]
#     print(inf)
#     sup = [reel > 3]
#     print(sup)


# my_list = [1,2,3,4,5,6,7,8,9,10]

# #puts first 5 elements in new list
# first_five = [x for x in my_list[0:5]]
# print(first_five)

# #puts elements after index 5 into new list
# last_five = [x for x in my_list[5:]]
# print (last_five)



my_list = [275345]
i=0
while i < 10000:
    print(my_list[i])
    i +=1
    a=my_list.len()
    b= a-10000
while b<a:
    print(my_list[b])
    b+=1







# Suite_de_valeurs = []
# pairs = 0
# total = int()
# Number = int(input("combien de valeurs voulez vous saisir: "))
# for i in range(1, Number + 1):
#     value = int(input("valeurs %d : " %i))
#     Suite_de_valeurs.append(value)
#     while value == 0:
#         break
#     else:
#         if value % 2 == 0:
#             total += value
#     if value % 2 == 0:
#         pairs += value
#         print(f"somme valeurs pairs: {pairs}")
# total = sum(Suite_de_valeurs)
# print("\n la somme des valeurs saisies: ", total)



