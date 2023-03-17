# Swathi Rajendran

import heapq
import sys
import math

"""
Vertex Class holds the information about the vertices.
The constructor holds the name, adjacent vertices name as keys
and its edge to the adjacent vertex as the values in the adj dictionary.
isUp - holds the boolean value (True) for Vertex is up (working phase).
"""

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj = {}
        self.isUp = True

'''
Edge Class holds the information about the edges.
The constructor holds the startVertex, endVertex between which the edge passes.
weight - The distance between the start and end vertex.
isUp - This gives a boolean value (True) when the Edge is up (working phase).
'''
class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = float(weight)
        self.isUp = True
'''
Graph class represents all the vertices and edges in a graph and holds all the methods that are needed to compute 
the tasks as a part of the problem statement. 
The constructor holds a (vertList) 
dictionary of list of all vertices names as keys and vertices object as values
'''

class Graph:
    def __init__(self):
        self.vertList = dict()

    # BUILDING THE INITIAL GRAPH
    '''
    addEdge method- if an edge is already present, updates the edge between start and end vertex, 
    if not creates a new edge object and adds it. 
    '''
    def addEdge(self, start, end, weight):
        start = self.getVertex(start)
        end = self.getVertex(end)
        e = None
        if end.name not in start.adj:
            e = Edge(start.name, end.name, weight)
        else:
            e = start.adj[end.name]
            e.weight = weight
        start.adj[end.name] = e
    '''
    printGraph method - all the vertices whose vertex is up working is printed along with its 
    adjacent vertices names and edges weight which are called from the printEdges method inside the loop,
    if not working (DOWN) is printed near it.
    '''
    def printGraph(self):
        items = sorted(self.vertList.items())
        for vertex_name, vertex in items:
            if vertex.isUp:
                print(vertex_name)
            else:
                print(vertex_name + " " + "DOWN")
            self.printEdges(self.vertList[vertex_name])
    '''
    printEdges method - all the adjacent vertices names of the vertex
    and its edges weight where edge is up working is printed, 
    if not working (DOWN) is printed near the respective adjacent vertex and edge weight.
    '''
    def printEdges(self, vertex: Vertex):
        value = sorted(vertex.adj.keys())
        for edge in value:
            if vertex.adj[edge].isUp:
                print(" "+" "+ vertex.adj[edge].endVertex + " " + str(
                    vertex.adj[edge].weight))
            else:
                print(" "+" "+ vertex.adj[edge].endVertex + " " + str(vertex.adj[edge].weight) + " " + "DOWN")
    '''
    getVertex method - checks if a vertex is already in the vertList dictionary,
    if not creates the vertex object and adds it to the vertList dictionary.
    '''
    def getVertex(self, vertexName):
        if vertexName not in self.vertList:
            v = Vertex(vertexName)
            self.vertList[vertexName] = v
        else:
            v = self.vertList[vertexName]
        return v

    # CHANGES TO THE GRAPH
    '''
    edgeDown method - sets the edge to down (not working phase) 
    which passes between a start and end vertex to type boolean (FALSE).
    '''

    def edgeDown(self, start, end):
        edge = self.vertList[start].adj[end]
        edge.isUp = False
    '''
    edgeUp method - sets the edge to up (working phase) passing between
    start and end vertex to type boolean (TRUE).
    '''

    def edgeUp(self, start, end):
        edge = self.vertList[start].adj[end]
        edge.isUp = True
    '''
    vertexDown method - sets the vertex to down (not working phase) to type boolean (FALSE).
    '''
    def vertexDown(self, vertex):
        vertex = self.vertList[vertex]
        vertex.isUp = False
    '''
    vertexUp method - sets the vertex to up (working phase) to type boolean (TRUE).
    '''
    def vertexUp(self, vertex):
        vertex = self.vertList[vertex]
        vertex.isUp = True
    '''
    deleteEdge method - deletes the edge passing between the start and end vertex 
    given as paramater to the deleteEdge method.
    '''
    def deleteEdge(self, start, end):
        del self.vertList[start].adj[end]

    # FINDING THE SHORTEST PATH
    '''
    Shortest Path from the start vertex to end vertex is found using Dijkstra's Algorithm which uses priority queue.
    Min Binary heap data structure is used here as it is the best for priority queue implementation.
    '''
    '''
    shortestPath method - Using Heapq inbuilt library function in python, 
    the smallest distance edge is popped from the queue, 
    if not seen or less than the already stored distance of the vertex then looked into its 
    adjacent vertices. Updates the distance by adding the cost and edge weight,
    checks if the new distance is less than the stored distance, 
    if so updates the distance and pushes it into the queue.
    The time complexity for shortest path is O((V+E)logV)
    '''
    #finding ShortestPath using Heapq
    def shortestPath(self, start, end):
        if start not in self.vertList or end not in self.vertList:
            return "The given Input vertices to find the shortest path is not present in the graph"
        else:
            queue = [(0, start, [])]
            seen = set()
            dist = {}
            dist[start] = 0
            if self.vertList[start].isUp:
                while len(queue) > 0:
                    cost, v, path = heapq.heappop(queue)
                    if v == end:
                        return " ".join(path + [v]) +" "+str((math.floor(cost*10**2)/10**2))
                    elif v != seen:
                        seen.add(v)
                        if cost > dist[v]:
                            continue
                        path = path + [v]
                        for adjVertex, edge in self.vertList[v].adj.items():
                            if self.vertList[adjVertex].isUp and edge.isUp:
                                distance = cost + edge.weight
                                if adjVertex not in dist:
                                    dist.update({adjVertex: distance})
                                elif adjVertex in seen:
                                    continue
                                elif distance < dist[adjVertex]:
                                    dist[adjVertex] = distance
                                heapq.heappush(queue, (distance, adjVertex, path))
                print("The shortest path from"+start+"to"+end+"Is not found")

    # FINDING REACHABLE VERTICES
    '''
    To find the reachable vertices, Depth First Search Algorithm is used here.
    Its time complexity is O(V(V + E)), 
    which indicates that for each vertex, we traverse all the reachable vertices and all the edges.
    When a particular edge or a vertex is down, a few of the edges and vertices might be removed from the reachable vertices.
    The above mentioned time complexity is excluding the sorting, which is done to print the vertices in alphabetical order.
    '''
    '''
    reachable method - For every vertex in the graph, the reachableNodes method is called to 
    add its adjacent vertices if not already in the reachable set and sorts the set to print 
    the vertices in alphabetical order. 
    '''

    def reachable(self):
        items = sorted(self.vertList.keys())
        for vertex_name in items:
            if self.vertList[vertex_name].isUp:
                print(vertex_name)
            else:
                continue
            reachable_set = set()
            self.reachableNodes(vertex_name, reachable_set)
            sortedSet = sorted(reachable_set)
            for i in sortedSet:
                if i == vertex_name:
                    continue
                else:
                    print(" "+" "+ i)

    '''
    reachableNodes method - This gets the Vertex and reachable set from the reachable method
    and checks if an adjacent vertex is present in the visited set, if not adds the vertex to it recursively.
    '''

    def reachableNodes(self, v, visited):
        visited.add(v)
        for adjvertex, edge in self.vertList[v].adj.items():
            if edge.isUp == False or self.vertList[adjvertex].isUp == False:
                continue
            elif adjvertex not in visited:
                self.reachableNodes(adjvertex, visited)

