class Employee():
    """ afja;ld """
    def __init__(self, first , last , salary):
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary
 
    def give_raise( self , increment=5000 ):
        self.annual_salary += increment
        return self.annual_salary

    def describe_employee( self ):
        print( "first name: " + self.first_name )
        print( "last name: " + self.last_name )
        print( "annual salary: " + str(self.annual_salary) )
 
    def auto_raise( self ):
        self.give_raise()
