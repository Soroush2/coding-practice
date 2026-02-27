""" This script computes the sum of the factorial of a 
list of numbers"""
import math
def factorial_sum(numbers):
    total=0
    for n in numbers:
        total+=math.factorial(n)
    return total