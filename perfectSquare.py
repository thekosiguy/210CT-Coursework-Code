def perfectSquare(n):
    for i in range(1, n):
        if (i**2) == n:
            return i
    return str(n)+" has no perfect square" 

print perfectSquare(3)
