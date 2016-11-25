def maxAsc(array):
    asccount, maxasccount, l, i = 0, 0, len(array), 0
    asclist = []
    firstindex = i
    lastindex = 0
    tempindex = 0

    if len(array) == 0:
        return "array empty"
    elif len(array) == 1:
        return array 
    
    while i < l-1 and len(array) > 1:
        if array[i] < array[i+1]:
            asccount += 1
        elif array[i] >= array[i+1]:
            asccount = 0
            tempindex = i
        if maxasccount < asccount:
                maxasccount = asccount
                firstindex = tempindex + 1  
        i += 1
    maxasccount += 1
    lastindex += 1
        
    for i in range(firstindex, firstindex+maxasccount):
        asclist.append(array[i])
        
    return ("Length of ascending list = "+str(maxasccount)+ ", Ascending list: "+str(asclist))

print maxAsc([7,8,1,2,3,5,45,53,4,9,10,19,27])

