bob = { 'kind' : 'dog' , 'owner' : 'din' }

mia = { 'kind' : 'cat' , 'owner' : 'afiq' }

putih = { 'kind' : 'mouse' , 'owner' : 'naga' }

pets = [ bob , mia , putih ]



#loop through the list of dictionaries
for pet in pets:
   for key, value in pet.items():
        print( key + " : "  + value )
