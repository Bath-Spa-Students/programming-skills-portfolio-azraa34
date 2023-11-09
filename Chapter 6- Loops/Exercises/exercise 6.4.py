#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


# A list of sandwich orders
sandwich_orders = ['turkey', 'chicken', 'egg', 'pastrami', 'cheese']

# An empty list for finished sandwiches
finished_sandwiches = []

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
