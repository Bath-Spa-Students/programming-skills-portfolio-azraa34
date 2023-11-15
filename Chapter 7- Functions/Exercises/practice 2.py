# Write a Python function that calculates the factorial of a given positive integer using
# recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input())
result = factorial(number)
print(result)

