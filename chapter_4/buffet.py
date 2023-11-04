buffets = ( 'nasi' , 'kambing' , 'mee' , 'kuih' , 'air' ) 

print( "Original menu: ")
for buffet in buffets:
    print( buffet )

#attempt to modify individual tuple element will result in a error
#buffets[ -1 ] = 'buah'

#modify the whole tuple is however, allowed
print( "\nUpdated menu: " )
buffets = ( 'nasi' , 'kambing' , 'chicken chop' , 'kuih' , 'buah' ) 
for buffet in buffets:
    print( buffet )
