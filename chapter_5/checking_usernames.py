current_users = [ "ali" , "abu" , "ahseng" , "ahmad" , "pokya" , "husin" ]
new_users = [ "ALI" , "abU" , "samad" , "wokyoh" , "stopa" ]

print( current_users )

for new_user in new_users:
    if new_user.lower() in current_users:
        print( new_user + " : this username has already been used" )
    else:
        print( new_user + " : this username is available" )
