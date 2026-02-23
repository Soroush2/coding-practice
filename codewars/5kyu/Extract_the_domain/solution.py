"""
Problem: Extract the domain name from a URL
Platform: Codewars
Difficulty: 5kyu
URL: https://www.codewars.com/kata/514a024011ea4fb54200004b
Category: 
"""
#Solution 1 - Initial Attempt
def domain_name(url):
    if url.startswith(('http://','https://')):
        domain=url.split("//")[1].split('.')
        if 'www' in domain:
            return(domain[1])
        else:
            return(domain[0])
    else:
        domain=url.split('.')
        if 'www' in domain:
            return(domain[1])
        else:
            return(domain[0])