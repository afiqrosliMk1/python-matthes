#favorite_languages = {
#    'jen' : 'python' ,
#    'sarah' : 'c' ,
#    'edward' : 'ruby' ,
#    'phil' : 'python' , 
#    }
#
#for name, language in favorite_languages.items():
#    print( name.title() + "'s favorite language is " + 
#        language.title() + "." )
#
##demonstrating looping through only key values
#for name in favorite_languages.keys():
#    print( name.title() )
#
#friends = [ 'phil' , 'sarah' ]
#for name in favorite_languages.keys():
#    print( name.title() )
#
#    if name in friends:
#        print( " Hi " , name.title() + 
#            ", I see your favorite language is " +
#            favorite_languages[ name ].title() + "!" )
#
#if 'erin' not in favorite_languages.keys():
#    print( "Erin , please take our poll!" )
#
#
##looping through all values in a dictionary
#print( "\nThe following languages has been mentioned" )
#
#for language in favorite_languages.values():
#    print( language.title() ) #this will print 'python' two times. to make sure no repetition, use 'set' (see below)
#
##using set to get unique value
#print( "\ndemonstrating 'set'\n" )
#for language in set( favorite_languages.values() ):
#    print( language.title() )

###################demonstrating list inside a dictionary########################3

favorite_languages = {
    'jen' : [ 'python' , 'ruby' ] ,
    'sarah' : [ 'c' ] ,
    'edward' : [ 'ruby' , 'go' ] ,
    'phil' : [ 'python' , 'haskell' ] , 
    }

for name , languages in favorite_languages.items():
    if len( languages ) < 2:
        print( name + "'s favorite language is: " )
        for language in languages:
           print( language )
    else:
        print( name + "'s favorite languages are: " )
        for language in languages:
	         print( language )
