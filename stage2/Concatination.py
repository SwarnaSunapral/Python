# Concatenation
str1 = "Hello"
str2 = "world"
str3 = str1 + str2                # Helloworld
print(str3)  
print(len(str3))                  # 10
print(len(str1 + "   " + str2))   # 13


# Indexing
str = "apna college"
print(str[3])                     # a
print(str[6])                     # o


# Slicing
str = "apna college"
print(str[1 : 4])                 # pna
print(str[ : 4])                  # apna
print(str[0 : len(str)])          # apna college
print(str[5 : ])                  # college

**Negative Indec
str = "Apple"
print(str[ -3 : -1 ])             # pl


# Functions

**str.endswith("")               # returns true if string ends with substr

str = "I am Swarna from Hyderabad"
print(str.endswith("ad"))        # True

**str.capitalize()               # Capitalize 1st character

str = "i am Swarna from Hyderabad"
print(str.capitalize())          # This is making changes only in the new string but it doesnot make changes in the old string

str = print(str.capitalize())    # This makes changes in the old string as we are storing it in the old string itself 
print(str)

**str.replace(old, new)          # replaces all occurrences of old one with new 

str = "i am Swarna from Hyderabad"
print(str.replace("a", "i"))     # i im Swirni from Hyderibid

**str.find(word)                 # Helps to find the index of that starting word
str = "i am Swarna from Hyderabad"
print(str.find("Swarna"))        # 5

**str.count("am")                # counts the occurrence of substr

str = "i am from iitpallakd and i am from hyderabad"
print(str.count("from"))        # 2






