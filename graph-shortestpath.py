class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj = {}
        self.isUp = True

class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight
        self.isUp = True

class Graph:
    def __init__(self):
        self.vertList = dict() #consists of all the vertices

    def addEdge(self, start, end, weight):
        v = self.getVertex(start)   # start vertex
        w = self.getVertex(end)     #end vertex
        e = None
        if w.name not in v.adj:     #if w vertex not in the v-adj list
            e = Edge(v.name, w.name, weight)    # create an edge object and store in the e
        else:
            e = v.adj[w.name]    # if vertex w is present, store the edge at e
            e.weight = weight
        v.adj[w.name] = e

    def printGraph(self):
        for vertex_name in self.vertList.keys():    # read the vertex in vertList
            print(vertex_name)                      # print one vertex
            self.printEdges(self.vertList[vertex_name])     #call printedge func

    def printEdges(self, vertex: Vertex):
        for edges in vertex.adj.values():       # access edges from the vertex class adj list values
            print("\t "+edges.endVertex+" "+str(edges.weight))      # print as per the format asked.

    def getVertex(self, vertexName):
        if vertexName not in self.vertList:     # check if the vertex is present in the vertlist, if not
            v = Vertex(vertexName)              # create the vertex and store in  v
            self.vertList[vertexName] = v       # pass the vertex v into the vertList
        else:
            v = self.vertList[vertexName]       # store the vertex under v and return
        return v
def main():
    g = Graph() # or use defaultdict(list)
    g.addEdge("swathi", "siddhart", 20)
    g.addEdge("swathi", "siddhart", 40)
    g.addEdge("swathi", "ka", 10)
    g.addEdge("siddhart", "ka", 30)
    g.addEdge("sneha", "ka", 40)
    g.printGraph()

if __name__=="__main__":
    main()






















"""

            def graph(self, ):
                add
                edge
                add
                vertex
                shortest
                path


###

line[]
line[0] = Belk
line[1] = Grigg
line[2] = 1.2

Belk
Grigg
1.2
Belk
Health
0.5
Duke
Belk
0.6
Belk
Woodward
0.25
Woodward
Grigg
1.1
Grigg
Duke
1.6
Health
Woodward
0.7
Health
Education
0.45
Woodward
Education
1.3
Duke
Education
0.3
Woodward
Duke
0.67

###


"""