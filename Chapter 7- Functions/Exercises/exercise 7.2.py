#Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my
#favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.


def favorite_book(title):
    # Use triple quotes for multi-line strings
    message = f"One of my favorite books is {title}."
    print(message)

# Call the function with the title of your favorite book as an argument
favorite_book("Death on the Nile")
