#def build_profile( first , last , **user_info ):
#    """Build a dictionary containing everything we know about a user"""
#    profile = {}
#    profile[ 'first name' ] = first
#    profile[ 'last name' ] = last
#    for key , value in user_info.items():
#        profile[ key ] = value
#    return profile
#
#user_profile = build_profile( 'albert' , 'einstein' ,
#                              location='princeton' ,
#                              field='physics' )
#
#print( user_profile )

def build_profile( first , last , **user_info ):
    #create a blank dictionary
    profile = {}
    profile[ 'first name ' ] = first
    profile[ 'last name ' ] = last

    #loop every item in dict user info {} and store it in profile {} dict
    for key , value in user_info.items():
        profile[ key ] = value
    
    return profile


my_profile = build_profile( 'afiq' , 'rosli' , age = 28 , gender = 'male' )
print( my_profile )
