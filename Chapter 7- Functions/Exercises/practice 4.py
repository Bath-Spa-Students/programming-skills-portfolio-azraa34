# Write a Python program that defines a function to calculate the area of a circle, and then
# calls that function with a given radius.

import math

def calculate_area(radius):
    
    area = math.pi * radius * radius
    return area

# Now, we call the function with a given radius
radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area}")

