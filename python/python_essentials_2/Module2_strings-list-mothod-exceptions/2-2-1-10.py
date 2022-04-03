#2.2.1.10 - Operations on a string: continued
# You can do other things to get around a string's immutability

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet #concatinating two strings and assigning that value to the variable
alphabet = alphabet + "z"

print(alphabet)

#NOTE: creating a new copy of a string each time you modify its contents worsens the effectiveness of the code
    #only worsens the effectiveness a little bit

