"""Author - Sidharth Satapathy"""

# Problem 2

# Removing duplicates O(n^2)

def remoceDuplicates(a):
    m = 0
    for i in range(0,len(a)):
        if not elem(a,m,a[i]):
            a[m] = a[i]
            m += 1
    return m        
def elem(a,n,e):
    for i in range(0,n):
        if(a[i] == e):
            print (a[i]," is duplicate")
            return 1
    return 0

a = [1,2,1,3,4,5]
remoceDuplicates(a)
print (a)        
