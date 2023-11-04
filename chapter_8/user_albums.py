def make_album( artist , title , noOfTracks=0 ):
    album = {}
    album[ 'artist' ] = artist 
    album[ 'title' ] = title
    if noOfTracks:
        album[ 'noOfTracks' ] = noOfTracks
    return album

album_saleem = make_album( 'saleem' , 'tak tahu' , 4 )   
print( album_saleem )

album_rahmat = make_album( 'rahmat' , 'enggak tahu juga' )
print( album_rahmat )

album_mamat = make_album( 'mamat' , 'anything' )
print( album_mamat )

active = True
while active: 
    print( "enter 'quit' to end " )
    artist = input( "Enter artist name: " )
    if artist == 'quit':
            break
    title = input( "Enter title " )
    if title == 'quit':
            break
    created_album =  make_album( artist , title )

    print( created_album )
    
