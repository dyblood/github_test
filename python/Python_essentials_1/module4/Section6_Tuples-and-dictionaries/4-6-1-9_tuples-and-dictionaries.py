#4.6.1.9 tuples and dictionaries can work together

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break

    if name in school_class: #type: ignore
        school_class[name] += (score,) # making score a tuple so score doesn't add together it lists all the scores separately
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

#creating to show that score is stored as a tuple
for name, score in sorted(school_class.items()):
    print(name, ":", score)
