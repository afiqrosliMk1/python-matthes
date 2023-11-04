favorite_numbers = { "ali" : [ 8 , 88 ] , "abu" : [ 99 , 100 ] , "ahmad" : [ 46 , 77 ] , "jamal" : [ 0 , 22 ] , "pokya" : [ 1 , 70 ] }

for key , value in favorite_numbers.items():
    print( key + "'s favorite numbers: " )
    for number in value:
        print( str( number ) )

#print( "ali's favorite number: " + str(  favorite_numbers[ 'ali' ] ) )
#print( "abu's favorite number: " + str(  favorite_numbers[ 'abu' ] ) )
#print( "ahmad's favorite number: " + str(  favorite_numbers[ 'ahmad' ] ) )
#print( "jamal's favorite number: " + str(  favorite_numbers[ 'jamal' ] ) )
#print( "pokya's favorite number: " + str(  favorite_numbers[ 'pokya' ] ) )
