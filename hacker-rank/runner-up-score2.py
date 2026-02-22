n = input("Enter the number of the array lenght")

scores = input("Enter your scores \n")
scores_array=list(map(int,scores.split()))
max = 0
second_number = 0
temp = 0
for i in scores_array:

    if i > max:
        second_number = max

        max = i
    if i < max and i > second_number :
        second_number = i
print(second_number)
    

