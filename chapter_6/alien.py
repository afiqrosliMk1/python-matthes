##############################START OF FIRST PART###########################
#alien_0 = { 'color' : 'green' , 'points' : 5 }
##alien_0 = {}
#
#print( alien_0[ 'color' ] )
#print( alien_0[ 'points' ] )
#
#alien_0[ 'x_position' ] = 0
#alien_0[ 'y_position' ] = 25
#print( alien_0 )
#
##print( type( alien_0 )
#
##demonstrate modifying value
#print( "The alien is " + alien_0[ 'color' ] )
#
#alien_0[ 'color' ] = 'yellow'
#print( "The alien is " + alien_0[ 'color' ] )


##############################START OF SECOND PART###########################
#alien_0 = { 'x_position' : 0 , 'y_position' : 25 , 'speed' : 'medium' , 'points' : 5 }
#print( "Original x-position: " + str( alien_0[ 'x_position' ] ) )
#
##move alien to the right
##determine how far to move the alien based on its current speed
#if alien_0[ 'speed' ] == 'slow' :
#    x_increment = 1
#elif alien_0[ 'speed' ] == 'medium' :
#    x_increment = 2
#else:
#    # this must be a fast alien
#    x_increment = 3
#
##the new position is the old position plus the increment
#alien_0[ 'x_position' ] = alien_0[ 'x_position' ] + x_increment
#
#print( "New x-position: " + str( alien_0[ 'x_position' ] ) ) 
#
#print( alien_0 )
#del alien_0[ 'points' ]
#print( alien_0 )
#

##############################START OF THIRD PART###########################
######FROM NESTING - A LIST OF DICTIONARIES ################################

#make and empty list for storing aliens.
aliens = []

#make 30 green aliens
for alien in range( 30 ):
    new_alien = { 'color' : 'green' , 'points' : 5 , 'speed' : 'slow' }
    aliens.append( new_alien )

for alien in aliens[ 0 : 3 ]:
    if alien[ 'color' ] == 'green':
        alien[ 'color' ] = 'yellow'
        alien[ 'speed' ] = 'medium'
        alien[ 'points' ] = 10
    elif alien[ 'color' ] == 'yellow':
        alien[ 'color' ] = 'red'
        alien[ 'speed' ] = 'fast'
        alien[ 'points' ] = 15

#show first 5 aliens:
for alien in aliens[ : 5 ]:
    print( alien )
print( "..." )

#show how many aliens has been created
print( "Total number of aliens: " + str( len( aliens ) ) )

