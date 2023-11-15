# You have given a Python list. Write a program to find value 20 in the list, and if it is present,
# replace it with 200. Only update the first occurrence of an item. Work with the given list:
# list1 = [5, 10, 15, 20, 25, 50, 20]

# Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

# Find and replace the first occurrence of value 20 with 200
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break  # Stop after updating the first occurrence

# Print the updated list
print("Updated list:", list1)