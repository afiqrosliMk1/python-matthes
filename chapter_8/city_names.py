def city_country( city , country ):
    text = city.title() + ", " + country.title()
    return text

print( city_country( 'new york' , 'usa' ) )
print( city_country( 'kl' , 'malaysia' ) )
print( city_country( 'bangkok' , 'thailand' ) )
