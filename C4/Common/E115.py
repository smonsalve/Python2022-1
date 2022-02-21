
def pig(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        word=word+"way"
        return word
    else:
        word=word[1:]+"ay"
        return word

print(pig("think"))
