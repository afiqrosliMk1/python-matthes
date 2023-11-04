places_to_visit = [ "melaka" , "sabah" , "sarawak" , "cameron" , "penang" , "thailand" ]
print( places_to_visit )

print( "sorted order\n" )
print( sorted(places_to_visit) )

print( "original order\n" )
print( places_to_visit ) 

print( "reversed order\n" )
print( sorted( places_to_visit , reverse=True ) )

print( "original order\n" )
print( places_to_visit )

print( "permanent reverse\n" )
places_to_visit.reverse()
print( places_to_visit )

#reverse once more to get the original order
places_to_visit.reverse()
print( "after reverse once more\n" )
print( places_to_visit )

#sort permanently
places_to_visit.sort()
print("sort permanently in alphabetical order")
print( places_to_visit )

#sort again but in reverse aplhabetical order
places_to_visit.sort(reverse=True)
print( "sorted in reverse alphabetical order" )
print( places_to_visit )
