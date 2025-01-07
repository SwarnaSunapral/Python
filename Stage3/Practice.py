# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movie1 = input("Enter the 1st movie name:")
movie2 = input("Enter the 2nd movie name:")
movie3 = input("Enter the 3rd movie name:")

movies = [movie1, movie2, movie3]

print(movies)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method).

lists = [1, 2, 3, 2, 1]

list1 = lists.copy()

list1.reverse()

if(list1 == lists):
    print("yes")

else:
    print("no")


# WAP to count the number of students with the "A" grade in the following tuple.
#              ["C", "D", "A", "A", "B", "B", "A"]

tup = ("C", "D", "A", "A", "B", "B", "A")

print(tup.count("A"))

# Store the above values in a list & sort them from "A" to "D"

list = ["C", "D", "A", "A", "B", "B", "A"]

list.sort()

print(list)
