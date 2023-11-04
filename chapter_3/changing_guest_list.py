guests = [ "van nistelrooy" , "cr7" , "najib bossku" , "frank whittle" ]

print( guests[ 0 ].title() + " , please come to dinner" )
print( guests[ 1 ].title() + " , please come to dinner" )
print( guests[ 2 ].title() + " , please come to dinner" )
print( guests[ 3 ].title() + " , please come to dinner" )

cannot_attend = guests.pop( 2 )
print( cannot_attend + " can't make it" )

guests.insert( 2 , "bangnon" )

print( guests[ 0 ].title() + " , please come to dinner" )
print( guests[ 1 ].title() + " , please come to dinner" )
print( guests[ 2 ].title() + " , please come to dinner" )
print( guests[ 3 ].title() + " , please come to dinner" )
