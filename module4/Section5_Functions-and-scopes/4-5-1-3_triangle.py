#4-5-1-3
# -------------------------------------------------------------------- 
# checking to see if three sides can create a triangle

# def is_a_triangle(a, b, c):
#     # if a + b <= c:
#     #     return False
#     # if b + c <= a:
#     #     return False
#     # if c + a <= b:
#     #     return False
#
#     if a + b <= c or b + c <= a or c + a <= b: #shortend version 
#         return False
#     return True
#-------------------------------------------------------------------
#shortened version of the is_a_triangle function

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b #shorter version => returns either true or false

#---------------------------------------------------------------------
#function to test if triangle is a right triangle
# c**2 = a**2 + b**2 (Pythagorean theorem)

def is_a_right_triangle(a,b,c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c**2 == a**2 + b**2
    if a > b and a > c:
        return a**2 == b**2 + c**2
    if b > a and b > c:
        return b**2 == a**2 + c**2
#----------------------------------------------------------------------
print(is_a_triangle(1,1,1))
print(is_a_triangle(1,1,3))

print("------------------------------------------")

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')

print("--------------------------------------------")

print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
