active = True

while active:
    age = input( "\nEnter your age, enter 'quit' to end : " )
    if age == 'quit':
        break
    else:
        age = int( age )
        if ( age < 3 ):
            print( "Free of charge." ) 
        elif ( age >= 3 and age <= 12 ):
            print( "price RM10" )
        elif ( age >= 12 and age <= 120 ):
            print( "price RM15" )
        elif ( age == 'quit' ):
            active = False 
        else:
            print( "Invalid age" ) 
