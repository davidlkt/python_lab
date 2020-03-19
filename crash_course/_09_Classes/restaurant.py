print("\n-----------")
print("9-1. Restaurant:") #Make a class called Restaurant . The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type . Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indi- cating that the restaurant is open .
# Make an instance called restaurant from your class . Print the two attri- butes individually, and then call both methods .
print("-----------\n")

from mod_restaurant import Restaurant


my_resto = Restaurant('el loco david','parilla', 55)

print(my_resto.name.title())
print(my_resto.type.title())
my_resto.describe_restaurant()
my_resto.open_restaurant()


print("\n-----------")
print("9-4. Number Served:") #Start with your program from Exercise 9-1 (page 166) . Add an attribute called number_served with a 
# default value of 0 . Create an instance called restaurant from this class . Print the number of customers the restaurant has 
# served, and then change this value and print it again .
# Add a method called set_number_served() that lets you set the number of customers that have been served . Call this method with a 
# new number and print the value again .
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served . Call this 
# method with any num- ber you like that could represent how many customers were served in, say, a day of business .
print("-----------\n")

my_resto.show_customers_served()
my_resto.set_number_served(67)
my_resto.show_customers_served()
my_resto.increment_number_served(3)
my_resto.show_customers_served()
my_resto.increment_number_served(2)
my_resto.show_customers_served()

print("\n-----------")
print("9-6. Ice Cream Stand:") #An ice cream stand is a specific kind of restaurant . Write a class called IceCreamStand that inherits 
# from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of
# the class will work; just pick the one you like better . Add an attribute called flavors that stores a list of ice cream flavors . 
# Write a method that displays these flavors . Create an instance of IceCreamStand, and call this method .
print("-----------\n")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served, flavors):
        super().__init__(restaurant_name, cuisine_type, number_served)

        self.flavors = flavors

    def show_flavors(self):
        print('Available ice-cream flavors in %s' % self.name.title())
        for flavor in self.flavors:
            print('. %s' % flavor.title())


my_hela1 = IceCreamStand('la loca heladeria','heladeria', 1, ['menta granizada', 'bananita', 'sambayon'])

my_hela1.show_flavors()
