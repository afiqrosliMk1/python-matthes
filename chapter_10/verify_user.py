import json

def get_stored_username():
    """Get stored username if available."""

    filename = 'username.json' 
    try:
        #default for open() is 'r'
        with open(filename) as f_obj:
            username = json.load(f_obj) 
    
    except FileNotFoundError:
        return None
    
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    filename = 'username.json'

    username = input("What is your name? ")
    with open(filename , 'w') as f_obj:
        json.dump(username , f_obj)
    return username


def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    if username:
        print( "username : " + username + "\nIs this correct username?" )
        verify = input( "y/n?")
        if (verify == "y" ):
            print( "Welcome back, " + username + "!" ) 
        else:
            get_new_username()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!" )


greet_user()
