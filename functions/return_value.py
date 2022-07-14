def get_formatted_name(first_name, last_name, surnom_name):
    full_name = f"{first_name}{last_name} surnom: {surnom_name}"
    return full_name
musician = get_formatted_name('Nek', 'Feu', "screw")
print(musician)