#-----------------------------------------------------------------------------------------
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b #testing if lengths given make a triangle
#-----------------------------------------------------------------------------------------
#Function to evaluate the area of a triangle
#Heron's formula
    # s = ((a + b + c)/2) (s = semi parameter)
    # A = ((s(p-a)*(s-b)*(s-c))**0.5)
def heron (a, b, c):
    p = ((a + b + c)/2) # p = semi-parameter
    return((p*(p-a)*(p-b)*(p-c))**0.5)

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):#testing to see if three measurements make a triangle
        return None
    return heron(a, b, c) #if three lengths do make a triangle then use heron's formula to calculate area



print(area_of_triangle(1., 1., 2.**.5))

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')