# step 1
# step 1: create an empty list named beatles;
beatles = []
print("Step 1:", beatles)

# step 2
# appending list to add John Lennon, Paul McCartney, and George Harrison

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Step 2:", beatles)

# step 3
#use for loop and the append() method to prompt the user to add
#the following members of the band to the list:
#Stu Sutcliffe, and Pete Best
for i in range(2):
    beatles.append(input("Enter singers name: "))

print("Step 3:", beatles)

# step 4
#use the del instruction to remove Stu Sutcliffe and Pete Best
#[-1] points at the last element in the list
for i in range(2):
    del beatles[-1]
print("Step 4:", beatles)

# step 5
#use insert() method to add Ringo Starr to the beginning of the list
#[0] inserts an item to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)



# testing list legth
print("The Fab", len(beatles))
