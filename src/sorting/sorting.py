# TO-DO: complete the helper function below to merge 2 sorted arrays
verbose = 0
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    for i in range(elements):
        if  len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        else:
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB.pop(0)
                if verbose:
                    print('Merge -->', merged_arr)
            elif arrA[0] < arrB[0]:
                merged_arr[i] = arrA.pop(0)
                if verbose:
                    print('Merge -->', merged_arr)
            else:
                merged_arr[i] = arrA.pop(0)
                if verbose:
                    print('Merge -->', merged_arr)
                i += 1
                merged_arr[i] = arrB.pop(0)
                if verbose:
                    print('Merge -->', merged_arr)



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    
    if len(arr)>1:
        mid = len(arr) // 2
        mid = mid if mid else 1
        l = arr[:mid]
        r = arr[mid:]
        l = merge_sort(l)
        r = merge_sort(r)
        arr = merge(l, r)
        if verbose:
            print('MergeSort -->',l, r, arr)
        
    return arr
        
    # print(mid, l, r, arr)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
# print(merge([-3,-2,-1,-0,1,2,3,3,3], [4,5,6,7,8,9,10,34,34,34,55,67]))