#Write a function that checks if a number is a prime and print the check result

def isPrime(number):
    for n in range(1,number):
            if (number/n)%2 == 0:
                print(str(number) + " is not a prime number")
                return
    print(str(number) + " is a prime number")


isPrime(0)

    