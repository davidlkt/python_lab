print("\n-----------")
print("5-8. Hello Admin:") #Make a list of five or more usernames, including the name 'admin' . 
# Imagine you are writing code that will print a greeting to each user after they log in to a website . 
# Loop through the list, and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for log- ging in again.
print("5-9. No Users:") #Add an if test to hello_admin.py to make sure the list of users is not empty .
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed .
print("-----------\n")

users = ["David", "Lucía", "Santiago", "Blanca","Admin", "Kari", "Ivana"]
#users = []
if users:
    for user in users:
        if user == "Admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello %s, thank you for log- ging in again." % user)
else:
    print("We need find more users")

print("\n-----------")
print("5-10. Checking Usernames:")  #Do the following to create a program that simulates how websites ensure that 
# everyone has a unique username .
# • Make a list of five or more usernames called current_users .
# • Make another list of five usernames called new_users . Make sure one or
# two of the new usernames are also in the current_users list .
# • Loop through the new_users list to see if each new username has already been used . If it has, 
# print a message that the person will need to enter a new username . If a username has not been used, print a 
# message saying that the username is available .
# • Make sure your comparison is case insensitive . If 'John' has been used, 'JOHN' should not be accepted .
print("-----------\n")

current_users = []
for user in users:
    current_users.append(user.lower())

new_users = ["Miriam", "Paula", "IVANA", "KARI"]

for user in new_users:
    if user.lower() in current_users:
        print("The user %s has been already taken." % user)
    else:
        print("Username %s is available" % user)

print("\n-----------")
print("5-11. Ordinal Numbers:") # Ordinal numbers indicate their position in a list, such as 1st or 2nd . 
# Most ordinal numbers end in th, except 1, 2, and 3 .
# • Store the numbers 1 through 9 in a list .
# • Loop through the list .
# • Use an if-elif-else chain inside the loop to print the proper ordinal end- ing for each number . Your 
# output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line .
print("-----------\n")

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(". %sst" % number)
    elif number == 2:
        print(". %snd" % number)
    elif number == 3:
        print(". %srd" % number)
    else:
        print(". %sth" % number)

    