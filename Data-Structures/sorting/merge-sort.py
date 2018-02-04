""" Author - Sidharth Satapathy """
""" This is python 3 code """

def merge_sort(arr):
    if(len(arr) > 1):
        mid = int(len(arr)/2)
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i=0
        j=0
        k=0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                k+=1
                i+=1
            else :
                arr[k] = rightHalf[j]
                k+=1
                j+=1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            k+=1
            i+=1
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            k+=1
            j+=1
        return arr

array = input("Enter the elements into the array separated by space : ") 
array = [int(x) for x in array.split(" ")]
print (f"The array after being sorted is : {merge_sort(array)}")   
