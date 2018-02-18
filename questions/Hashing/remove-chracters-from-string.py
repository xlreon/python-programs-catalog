"""Author - Sidharth Satapathy"""

# Problem 13

# Remove a set of characters from a given string

def removeCharacters(str,characters):
    table = {}
    temp = []
    for char in characters.lower():
        table[char] = 1
    for char in str.lower():
        if char in table:
            continue
        else:
            temp.append(char)
    return "".join(temp)

print (removeCharacters("success","cs"))            

