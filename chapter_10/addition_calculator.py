#first try
#a = input( "enter first number: " )
#b = input( "enter second number: " ) 
#
#
#try:
#    sum = int(a) + int(b)
#    print( "sum = " + str(sum) )
#
#except TypeError:
#    print( "key in numbers only!" )
#


#second try
flag = True

while(flag):
    try:
        print( "--(quit) to end--\n" )
        a = input("enter first number: " ) 
        if (a == 'quit'):
            flag = False 
        else: 
            a = int(a)
            b = input( "enter second number: " )
            if ( b == 'quit' ):
                flag = False
            else:
                b = int(b)
    
    except ValueError:
        print( "Key in a number only!" )
    
    else:
        if ( flag == True ):
            sum = a + b
            print( "sum = " + str(sum) )
