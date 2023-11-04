class Restaurant():
    """a restaurant"""

    def __init__( self , name , cuisine ):
        """Initialise dfadf and adfadf"""
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print( "Welcome to " + self.restaurant_name + " , we serve " + self.cuisine_type )

    def open_restaurant(self):
        print( "WE ARE OPEN!" )

class IceCreamStand(Restaurant):
    """inherit from Restaurant Class"""
    
    def __init__( self , name , cuisine='ice cream' ):
        """
        Initialize attributes of the parent class. 
        Then add additional attributes specific to IceCreamStand
        """
        super().__init__( name , cuisine )
        self.flavors = [ 'coklat' , 'vanilla' ]

    def display_flavors( self ):
        """display list of available flavors"""
        print( "Perisa: " )
        for flavor in self.flavors:
            print( flavor )
        print( "***end**" )

aiskrimPokLi = IceCreamStand( 'Ais Krim PokLi' , 'Aiskrim' )
aiskrimPokLi.display_flavors()
#adding flavors
aiskrimPokLi.flavors.append('durian')
aiskrimPokLi.display_flavors()
