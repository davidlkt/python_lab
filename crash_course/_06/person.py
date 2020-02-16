print("\n-----------")
print("6-1. Person:") #Use a dictionary to store information about a person you know . Store their first name, 
# last name, age, and the city in which they live . You should have keys such as first_name, last_name, age, 
# and city . Print each piece of information stored in your dictionary .
print("-----------\n")

person = {
    'first_name': 'david',
    'last_name': 'carbone',
    'age': 42,
    'city': 'llavallol'
}

print("%s %s, edad: %s años, vive en %s." % (
    person['first_name'].title(),
    person['last_name'].title(),
    person['age'],
    person['city'].title())
    )

print("\n-----------")
print("6-7. People:") #Start with the program you wrote for Exercise 6-1 (page 102) . Make two new dictionaries 
# representing different people, and store all three dictionaries in a list called people . Loop through your list 
# of people . As you loop through the list, print everything you know about each person .
print("-----------\n")

people = {
    'person1' : {
    'first_name': 'david',
    'last_name': 'carbone',
    'age': 42,
    'city': 'llavallol'
    },
    'person2' : {
    'first_name': 'karina',
    'last_name': 'chavez',
    'age': 45,
    'city': 'monte chingolo'
    },
    'person3' : {
    'first_name': 'ivana',
    'last_name': 'roco',
    'age': 44,
    'city': 'garín'
    }
}

for person, info in people.items():
    print("%s %s, edad: %s años, vive en %s." % (
    info['first_name'].title(),
    info['last_name'].title(),
    info['age'],
    info['city'].title())
    )