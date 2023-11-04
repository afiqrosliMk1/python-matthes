cities = { 'kl' : { 'country' : 'malaysia' ,  'population' : 200000 , 'fact' : 'capital city' } , 
    'kb' : { 'country': 'malaysia' , 'population' : 30000 , 'fact' : 'capital of kelantan' } , 
    'jb' : { 'country' : 'malaysia' , 'population' : 120000 , 'fact' : 'capital of johor' }  }

for city , info in cities.items():
    print( city )
    for key , value in info.items():
        print( key + " : " + str( value ) )
    print( "\n" ) 
