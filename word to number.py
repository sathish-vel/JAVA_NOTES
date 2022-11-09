def word2num(word):
    word1=[]
    count=0
    print(word.split(" "))
    print(word.upper())
    print(word)
    for i in word:
        print(i)
        count+=1
    print()    
    print(count)    
    # word1.append(word(split(" ")))
    # for i in word1:
    #     print(i)
    # return{
    #     "one":"1",
    #     "two":"2",
    #     "three":"1",
    #     "four":"1",
    # }.get(word,"invalid")
word=str(input("enter the number is word : "))
# word.append(word1)
# word.split(" ")
# print(word)
word2num(word)
# print(word2num(word))