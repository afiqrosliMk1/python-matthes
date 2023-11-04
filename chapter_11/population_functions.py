

def city_function( city , country , population=0 ):
    if population == 0:
        name = city.title() + ", " + country.title()
    else:
        name = city.title() + ", " + country.title() + " - population=" + str(population)
    
    return name


