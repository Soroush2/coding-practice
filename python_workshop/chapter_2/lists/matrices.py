x=[
    [1,2],
    [4,5],
    [7,8]
]
y=[
    [11,12,13,14],
    [15,16,17,18]
]
def matrice_additon(x,y):
    if len(x) == len(y) and len(x[0]) == len(y[0]):
        rows=len(x)
        cols=len(x[0])
        z=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                z[i][j]=x[i][j]+y[i][j]
        return z
    else:
        return "The Matrices Shold Be Of The Same Size"
def matrice_subtraction(x,y):
    if len(x) == len(y) and len(x[0]) == len(y[0]):
        rows=len(x)
        cols=len(x[0])
        z=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                z[i][j]=x[i][j]-y[i][j]
        return z
    else:
        return "The Matrices Shold Be Of The Same Size"
def matrice_multiplication(x,y):
    if len(x[0]) == len(y):
        rows=len(x)
        cols=len(y[0])
        col_x=len(x[0])
        z=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                sum = 0
                for k in range(col_x):
                    sum+=x[i][k]*y[k][j]
                z[i][j]=sum
        return z
    else:
        return "Cannot Multiply These Matrices"
print(matrice_multiplication(x,y))
