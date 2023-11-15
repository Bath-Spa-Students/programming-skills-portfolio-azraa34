# Write a Python program that uses a while loop to find the largest number among a series of
# user-input values until they enter '0' to exit the loop.

def find_largest():
    print("Enter a series of numbers until you enter '0' to exit.")
    
    # initialize the maximum number as negative infinity
    max_num = float('-inf')
    
    # use a while loop to continue accepting numbers until '0' is entered
    while True:
        num = input()
        
        # break the loop if '0' is entered
        if num == '0':
            break
        
        # convert the input to a float and update the maximum number if necessary
        num = float(num)
        if num > max_num:
            max_num = num
    
    # print the maximum number
    print("The largest number is:", max_num)

find_largest()

