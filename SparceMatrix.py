#Sparce Matrices

def isSparce(n):
    zero = 0
    notzero = 0
    Sparce = False

    for i in n:
        for j in i:
            if j == 0:
                zero+=1
            else:
                notzero+=1

    if zero > notzero:
        Sparce = True

    return Sparce
 
numofmatrix = input("input of number of matrices: ")

#Assumes matrices have same size

def addMatrices(Sparcearray):
    if len(Sparcearray[0][0]) == len(Sparcearray[1][0]) and len(Sparcearray[0][1]) == len(Sparcearray[1][1]):
        
        newmatrix = [[],[]]
        index = 0
        
        while 1:
            res = Sparcearray[0][0][index] + Sparcearray[1][0][index]
            newmatrix[0].append(res)
            index +=1
            if index == len(Sparcearray[0][0]):
                break
        
        index = 0

        while 1:
            res = Sparcearray[0][1][index] + Sparcearray[1][1][index]
            newmatrix[1].append(res)
            index +=1
            if index == len(Sparcearray[0][1]):
                break

        return newmatrix
    
    else:
        return "Matrices must have the same size"
    

def subMatrices(Sparcearray):
    newmatrix = [[],[]]
    index = 0

    if len(Sparcearray[0][0]) == len(Sparcearray[1][0]) and len(Sparcearray[0][1]) == len(Sparcearray[1][1]):
        while 1:
            res = Sparcearray[0][0][index] - Sparcearray[1][0][index]
            newmatrix[0].append(res)
            index +=1
            if index == len(Sparcearray[0][0]):
                break

        index = 0

        while 1:
            res = Sparcearray[0][1][index] - Sparcearray[1][1][index]
            newmatrix[1].append(res)
            index +=1
            if index == len(Sparcearray[0][1]):
                break

        return newmatrix
    else:
        return "Matrices must have the same size"

Sparcearray = []

def multiplyMatrices(Sparcearray):
    if len(Sparcearray[0]) == len([i for i in Sparcearray[1][0]]):
        
        l = Sparcearray 
        newmat = [[],[]]
        t = 0

        lindex = 0
        pos = 0

        for i in l[0][0]:
            t+=i*l[1][lindex][pos]
            lindex+=1

        newmat[0].append(t)

        lindex = 0
        pos = 1
        t = 0

        for i in l[0][0]:
            t+=i*l[1][lindex][pos]
            lindex+=1

        newmat[0].append(t)
    
        lindex = 0
        pos = 0
        t = 0

        for i in l[0][1]:
            t+=i*l[1][lindex][pos]
            lindex+=1

        newmat[1].append(t)

        lindex = 0
        pos = 1
        t = 0

        for i in l[0][1]:
            t+=i*l[1][lindex][pos]
            lindex+=1

        newmat[1].append(t)

        return newmat
    else:
        return "Error: number of columns in first matrix must be equal to number of rows in second matrix"
                                    

for i in range(0, numofmatrix):
    matrix = input("input matrix: ") 
    if isSparce(matrix):
        Sparcearray.append(matrix)
    else:
        print "Matrix is not sparce!"
        break 


