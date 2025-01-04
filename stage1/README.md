Drive link for Stage1

https://drive.google.com/drive/folders/1LahwPSc6f9nkxBiRrz6LFUzkrg-Kzvov 

Code(python)  --------Complier/Interpreter-------->  Machine(0,1)
                        
        

**FIRST PROGRAM**

. print(" Hello World ")   // print is a Function

**CHARACTER SET**

. letters          - a-z, A-Z

. digits           - 0-9

. symbols          - +, _, *, etc...   // Whatever present on keyboard we can use them

. whitespace       - blank space, tab 

. other characters - ASCII and Unicode Characters as part of data or literals

//(https://theasciicode.com.ar/) - ASCII Table list 

//(https://en.wikipedia.org/wiki/List_of_Unicode_characters) - Unicode Characters 

**PYTHON SAMPLES**

''' We can print strings on pyhton 
- print("My name is swarna")
- print("My age is 21")
- output = My name is swarna
                     My age is 21
  
'''
- print("My name is swarna.", "My age is 21.")
- output = My name is swarna. My age is 21.

''' We can print numbers on python
- print(32)
- output = 32
  
'''

- print(32, 23, 45)
- output = 32 23 45
  
'''

- print(2*3)
- output = 6  (multiplication)
   
'''we can add, subtract, multiply etc...... in python

                       ----VARIABLES----
A variable is a name given to a memory location in a program
                                  |
                               ___________________________________
                              |  ____    ____     ____     ____   |-------------> Memory 
                              | |____|  |____|   |____|   |____|--|-------------> data will be stored in this cells
                              |___________________________________|
Syntax  : var  = value                                         
Example : name = Swarna
          age  = 21 
              ( variable means it can vary from time to time. Today it is 21, next year it will be 22. So we can change accordingly on pyhton )

''' code 
name = "Swarna"
age = 21                ---------// here '=' is a assignmnet value. 21 is getting stored in age variable
                                    age1 = age ( here age will be stored in age1 i.e, 21 
print("My name is:", name)      
print("My age is:", age) 
              //output = My name is : Swarna
                         My age is : 21

                       ----Rules for Identifiers----
1. Identifiers can be the combination of 
                                  . a - z
                                  . A - Z
                                  . 0 - 9
                                  . _ ( underscore )
2. Identifier cannot start with digit.
                variable1 is valid
                1variable is not valid
3. We cannot use specific symbols like $,%,@ etc 
4. Identifiers can be of any length.

              Variable name should be simple, short, and meaningful

                         ----DATA TYPES----
print(type(name))
            output = <class 'str'>
