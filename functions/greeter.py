# def greet_user(lamine):
#     print(f"salut, {lamine.title()}")
# greet_user('momo')

# def display_message():
#     print("what are you learning in this chapter")
# display_message()

# def favorite_book(title):
#     print(f"my favorite book is {title.title()}")
# favorite_book("python crash course")

# def make_shirt(size, text):
#     print(f"la  taille est {size}")
#     print(f"descrition {text}")
# make_shirt("167", 'fckng')
# make_shirt(size= '167', text= 'fckng') #keyword arguments
# make_shirt(text = "I love python")
# make_shirt(size = "large")
# make_shirt(size = "medium")
# def describe_city(name, country="Sn"):
#     print("Reykjavik is in iceland")
# describe_city("Dakar", "m", "l", "k") #c'est un test d'erreur9



def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("Dite votre nom: ")
    print("(appuyez sur 'q' pour quitter)")
    f_name = input("nom: ")
    l_name = input("prenom: ")
    if f_name == 'q':
        break
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name) 
    print(f"salut, {formatted_name}")