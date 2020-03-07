print("\n-----------")
print("7-8. Deli:") #Make a list called sandwich_orders and fill it with the names of vari- ous sandwiches . 
# Then make an empty list called finished_sandwiches . Loop through the list of sandwich orders and 
# print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move 
# it to the list of finished sandwiches . After all the sandwiches have been made, print a message l
# isting each sandwich that was made .
print("-----------\n")

sandwich_orders = ["Jamón y Queso", "Lever y Roquefort", "Salame y queso", "Vegetariano", "Pollo y Cheddar"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Preparing a %s sandwich" % current_sandwich)
    finished_sandwiches.append(current_sandwich)
print("")
for order in finished_sandwiches:
    print("Already done a %s sandwich" % order)


print("\n-----------")
print("7-9. No Pastrami:") #Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' 
# appears in the list at least three times . Add code near the beginning of your program to print a message saying 
# the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from 
# sandwich_orders . Make sure no pastrami sandwiches end up in finished_sandwiches .
print("-----------\n")

sandwich_orders = ["Pastrami", "Jamón y Queso", "Lever y Roquefort","Pastrami", "Salame y queso", "Vegetariano", "Pastrami", "Pollo y Cheddar"]
finished_sandwiches = []

print("Sorry we don´t have more Pastrami sandwiches\n")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Preparing a %s sandwich" % current_sandwich)
    finished_sandwiches.append(current_sandwich)
print("")
for order in finished_sandwiches:
    print("Already done a %s sandwich" % order)