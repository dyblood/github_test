hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

fmin = (mins + dura)%60
#%60 ensures that minutes value does not go passed 60 min

fhour = (hour + ((mins + dura)//60))%24
#// ensures value stays an int and not a float
#%24 ensures value does not go over 24 hrs

print(fhour, ":", fmin, sep="")