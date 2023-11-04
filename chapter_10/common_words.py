filenames = [ 'text_files/alice.txt'  , 'text_files/moby_dick.txt' ]

def count_word( filename , word):
    try:
        with open(filename) as file_obj:
            lines = file_obj.read()
    except FileNotFoundError:
        print( 'file cannot be found' )
    else:
        word_count = lines.lower().count(word)
        print("the word '" + word + "' appears " + str(word_count) + " times in " + filename.replace( 'text_files/' , '') )

for filename in filenames:
    count_word(filename , 'the' )
