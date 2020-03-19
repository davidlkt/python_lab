# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module . 
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly .

from mod_user import User

class Privileges():
    def __init__(self,privileges):

        self.privileges = privileges
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(". %s" % privilege)

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, privs, login_attempts=0):
        super().__init__(first_name, last_name, gender, age, login_attempts)

        self.privileges = Privileges(privs)