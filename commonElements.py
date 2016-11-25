def commonElements(a,b):
    newstring = ""
    for i in a:
        for j in b:
            if i == j and i not in newstring:
                newstring+=i
    return newstring

print commonElements("3758465","9382673")
