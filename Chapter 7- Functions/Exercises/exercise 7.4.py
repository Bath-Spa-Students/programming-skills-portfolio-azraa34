#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


def make_shirt(size='large', message='I love Python'):
    print(f"The shirt is a size {size} with the message '{message}'.")

# Call the function using default values
make_shirt()

# Call the function to make a medium shirt with the default message
make_shirt('medium')

# Call the function to make a shirt of any size with a different message
make_shirt('small', 'I love coding')