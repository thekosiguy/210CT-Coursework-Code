class Node(object):
  def __init__(self, value):
      self.value=value
      self.next=None
      self.prev=None

class List(object):
  def __init__(self):
      self.head=None
      self.tail=None
  def insert(self,n,x):
      #Not actually perfect: how do we prepend to an existing list?
      if n!=None:
          x.next=n.next
          n.next=x
          x.prev=n
          if x.next!=None:
              x.next.prev=x              
      if self.head==None:
          self.head=self.tail=x
          x.prev=x.next=None
      elif self.tail==n:
          self.tail=x
  def remove(self,n):
      if n.prev!=None:
         n.prev.next = n.next
      else:
          self.head = n.next
      if n.next!=None:
          n.next.prev = n.prev
      else:
          self.tail = n.prev   
  def display(self):
      values=[]
      n=self.head
      while n!=None:
          values.append(str(n.value))
          n=n.next
      print ("List: ", ",".join(values))
  def f(self,head):
    
    if head != None:
      print("\tDBG: f(",head.value,")")
    else:
      print("\tDBG: f(None)")

    if head == None:
      return
    # recursive call
    self.f(head.next)
    print(head.value)

    
if __name__ == '__main__':

  lst = List()

  lst.insert(None, Node(1))
  lst.insert(lst.head,Node(2))
  lst.insert(lst.head.next,Node(3))

  lst.display()
  lst.f(lst.head)

  
##  l=List()
##  l.insert(None, Node(4))
##  l.insert(l.head,Node(6))
##  l.insert(l.head,Node(8))
##  l.display()
