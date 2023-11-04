favorite_languages = {
    'jen' : 'python' ,
    'sarah' : 'c' ,
    'edward' : 'ruby' ,
    'phil' : 'python' , 
    }

people_should_poll = [ 'jen' , 'ali' , 'sarah' , 'edward' , 'erin' , 'phil' , 'samsul' , 'johnny' ]

for name, language in favorite_languages.items():
    print( name.title() + "'s favorite language is " + 
        language.title() + "." )

#demonstrating looping through only key values
for name in favorite_languages.keys():
    print( name.title() )

friends = [ 'phil' , 'sarah' ]
for name in favorite_languages.keys():
    print( name.title() )

    if name in friends:
        print( " Hi " , name.title() + 
            ", I see your favorite language is " +
            favorite_languages[ name ].title() + "!" )

#if 'erin' not in favorite_languages.keys():
#    print( "Erin , please take our poll!" )


#looping through all values in a dictionary
print( "\nThe following languages has been mentioned" )

for language in favorite_languages.values():
    print( language.title() ) #this will print 'python' two times. to make sure no repetition, use 'set' (see below)

#using set to get unique value
print( "\ndemonstrating 'set'\n" )
for language in set( favorite_languages.values() ):
    print( language.title() )

#lines below added for 6-6 polling.py
for people in people_should_poll:
    if people in favorite_languages.keys():
        print( "thanks " + people + " for reponding!" )
    else:
        print( people + " , please take our poll!" )

   
