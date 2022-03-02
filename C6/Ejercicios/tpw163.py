# There is at least one word in the English language that contains:
    # each of the vowels a, e, i, o, u and y 
    # exactly once and in order. 

# Write a program that searches a file containing a list of words and displays all of the words that meet this constraint. 
# The user will provide the name of the file that will be searched. 

# Display an appropriate error message and exit the program if the user provides an invalid file name or if
# something else goes wrong while searching for words with six vowels in order.

cont = 0

with open("aux/words_alpha.txt") as file:
    for line in file.readlines():
        cont += 1
        print(line.strip())
        if cont > 100: break


def process_word(word):
    count = {"a":0,"e":0,"i":0,"o":0,"u":0,"y":0,}
    for c in word:
        if c in count:
            count[c] += 1


def process_word2(word):
    consonants = list("bcdfghjklmnpqrstvwxz")
    for i in consonants:
        print(i)

process_word2("hola")