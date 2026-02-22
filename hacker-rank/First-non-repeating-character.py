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