class Restaurant():
    """a restaurant"""

    def __init__( self , name , cuisine ):
        """Initialise dfadf and adfadf"""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print( "Welcome to " + self.restaurant_name + " , we serve " + self.cuisine_type )

    def open_restaurant(self):
        print( "WE ARE OPEN!" )

    def set_number_served(self , number ):
        """set the number of customer served"""
        self.number_served = number

    def increment_number_served( self , number):
        """increment the number of customer served"""
        self.number_served += number 

restaurant = Restaurant( 'kedai tok wok' , 'teh')
restaurant.describe_restaurant()
print( "number of customer served " + str(restaurant.number_served) )
restaurant.set_number_served( 2 )
print( "number of customer served " + str(restaurant.number_served) )
restaurant.increment_number_served( 10 )
print( "number of customer served " + str(restaurant.number_served) )


