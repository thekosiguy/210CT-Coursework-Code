import sys

class Graph():
    dic = {}

    def __init__(self):
        self.value = 0
        self.edge = []
        self.state = "unvisited" 
        
    def addValue(self, value):
        self.value = value
        Graph.dic[self.value] = [] 

    def addEdge(self, tonode):
        self.edge.append(tonode)
        tonode.edge.append(self)
        
        self.dic[self.value] = self.edge
        self.dic[tonode.value] = tonode.edge

    def displayGraph(self):
        print "Node    Adjacent list" 
        for node in Graph.dic:
            print " "+str(node)+"      "+str([vertex.value for vertex in Graph.dic[node]])
            
    def DFS(self, node, endnode):
        if node == endnode:
            print "over"
        else:
            node.state = "visit in progress"
            for node in Graph.dic:
                for vertex in Graph.dic[node]:
                    if vertex.state == "unvisited":
                        self.DFS(vertex, endnode)
            node.state = "visited"
            print node.value

    def initialDFS():
        DFS(self, node, endnode)            

array = [1,2,3,4,5,6,7,8,9]

node1 = Graph() 
node2 = Graph()
node3 = Graph() 
node4 = Graph()  
node5 = Graph() 
node6 = Graph()
node7 = Graph() 
node8 = Graph()  
node9 = Graph() 

node1.addValue(1)
node2.addValue(2)
node3.addValue(3)
node4.addValue(4)
node5.addValue(5)
node6.addValue(6)
node7.addValue(7)
node8.addValue(8)
node9.addValue(9)

node1.addEdge(node2)
node1.addEdge(node3)
node3.addEdge(node4)
node3.addEdge(node5)
node4.addEdge(node6)
node4.addEdge(node7)
node4.addEdge(node8)
node5.addEdge(node8)
node5.addEdge(node9)
node7.addEdge(node9)

graph = Graph()
graph.displayGraph()

graph.initialDFS
graph.DFS(node1, node9)  



        
    
