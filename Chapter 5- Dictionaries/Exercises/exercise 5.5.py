#Make several dictionaries, where each dictionary represents a different pet.
#In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
#Next, loop through your list and asyou do, print everything you know about each pet.

   
# Create dictionaries for different pets
pet1 = {
    "type": "Cat",
    "breed": "Munchkin cat",
    "owner": "Arthur"         
}

pet2 = {
    "type": "Bird",
    "breed": "Goldfinch",
    "owner": "Gwaine"
}

pet3 = {
    "type": "Dog",
    "breed": "Husky",
    "owner": "Azira"
}

# Store these dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Display information about each pet.
for pet in pets:
     print("Type of pet:", pet["type"])
     print("Breed:", pet["breed"])
     print("Owner of the pet:", pet["owner"])
     print()  # Add an empty line for separation