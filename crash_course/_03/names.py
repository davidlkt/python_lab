# 3-1. Names: Store the names of a few of your friends in a list called names . 
# Print each person’s name by accessing each element in the list, one at a time .

names = ["Karina", "Ivana", "Miriam", "Paula", "Patricia"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print("-----------------------------")
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing
#  each person’s name, print a message to them . The text of each mes- sage should be the same,
#   but each message should be personalized with the person’s name .
print("-----------------------------")

message="Hello, how are you today "

print(message + names[0] + " ?")
print(message + names[1] + " ?")
print(message + names[2] + " ?")
print(message + names[3] + " ?")
print(message + names[4] + " ?")