"""Author - Sidharth Satapathy"""

# Problem 14

# Returns only the first non-repeated character

def nonRepeated(a):
    n = len(a)
    for i in range(0,n):
        repeated = 0
        for j in range(0,n):
            if i != j and a[i] == a[j]:
                repeated = 1
        if repeated == 0:
            return a[i]
    return 

print (nonRepeated("success"))        

