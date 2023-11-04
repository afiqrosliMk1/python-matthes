class Restaurant():
    """a restaurant class"""

    def __init__( self , name , cuisine ):
        """Initialise dfadf and adfadf"""
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print( "Welcome to " + self.restaurant_name + " , we serve " + self.cuisine_type )

    def open_restaurant(self):
        print( "WE ARE OPEN!" )

