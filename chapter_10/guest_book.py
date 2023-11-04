filename = 'text_files/guest.txt'

flag = True

while flag:
    username = input("input your name, type 'end' to end: ")
    if username != 'end':
        with open(filename , 'a') as file_object:
            file_object.write(username + "\n")
    else:
        flag = False
