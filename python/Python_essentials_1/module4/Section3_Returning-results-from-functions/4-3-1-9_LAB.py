#check if number is prime / return prime numbers only
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5+1)): #start at 2 because we can't use 1 to divide w/
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1): #runs i through the program to see if it is true (prime)
			print(i + 1, end=" ")
print()
