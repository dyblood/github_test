#2.2.1.12 - Operations on strings: max()

#max() finds the maximum element of the sequence
    #maximum element based on ASCII table

#Example 1:
print(max("aBbByYzZ")) #lowercase numbers come after so 'z' should be highest value

#Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))