# 2.3.1.10 - lstrip()

#lstrip() => returns a newly created string formed from the original one by removing all leading whitespaces

#Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]") #only removes the leading whitespace

print("www.cisco.com".lstrip("w."))

print("pythoninstitute.org".lstrip(".org")) # '.org' is not leading so it will not be removed