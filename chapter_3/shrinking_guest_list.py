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

print( "\n\nI AM SO SORRY TO INFORM THAT THE DINNER TABLE WON'T ARRIVE IN TIME. ONLY TWO GUESTS CAN ATTEND" )

cannot_invite = guests.pop()
print( cannot_invite + ", I'm sorry you cannot attend" ) 
cannot_invite = guests.pop()
print( cannot_invite + ", I'm sorry you cannot attend" ) 
cannot_invite = guests.pop()
print( cannot_invite + ", I'm sorry you cannot attend" ) 
cannot_invite = guests.pop()
print( cannot_invite + ", I'm sorry you cannot attend" ) 
cannot_invite = guests.pop()
print( cannot_invite + ", I'm sorry you cannot attend" ) 

print(guests[0].title() + " , please come, you are still invited" )
print(guests[1].title() + " , please come, you are still invited" )
del guests[ 0 ]
del guests[ 0 ]

print("guests list after del")
print( guests )
