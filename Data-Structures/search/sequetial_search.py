""" Author - Sidharth Satapathy """
""" This code is in python 2 """
def seq_search(arr,ele):
    found = False
    i = 0

    while i < len(arr) and not found:
        if arr[i] == ele:
            found = True
        else :
            i+=1
    return found            

def ordered_seq_search(arr,ele):
    found = False
    stopped = False
    i = 0

    while i < len(arr) and not found and not stopped:
        if arr[i] == ele:
            found = True
        else :
            if arr[i] > ele:
                stopped= True
            else :
                i+=1
    return found            



array = raw_input("Enter the array elements separated by space :")
array = [int(x) for x in array.split(" ")]
element = int(raw_input("Enter the element to be search :"))
print "1 - Unordered array"
print "2 - Ordered array"
choice = int(raw_input("Enter choice :"))
if choice == 1:
    print seq_search(array,element)
elif choice == 2:
    print ordered_seq_search(array,element)
else:
    print "Invalid choice."        




