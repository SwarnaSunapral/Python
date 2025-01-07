Drive link 
---
https://drive.google.com/drive/folders/1LahwPSc6f9nkxBiRrz6LFUzkrg-Kzvov

Dictionary
---
Dictionaries are used to store data values in key:value pairs

They are unordered, mutable(changeable) & don't allow duplicate keys

    dic = {
       "name" : "Swarna",
       "age" : 21,
       "list" : [1, 2, 3],
       "is_adult" : True,
       12 : 34
    }
    
    print(dic)
    print(dic["name"])           # prints the value of that key "name".
    dic["name"] = ["sandeep"]    # replaces name value to sandeep
    dic["surname"] = "Sunapral"  # this directly adds value to the dictionary dic
    dic["name"] = ["sandeep"]    # This overwrites the before value


Nested Dictionaries
---
Dic.keys()  - returns all keys

Dic.values() - returns all values

Dic.items() - returns all (key, val) pairs as tuples

Dic.get("key") - returns the key according to the value

Dic.update(newDict) - inserts the specified items to the dictionary

    student = {
        "name" : "swarna",
        "subjects" : {
            "phy" : 97,
            "chem" : 90,
            "math" : 100,
        }
    }

    print(student)
    print(student["name"])
    
    print(student.keys())                # prints all the keys present in the dictionary
    print(list(student.keys()))          # prints all keys in the form of list
    print(len(list(student.keys())))     # prints length of the list of the keys

    print(student.values())              # Prints all the values present in the dictionary
    print(list(student.values()))        # prints all the values in the list
    print(len(list(student.values())))   # prints the length of the list of the values

    print(student.items())               # returns all the (key, value)
    print(list(student.items()))         # returns in the form of the list
    print(len(list(student.items())))    # returns the length

    print(student["name"])               # returns the value
    print(student.get("name"))           # returns the value 
    # when both are returning the same value why do we need both methods. Because when u place a key which is not present in the dictory it should give None but this print(student["name"]) gives the error.

    print(student["name1"])              # gives error
    print(student.get("name1"))          # gives None

   
    student.update({"name5" : "bubblu"}) # adds the new key to the dictionary and updates the same
    print(student)

Sets
---

Set is the collection of the unordered items

Each element in the set must be the unique & immutable


    

    





    







