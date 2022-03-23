#4.6.1.12 Practice questions
#----------------------------------------------------------------------
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4
#----------------------------------------------------------------------#
print("----------------------------------------------------------------")
#----------------------------------------------------------------------#
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
#----------------------------------------------------------------------#
print("----------------------------------------------------------------")
#----------------------------------------------------------------------#
my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list) #list into a tuple

print(t)
#----------------------------------------------------------------------#
print("----------------------------------------------------------------")
#----------------------------------------------------------------------#
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors) #turns color tuples into a dictionary

print(colors_dictionary)

#----------------------------------------------------------------------#
print("----------------------------------------------------------------")
#----------------------------------------------------------------------#
#NOTE: note how the copy() and .clear() method work

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy() # copy() method copies the values and not the list location
my_dictionary.clear() #clear() method deletes everything in the dictionary

print(copy_my_dictionary)
#----------------------------------------------------------------------#
print("----------------------------------------------------------------")
#----------------------------------------------------------------------#