'''fruits = ["banan","jordbær","avokado","eple","druer"]
fruits.append("melon")
fruits.pop(1)
fruits = tuple(fruits)
print(type(fruits))
print(fruits)'''

# ##Exercise 2

# students = {'0': ("bilal","25","cloud based services"), '1': ("ilyas", "22","cloud based services"), '2': ("youssef","23","cloud based services")}
# print(students)
# ##print(students['0'])
# #print(type(students))
# students[3] = "samatar", "22","cloud based services"


'''courses = {"course 1", "course 2", "course 3"}
courses.add("course 4")
courses.pop
print(courses)
'''
##Excercise 3

name = input("What is your name? ")
age = input("Nice to meet you " + name + ". What is your age? ")
favorite_language = input("what is your favourite programming language? ")
hobbies = input("What are your hobbies? Seperate your hobbies with comma ")
print("Welecome to the " +favorite_language+ " course " + name + "! You are "+ age + " years old and your hobbies are: " + hobbies )

programming_languages_set = set(input("what programming languages do you know? Seperate them with commas ").split(","))
data_dict = {"name": name, "age": age, "favorite_language": favorite_language, "hobbies": hobbies}

print(data_dict)
print(programming_languages_set)
