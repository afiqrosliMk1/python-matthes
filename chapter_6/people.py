person1 = { 'first_name' : 'afiq' , 'last_name' : 'rosli' ,
    'age' : 28 , 'city' : 'jb' }

person2 = { 'first_name' : 'muhammad' , 'last_name' : 'x' ,
    'age' : 70 , 'city' : 'uganda' }

person3 = { 'first_name' : 'din' , 'last_name' : 'naga' ,
    'age' : 99 , 'city' : 'takbai' }

people = [ person1 , person2 , person3 ]

for person in people:
    for key, value in person.items():
        print( key + " : " + str( value ) ) 
    print( "\n" )


#print( "name: " + person[ 'first_name' ] )
#print( "last name: " + person[ 'last_name' ] )
#print( "age: " + str(person[ 'age' ]) )
#print( "city: " + person[ 'city' ] )
