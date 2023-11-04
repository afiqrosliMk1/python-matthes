filename = 'text_files/programming_poll.txt'
flag = True

with open(filename , 'a') as file_object:
    while flag:
        reason = input( "why you like programming? (quit to end): " )
        if reason != 'quit':
            file_object.write(reason + "\n")
        else:
            flag = False
