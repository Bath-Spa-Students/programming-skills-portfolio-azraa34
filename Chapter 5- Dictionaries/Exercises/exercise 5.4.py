#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

rivers = {
    'Volga': 'Russia',
    'Ganges': 'India',
    'Euphrates': 'Syria'
    }

# Print a sentence about each river
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

# Print the name of each river
print("\nRivers included in this dictionary are:")
for river in rivers.keys():
    print("- " + river.title())

# Print the name of each country
print("\nCountries are included in this dictinary are:")
for country in rivers.values():
    print("- " + country.title())