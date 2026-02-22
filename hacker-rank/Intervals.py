n=int(input("Enter the number of lists: "))
m = int(input("Enter the number of elements of each list"))
custom_list=[None]* n
i=0
custom_list=[list(map(int,input("Enter your values of your lists: ").split())) for _ in range(n)]
j=0
count=0
other_list=[[]for _ in range(n)]
for i in custom_list:
    for start_time in range(i[j],i[j+1]+1):
        other_list[count].append(start_time)
        start_time+=1
    count+=1
j = 0
count= 0
for my_list in range(len(other_list)-1):
    for member in range(len(other_list[my_list])):
        if other_list[my_list][member] in other_list[my_list+1]:
            custom_list[my_list][0]=other_list[my_list][0]
            custom_list[my_list][1]=other_list[my_list+1][len(other_list[my_list+1])-1]
            custom_list.remove(custom_list[my_list+1])
            my_list=0
            # print(other_list[my_list][0],other_list[my_list+1][len(other_list[my_list+1])-1])
            break
print(custom_list)