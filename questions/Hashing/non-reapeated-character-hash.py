"""Author - Sidharth Satapathy"""

# Problem 15

# find the first non-repeated character using hash tables

def nonRepeated(a):
    table = {}
    for char in a.lower():
        if char in table:
            table[char] += 1
        elif char != " ":
            table[char] = 1
        else:
            table[char] = 0
    for char in a.lower():
        if table[char] == 1:
            return char 
    return 

print (nonRepeated("Success"))                  

