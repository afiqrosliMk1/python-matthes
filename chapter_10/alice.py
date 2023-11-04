filename = 'text_files/alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    msg = "Sorry , the file " + filename + " does not exist."
    print( msg )

else:
    #count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    short_filename = filename.replace('text_files/' , '' )
    print( "The file " + short_filename + " has about " + str(num_words) + " words." )
