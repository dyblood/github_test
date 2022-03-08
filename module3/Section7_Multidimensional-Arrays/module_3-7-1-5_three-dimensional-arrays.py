#Three-dimensional arrays

#three-dimensional array
#A huge hotel that you need an array to collect and process information on the occupied/free rooms
#Hotel consist of:
    # 3 buildings
    #15 floors each
    #20 rooms on e/ floor
#step 1
    #type of array's elements => in this case a boolean value (True / False)
#step 2
    #calm analysis of the situation
    #sumarize the available information: 3 buildings => 15 floors => 20 rooms 
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)] 
    #rooms[#select building][#select floor][#select room]

#book room for newly weds in the second building, tenth floor, room 14
rooms[1][9][13] = True #True means the room is booked

#release the second room on the fifth floor located in the first building
rooms[0][4][1] = False #False means the room is available

#check for vacancies on the 15th floor of the third building
vacancies = 0

for room_number in range(20): #setting the room number as the iterable value
    if not rooms[2][14][room_number]: #checking all the rooms in the 3rd building on the 15th floor
                                      #if not test if the room is false. False = room is vacant
        vacancies += 1 

print("Vacancies in building 3 on the 15th floor is:", vacancies)
