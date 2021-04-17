
input_file = open('english.sorted', encoding="iso-8859-1")
#input_file = open('english.sorted.python', 'r')


wordlengths = {}

for word in input_file.readlines():
    length = len(word)

    if(length in wordlengths):
        wordlengths[length]+=1
    else:
        wordlengths[length] = 1

print("Word Length\tOccurrences")


for length in wordlengths.keys():
    print(str(length)+ "\t\t" + str(wordlengths[length]))
