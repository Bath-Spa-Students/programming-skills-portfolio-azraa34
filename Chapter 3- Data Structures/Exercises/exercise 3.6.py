#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#Print a message to each of the two people still on your list, letting them know they’re still invited.
#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program


#Create a list of guests to invite to dinner
guests = ['Jane Austin', 'Neil Gaiman', 'Agatha Christie']

#Invite each person to dinner
name = guests[0].title()
print(f"{name}, I'd like to invite you over for dinner.")

name = guests[1].title()
print(f"{name}, I'd like to invite you over for dinner.")

name = guests[2].title()
print(f"{name}, I'd like to invite you over for dinner.")

#Name of guest who can't make it
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

#Replace the guest who cant make it with someone else
del(guests[1])
guests.insert(1, 'Fyodor Dostoevksy')

#Print the invitations again.
name = guests[0].title()
print(f"\n{name}, I'd like to invite you over for dinner.")

name = guests[1].title()
print(f"{name}, I'd like to invite you over for dinner.")

name = guests[2].title()
print(f"{name}, I'd like to invite you over for dinner.")

#Print a msessage saying only two people can be invited for dinner
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} you're not invited to dinner this time.")

#Invite the two people who are still left 
name = guests[0].title()
print(f"{name}, You're still invited over for dinner.")

name = guests[1].title()
print(f"{name}, You're still invited over for dinner.")

#Empty out the list.
del(guests[0])
del(guests[0])

#Prove the list is empty.
print(guests)