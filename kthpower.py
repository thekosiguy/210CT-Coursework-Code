class point:
    def __init__(self):
        self.value = 0
        self.next = None

class header:
    def __init__(self):
        self.value = 0
        self.next_head = None
        self.next_point = None

mat = [[1,4,5], [12,5,6], [6,8,9]]

rowindex, colindex = 0, 0
head = header()
head.value = mat[rowindex][colindex]

while head != None:
    prevhead = head 
    rowindex += 1

    if colindex > 2:
        colindex = 0
        rowindex += 1
        
    head = head.next_head
    head.value = mat[rowindex][colindex]
    prevhead.next_head = head
    print head.value


    
        
    
