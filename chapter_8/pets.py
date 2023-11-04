###DEMONSTRATE POSITIONAL ARGUMENT
#def describe_pet( animal_type , pet_name ): 
#   """display information about a pet""" 
#   print( "\nI have a " + animal_type + "." )
#   print( "My " + animal_type + " 's name is " + pet_name.title() + "." )
#
#describe_pet( 'kucing' , 'cekbob' )


#DEMONSTRATE KEYWORD ARGUMENTS 
#def describe_pet( animal_type , pet_name ):  
#   """display information about a pet""" 
#   print( "\nI have a " + animal_type + "." )
#   print( "My " + animal_type + " 's name is " + pet_name.title() + "." )
#
#describe_pet( animal_type='kucing' , pet_name='cekbob' )
#

#DEMONSTRATE DEFAULT VALUE
#note that default argument should appear last, 
#so that python can continue to interpret positional argument
def describe_pet( pet_name , animal_type='dog' ):
    """Display information about a pet."""
    print( "\nI have a " + animal_type + "." )
    print( "My " + animal_type + "'s name is " + pet_name.title() + "." )

#describe_pet( pet_name='willie' )
#describe_pet( 'bob' )
#describe_pet( animal_type='cat' , pet_name='bob' )
#describe_pet( pet_name='bob' )
describe_pet()
