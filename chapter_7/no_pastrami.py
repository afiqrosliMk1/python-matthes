sandwich_orders = [ 'cheese' , 'pastrami' , 'tuna' , 'pastrami' , 'pastrami' , 'sardine' , 'mayo' ]
finished_orders = []

print( "The deli has run out of pastrami" )
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove( 'pastrami' )

while sandwich_orders:
    finish = sandwich_orders.pop()
    print( "I made your " + finish + " sandwich" )
    finished_orders.append( finish )

print( finished_orders )
