class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph if it doesn't already exist
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add an edge between two vertices (assuming an undirected graph)
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:  ## to add an edge there should be vertex1 and vertex2 in adjacency list which is a dictionary first
            self.adjacency_list[vertex1].append(vertex2)  # adding to the list of vertex1 
            self.adjacency_list[vertex2].append(vertex1)  # Uncomment for an undirected graph

    def display(self):
        # Display the adjacency list representation of the graph
        for vertex, neighbors in self.adjacency_list.items():
            print(vertex, '->', neighbors)


# Create a graph instance
graph = Graph()
# Add vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')


# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

# Display the graph
graph.display()

