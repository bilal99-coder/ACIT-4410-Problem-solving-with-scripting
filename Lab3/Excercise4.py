# Define a function named Fibonacci that calculates the nth Fibonacci number

def fibonnaci(n):
        if (n == 1 or n == 2):
            return 1
        return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(5))