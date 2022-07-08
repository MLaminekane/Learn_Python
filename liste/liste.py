plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

print(plateformes_sociales[0:3])
plateformes_sociales[0] #premier element d'une liste
plateformes_sociales[-1] #twitter
plateformes_sociales.append('quora') #.append: pour ajouter un element a la fin d'une liste
print(plateformes_sociales)
plateformes_sociales.remove("Facebook")
print(plateformes_sociales)
len(plateformes_sociales) #connaitre la longeur d'une liste
plateformes_sociales.sort() 
print(plateformes_sociales) #trier une liste
plateformes_sociales.pop(2) # supprimer un element d'une liste sur une position epecifie
print(plateformes_sociales)
plateformes_sociales.reverse() #inverse l'ordre d'une liste
plateformes_sociales.copy() #fait une copie d'une liste 
plateformes_sociales.clear() #supprime tous les elements d'une liste


plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
best_plateformes = plateformes_sociales[:] #permet de copier une liste 
print("first three item in the list are: ", plateformes_sociales[0:3])
print("three items from the middle are: ", plateformes_sociales[1:3])
print("three last items are: ", plateformes_sociales[1:4])
for plateform in plateformes_sociales:
    print(plateformes_sociales[0])
'Facebook' in plateformes_sociales
print('TWITTER' in plateformes_sociales)