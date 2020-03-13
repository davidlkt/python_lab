print("\n-----------")
print("6-6. Polling:") #Use the code in favorite_languages.py (page 104) .
# • Make a list of people who should take the favorite languages poll . Include
# some names that are already in the dictionary and some that are not .
# • Loop through the list of people who should take the poll . If they have already taken the poll, 
# print a message thanking them for responding . If they have not yet taken the poll, print a message 
# inviting them to take the poll .
print("-----------\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ["jen","edward", "david", "phil"]

for p in people:
    if p in favorite_languages.keys():
        print("Hi %s thank you for taken the poll" % p.title())
    else:
        print("Hi %s you should please take our poll" % p.title())


print("\n-----------")
print(  "6-10. Favorite Numbers:") #Modify your program from Exercise 6-2 (page 102) so each person can 
#have more than one favorite number . Then print each person’s name along with their favorite numbers .
print("-----------\n")

favorite_languages = {
    'jen': ['python', 'java'],
    'sarah': ['c', 'c++'],
    'edward': ['ruby'],
    'phil': ['python', 'typescript'],
    }

for name, languages in favorite_languages.items():
    print("%s's favourite languages: " % name.title())
    for language in languages:
        print(". %s" % language)