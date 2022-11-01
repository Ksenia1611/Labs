import math
 
class Graph(object):
    def __init__(self, n, Fgraph):
        self.nodes = n
        self.graph = self.simmetric(nodes, Fgraph)
        
    def simmetric(self, nodes, Fgraph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(Fgraph)
        for node, edges in graph.items():
            for AdjacentNode, value in edges.items():
                if graph[AdjacentNode].get(node, False) == False:
                    graph[AdjacentNode][node] = value
        return graph
    
    def GettingEdges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

def DijkstraAlgorithm(graph, StartNode):
    UnvisitedNodes = list(graph.nodes)
    ShortestPath = {}
    PreviousNodes = {}  
    MaxValue = math.inf
    for node in UnvisitedNodes:
        ShortestPath[node] = MaxValue
    ShortestPath[StartNode] = 0
    while UnvisitedNodes:
        CurrentMin = None
        for node in UnvisitedNodes:
            if CurrentMin == None:
                CurrentMin = node
            elif ShortestPath[node] < ShortestPath[CurrentMin]:
                CurrentMin = node
        neighbors = graph.GettingEdges(CurrentMin)
        for neighbor in neighbors:
            TentativeValue = ShortestPath[CurrentMin] + graph.graph[CurrentMin][neighbor]
            if TentativeValue < ShortestPath[neighbor]:
                ShortestPath[neighbor] = TentativeValue
                PreviousNodes[neighbor] = CurrentMin
        UnvisitedNodes.remove(CurrentMin)
    
    return PreviousNodes, ShortestPath

def print_result(PreviousNodes, ShortestPath, StartNode, TargetNode):
    path = []
    node = TargetNode
    
    while node != StartNode:
        path.append(node)
        node = PreviousNodes[node]
    path.append(StartNode)
    
    print("Длина короткого маршрута: {}.".format(ShortestPath[TargetNode]))
    print("Короткий путь: " + " -> ".join(reversed(path)))

nodes = ['A', 'B', 'C', 'D', 'E', 'F','G']
 
GraphEdges = {}
for node in nodes:
    GraphEdges[node] = {}
    
GraphEdges['A']['B'] = 7
GraphEdges['A']['C'] = 1
GraphEdges['A']['G'] = 3
GraphEdges['B']['E'] = 3
GraphEdges['C']['D'] = 4
GraphEdges['D']['E'] = 4
GraphEdges['D']['F'] = 2
GraphEdges['D']['G'] = 2
GraphEdges['E']['F'] = 5
GraphEdges['D']['G'] = 2


graph = Graph(nodes, GraphEdges)

PreviousNodes, ShortestPath = DijkstraAlgorithm(graph=graph, StartNode='A')

print_result(PreviousNodes, ShortestPath, StartNode='A', TargetNode='F')
