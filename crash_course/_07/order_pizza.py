print("\n-----------")
print("7-4. Pizza Toppings:") #Write a loop that prompts the user to enter a 
# series of pizza toppings
#  until they enter a 'quit' value . As they enter each topping, print a message saying you’ll
#   add that topping to their pizza .
print("-----------\n")

flag = True
message = "\nPlease select a topping for your pizza: "
message += "\nEnter quit to exit.\n"

while flag:
    topping = input(message)

    if topping == "quit":
        print("\nThank you! Your order is being prepared now!")
        flag = False
    else:
        print("%s will be added to your pizza. Do you want to add any other topping?" % topping)


