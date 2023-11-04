class Restaurant():
    """a restaurant"""

    def __init__( self , name , cuisine ):
        """Initialise dfadf and adfadf"""
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print( "Welcome to " + self.restaurant_name + " , we serve " + self.cuisine_type )

    def open_restaurant(self):
        print( "WE ARE OPEN!\n" )

kedai = Restaurant( 'Kedai Wok' , 'Teh' )
print( kedai.restaurant_name.title() )
kedai.describe_restaurant() 
kedai.open_restaurant()

kedai_make = Restaurant( 'Kedai Make' , 'Nasi Kerabu' )
print( kedai_make.restaurant_name.title() )
kedai_make.describe_restaurant()
kedai_make.open_restaurant()

kedai_sate = Restaurant( 'Kedai Sate' , 'sate' )
print( kedai_sate.restaurant_name.title() )
kedai_sate.describe_restaurant()
kedai_sate.open_restaurant()
