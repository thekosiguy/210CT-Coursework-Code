def reverseWords(sentence):
    reversedsentence = "" 
    sentence = sentence.split()
    sentence = reversed(sentence) 
    for i in sentence:
        reversedsentence+=i+" "
    return reversedsentence 

print reverseWords("This is awesome") 
