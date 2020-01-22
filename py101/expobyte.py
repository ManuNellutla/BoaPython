
byteNames = ("byte","kilobyte","megabyte","gigabyte","terabyte","peta","exa","zetta","yotta")
for a in range(1,9):
    print(" %s is 1024 ^ %d and value is = %d" %(byteNames[a],a, 1024 ** a))