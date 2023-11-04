import json

filename = 'favorite_number.json'

try:
    with open( filename ) as file_obj:
         number = json.load( file_obj )

except FileNotFoundError:
    print( "file tak ada" )


else:
    print( "I know your favorite number is " + str(number) )
