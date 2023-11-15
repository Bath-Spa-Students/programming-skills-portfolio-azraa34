# Write a python program with an if-else statement that displays Speed is normal if the speed
# variable is within the range of 24 to 56. If the speed variable's value is outside this range, display
# 'Speed is abnormal

# input the speed variable
speed = float(input("Enter the speed: "))

# perform the decision
if 24 <= speed <= 56:
    print("Speed is normal")
else:
    print("Speed is abnormal")


    