'''Objective:
Write a Python program that processes a list of numbers using lambda functions
and list comprehensions.
Task: Given a list of integers, use a lambda function to create a new list where:
• Each number is squared if it is even.
• Each number remains unchanged if it is odd Use a list comprehension to
achieve this.
Example Input:
numbers = [1, 2, 3, 4, 5, 6]
Example Output:
[1, 4, 3, 16, 5, 36]
Hints: You can use the map() function with a lambda function to apply trans-
formations. Use the modulus operator % to check if a number is even or odd.
Example of lambda syntax: lambda x: x * x
'''

# Without creating a new list
def processNumbers_1(numbers):
    for i, n in enumerate(numbers):
        if(n%2 == 0):
            #number is even
            numbers[i] = numbers[i]**2
    print(numbers)

input=[1, 2, 3, 4, 5, 6]
processNumbers_1(input)


# With using list comprehensions:
def processNumbers_2(numbers):
    processedNumbers = [x**2  if x%2==0 else x for x in numbers]
    print(processedNumbers)

input=[1, 2, 3, 4, 5, 6]
processNumbers_2(input)




# With using lambda:
input=[1, 2, 3, 4, 5, 6]
processedNumbers_3 = list(map(lambda x: x**2 if x%2 ==0 else x, input))
print(processedNumbers_3)

            
