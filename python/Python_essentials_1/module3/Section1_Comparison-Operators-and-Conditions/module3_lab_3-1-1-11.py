#module3_lab_3-1-1-11

income = float(input("Enter the annual income: "))
tincome = 85528

# if the citizen's income was not higher than 85,528 thalers, 
# the tax was equal to 18% of the income minus 556 thalers and 2 cents 
# (this was the so-called tax relief)
if income <= tincome:
    tax = income * .18
    tax -= 556.02 #fixed tax amount
    if tax < 0: #tax can't be less then zero
        tax = 0

#If you make more than 85,528
#tax was equal to 14,839 plus 32% of the surplus over 85,528
if income > tincome:
    tax = 14839.02 #applies the fixed tax
    income -= tincome # only the surplus over 85,528 gets taxed
    tax += income * .32 #calculates the tax amount of the surplus + the fixed rate

tax = round(tax, 0)
print("The tax is:", tax, "thalers")