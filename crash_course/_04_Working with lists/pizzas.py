print("\n-----------")
print("4-1. Pizzas:") #Think of at least three kinds of your favorite pizza . Store these pizza names in a list, 
# and then use a for loop to print the name of each pizza .
# • Modify your for loop to print a sentence using the name of the pizza instead of printing just the 
# name of the pizza . For each pizza you should have one line of output containing a simple statement 
# like I like pepperoni pizza .
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza . T
# he output should consist of three or more lines about the kinds of pizza you like and then an additional 
# sentence, such as I really love pizza!
print("-----------\n")
pizzas = ["Provolone", "Roquefort", "Jamón y morrones"]

for pizza in pizzas:
    print("I like %s pizza" % pizza)

print("I really love pizza!")

print("\n-----------")
print("4-11. My Pizzas, Your Pizzas:") # Start with your program from Exercise 4-1 (page 60) . Make a copy of the list 
# of pizzas, and call it friend_pizzas . Then, do the following:
# • Add a new pizza to the original list .
# • Add a different pizza to the list friend_pizzas .
# • Prove that you have two separate lists . Print the message, My favorite pizzas are:, and then use a for 
# loop to print the first list . Print the message, My friend’s favorite pizzas are:, and then use a for loop 
# to print the sec- ond list . Make sure each new pizza is stored in the appropriate list .
print("-----------\n")

friend_pizzas = pizzas[:]
 
pizzas.append("Napolitana")
friend_pizzas.append("Calabresa")

print("My favourite pizzas are")
for p in pizzas:
     print(". %s" % p)

print("My friends favourite pizzas are: ")
for p in friend_pizzas:
    print(". %s" % p)

print("\n-----------")
print("4-10. Slices:") #Using one of the programs you wrote in this chapter, add several lines to the end of the program
#  that do the following:
# • Print the message, The first three items in the list are: . Then use a slice to print the first three items 
# from that program’s list .
# • Print the message, Three items from the middle of the list are: . Use a slice to print three items from the 
# middle of the list .
# • Print the message, The last three items in the list are: . Use a slice to print the last three items in the list .
print("-----------\n")
friend_pizzas.append("Anchoas")
friend_pizzas.append("Tropical")
friend_pizzas.append("Fugazetta")
friend_pizzas.append("Muzzarella")

print("The first three items in the list are:")
for p in friend_pizzas[:3]:
    print(". %s" % p)
print("Three items from the middle of the list are:")
for p in friend_pizzas[int(len(friend_pizzas) / 2 - 1):int(len(friend_pizzas) / 2 - 1 + 3)]:
    print(". %s" % p)
print("The last three items in the list are:")
for p in friend_pizzas[-3:]:
    print(". %s" % p)