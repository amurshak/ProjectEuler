#Factorial Digit Sum
#Project Euler Problem 20
# Find the sum of the digits in the number 100!
#
#Solution by Alex Murshak

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

digits = factorial(100)



sum_digits = 0
for i in str(digits):
    sum_digits += int(i)

print(sum_digits)
