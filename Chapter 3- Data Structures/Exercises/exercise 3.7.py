#Think of at least five places in the world you’d like to visit.
#Store the locations in a list. Make sure the list is not in alphabetical order.
#Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#Use sorted() to print your list in alphabetical order without modifying the actual list.
#Show that your list is still in its original order by printing it.
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#Show that your list is still in its original order by printing it again.
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.


#list of places to visit
locations = ["Edinburgh", "Port Talbot", "Gaza", "Dublin", "Cairo"]

#print the list in its original order
print("Original order:")
print(locations)

#print the list in alphabetical order without modifying the actual list
print("\nAlphabetical order:")
print(sorted(locations))

#verify the list is still in its original order
print("\nOriginal order:")
print(locations)

#print the list in reverse alphabetical order without modifying the orginal order
print("\nReverse alphabetical order:")
print(sorted(locations , reverse=True))

#verify the lsit is still in its original order
print("\nOriginal order:")
print(locations)

#use reverse() to change the order of the lsit
print("\nReversed order:")
locations.reverse()
print(locations)

#use reverse() again to change the order back to the original
print("\nOriginal order:")
locations.reverse()
print(locations)

#use sort() to change the list to alphabetical order
print("\nAlphabetical order")
locations.sort()
print(locations)

#use sort() again to change the list to reverse alphabetical order
print("\nReverse alphabetical order:")
locations.sort(reverse=True)
print(locations)