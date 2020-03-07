print("\n-----------")
print("7-5. Movie Tickets:") #A movie theater charges different ticket prices depending on a 
# person’s age . If a person is under the age of 3, the ticket is free; if they are between 3 and 12, 
# the ticket is $10; and if they are over age 12, the ticket is $15 . Write a loop in which you ask 
# users their age, and then tell them the cost of their movie ticket .
print("-----------\n")

flag = True
total = 0


message = "\nPlease enter you age. When ready select 0."

while flag:
    age = input(message)

    if age > 0 and age < 3:
        ticket = 0
        print("Cost of ticket: $%s" % ticket)
        total = total + ticket
    elif age >= 3 and age < 12:
        ticket = 10
        print("Cost of ticket: $%s" % ticket)
        total = total + ticket
    elif age > 12:
        ticket = 15
        print("Cost of ticket: $%s" % ticket)
        total = total + ticket
    elif age == 0:
        print("Thank you! you will be charged for a total of $%s." % total)
        print("Enjoy your movie.")
        flag = False
