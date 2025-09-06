def printNumberOfStudentsInEachGrade(numberOfStudentsPerGrade):
    for grade,total in numberOfStudentsPerGrade.items():
        print("The number of students that got " + grade + " is: " + str(total) + ".")
            
            
def calculateGrades(listOfStudents = {}):

    print("The input is: ")
    print(listOfStudents)

    numberOfStudentsPerGrade = {"A" : 0,
    "B" : 0 ,
    "C" : 0 ,
    "D" : 0 ,
    "F" : 0 }


    for name,grade in listOfStudents.items():
        if grade < 0 or grade > 100:
            print("Warning: Grade cannot be under 0 or above 100.")

        elif grade >= 90 and grade <= 100:
            if grade == 100:
                print("Congratulations to " + name + " for getting 100 in the exam")
            numberOfStudentsPerGrade["A"] += 1
            listOfStudents[name] = "A"
        
        elif grade >=80 and grade < 90:
            numberOfStudentsPerGrade["B"] += 1
            listOfStudents[name] = "B"
        
        elif grade >=70 and grade < 80:
            numberOfStudentsPerGrade["C"] += 1
            listOfStudents[name] = "C"

        elif grade >=60 and grade < 70:
            numberOfStudentsPerGrade["D"] += 1
            listOfStudents[name] = "D"
        
        else:
            numberOfStudentsPerGrade["F"] += 1
            listOfStudents[name] = "F"

    print(listOfStudents)
    printNumberOfStudentsInEachGrade(numberOfStudentsPerGrade)


calculateGrades({"Bilal":100,"Ahmed":99,"Ilyas":98,"Alex":19,"Zebra":-9})

