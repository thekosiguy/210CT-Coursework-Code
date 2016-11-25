def binarySearch(array, lb, ub):
    boundsarray = [i for i in range(lb, ub+1)]
    
    f = 0
    l = len(array) - 1
    found = False
    numdiv = 0

    while f <= l and found == False:
        mp = (f + l)//2
        for i in boundsarray:
            if array[mp] == i:
                found = True
        if array[mp] > ub:
            l = mp - 1
        elif array[mp] < lb:
            f = mp + 1
        numdiv+=1 


    if found == True:
        return "At least 1 value was found between "+str(lb) +" and "+str(ub) +  " after "+str(numdiv)+" array divide(s)."
    else:
        return "A value wasn't not found within the specified bounds."

print binarySearch([17,20,26,31,44,54,55,65,77,93], 56, 65)
