#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters.
#Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# Create a Python glossary
glossary = {
    'variable': 'A name that represents a value or data in Python.',
    'list': 'A collection of items in a particular order.',
    'print': 'A built-in function that displays information to the console',
    'loop': 'A control structure that allows to repeatedly execute a block of code',
    'dictionary': "A data structure that stores key-value pairs.",
    }

# Print the glossary 
word = 'variable'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'print'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])