def show_magicians( name_list ):
    for name in name_list:
        print( name )

def make_great( name_list ):
    for count in range( 0 , len(name_list) ):
        name_list[ count ] = "Great " + name_list[ count ]


magicians = [ 'din' , 'naga' , 'afiq' , 'rosli' ]

show_magicians( magicians )
make_great( magicians )
show_magicians( magicians )
