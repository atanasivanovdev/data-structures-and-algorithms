class Graph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}

    def add_vertex(self, node):
        if not isinstance(node, int):
            raise TypeError("Node must be an integer")
        
        self.adjacentList[node] = set()
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        if not all([node in self.adjacentList for node in (node1, node2)]):
            raise ValueError("Nodes must be added to the graph!")
        
        if node1 in self.adjacentList[node2]:
            raise ValueError("The edge already exists")
        
        self.adjacentList[node1].add(node2)
        self.adjacentList[node2].add(node1)

    def show_connections(self):
        all_nodes = self.adjacentList.keys()
        for node in all_nodes:
            node_connections = self.adjacentList[node]
            connections = ""
            vertex = None
            for vertex in node_connections:
                connections += f"{vertex} "
            print(f"{node} --> {connections}")


my_graph = Graph()
my_graph.add_vertex(0)
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_vertex(6)
my_graph.add_edge(3, 1)
my_graph.add_edge(3, 4)
my_graph.add_edge(4, 2)
my_graph.add_edge(4, 5)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 0)
my_graph.add_edge(0, 2)
my_graph.add_edge(6, 5)

my_graph.show_connections()