#Exercise 21
shopping=["bread", "milk","egg"]
print(shopping)
for item in shopping:
    print(item)
#using mixed types in lists
mixed=[365,"days",True]
print(mixed)
# Exercise 23
list3=['oi']*3 #outputs: ['oi','oi','oi']
list3=['oi'*3] #outputs: 'oioioi'
shopping[-1] # outputs: the last member of shopping list
# Exercise 24
shopping=[]
shopping.append('bread')
shopping.append('milk')
shopping.append('eggs')
shopping.append('apple')#shopping = ['bread','milk','eggs','apple']
shopping.insert(2,'ham')#inserts the element at given index = ['bread','milk','ham','eggs','apple']
# Exercise 25
primes=[2,3,5,7,11]
squared_prime=[]
for i in primes:
    squared_prime.append(i**2)

# Exercise 26
m=[[1,2,3],[4,5,6]]
for i in range(len(m)):
    for j in range(len(m[i])):
        pass
for row in m:
    for col in row:
        pass
        # print(col)

# Exercise 27 Matrices summation and subtraction
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[10,11,12],[13,14,15],[16,17,18]]
rows=len(x)
cols=len(x[0])
result=[[0]*cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        result[i][j]=x[i][j]+y[i][j]
print(result)
