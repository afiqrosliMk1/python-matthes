def count_words(filename):
    """Count the approximate number of words in a file"""

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    
    #except FileNotFoundError:
    #    msg = "Sorry , the file " + filename + " does not exist."
    #    print( msg )
    except FileNotFoundError:
        pass
    
    else:
        #count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print( "The file " + filename.replace('text_files/' , '') +
               " has about " + str(num_words) + " words." )

filenames = [ 
    'text_files/alice.txt' , 'text_files/siddharta.txt' , 'text_files/moby_dick.txt' , 
    'text_files/little_women.txt' 
    ]
    
for filename in filenames:       
    count_words(filename)

