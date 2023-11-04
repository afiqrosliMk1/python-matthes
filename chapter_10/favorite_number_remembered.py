import json

filename = "favorite_number.json"

try:
    with open( filename ) as file_obj:
         number = json.load( file_obj )

except FileNotFoundError:
    with open(filename , 'w' ) as file_obj:
        number = input("enter your favorite number: ")
        json.dump( number , file_obj )
        print( "We will remember " + str(number) + " next time!" )
    
else:
    print( "I know your favorite number is " + str(number) )
