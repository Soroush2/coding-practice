"""
Problem: Delete occurrences of an element if it occurs more than n times
Platform: Codewars
Difficulty: 6kyu
URL: https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
Category: 
"""
#Solution 1 - Initial Attempt
def delete_nth(order,max_e):
    new_list=[]
    for item in order:
        if new_list.count(item)<max_e:
            new_list.append(item)
    return new_list
n=int(input("Enter the maximum number of occurrences allowed: "))
custom_list=list(map(int,input("Enter your list elements with space: ").split()))
delete_nth(custom_list,n)
