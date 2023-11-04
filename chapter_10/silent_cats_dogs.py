filenames = [ 'text_files/cats.txt' , 'text_files/dogs.txt' ]

for filename in filenames:
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        pass

    else:
        for line in lines:
            print( line.rstrip() )
