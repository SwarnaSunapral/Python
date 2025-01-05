Drive link for Lecture2
---
   https://drive.google.com/drive/folders/1LahwPSc6f9nkxBiRrz6LFUzkrg-Kzvov 
   
Strings
---
String is data type that stores a sequence of characters.

Different ways of quoting the string

. str1 = "This is a string."

. str2 = 'Swarnalatha Bai'

. str3 = '''string in triple quotes'''

Example:

'This is a apnacollege's tutorial'

Here starting from 'this and ending at tutorial' but in between there is college's. so this may create a problem. so we make use of double quotes.

Corrected Sentence

. "This is a apnacollege's tutorial"

- str4 = "Hi my name is swarna. 
- I am from Hyderabad"

Here this throws an error it is not allowed as word done in word docs. Instead we use 'Escape Sequence Characters'.

Escape Sequence Characters
---
. str4 = "Hi my name is swarna.\nI am from Hyderabad"
print(str4)

. str5 = "Hi my name is swarna.\tI am from Hyderabad"
print(str5)

Basic Operations
---
. Concatenation

"Hello" + "world" = "Helloworld"

. length of str

len(str)

Indexing
---
**A P N A _ C O L L E G E**

 0 1 2 3 4 5 6 7 8 9 10 11

 str = "apna college"
 
print(str[3])

print(str[6])

![image](https://github.com/user-attachments/assets/6e898b77-fa6c-4925-b0a9-504e67f8971d)

Slicing
---
Accessing parts of a string.

str = "ApnaCollege"

str[starting_idx : ending_idx]  - (ending_idx is not included)

str[1 : 4] is "pna"

str[ : 4] is same as str[0 : 4]

str[1 :  ] is same as str[ 1 : len(str) ]

** Negative Index


**A  P  P  L  E

-5-4-3-2-1

str = "Apple"

str[-3 : -1] is "pl"

Functions
---

**str.endswith("")**               

returns true if string ends with substr

str = "I am Swarna from Hyderabad"

print(str.endswith("ad"))        

True

............................................................................................................................

**str.capitalize()**               

Capitalize 1st character

str = "i am Swarna from Hyderabad"

print(str.capitalize())          

This is making changes only in the new string but it doesnot make changes in the old string

str = print(str.capitalize())    

This makes changes in the old string as we are storing it in the old string itself 

print(str)

............................................................................................................................

**str.replace(old, new)**          

replaces all occurrences of old one with new 

str = "i am Swarna from Hyderabad"

print(str.replace("a", "i"))     

i im Swirni from Hyderibid

............................................................................................................................

**str.find(word)**                 

Helps to find the index of that starting word

str = "i am Swarna from Hyderabad"

print(str.find("Swarna"))        

5

............................................................................................................................

**str.count("am")**                

counts the occurrence of substr

str = "i am from iitpallakd and i am from hyderabad"

print(str.count("from"))        

2

............................................................................................................................

Practice Questions 
---
1. WAP to input user's first name & print its length

str = input("Enter the first name:")

print(len(str))

![image](https://github.com/user-attachments/assets/406c205e-dc6c-4fc8-8be8-253144cb2136)

#2. WAP to find the occurrence of'$' in a string

str = "I am $warna from $rinagar and i can $ing better"

print(str.count("$"))

![image](https://github.com/user-attachments/assets/94f52aab-a274-46b4-a08d-2b3a8f2d61c6)

Conditional Statements
---
if-elif-else(SYNTAX)

if(condition):

    Statement1
    
elif(condition):

    Statement2
else:

    StatementN

INdentation
---
proper spacing is the important thing in python

Nesting
---
![image](https://github.com/user-attachments/assets/ab73eb7e-5a7e-40f2-9c6a-dde379e194d6)

![image](https://github.com/user-attachments/assets/44b41cf3-c70b-44a8-92f7-3d667b7882f8)

Practice Questions
---

4. WAP to check if a number entered by the user is odd or even

6. WAP to find the greatest of 3 numbers entered by the user

7. WAP to check if a number is a multiple of 7 or not.

Codes present at - https://github.com/SwarnaSunapral/Python/blob/main/stage2/Practice.py




































