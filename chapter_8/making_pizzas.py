###############demonstrating importing entire module (pizza.py)############
#import pizza
#
#pizza.make_pizza( 16 , 'pepperoni' )
#pizza.make_pizza( 12 , 'mushrooms' , 'green peppers' , 'extra cheese' )

#######3demonstrating importing specific function###############
from pizza import make_pizza

#note that if you import specific function
#"pizza." is not needeed
#make_pizza( 16 , 'pepperoni' )
#make_pizza( 12 , 'mushrooms' , 'green peppers' , 'extra cheese' )

#############using 'as' to give function an alias##############3
#from pizza import make_pizza as mp
#
#mp( 16 , 'pepperoni' )
#mp( 12 , 'mushrooms' , 'green peppers' , 'extra cheese' )

##############using 'as' to give module an alias############3
#import pizza as p 
#p.make_pizza( 16 , 'pepperoni' )
#p.make_pizza( 12 , 'mushrooms' , 'green peppers' , 'extra cheese' )

############demonstrating import all functions in a module#########
##best to avoid this approach
from pizza import *
make_pizza( 16 , 'pepperoni' )
make_pizza( 12 , 'mushrooms' , 'green peppers' , 'extra cheese' )



