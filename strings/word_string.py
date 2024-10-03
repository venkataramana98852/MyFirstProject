
def string_word_count(str1, k):
    list1=str1.split()

    word_count={}
    for word in list1:
        word=word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1    
    print(word_count)

    match = [word for word, count in word_count.items() if count == k]
    return match

words=string_word_count("I am the Happy person and sad name is venkat", 2)  

if words:
    print(f"the match word is {words}")
else:    
    print("no match")
