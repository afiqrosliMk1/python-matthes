car = 'subaru'
print( "Is car == 'subaru'? I predict True." )
print( car == 'subaru' )

print( "\nIs car == 'audi'? I predict False." )
print( car == 'audi' )
print( "\n" )

##################################################
brands = ( 'honda' , 'toyota' , 'tesla' , 'volkswagen' )

for brand in brands:
    if brand.lower() == "tesla":
        print( brand + " is overrated" )
    else:
        print( brand + " is good" )
##################################################
if len( car ) >= 2:
    print( "length greater than 2" )

print( car.lower() == car.upper() )
print( brands[ 0 ] == car )

print( brands[ -1 ] == 'volkswagen' )
print( brands[ -2 ].lower() == 'tesla')

##################################################
print( "brands[ 0 ] ==  honda and brands[ 1 ] == toyota" )
print( brands[ 0 ] == 'honda' and brands[ 1 ] == 'toyota' )

print( "volkswagen in the list?" )
print( 'volkswagen' in brands )

print( "mitsubishi in the list?" )
print( 'mitsubishi' in brands )

print( "honda not in the list?" )
print( 'honda' not in brands )

print( "rivian or tesla in the list?" )
print( 'rivian' in brands or 'tesla' in brands )
