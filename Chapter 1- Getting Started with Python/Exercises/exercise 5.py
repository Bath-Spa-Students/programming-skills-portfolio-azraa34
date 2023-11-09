# Write a Python program which accepts the radius of a circle from the user and compute the area.

# Import the pi constant from the math module
from math import pi

# Prompt the user to input the radius of the circle.
radius = float(input("Please enter the radius of the circle: "))

# Calculate the area of the circle.
area = pi * radius * radius

# We can print the computed area.
print(f"The area of the circle is {area:.2f}.")