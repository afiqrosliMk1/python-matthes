toppings = []
selection = ""
active = True

while active:
    selection = input( "What topping do you want?" )
    if selection == 'quit':
        active = False
    else:
        print( "I will add " + selection + " to your pizza" )
        toppings.append( selection )

for topping in toppings:
    print( topping)
