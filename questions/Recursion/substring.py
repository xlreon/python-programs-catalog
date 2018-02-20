""" Author - Sidharth Satapathy """

# To get find how many times a string S can be repeated to make another string B as substring

def makeSubstring(a,b):
    
    tableA = {}
    tableB = {}
    maxCount = 0
    if len(a) == 0 or len(b) == 0:
        return 0
    for i in a:
        tableA[i] = 1
    for i in b:
        if i not in tableA:
            return -1
        if i not in tableB:
            tableB[i] = 1
        else:
            tableB[i] += 1    
    for i in a:
        if i not in tableB:
            return -1    
    for key in tableB:
        if tableB[key] >= maxCount:
            maxCount = tableB[key]
    return maxCount+1

a = "abcd"
b = "cdabcdab"

print (makeSubstring(a,b))        