secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter your guess: "))

while number != 777:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter another guess muggle! "))
print(
"""
Well done, muggle!
You are free now.
""")