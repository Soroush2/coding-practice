def translate(sentence):
    vowls=['a','e','i','o','u']
    punctuation_marks=[',','.','!','?',':',';']
    consanants=''
    sentence_list=sentence.split()
    pig_equivalant=[]
    index=0
    for word in sentence_list:
        punctuation=[mark for mark in word if mark in punctuation_marks]
        for punc in punctuation:
            word=word.replace(punc,'')
        word_capitalization=False
        first_letter=word[0]
        if first_letter.isupper():
            word_capitalization = True
        if first_letter.lower() not in vowls:
            for letter in word:
                if letter not in vowls:
                    if letter in punctuation_marks:
                        punctuation+=letter
                    else:
                        consanants+=letter
                else:
                    index=word.index(letter)
                    break
            if word_capitalization:
                new_word=(word[index:]+consanants+'ay').capitalize()
            else:
                new_word=(word[index:]+consanants+'ay')

        else:
            new_word=word+'way'
        new_word+="".join(punctuation)
        consanants=''
        punctuation=[]
        pig_equivalant.append(new_word)
    return " ".join(pig_equivalant)
text=''
while text.lower()!='exit':
    text=input("Enter a set of words or type exit: ")
    if translate(text):
        print(translate(text))
