def show_magicians( name_list ):
    for name in name_list:
        print( name )

def make_great( name_list ):
    #changed_list = []
    #while name_list:
    #    changed_name = "great " + name_list.pop()
    #    changed_list.append( changed_name )
    for count in range( 0 , len(name_list) ):
        name_list[ count ] = "Great " + name_list[ count ]
    return name_list

magicians = [ 'din' , 'naga' , 'afiq' , 'rosli' ]

show_magicians( magicians )
great_name = make_great( magicians[:] )
show_magicians( magicians )
show_magicians( great_name )
