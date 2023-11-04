usernames = [ "afiq" , "muhammad" , "rosli" , "admin" , "naga" , "din" ]
#usernames = []

if usernames:
	for username in usernames:
		 if username == 'admin' :
			  print( "Hello admin , would you like to see a status report?" )
		 else:
			  print( "Hello " + username + " thank you for logging in again" )
else:
   print( "empty list" )
