import unittest
from city_functions import city_function 

class CityTestCase( unittest.TestCase ):
    """ dfal;jdfl """
    
    def test_city_country( self ):
        """ adlkfakldjf """
        city_name = city_function( "kulai" , "malaysia" )
        self.assertEqual( city_name , 'Kulai, Malaysia' )


unittest.main()
        
        
