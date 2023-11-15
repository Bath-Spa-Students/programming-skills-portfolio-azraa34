# Write a python program with nested decision structures that perform the following: If amount1
# is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2

# Test amounts
amount1 = 20
amount2 = 90

# Perform the decision
if amount1 > 10 and amount2 < 100:
    # Check which amount is greater
    if amount1 > amount2:
        print("The greater amount is:", amount1)
    else:
        print("The greater amount is:", amount2)
else:
    print("Either amount1 is not greater than 10 or amount2 is not less than 100.")


    