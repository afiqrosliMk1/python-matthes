import json

filename = 'username.json'
with open(filename , 'r') as file_obj:
    username = json.load(file_obj)
    print("welcome back " + username + " !")
