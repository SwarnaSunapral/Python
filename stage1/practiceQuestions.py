# 1. Write a program to input 2 numbers & print their sum.

a = int(input("Enter the value of a:"))  # a = 5
b = int(input("Enter the value of b:"))  # b = 2
sum = a + b                              # sum = 7
print(type(sum), sum)               

#2. WAP to input side of a square & print its area

side = int(input("Enter the side of a square:"))  # side = 5
area = side*side                                  # area = 25
print("Area of a square is:", area)  

#3. WAP to input 2 floating point numbers & print their average

val1 = float(input("Enter the value:"))         # 3.0
val2 = float(input("Enter the value:"))         # 5.0
sum = val1 + val2                               # 8.0
average = sum/2                                 # 4.0
print(sum)
print("Average of the numbers is:", average)
