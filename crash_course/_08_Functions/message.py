print("\n-----------")
print("8-1. Message:") #Write a function called display_message() that prints one sen- tence telling everyone what 
#you are learning about in this chapter . Call the function, and make sure the message displays correctly .
print("-----------\n")

def display_message():
    print("Helo World!\n")

display_message()

print("\n-----------")
print("8-2. Favorite Book:") #Write a function called favorite_book() that accepts one parameter, title . 
# The function should print a message, such as One of my favorite books is Alice in Wonderland . Call the 
# function, making sure to include a book title as an argument in the function call .
print("-----------\n")

def favorite_book(title):
    print("One of my favourite books is %s\n" % title)

favorite_book("IT")

print("\n-----------")
print("8-3. T-Shirt:") #Write a function called make_shirt() that accepts a size and the text of a message that should be 
# printed on the shirt . The function should print a sentence summarizing the size of the shirt and the message 
# printed on it . Call the function once using positional arguments to make a shirt . Call the function a second 
# time using keyword arguments .
print("-----------\n")

def make_shirt(size,text):
    print("T-Shirt size: %s with the message: %s\n" % (size,text))

make_shirt("S","I luv LVS")
make_shirt(size="M", text="Luke Im your father")

print("\n-----------")
print("8-4. Large Shirts:") #Modify the make_shirt() function so that shirts are large by default with a message 
# that reads I love Python . Make a large shirt and a medium shirt with the default message, and a shirt of any 
# size with a different message .
print("-----------\n")

def make_shirt(size="L",text="I love Python"):
    print("T-Shirt size: %s with the message: %s\n" % (size,text))

make_shirt()
make_shirt(size="M")
make_shirt("XXS","I came for the food")

print("\n-----------")
print("8-5. Cities:") #Write a function called describe_city() that accepts the name of a city and its country . 
# The function should print a simple sentence, such as Reykjavik is in Iceland . Give the parameter for the 
# country a default value . Call your function for three different cities, at least one of which is not in 
# the default country .
print("-----------\n")

def describe_city(city,country="Argentina"):
    print("%s is in %s\n" % (city,country))

describe_city("Buenos Aires")
describe_city("Trelew")
describe_city("Las Vegas","USA")

print("\n-----------")
print("8-6. City Names:") #Write a function called city_country() that takes in the name of a city and its country . 
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value that’s returned .
print("-----------\n")

def city_country(city,country):
    print("%s, %s\n" % (city.title(),country.title()))

city_country("buenos aires","argentina")
city_country("las vegas","usa")
city_country("montevideo","uruguay")

print("\n-----------")
print("8-12. Sandwiches:") #Write a function that accepts a list of items a person wants on a sandwich . The function should have one 
# parameter that collects as many items as the function call provides, and it should print a summary of the sand- wich that 
# is being ordered . Call the function three times, using a different num- ber of arguments each time .
print("-----------\n")

def make_sandwich(*ingredients):
    print("\nYour Sandwich has: \n")
    for i in ingredients:
        print(". %s" % i)

make_sandwich('Roquefort')
make_sandwich('Jamón','Queso','Tomate')

print("\n-----------")
print("8-14. Cars:") #Write a function that stores information about a car in a dictionary . The function should always receive a 
# manufacturer and a model name . It should then accept an arbitrary number of keyword arguments . Call the function with 
# the required information and two other name-value pairs, such as a color or an optional feature . Your function should work 
# for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly .
print("-----------\n")

def make_car(manufacturer,model,**features):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key,value in features.items():
        car[key] = value

    return car

print(make_car('Renault','Scenic 2', color = 'Dark Blue', year = 2006, AA = True ))
print(make_car('Wolswaven','Suran', color = 'Silver'))





