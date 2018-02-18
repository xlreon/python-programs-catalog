"""Author - Sidharth Satapathy"""

# Problem 4

# Remove duplicates using hash tables

def removeDuplicates(a):
    unique = []
    helper = set()
    for x in a:
        if x not in helper:
            unique.append(x)
            helper.add(x)
    return unique

a = [1,2,1,3,4,5]
print (a)
print (removeDuplicates(a))        

