#import entire module
#import cars_function
#
#car1 = cars_function.make_car( 'subaru' , 'outback ' , color='blue' , tow_package=True )
#car2 = cars_function.make_car( 'honda' , 'civic ' , color='blue' )
#car3 = cars_function.make_car( 'toyota' , 'GR Corolla' )
#print( car1 )
#print( car2 )
#print( car3 )

#import specific function
#from cars_function import make_car
#
#car1 = make_car( 'subaru' , 'outback ' , color='blue' , tow_package=True )
#car2 = make_car( 'honda' , 'civic ' , color='blue' )
#car3 = make_car( 'toyota' , 'GR Corolla' )
#print( car1 )
#print( car2 )
#print( car3 )

#import specific function AND give function an alias
#from cars_function import make_car as mc
#
#car1 = mc( 'subaru' , 'outback ' , color='blue' , tow_package=True )
#car2 = mc( 'honda' , 'civic ' , color='blue' )
#car3 = mc( 'toyota' , 'GR Corolla' )
#print( car1 )
#print( car2 )
#print( car3 )

#import module AND give the module and alias

#import cars_function as cf
#
#car1 = cf.make_car( 'subaru' , 'outback ' , color='blue' , tow_package=True )
#car2 = cf.make_car( 'honda' , 'civic ' , color='blue' )
#car3 = cf.make_car( 'toyota' , 'GR Corolla' )
#print( car1 )
#print( car2 )
#print( car3 )

#import all function in module
from cars_function import *

car1 = make_car( 'subaru' , 'outback ' , color='blue' , tow_package=True )
car2 = make_car( 'honda' , 'civic ' , color='blue' )
car3 = make_car( 'toyota' , 'GR Corolla' )
print( car1 )
print( car2 )
print( car3 )


