dimensions = ( 200 , 50 )
#try to change tuple value will result in error
#dimensions[ 0 ] = 250

print( "Original dimensions:" )
for dimension in dimensions:
    print( dimension )

dimensions = ( 400 , 100 )
print( "\nModified dimensions:" )
for dimension in dimensions:
    print( dimension )


