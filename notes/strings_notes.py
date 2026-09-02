sentence = "the quick brown fox jumps over the lazy dog"
print(sentence)
print(sentence.find("e"))
print(sentence[10:15])
word = input("what word do you want sire? ")
start = sentence.find(word)
length = len(word)
print(sentence[start:start+length])