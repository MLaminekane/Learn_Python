def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name} 
    if age:
        person['age'] = age
        return person


musician = build_person('M', 'J', age = 39)  
print(musician)