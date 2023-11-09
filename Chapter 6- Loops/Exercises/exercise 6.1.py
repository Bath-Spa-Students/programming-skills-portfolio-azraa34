#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#As they enter each topping, print a message saying you’ll add that topping to their pizza.


# Start an infinite loop
while True:

    # Prompt the user to eneter a pizza topping
    topping = input("\nEnter a pizza topping (or type 'quit' to finish): ")
    
    # Check if the user wants to quit (case-insensitive)
    if topping.lower() == 'quit':
        # Exit the loop if 'quit' is entered
        break
    
    # Confirm the topping is added
    print(f"I'll add {topping} to your pizza.") 