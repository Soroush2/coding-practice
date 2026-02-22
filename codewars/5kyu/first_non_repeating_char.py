"""
Problem: First non-repeating character
Platform: Codewars
Difficulty: 5kyu
URL: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
Category: 
"""
#Solution 1 - Initial Attempt
def first_non_repeating_letter(s):
    s_lower=s.lower()
    if s_lower != '':
        for i in range(len(s)):
            if s_lower.count(s_lower[i])==1:

                return s[i]
        return ''
    else:
        return ''
print(first_non_repeating_letter("abba"))