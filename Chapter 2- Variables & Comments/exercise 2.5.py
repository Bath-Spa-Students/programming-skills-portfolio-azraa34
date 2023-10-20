#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.


# Define the cost of each USB stick and the budget
usb_stick_cost = 6
total_money = 50

# Calculate how many USB sticks she can buy
usb_sticks_bought = total_money // usb_stick_cost

# Calculate how many pounds she will have left
money_left = total_money % usb_stick_cost

# Print the results
print("The girl can buy", usb_sticks_bought, "USB sticks.")
print("She will have £", money_left, "left.")