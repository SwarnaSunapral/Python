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


