n = input("Enter the number of the array lenght")

scores = input("Enter your scores \n")
scores_array=list(map(int,scores.split()))
i = 0
max= 0
sorted_array=[]
length= len(scores_array)
while len(sorted_array) < length:
    max=float('-inf')
    for i in scores_array:
        if i >max :
            max = i
    sorted_array.append(max)
    while max in scores_array:
        scores_array.remove(max)
    

print(sorted_array[1])
    


# for _ in range(2):
#     for i in scores_array:
#         if i > max:
#             max=i
#     while max in scores_array:
#         scores_array.remove(max)
#     temp = max
#     max=0