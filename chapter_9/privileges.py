from multiple_module import User

class Admin(User):
    """special class of User"""
    def __init__(self, first , last , age , gender ):
        """initialise attributes of parent class"""
        super().__init__(first , last , age , gender)
        self.privileges = Privileges()
        

class Privileges():
    """separate class for Privileges to store what an admin can do"""
    def __init__(self):
        """initialise Privileges attributes"""
        self.privileges = [] 
   
    def show_privileges(self):
        """show privileges"""
        for privilege in self.privileges:
            print( privilege )
