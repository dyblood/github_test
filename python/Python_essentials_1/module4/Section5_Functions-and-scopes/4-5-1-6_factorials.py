#4.5.1.6 Factorials
#example of Factorials
    # 	0! = 1 (yes! it's true)
    # 	1! = 1
    # 	2! = 1 * 2
    # 	3! = 1 * 2 * 3
    # 	4! = 1 * 2 * 3 * 4
    # 	:
    # 	:
    # n! = 1 * 2 ** 3 * 4 * ... * n-1 * n
#-------------------------------------------------------------------
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
#--------------------------------------------------------------------

for n in range(1, 6):  # testing
    print(n, factorial_function(n))

