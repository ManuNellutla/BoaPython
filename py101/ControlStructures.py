# looping through words

wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)

print("printing all letters in word list")
print(letterlist)

print("printing all letters in word list - sorted")
print(sorted(letterlist))

print("Print sorted and non duplicates")
print(sorted(set(letterlist)))
