class User():
    """a class describing user"""
    def __init__( self , first , last , age , gender ):
        """ initialise info"""  
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender

    def describe_user(self):
        """print summary of user info"""
        print( "First Name: " + self.first_name )
        print( "Last Name: " + self.last_name )
        print( "Age: " + str(self.age) )
        print( "Gender: " + self.gender )

    def greet_user(self):
        """greet user, personalised message"""
        full_name = self.first_name + " " + self.last_name
        print( "Hi " + full_name )

class Admin(User):
    """special class of User"""
    def __init__(self, first , last , age , gender ):
        """initialise attributes of parent class"""
        super().__init__(first , last , age , gender)
        self.privileges = []
        
    def show_privileges(self):
        for privilege in self.privileges:
            print( privilege )
   

#create an admin
admin = Admin( 'nothing' , 'nothing' , 999 , 'none' )
admin.privileges = [ 'can block' , 'can approve' , 'can hide' ]
admin.show_privileges()
