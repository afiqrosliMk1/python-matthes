glossary = { 'list' : "can store any data type. Enclosed within []" ,
    'immutable' : "cannot be change." , 
    'tuple' : "immutable list. Enclosed within ()" , 
    'dictionary' : "store value as 'key-value' pair." ,
    'functions' : "code block that only runs when it is called. You can pass argument to it. " ,
    'classes' : "blueprint which object is created."
 }

#replacing these series of print statements with loop
#print( "list: \n" + glossary[ 'list' ] + "\n" )
#print( "immutable: \n" + glossary[ 'immutable' ] + "\n" )
#print( "tuple: \n" + glossary[ 'tuple' ] + "\n" )
#print( "dictionary: \n" + glossary[ 'dictionary' ] + "\n" )
#print( "functions: \n" + glossary[ 'functions' ] + "\n" )
#print( "classes: \n" + glossary[ 'classes' ] + "\n" )

for key, value in glossary.items():
    print( key + " : " + value )

glossary[ 'set' ] = "method that gives a unique list. Use this to avoid duplicate items."
glossary[ 'keys' ] = "use this method to get list of keys from dictionary."
glossary[ 'values' ] = "use this method to get list of values from dictionary."

print( "\n\n" )
for key, value in glossary.items():
    print( key + " : " + value )

   
   
   
   