'''
subMain - This method constructs the graph based on the input given in the file
'''
def subMain(filename):
    g = Graph()
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split()
        start = line[0]
        end = line[1]
        weight = line[2]
        g.addEdge(start, end, weight)
        g.addEdge(end, start, weight)
    return g

'''
Main function - From here the program execution starts where we get the filename from the user for constructing the graph.
Various constraints are performed here like
printGraph; addEdge; deleteEdge; edgeDown; edgeUp; vertexDown; vertexUp; reachable; path start to end; quit 
'''
def main():
    temp=sys.argv
    if(len(temp)==1):
        print("Please give the input file name, the query filename and the output filename")
        return
    else:
       filename = temp[1]
       g = subMain(filename)
       for line in sys.stdin:
            lines = line.split()
            if "graph" == lines[0]:
                filename = lines[1]
                print(filename)
                g = subMain(filename)
            elif "print" == lines[0]:
                g.printGraph()
            elif "addedge" == lines[0]:
                start = lines[1]
                end = lines[2]
                weight = lines[3]
                if start == lines[1] and end == lines[2]:
                    g.addEdge(start, end, float(weight))
            elif "deleteedge" == lines[0]:
                start = lines[1]
                end = lines[2]
                if start == lines[1] and end == lines[2]:
                    g.deleteEdge(start, end)
            elif "edgedown" == lines[0]:
                start = lines[1]
                end = lines[2]
                if start == lines[1] and end == lines[2]:
                    g.edgeDown(start, end)
            elif "edgeup" == lines[0]:
                start = lines[1]
                end = lines[2]
                if start == lines[1] and end == lines[2]:
                    g.edgeUp(start, end)
            elif "vertexdown" == lines[0]:
                start = lines[1]
                if start == lines[1]:
                    g.vertexDown(start)
            elif "vertexup" == lines[0]:
                start = lines[1]
                if start == lines[1]:
                    g.vertexUp(start)
            elif "reachable" == lines[0]:
                g.reachable()
            elif "path" == lines[0]:
                start = lines[1]
                end = lines[2]
                if start == lines[1] and end == lines[2]:
                    print(g.shortestPath(start, end))
            elif "quit" == lines[0]:
                break


'''
Main function is called here.
'''
if __name__=="__main__":
    main()


























