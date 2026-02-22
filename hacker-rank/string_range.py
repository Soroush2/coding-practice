word="aabbcclll"
word_list=list(word)
word_set=set(word_list)
sorted_list=sorted(word_set)
word_count=[]
count=0
for i in sorted_list:
    letter=i
    count=word_list.count(i)
    
    word_count.append(letter)
    word_count.append(str(count))

print("".join(word_count))