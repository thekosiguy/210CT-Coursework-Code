#parameters = array, start index, end index, mth smallest element
def quicksort(array, start, end, m):
    if start < end:
        pindex = partition(array, start, end)
        quicksort(array, start, pindex-1, m)
        quicksort(array, pindex+1, end, m)
    
    return "ordered array:",array, "mth smallest element = "+str(array[m-1]) 

def partition(array, start, end):
    pivot = array[end]
    pindex = start
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[pindex] = array[pindex], array[i]
            pindex+=1
    array[pindex], array[end] = array[end], array[pindex] 
    return pindex 

print quicksort([7,2,1,6,8,5,3,4], 0, 7, 4) 

    
