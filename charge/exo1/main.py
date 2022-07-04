import csv

# Ecrivez le code ci-dessous. Utilisez le package csv !
with open('F:\Documents\GitHub\Learn_Python\charge\exo1\input.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for heures in reader:
        print(heures)

