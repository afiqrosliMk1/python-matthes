guests = [ "van nistelrooy" , "cr7" , "najib bossku" , "frank whittle" ]

print( guests[ 0 ].title() + " , please come to dinner" )
print( guests[ 1 ].title() + " , please come to dinner" )
print( guests[ 2 ].title() + " , please come to dinner" )
print( guests[ 3 ].title() + " , please come to dinner" )

cannot_attend = guests.pop( 2 )
print( cannot_attend + " can't make it" )
print( "*current no of guest:" + str( len(guests) ) )

guests.insert( 2 , "bangnon" )

print( guests[ 0 ].title() + " , please come to dinner" )
print( guests[ 1 ].title() + " , please come to dinner" )
print( guests[ 2 ].title() + " , please come to dinner" )
print( guests[ 3 ].title() + " , please come to dinner" )
print( "*current no of guest:" + str( len(guests) ) )

print( "I HAVE FOUND A BIGGER TABLE!" )

guests.insert( 0 , "mark zuckerberg" )
guests.insert( 2 , "mas elon" )
guests.append( "halim napi" )

print( guests[ 0 ].title() + " , please come to dinner" )
print( guests[ 1 ].title() + " , please come to dinner" )
print( guests[ 2 ].title() + " , please come to dinner" )
print( guests[ 3 ].title() + " , please come to dinner" )
print( guests[ 4 ].title() + " , please come to dinner" )
print( guests[ 5 ].title() + " , please come to dinner" )
print( guests[ 6 ].title() + " , please come to dinner" )
print( "*current no of guest:" + str( len(guests) ) )



