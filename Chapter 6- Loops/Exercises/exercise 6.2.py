#A movie theater charges different ticket prices depending on a person’s age.
#If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

# start a loop
while True:
    age = input("\nEnter your age ('quit' to exit): ")

    if age == 'quit':
        break
# convert to integer
    age = int(age)
    
# print the cost of tickets
    if age < 3:
        print(" You can get in free!") #free for 3 and under
    elif age < 13:
        print(" Your ticket costs $10.") #$10 for ages below 13
    else:
        print(" Your ticket costs $15.") #$15 for ages 13 and above