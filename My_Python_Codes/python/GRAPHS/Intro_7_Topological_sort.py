# from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_edge(self, u, v):
#         self.graph[u].append(v)

#     def topological_sort(self):
#         # Count the in-degrees of all vertices
#         in_degree = {vertex: 0 for vertex in self.graph}
#         for vertex in self.graph:
#             if vertex not in in_degree:
#                 in_degree[vertex] = 0
#             for neighbor in self.graph[vertex]:
#                 in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

#         # Initialize a queue for topological sorting
#         queue = deque()
#         for vertex in in_degree:
#             if in_degree[vertex] == 0:
#                 queue.append(vertex)

#         # Perform topological sorting
#         result = []
#         while queue:
#             vertex = queue.popleft()
#             result.append(vertex)
#             for neighbor in self.graph[vertex]:
#                 in_degree[neighbor] -= 1
#                 if in_degree[neighbor] == 0:
#                     queue.append(neighbor)
        
#         # Check for cycles (if not all vertices were included)
#         if len(result) != len(self.graph):
#             raise ValueError("The graph has a cycle!")

#         return result

# # Create a graph instance
# graph = Graph()

# # Add edges
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.add_edge('B', 'D')
# graph.add_edge('C', 'D')
# graph.add_edge('D', 'E')

# # Perform topological sorting
# try:
#     topological_order = graph.topological_sort()
#     print("Topological Sorting:", topological_order)
# except ValueError as e:
#     print(e)






#####################################              Topological sort using  DFS                #####################################
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def topological_sort(self):
        visited = set()
        result = []

        def dfs(vertex):
            if vertex in visited:
                if vertex in result:
                    return
                raise ValueError("The graph has a cycle!")

            visited.add(vertex)
            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    dfs(neighbor)
            result.append(vertex)

        for vertex in self.graph:
            dfs(vertex)

        result.reverse()
        return result

# Create a graph instance
graph = Graph()

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Perform topological sorting
try:
    topological_order = graph.topological_sort()
    print("Topological Sorting:", topological_order)
except ValueError as e:
    print(e)
