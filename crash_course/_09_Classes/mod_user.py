# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178) . Store the classes User, Privileges, and Admin in one module . 
# Create a sepa- rate file, make an Admin instance, and call show_privileges() to show that everything is working correctly .

class User():

    def __init__(self, first_name, last_name, gender, age, login_attempts = 0):

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print("User: %s %s" % (self.first_name.title(),self.last_name.title()))
        print("%s" % self.gender.title())
        print("Age: %s years" % self.age)
        print("Login attemps: %s" % self.login_attempts)

    def greet_user(self):
        print("Hello %s %s, how are you today?" % (self.first_name.title(),self.last_name.title()))
    
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0