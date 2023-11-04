import json

filename = "favorite_number.json"

with open(filename , 'w' ) as file_obj:
    number = input("enter your favorite number: ")
    json.dump( number , file_obj )
