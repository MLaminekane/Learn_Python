utilisateur = {
    "Nom": "lamine",
    "Prenom": "kane",
    "Age": '21',
    "Age": '21',
    "Niveau_etude": "Licence 1"
}
for k,v in utilisateur.items():
    print(f"cle: {k}")
    print(f"valeur: {v}")
print("\n")
for name, per in utilisateur.items():
    print(f"{name.title()} utilisateur {per.title()}")
print("\n")
for name in sorted(utilisateur.keys()): # sorted permet d'arranger un dictionnaire
    print(f"{name.title()} utilisateur")
print("\n")
for name in set(utilisateur.keys()): #permet de supprimer les doublons d'un dictionnaire
    print(name.title())