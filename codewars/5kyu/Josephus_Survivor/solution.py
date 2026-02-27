"""
Problem: Josephus Survivor
Platform: Codewars
Difficulty: 5kyu
URL: https://www.codewars.com/kata/555624b601231dc7a400017a
Category: 
"""
#Solution 1 - Initial Attempt
def josephus_survivor(n,k):
    new_list=list(range(1,n,k))
    print(new_list)
# josephus_survivor(7,3)
new_list=[i for i in range(1,8)]
k=3
for i in range(k-1,len(new_list),k):
    new_list.remove(new_list[i])