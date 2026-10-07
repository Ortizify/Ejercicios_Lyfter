words = []
#1 Ask the user to enter 5 words
for i in range (5):
    word = input("Ingrese una palabra: ")
    words.append(word)
#2 Create a new list with words longer than 4 letters 
long_words = []
for i in range (len(words)):
    if len(words[i]) > 4:
        long_words.append(words[i])
#3 Display the new list 
print(long_words)