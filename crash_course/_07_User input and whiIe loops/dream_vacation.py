print("\n-----------")
print("7-10. Dream Vacation:") #Write a program that polls users about their dream vacation . Write a prompt similar to If 
#you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll .
print("-----------\n")
flag = True
poll = {}

while flag:
    person = input("What's your name: ")
    place = input("\nWhat is your favourite place for vacations: ")
    poll[person] = place
    
    response = input("\nWould you like enter another person? y/n")

    if response == 'n':
        flag = False

for person,place in poll.items():
    print("Favourite place for %s to go on vacations is %s" % (person,place))






