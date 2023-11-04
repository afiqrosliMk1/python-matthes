requested_toppings = []

#when name of a list is used in an if statement, 
#python returns True if the list contains at least
#one item, and empty list evaluates to False

if requested_toppings:
    for requested_toppings in requested_toppings:
        print( "Adding " + requested_topping + "." )
    print( "\nFinished making your pizza!" )
else:
    print( "Are you sure you want a plain pizza?" )
