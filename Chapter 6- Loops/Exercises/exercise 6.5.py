#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.


# A list of sandwich orders
sandwich_orders = [
    'pastrami', 'turkey', 'chicken', 'pastrami',
    'egg', 'cheese', 'pastrami']

# An empty list for finished sandwiches
finished_sandwiches = []

# The deli has run out of pastrami
print("I'm sorry, the deli has run out of pastrami.\n")

# Use a while loop to remove all occurences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# While loop to go through the sandwich orders
while sandwich_orders:

    # The next sandwich to be made
    current_sandwich = sandwich_orders.pop(0)

     # Make the sandwich
    print(f"I made your {current_sandwich} sandwich.")

    # Move the sandwich to the finished list
    finished_sandwiches.append(current_sandwich)

# Print the finished sandwiches
print("\nI made these sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)