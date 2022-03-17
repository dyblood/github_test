#4.6.1.8 dictionary: modifying and adding values

# dictionaries are fully mutable

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

#changing value of an existing key
dictionary['cat'] = 'minou' #replacing the value 'chat' w/ 'minou'

#adding a new key and value pair
dictionary['swan'] = 'cygne' #adding a new key and value pair to the dictionary

#OR: you can use the update() method
dictionary.update({"duck": "canard"})

#removing a key
del dictionary['dog'] #removing a key will always remove the associated value

###EXTRA: remove the last item in a dictionary, using popitem() method
dictionary.popitem() #deletes last item in dictionary
print(dictionary)


print(dictionary)
