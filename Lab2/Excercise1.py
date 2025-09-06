# Exercise 1: Basic Logic and Conditionals
     # Write a Python script that prompts the user to enter a number.
while True:
    user_input = input("Enter a number (or type 'exit' to quit) ")
    if (user_input.lower() == 'exit'):
        break
    number = float(user_input)
    if (number > 0):
        output = "The number is positive"
        if (number%2 == 0):
            output += " and even"
        else:
            output += " and odd"
    elif (number == 0):
        output = "The number is equal to zero"
    else:
        output = "The number is negative"

    print(output)


    