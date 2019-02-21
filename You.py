#Variables
name = input("What is your name?: ")
age = input("What is your age?: ")
city = input("Where are you from?: ")
enjoy = input("What do you enjoy?: ")     
string = "Your name is {0} and you're {1} years old. You're from {2}, and you love {3}."

output = string.format(name,age,city,enjoy)


print(output)
