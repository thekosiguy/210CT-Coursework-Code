uniquestring = ""

def uncommonElements(a,b, uniquestring):
    for i in a:
        unique = True
        for j in b:
            if i == j:
                unique = False
                break
        if unique == True:
            uniquestring+=i
    return uniquestring

print "Elements not found in second string: "+uncommonElements("1467310","89507", uniquestring)
