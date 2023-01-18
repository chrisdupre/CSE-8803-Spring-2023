import NetGraphics

class UndirectedGraph:
    
    def __init__(self):
        self.connections = {}
    
    def HasNode(self,node):
        return (node in self.connections)
    
    def AddNode(self,node):
        if not self.HasNode(node):
            self.connections[node] = [node]
        return
    
    def AddEdge(self,node1,node2):
        if not self.HasNode(node1):
            self.AddNode(node1)
        if not self.HasNode(node2):
            self.AddNode(node2)
        if not node2 in self.connections[node1]:
            self.connections[node1].append(node2)
        if not node1 in self.connections[node2]:
            self.connections[node2].append(node1)
        return 
    
    def GetNodes(self):
        return list(self.connections.keys())
    
    def GetNeighbors(self,node):
        return self.connections[node].copy()
    
    
    def FindPathLengthsFromNode(graph, node):
        distances = {node:0}
        currDist = 0
        currentLevel = [node]
        nextLevel = graph.GetNeighbors(node)
        while not nextLevel==[]:
            currDist +=1
            currentLevel = nextLevel
            nextLevel = []
            for node in currentLevel :
                if not node in distances:
                    distances[node] = currDist
            for node in currentLevel:
                for neigh in graph.GetNeighbors(node):
                    if not(neigh in distances):
                        nextLevel.append(neigh)
        return distances
    
    def FindAllPathLengths(graph):
        tupleDict = {}
        for node in graph.GetNodes():
            currDistDict = graph.FindPathLengthsFromNode(node)
            for otherNode in currDistDict:
                tupleDict[(node,otherNode)] = currDistDict[otherNode]
        return tupleDict
    
    def FindAveragePathLength(graph):
        tupleDict = graph.FindAllPathLengths()
        return sum(tupleDict.values())/len(tupleDict.keys())
    
def pentagraph():
    """pentagraph() creates a simple 5-node UndirectedGraph, and then uses
    the imported NetGraphics module to layout and display the graph.
    The graph is returned from the function.
    """
    g = UndirectedGraph()
    g.AddEdge(0,2)
    g.AddEdge(0,3)
    g.AddEdge(1,3)
    g.AddEdge(1,4)
    g.AddEdge(2,4)
    NetGraphics.DisplayCircleGraph(g)
    return g

def circle8():
    """circle8() creates an 8-node UndirectedGraph, where the nodes are
    arranged in a circle (ring), and then uses the imported NetGraphics
    module to layout and display the graph.  The graph is returned from
    the function.
    """
    g = UndirectedGraph()
    g.AddEdge(0,1)
    g.AddEdge(1,2)
    g.AddEdge(2,3)
    g.AddEdge(3,4)
    g.AddEdge(4,5)
    g.AddEdge(5,6)
    g.AddEdge(6,7)
    g.AddEdge(7,0)
    NetGraphics.DisplayCircleGraph(g)
    return g

