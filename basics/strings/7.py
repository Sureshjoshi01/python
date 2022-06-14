word = input("Enter a word : ")
if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'u' or word[0] == 'u':
    word1 = word+'way'
    print(word1.lower())
else:
    word2 = word[1:]+word[0]+'ay'  
    print(word2.lower())
   

