# Write a Python program that uses the elif statement to determine the season based on the 
# month provided as input

month = input("Enter the month: ").lower()

if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Fall"
else:
    season = "Invalid month"

print(f"The season for {month.capitalize()} is {season}.")

