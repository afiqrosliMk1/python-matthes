my_foods = [ 'pizza' , 'falafel' , 'carrot cake' ]
#friends_foods = my_foods[:] #this is how you copy lists!
friends_foods = my_foods #this is how you do it!

print( "My favorite foods are:" )
print( my_foods )

print( "\nMy friend's favorite foods are:" )
print( friends_foods )

my_foods.append( 'cannoli' )
friends_foods.append( 'ice cream' )

print( "My favorite foods are:" )
print( my_foods )

print( "\nMy friend's favorite foods are:" )
print( friends_foods )

#printing with loop
print( "\nprint again with for loop\n" )

for food in my_foods:
    print( food )

for food in friends_foods:
    print( food )
