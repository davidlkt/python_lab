print("\n-----------")
print("9-3. Users:") #Make a class called User . Create two attributes called first_name and last_name, and then create several other 
# attributes that are typically stored in a user profile . Make a method called describe_user() that prints a summary of the 
# user’s information . Make another method called greet_user() that prints a personalized greeting to the user .
print("-----------\n")

from mod_user import User
from mod_admin import Privileges, Admin

user_1 = User('david','carbone','male', 42)
user_2 = User('lucía', 'carbone', 'female', 13)
user_3 = User('santiago', 'carbone', 'male', 7)

user_1.greet_user()
user_1.describe_user()
user_2.greet_user()
user_2.describe_user()
user_3.greet_user()
user_3.describe_user()


print("\n-----------")
print("9-5. Login Attempts:") #Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166) . Write a method 
# called increment_ login_attempts() that increments the value of login_attempts by 1 . Write another method called 
# reset_login_attempts() that resets the value of login_ attempts to 0 .
# Make an instance of the User class and call increment_login_attempts() several times . Print the value of login_attempts to 
# make sure it was incremented properly, and then call reset_login_attempts() . Print login_attempts again to make sure it was 
# reset to 0
print("-----------\n")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.describe_user()
user_1.reset_login_attempts()
user_1.describe_user()


print("\n-----------")
print("9-7. Admin:") #An administrator is a special kind of user . Write a class called Admin that inherits from the User class you wrote 
# in Exercise 9-3 (page 166) or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list of strings like 
# "can add post", "can delete post", "can ban user", and so on . Write a method called show_privileges() that lists the 
# administrator’s set of privileges . Create an instance of Admin, and call your method .
print("-----------\n")
print("\n-----------")
print("9-8. Privileges:") #Write a separate Privileges class . The class should have one attribute, privileges, that stores a list of strings as 
# described in Exercise 9-7 . Move the show_privileges() method to this class . Make a Privileges instance as an attribute in the Admin class . 
# Create a new instance of Admin and use your method to show its privileges .
print("-----------\n")


user_admin = Admin('david','carbone','male', 42, ['can add post', 'can delete post', 'can ban user'])

user_admin.privileges.show_privileges()