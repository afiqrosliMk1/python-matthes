def make_pizza( size , *toppings ):
    """Print the list of toppings that have been requested"""
    print( "Making a " + str( size ) +
           "-inch pizza  with the following toppings: " )
    for topping in toppings:
        print( "- " + topping ) 

#make_pizza( 16 , 'pepperoni' )
#make_pizza( 12 , 'mushrooms' , 'green peppers' , 'extra cheese' )


