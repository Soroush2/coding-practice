"""
Problem: Enumerable Magic #1 - True for All?
Platform: Codewars
Difficulty: 8kyu
URL: https://www.codewars.com/kata/54598d1fcbae2ae05200112c/train/python
Category: 
"""
#Solution 1 - Initial Attempt
def _all(seq, fun):
    condition=False
    if not seq:
        return True
    for i in seq:
        if not fun(i):
            return False
    return True
greater_than_9 = lambda x: x>9
less_than_9 = lambda x: x<9
print(_all([], less_than_9))