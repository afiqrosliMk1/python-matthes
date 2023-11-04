toppings = []
selection = ""

while selection != 'quit':
    selection = input( "What topping do you want?" )
    if selection != 'quit':
        print( "I will add " + selection + " to your pizza" )
        toppings.append( selection )

for topping in toppings:
    print( topping)
