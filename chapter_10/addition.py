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

try:
    a = input("enter first number: " )
    a = int(a)
  
    b = input( "enter second number: " )
    b = int(b)

except ValueError:
    print( "Key in a number only!" )

else:
    sum = a + b
    print( "sum = " + str(sum) )
