#4.5.1.1 Evaluating the BMI

#----------------------------------------------------------------------------------
#BMI = (weight in kilograms)kg / height in meteres ** 2
#BMI function
def bmi(weight, height):
    # the \ allows us to continue the argument on the next line underneath
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200: # tests to see if height or weight is unreasonable
        return None

    return weight / height ** 2
#-----------------------------------------------------------------------------------
#function to convert pounds (lb) to kg

def lb_to_kg(lb): 
    return lb * 0.45359237
#-----------------------------------------------------------------------------------
#function to convert ft and inches to meters

def ft_and_inch_to_m(ft, inch = 0.0): #set default for inches incase ft is the only one required
    return ft * 0.3048 + inch * 0.0254
#----------------------------------------------------------------------------------

print("BMI: ", bmi(52.5, 1.65))
print("kg:", lb_to_kg(1))
print("meters:", ft_and_inch_to_m(1,1))
print("meters:", ft_and_inch_to_m(6))
print("BMI is: ",bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))