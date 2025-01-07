Drive link for Lecture3
---
https://drive.google.com/drive/folders/1LahwPSc6f9nkxBiRrz6LFUzkrg-Kzvov

Lists
---
A built-in data type that stores set of values.

It can store the values of different types(integer, float, string, etc)

**Example:**

marks = [94.4, 87.5, 95.2, 66.4, 45.1]

print(marks)

![image](https://github.com/user-attachments/assets/42c42bfa-25a8-4d83-b211-4b6fb3458e0e)

![image](https://github.com/user-attachments/assets/074bfea1-edd0-47f8-8d59-959df8c25421)

. ** Lists are mutable(which can be changed) in python**

![image](https://github.com/user-attachments/assets/a4af20fa-858d-406c-8342-80a8f17569ad)

![image](https://github.com/user-attachments/assets/d5c9aae9-e2c6-490e-8132-e7b95e22b5db)


. ** Strings are immutable(which cannot be changed) in python**

Example: 
str = "hello"

print(str[0])

str[0] = "y"

List slicing
---
Similar to string slicing.

str = [ 2, 4, 5, 3, 68]

str = str[1 : 4]

print(str)    - output : 4, 5, 3

Methods
---

list.append()

list = [2, 1, 3]

print(list.append(6))

output: [2, 1, 3, 6

.............................................................................................................................

list.sort()

list = [2, 1, 3]

list.sort()

print(list)

output: [1, 2, 3]

.............................................................................................................................

list.sort(reverse = True) 

sorts in descending order

![image](https://github.com/user-attachments/assets/6ad50c67-cd3c-415f-8fa7-8e56bc6f7550)


.............................................................................................................................

list.reverse()

reverses the list

![image](https://github.com/user-attachments/assets/31648149-aff4-4868-91a2-5e41c9f50e0d)


............................................................................................................................

list.insert(idx, el)

insert element at index

list = [1, 2, 5, 3, 8]

list.insert(3, 9)

print(list)

![image](https://github.com/user-attachments/assets/13ccb185-f26d-43cf-ae14-2212a180d2e3)

............................................................................................................................

list.remove()

removes first occurance of element


list = [1, 2, 5, 3, 8]

list.remove(8)

print(list)

![image](https://github.com/user-attachments/assets/840d2993-361d-43bb-b9dc-a904bcd38ebf)

............................................................................................................................

list.pop(idx)

removes element at idx

list = [1, 2, 5, 3, 8]

list.pop(3)

print(list)

![image](https://github.com/user-attachments/assets/73d10193-ba0f-4cdc-bfdf-8d716579806d)

............................................................................................................................


Tuples 
---
A built-in data type that lets us create immutable sequences of values.

tup = (87, 64, 33, 95, 76)

tup[0] = 43  - This is not allowed in tuples as it is allowed in lists.

............................................................................................................................
Example:

tup = (1, 2, 5, 3, 8)

print(tup)

print(tup[0])

**tuple object doesnot support item assignment**

![image](https://github.com/user-attachments/assets/414d6018-ee36-4814-b638-2a95a095f48f)

![image](https://github.com/user-attachments/assets/23c5cefa-c27e-4d70-8ee0-766765ce3106)

Here it prints the empty tuple also and the type is also printed as the tuple

............................................................................................................................

![image](https://github.com/user-attachments/assets/c19e9ace-3d16-46e4-a8c4-386c4b2ecc04)


![image](https://github.com/user-attachments/assets/ddeec8f7-6425-4412-92a3-764b4d3ba82d)

Here if you could observe, tuple is considered as int as we missed coma in the tuple.


![image](https://github.com/user-attachments/assets/a5ce25c5-9bde-46b1-a1b5-5bde232800e7)


![image](https://github.com/user-attachments/assets/e611d62e-959a-4a34-b620-2a59ccbbb4e8)

Here if you observe the output, the tuple type is tuple itself. As we placed coma( , ) inside the tuple.


**Slicing is possible in tuple**


**Tuple methods*
---

tup.index(element)

returns index of first occurrence

............................................................................................................................

tup.count(element)

counts total occurrences

#Practice Questions











































