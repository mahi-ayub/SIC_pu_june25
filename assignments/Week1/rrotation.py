def isSameReflection(word1, word2):
    if len(word1) != len(word2):
        return -1
    if word2 in (word1 + word1):
        return 1
    else:
        return -1

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(isSameReflection(word1, word2))