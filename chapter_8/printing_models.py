##start with some designs that need to be printed
#unprinted_designs = [ 'iphone case' , 'robot pendant' , 'dodecahedron' ]
#completed_models = []
#
##simulate printing each design , until none are left
##move each design to completed models after printing
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#
#    #simulate creating a 3D print from the design
#    print( "Printing models: " + current_design )
#    completed_models.append( current_design )
#
##display all completed models
#print( "\nThe following models have been printed: " )
#for completed_model in completed_models:
#    print( completed_model )
#

import print_functions

def show_completed_models( completed_models ):
    """Show all the models that were printed"""
    print( "\nThe following models have been printed: ")
    for completed_model in completed_models:
        print( completed_model )


unprinted_designs = [ 'iphone case' , 'robot pendant' , 'dodecahedron' ]
completed_models = []

# [:] slice in function call below shows how to pass list by value
# so that the original list doesn't change
# this however, is less efficient and slower
print_functions.print_models( unprinted_designs[:] , completed_models )
show_completed_models( completed_models )
print( unprinted_designs )
