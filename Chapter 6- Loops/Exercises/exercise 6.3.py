#Write a loop that never ends, and run it. 
#To end the loop, press ctrl-C or close the window displaying the output.


#start an infinite loop
while True:
    height = input("Please enter your height: ")
    
    #convert input to float
    height = float(height)

    if height < 140:
        print("Your height does not meet the minimum height requirement to ride the roller coaster.")
    elif height > 180:
        print("Your height exceeds the maximum height requirement to ride the roller coaster.")
    else:
        print("You can ride the roller coaster!")
