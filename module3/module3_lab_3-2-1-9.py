sword = input("Enter the secret word: ")
while sword != "chupacabra":
    if sword == "chupacabra":
        break
    else:
        sword = input("That was not the secret word. Try again!")
print("Congrats!!! You've successfully entered the secret word!")