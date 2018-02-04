""" Author - Sidharth Satapathy """
""" This is python 3 code """

def selection_sort(arr):
    
    for i in range(len(arr)-1,0,-1):
        positionMax = 0
        for j in range(1,i+1):
            if arr[j] > arr[positionMax]:
                positionMax = j
        temp = arr[i]
        arr[i] = arr[positionMax]
        arr[positionMax] = temp
    return arr

array = input("Enter the array to sort :")
array = [int(x) for x in array.split(" ")]
print (f"The array after sorting is : {selection_sort(array)}")               
