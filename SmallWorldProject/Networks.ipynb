{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2d1a6c02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<module 'NetGraphics' from '/Users/chrisdupre/SmallWorldProject/NetGraphics.py'>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import NetGraphics\n",
    "import imp\n",
    "imp.reload(NetGraphics)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "978ebbe9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class UndirectedGraph:\n",
    "    \n",
    "    def __init__(self):\n",
    "        self.connections = {}\n",
    "    \n",
    "    def HasNode(self,node):\n",
    "        return (node in self.connections)\n",
    "    \n",
    "    def AddNode(self,node):\n",
    "        if not self.HasNode(node):\n",
    "            self.connections[node] = [node]\n",
    "        return\n",
    "    \n",
    "    def AddEdge(self,node1,node2):\n",
    "        if not self.HasNode(node1):\n",
    "            self.AddNode(node1)\n",
    "        if not self.HasNode(node2):\n",
    "            self.AddNode(node2)\n",
    "        if not node2 in self.connections[node1]:\n",
    "            self.connections[node1].append(node2)\n",
    "        if not node1 in self.connections[node2]:\n",
    "            self.connections[node2].append(node1)\n",
    "        return \n",
    "    \n",
    "    def GetNodes(self):\n",
    "        return list(self.connections.keys())\n",
    "    \n",
    "    def GetNeighbors(self,node):\n",
    "        return self.connections[node].copy()\n",
    "    \n",
    "    \n",
    "    def FindPathLengthsFromNode(graph, node):\n",
    "        distances = {node:0}\n",
    "        currDist = 0\n",
    "        currentLevel = [node]\n",
    "        nextLevel = graph.GetNeighbors(node)\n",
    "        while not nextLevel==[]:\n",
    "            currDist +=1\n",
    "            currentLevel = nextLevel\n",
    "            nextLevel = []\n",
    "            for node in currentLevel :\n",
    "                if not node in distances:\n",
    "                    distances[node] = currDist\n",
    "            for node in currentLevel:\n",
    "                for neigh in graph.GetNeighbors(node):\n",
    "                    if not(neigh in distances):\n",
    "                        nextLevel.append(neigh)\n",
    "        return distances\n",
    "    \n",
    "    def FindAllPathLengths(graph):\n",
    "        tupleDict = {}\n",
    "        for node in graph.GetNodes():\n",
    "            currDistDict = graph.FindPathLengthsFromNode(node)\n",
    "            for otherNode in currDistDict:\n",
    "                tupleDict[(node,otherNode)] = currDistDict[otherNode]\n",
    "        return tupleDict\n",
    "    \n",
    "    def FindAveragePathLength(graph):\n",
    "        tupleDict = graph.FindAllPathLengths()\n",
    "        return sum(tupleDict.values())/len(tupleDict.keys())\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "df68fbbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pentagraph():\n",
    "    \"\"\"pentagraph() creates a simple 5-node UndirectedGraph, and then uses\n",
    "    the imported NetGraphics module to layout and display the graph.\n",
    "    The graph is returned from the function.\n",
    "    \"\"\"\n",
    "    g = UndirectedGraph()\n",
    "    g.AddEdge(0,2)\n",
    "    g.AddEdge(0,3)\n",
    "    g.AddEdge(1,3)\n",
    "    g.AddEdge(1,4)\n",
    "    g.AddEdge(2,4)\n",
    "    NetGraphics.DisplayCircleGraph(g)\n",
    "    return g\n",
    "\n",
    "def circle8():\n",
    "    \"\"\"circle8() creates an 8-node UndirectedGraph, where the nodes are\n",
    "    arranged in a circle (ring), and then uses the imported NetGraphics\n",
    "    module to layout and display the graph.  The graph is returned from\n",
    "    the function.\n",
    "    \"\"\"\n",
    "    g = UndirectedGraph()\n",
    "    g.AddEdge(0,1)\n",
    "    g.AddEdge(1,2)\n",
    "    g.AddEdge(2,3)\n",
    "    g.AddEdge(3,4)\n",
    "    g.AddEdge(4,5)\n",
    "    g.AddEdge(5,6)\n",
    "    g.AddEdge(6,7)\n",
    "    g.AddEdge(7,0)\n",
    "    NetGraphics.DisplayCircleGraph(g)\n",
    "    return g\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ceb5d8e1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
