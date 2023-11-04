def make_sandwich( *toppings ):
    if toppings: 
        for topping in toppings:
           print( topping ) 


make_sandwich( 'tuna' , 'pepperoni' , 'beef' )
make_sandwich()
make_sandwich( 'tuna' )
