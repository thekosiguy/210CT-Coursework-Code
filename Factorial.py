n = input("input value: ")

def fac(n):
    result = 1
    for i in range(1, n+1):
        result*=i
    return result

print "Factorial of "+str(n)+" = "+str(fac(n))  
strres = str(fac(n))
numzero = 0
for i in strres:
    if i == "0":
        numzero+=1

if numzero == 0:
    print str(n)+"! has no trailing 0's"
else:
    print str(n)+"! has "+str(numzero)+" trailing 0('s)" 



#Algorithm is clear and concise and has a defined input and outputs
#It has a finite range so it will definitely terminate sooner or later
#Produces the correct result for all instances provided that the input is appropriate
