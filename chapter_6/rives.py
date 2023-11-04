rivers = { 'nile' : 'egypt' , 'kelantan' : 'malaysia' , 'mekong' : 'thailand' }

for key, value in rivers.items():
    print( "The " + key.title() + " runs through " + value.title() + "." )

print( "\nList of rivers: " )
for river in rivers.keys():
    print( river )

print( "\nList of countries: " )
for countries in rivers.values():
    print( countries )
