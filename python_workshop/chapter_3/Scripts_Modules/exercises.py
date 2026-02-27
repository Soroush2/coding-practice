#Exercise 35 sum of factorial of each number in the list
import math
numbers=[5,7,11]
total=0
for n in numbers:
    total+=math.factorial(n)
print(total)