# Given a Python list, write a program to remove all occurrences of item 20.
# Given list: list1 = [5, 20, 15, 20, 25, 50, 20]

# Given list
list1 = [5, 20, 15, 20, 25, 50, 20]

# Remove all the occurrences of item 20 using index
while 20 in list1:
    list1.remove(20)
         
# Print the updated list
print("List without 20:", list1)
