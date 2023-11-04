active = True
places = {}
prompt1 = "Enter your name: " 
prompt2 =  "If you could visit one place in the world, where would you go? : "

while active:
    user = input( prompt1 )
    if user == 'quit':
        break

    place = input( prompt2 )
    places[ user ] = place

print( "\n" )
for key , value  in places.items():
    print("user: " + key +  " , dream place: " +  value )
