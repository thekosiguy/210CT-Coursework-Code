lays = 3
hatch = 5
start = 1

aliens = [0]*31


for i in range(1, 31):
    if i == 1:
        aliens[i] = start
    elif i <= hatch:
        aliens[i] = aliens[i-1]
    else:
        aliens[i] = aliens[i-1] + aliens[i-hatch]*lays
    if i == 30:
        print aliens[i] 


    
        
    

