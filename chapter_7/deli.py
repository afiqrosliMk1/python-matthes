sandwich_orders = [ 'cheese' , 'tuna' , 'sardine' , 'mayo' ]
finished_orders = []

while sandwich_orders:
    finish = sandwich_orders.pop()
    print( "I made your " + finish + " sandwich" )
    finished_orders.append( finish )

print( finished_orders )
