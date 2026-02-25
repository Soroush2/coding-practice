"""
Problem: Sort Out The Men From Boys
Platform: Codewars
Difficulty: 7kyu
URL: https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/python
Category: 
"""
#Solution 1 - Initial Attempt
def men_from_boys(arr):
    even_numbers=sorted(list(set([i for i in arr if i %2==0])))
    odd_numbers=sorted(list(set([i for i in arr if i%2!=0])),reverse=True)
    main_arr=[]
    main_arr.extend(even_numbers)
    main_arr.extend(odd_numbers)
    return main_arr
print(men_from_boys([72, 76, 76, 82, 100, 91, 85]))
