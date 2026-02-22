def pig_it(text):
    punctuation_marks=["'","!",'"',"?"]
    pig_word=[]
    words=list(text.split())
    if words[0].lower() !='exit':
        for word in words:
                first_letter=word[0]
                if first_letter not in punctuation_marks:
                    new_word=word[1:]+first_letter+'ay'
                    pig_word.append(new_word)
                else:
                    pig_word.append(word)
        return pig_word
        
text=''
while text.lower()!='exit':
    text=input("Enter a set of words or type exit: ")
    if pig_it(text):
        result=" ".join(pig_it(text))
        print(result)






