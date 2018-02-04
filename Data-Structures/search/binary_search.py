""" Author - Sidharth Satapathy """
""" This code is in python 2 """
def binary_search(arr,ele):
    found = False
    first = 0
    last = len(arr)-1

    while first <= last and not found:

        mid = (first+last)/2
        if mid == ele:
            found = True
        else:
            if mid <= ele:
                last = mid-1
            else: 
                first = mid+1
    return found

a = raw_input("Enter the array elememnts separated by space :")
a = [int(a) for x in a.split(" ")]
element = int(raw_input("Enter element to be searched :"))

print binary_search(a,element)                
