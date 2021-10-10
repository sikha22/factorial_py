""" write a python function to print the factorial of a given number"""
import math
def fact(n):
    return(math.factorial(n))
num = int(input("Enter the number:"))
f = fact(num)
print("Factorial of", num, "is", f)  