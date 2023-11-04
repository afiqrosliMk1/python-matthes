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
   
#creating multiple users
ahmad = User( 'Ahmad' , 'Maslan' , 65 , 'Male' )
najib = User( 'Najib' , 'Razak' , 69 , 'Male' )
anwar = User( 'Anwar' , 'Ibrahim' , 70 , 'Male' )

ahmad.describe_user()
ahmad.greet_user()

najib.describe_user()
najib.greet_user()

anwar.describe_user()
anwar.greet_user() 
