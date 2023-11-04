def make_car( manufacturer , model , **other_info ):
    #create empty dict
    car = {}
    car[ 'manufacturer' ] = manufacturer
    car[ 'model' ] = model
    for key , value in other_info.items():
        car[ key ] = value

    return car

