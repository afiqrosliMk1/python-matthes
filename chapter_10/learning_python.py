filepath = 'text_files/learning_python.txt'

with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip() )
    print( '****end of read line by line****' )

with open(filepath) as file_object:
    contents = file_object.read()
    
    print(contents.rstrip() )
    print( '****end of reading entire file****' )

with open(filepath) as file_object: 
    lines = file_object.readlines()

for line in lines:
    print( line.rstrip() )
print( "*****end of storing in list, and working outside 'with' block****" )
