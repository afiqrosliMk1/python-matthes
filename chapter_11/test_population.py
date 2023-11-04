import unittest
from population_functions import city_function 

class CityTestCase( unittest.TestCase ):
    """ dfal;jdfl """
    
    def test_city_country( self ):
        """ adlkfakldjf """
        city_name = city_function( "kulai" , "malaysia" )
        self.assertEqual( city_name , 'Kulai, Malaysia' )

    def test_city_country_population( self ):
        """   adskfl;asdfj"""
        city_name = city_function( "kulai" , "malaysia" , 100000 )
        self.assertEqual( city_name , "Kulai, Malaysia - population=100000" )

unittest.main()
        
        
