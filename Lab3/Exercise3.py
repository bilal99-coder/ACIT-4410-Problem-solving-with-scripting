#Reverse string


def reverseString():
    while True:
        name = input("Enter a world you want to reverse (Type Exit to stop the program): ")
        if(name.lower() == "exit"):
            return
        reversedString = ""
        for n in range(0,len(name)):
            reversedString += name[len(name)-n-1]
        print(reversedString)


reverseString()