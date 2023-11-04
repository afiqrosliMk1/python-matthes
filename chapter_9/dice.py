from random import randint

class Die():
    """ a dice"""

    def __init__( self , sides=6 ):
        self.sides = sides

    def roll_die( self ):
        x = randint( 1 , self.sides )
        print( "try: " + str(count) + "---> " + str(x) )


my_die = Die(10)
for count in range(1,11):
    my_die.roll_die()

my_die = Die(20)
for count in range(1,11):
    my_die.roll_die()

