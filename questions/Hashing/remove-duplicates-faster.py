"""Author - Sidharth Satapathy"""

# Problem 3

# sort the array and remove duplicates in consecutive positions
# Time complexity O(nlog m)

def removeDuplicates(a):
    a.sort()
    j = 0
    for i in range(1,len(a)):
        if a[j] != a[i]:
            j += 1
            a[j] = a[i]
    print (a[:j+1])
a = [1,2,1,3,4,5]
print (a)
removeDuplicates(a)            

