# # fichier = open("Lamine.txt", "w")
# # fichier.write("Salut, Lamine!")
# # fichier.close()

# with open("Lamine.txt") as fichier:
#     for ligne in fichier:
#         print(ligne)

import csv

with open("F:\Download\convertcsv.csv") as fichier_csv:
   reader = csv.reader(fichier_csv, delimiter=',')
   for ligne in reader:
      print(ligne)

import csv

# with open('couleurs_preferees.csv') as fichier_csv:
#    reader = csv.DictReader(fichier_csv, delimiter=',')
#    for ligne in reader:
#       print(ligne['nom'] + " travaille en tant que " + ligne['metier']
#         + " et sa couleur préférée est " + ligne['couleur_preferee'])