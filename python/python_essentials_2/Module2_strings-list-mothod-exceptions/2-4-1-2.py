# 2.4.1.2 - Comparing strings: continued

#even if a string contains digits only => code point value is still used instead 

print("1", ('10' == '010')) #False
print("2", ('10' > '010')) #True - 1 (ASCII: 49) is greater than 0 (ASCII: 48)
print("3", ('10' > '8')) #False - 1 (ASCII: 49) is less than 8 (ASCII: 56)
print("4", ('20' < '8')) #True - 2 (ASCII: 50) is less than 8 (ASCII: 56)
print("5", ('20' < '80')) #True - 2 (ASCII: 50) is less than 8 (ASCII: 56)
