print("\n-----------")
print("5-7. Favorite Fruit:")# Make a list of your favorite fruits, and then write a series of independent if statements
#  that check for certain fruits in your list .
# • Make a list of your three favorite fruits and call it favorite_fruits .
# • Write five if statements . Each should check whether a certain kind of fruit is in your list . If the fruit is in your
#  list, the if block should print a statement, such as You really like bananas!
print("-----------\n")
fruits = ["apple", "banana", "peach"]

usual = str(input("What fruit do you usually eat? ")).lower()

if usual in fruits:
    print("Ah! %s is a fruit that I usually eat" % usual)
else:
    print("Ah! that's ok.")