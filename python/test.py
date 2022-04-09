# This file is used to test random codes
from sys import dont_write_bytecode


st1 = "donor"
str2 = "Nabucodonosor"
found = True
start = 0


for ch in str2:
    pos = str2.find(ch , start)
    if pos <0:
        found = False
        break
    start = pos + 1
if found:
    print("Yes")
else:
    print("No")
