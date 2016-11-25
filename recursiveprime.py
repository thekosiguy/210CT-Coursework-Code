def isprime(n, x):
    if n <= 1:
        return False
    if x == 1:
        return True
    else:
        if n % x == 0:
            return False
        else:
            return isprime(n, x-1) 
    
print isprime(8,7)
