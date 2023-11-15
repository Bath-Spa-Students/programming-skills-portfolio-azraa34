# Write a python program that takes courses marks as input and then calculates average of all the
# courses. After calculating the average, calculate the percentage of a student using total marks. Assume
# the total of all the courses marks is 500 or take the total marks from the user as input. 

# Number of courses
num_courses = int(input("Enter the number of courses: "))

# Collect course marks and calculate total
total_marks = sum(float(input(f"Enter the marks for course {i + 1}: ")) for i in range(num_courses))

# Assuming total marks is 500, you can also take it as input if needed
total_marks_possible = 500

# Calculate average and percentage
average = total_marks / num_courses
percentage = (total_marks / total_marks_possible) * 100

# Display results
print(f"\nAverage marks: {average}")
print(f"Percentage: {percentage}%")