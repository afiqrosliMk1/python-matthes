import unittest
from employee import Employee

class TestEmployee( unittest.TestCase ):
    """kadj;fa """
    def setUp(self):
        """ lkfaldfj adf """
        self.employee1 = Employee( 'din' , 'naga' , 50000 )        

    def test_give_default_raise(self):
        """ alkdjfa;ldfj  """
        self.employee1.give_raise()
        self.assertEqual( self.employee1.annual_salary , 55000 )

    def test_give_custom_raise(self):
        """f a;ldfj"""
        self.employee1.give_raise( 12000 )
        self.assertEqual( self.employee1.annual_salary , 62000 )

unittest.main()

