"""Author - Sidharth Satapathy"""

# Problem 16

# Finding the first repeated character using hash tables

def findRepeated(a):
    table = {}
    for char in a.lower():
        if char in table:
            table[char] += 1
            return char
        elif char != " ":
            table[char] = 1
        else:
            table[char] = 0
    return 

print (findRepeated("occasion"))               

