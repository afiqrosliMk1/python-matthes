filename = 'text_files/guest.txt'

username = input("input your name: ")

with open(filename , 'w') as file_object:
    file_object.write(username + "\n")
