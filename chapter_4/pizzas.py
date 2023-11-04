pizzas = [ 'chicken' , 'pepperoni' , 'beef' ]
#friend's pizzas is added after excercise 4-10 pg 102
friend_pizzas = pizzas[:]

#add pizzas
pizzas.append( 'vege' )
friend_pizzas.append( 'tuna' )

#print my pizzas
for pizza in pizzas:
    print( "I like " +  pizza + " pizza" )

print( pizzas[ 0 ] + " is great!" )
print( pizzas[ 1 ] + " always amazing" )
print( pizzas[ 2 ] + " is the best!" )
print( "I really love pizza!" )

#print friend's pizzas
print( "my friend likes" )
for pizza in friend_pizzas:
    print( pizza )
