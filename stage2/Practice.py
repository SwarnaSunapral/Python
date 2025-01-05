#1. WAP to input user's first name & print its length

str = input("Enter the first name:")   # Swarna
print(len(str))                        # 6

#2. WAP to find the occurrence of'$' in a string

str = "I am $warna from $rinagar and i can $ing better"      
print(str.count("$"))                  # 3


#3. To print the grades of the students according to the marks they obtain

marks = int(input("Enter the marks:"))

if(marks >= 90):
    print("grade = A")
elif(marks >= 80 and marks < 90):
    print("grade = B")
elif(marks >= 70 and marks < 80):
    print("grade = C")
elif(marks < 70):
    print("grade = D")

#4. WAP to check if a number entered by the user is odd or even 

num = int(input("Enter the number:"))

if(num % 2 == 0):
    print("The number is even", num)
else:
    print("The number is odd", num)

#5. WAP to find the greatest of 3 numbers entered by the user

a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))

if(a > b and a > c):
    print("The greatest number is:", a)
elif(b > c):
    print("The greatest number is",b)
else:
    print("The greatest number is",c)


#6. WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter the number:"))

if(num%7 == 0):
    print("The number is divisible by 7 is:", num)
else:
    print("The number is not divisible by 7")





