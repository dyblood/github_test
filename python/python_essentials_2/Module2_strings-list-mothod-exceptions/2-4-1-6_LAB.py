# 2.4.1.6 - LAB: seven-segment display

line = "###"

zero = line + "\n# #"*3 +"\n" + line
one = "#  \n"*4 + "#  "
two = line + "\n  #\n" + line + "\n#  \n" + line
three = line + "\n  #\n" + line + "\n  #\n" + line
four = "# #\n"*2 + line + "\n  #" + "\n  #"
five = line + "\n#  \n" + line + "\n  #\n" + line
six = line + "\n#  \n" + line + "\n# #\n" + line
seven = line + "\n  #"*4
eight = line + "\n# #\n" + line + "\n# #\n" + line
nine = line + "\n# #\n" + line + "\n  #\n" + line

led_list = [zero, one, two, three, four, five, six, seven, eight, nine]

# for i in range(len(led_list)):
#     print(led_list[i])

while True: 
    try:
        user_num = int(input("Please enter a non negative number whole number: "))
    except ValueError:
        print("You did not enter aw correct value.")
        print("Please try again, make sure the value you enter is a non-negative whole number.")
        continue
    except:
        print("Not sure what you entered, but it was wrong. Please try again.")
        continue
    
    if user_num < 0:
        print("You must enter a non negative whole number, please stry again.")
        continue
    else:
        dis_num = []
        for i in str(user_num):
            dis_num += led_list[int(i)]
        print(dis_num)
        break
        