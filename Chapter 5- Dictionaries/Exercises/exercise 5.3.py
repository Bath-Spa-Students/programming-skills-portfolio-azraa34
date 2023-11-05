#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99)
#by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
#When you’re sure that your loop works, add five more Python terms to your glossary.
#When you run your program again, these new words and meanings should automatically be included in the output.

# Create a Python glossary
glossary = {
    'variable': 'A name that represents a value or data in Python.',
    'list': 'A collection of items in a particular order.',
    'print': 'A built-in function that displays information to the console',
    'loop': 'A control structure that allows to repeatedly execute a block of code',
    'dictionary': "A data structure that stores key-value pairs.",
    'string': 'A sequence of characters used for text',
    'comment': 'A note that is ignored by the Python interpreter in a program.',
    'conditional statement': 'A statement that controls flow of execution based on some condition.',
    'exception': 'An event that disrupts normal code flow.',
    'value': 'A string or an intenger that can be store in a variable.',
    }

# Loop through the glossary and print 
for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)