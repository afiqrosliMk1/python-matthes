favorite_places = { 'ali' : ['amerika' , 'bangladesh' , 'antartika' ] , 
    'abu' : [ 'sri lanka' , 'manila' , 'hong kong' ] ,
    'ahmad' : [ 'pakistan' , 'myanmar' , 'kuala lumpur'] }

for key, value in favorite_places.items():
    print( key + "'s favorite places are: " )
    for place in value:
        print( place )
    print( "\n" )

