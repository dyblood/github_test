kilometers = input("Enter Kilometers to convert to miles: ")
kilometers = int(kilometers)
print(kilometers, "Kilometers")
miles = input("Enter Miles to convert to kilometers: ")
miles = int(miles)
print(miles, "Miles")

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")