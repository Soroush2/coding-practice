shopping=["bread", "milk","egg"]
#What happens if i insert at index 100?
shopping.insert(-100,'banana')
print(shopping)
#if index > len(list), Python inserts at the end. if index < 0 python inserts at the begining 
#Experiment #2
m=[[1,2,3],[4,5,6]]
m.append([7,8,9])
for i in range(len(m)):
    for j in range(len(m[i])):
        pass
        # print(m[i][j])
#Experiment #3
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[10,11,12],[13,14,15],[16,17,18]]
rows=len(x)
cols=len(x[0])
result=[[0 for _ in range(cols) ] for _ in range(rows)]
result=[[0]*cols for _ in range(rows)]
# result = [[0] * cols] * rows  # ❌ Wrong!
result[0][1]=2
for i in result:
    print(id(i))
print(result)
#Experiment #4
def some_array(x):
    print(id(x))
    x[0]=1
    print(id(x))
    x=[1,2]
    print(id(x))
a=[1,2,3]
print(a,id(a))
some_array(a)
#