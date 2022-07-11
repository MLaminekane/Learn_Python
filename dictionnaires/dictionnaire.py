Presentation = {
    "Nom": "lamine",
    "Prenom": "kane",
    "Age": 21,
    "Niveau_etude": "Licence 1"
}
nom = Presentation["Nom"]
print(nom)
Presentation["Sante"] = "90%" #pour ajouter une nouvelle valeur
del Presentation["Sante"] #supprimer une cle valueur
"Age" in Presentation #renvoie un boolean pour voir si une cle existe dans un dictionnaire
print(Presentation["Nom"]) #pour accerder aux valeurs
