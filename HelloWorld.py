n = int(input("How many squares of two do you want to see: "))
twos = [2 ** i for i in range(n)]
twos.reverse()
print(twos[:])