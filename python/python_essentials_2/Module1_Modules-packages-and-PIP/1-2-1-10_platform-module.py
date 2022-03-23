#1.2.1.10 Platform module
#platform module lets you access the underlying platform's data (hardware, os, interpreter version information)

from platform import platform, machine, processor, system, version, node
from platform import python_implementation, python_version_tuple


#aliased -> when set to True it may cause the function to present the alternative underlying layer names instead of the common ones
#terse -> when set to True it may convince the function to present briefer form of the result(if possible)

print(platform(aliased = False, terse = False))
print(platform())
print(platform(1))
print(platform(0, 1))

print(machine())
print(processor())
print(system())
print(version())
print(node())

print("--------------------------------------------------")

print(python_implementation())


for atr in python_version_tuple():
    print(atr)

import platform

for name in dir(platform):
    print(name, end="  /  ")

