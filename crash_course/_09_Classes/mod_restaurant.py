# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod- ule . Make a separate file that imports Restaurant . 
# Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is work- ing properly .

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, number_served):

        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("\nThe Restaurant %s has Cuisine: %s\n" % (self.name.title(),self.type.title()))
    
    def open_restaurant(self):
        print("The Restaurant %s is now open!\n" % self.name)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self,inc_number_served):
        self.number_served = self.number_served + inc_number_served

    def show_customers_served(self):
        print("Customers served in %s so far: %s.\n" % (self.name.title(), self.number_served))