cubes = [ value ** 3 for value in range( 1 , 11) ]
print ( cubes ) 
#for value in range( 1 , 11 ):
    #cube = value ** 3
    #cubes.append( cube )

#for cube in cubes:
    #print( cube)

item = cubes[ :3 ]
print( "\nThe first three items in the list are: " )
for value in item:
    print( value )

item = cubes[ 4:7 ]
print( "\nThe first three items from the middle the list are: " )
for value in item:
    print( value )

item = cubes[ -3: ]
print( "\nThe last three items in the list are: " )
for value in item:
    print( value )

