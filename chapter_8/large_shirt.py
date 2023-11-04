def make_shirt( size = "L" , text = "I love Python" ):
    print( "shirt size: " + size )
    print( "printed text: " + text )

make_shirt()
make_shirt( 'M' )
make_shirt( 'L' , 'Vim Advocate' )
make_shirt( text =  "Another Vim advocate" , size = 'S' ) 
