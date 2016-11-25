import random

def randShuffle(n):
    #calculate size of array n
    l = len(n)
    '''loop through array l-1 times and during each loop store 2 random values from
    array in variables randval and randval2, store their corresponding indexes
    in ind and ind2''' 
    for i in range(0, l):
        randval = n[random.randint(0, l-1)]
        randval2 = n[random.randint(0, l-1)]
        ind = n.index(randval)
        ind2 = n.index(randval2)

        '''Simply replace the value stored in array n in position ind with
        the second random value and the first random value in position ind2'''
        
        n[ind] = randval2
        n[ind2] = randval

    return n 

print randShuffle([1,3,5,7,9])

#Algorithm is clear and concise and has a defined input and output
#It has a finite range so it will definitely terminate sooner or later
#Produces the correct result for all instances provided that the input is appropriate
                    
