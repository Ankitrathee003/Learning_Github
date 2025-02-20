import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range (nVertices)]

    def addEdge(self,v1,v2):  ##  Undirected Graph both sides connection
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def __dfsHelper(self, sv, visited):  ### this will print complete depth for a given vertex
        # This function is a depth-first search (DFS) helper function.
        # It explores vertices in a depth-first manner, starting from vertex 'sv'.

        # Print the current vertex being visited.
        print(sv)

        # Mark the current vertex as visited.
        visited[sv] = True

        # Explore all neighbors of the current vertex.
        for j in range(self.nVertices):
            # Check if there is an edge between the current vertex 'sv' and vertex 'j',
            # and if vertex 'j' has not been visited yet.
            if self.adjMatrix[sv][j] > 0 and visited[j] is False:
                # Recursively call the DFS helper function on the unvisited neighbor 'j'.
                self.__dfsHelper(j, visited)

    def dfs(self):
        # This is the main DFS function that initializes the visited array and starts the DFS from the first vertex.
        # Create a boolean array to keep track of visited vertices.
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i, visited)   


    def bfsHelper(self,sv,visited):
        # Initialize a queue to store vertices for BFS traversal.
        q = queue.Queue()

        # Start BFS from the first vertex (vertex 0).
        q.put(sv)

        # Mark the first vertex as visited.
        visited[sv] = True

        # Perform BFS traversal while the queue is not empty.
        while not q.empty():
            # Get the front vertex from the queue.
            u = q.get()

            # Print the value of the current vertex being visited.
            print(u)

            # Iterate over all vertices to find neighbors of the current vertex.
            for i in range(self.nVertices):
                # Check if there is an edge between the current vertex 'u' and vertex 'i',
                # and if vertex 'i' has not been visited yet.
                if self.adjMatrix[u][i] > 0 and not visited[i]:
                    # Enqueue the unvisited neighbor 'i' and mark it as visited.
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited=[False for i in range(self.nVertices)]
        # Create a boolean array to keep track of visited vertices.
        for i in range(self.nVertices):
            if visited[i] is False:
                self.bfsHelper(i,visited)

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    
    def __str__(self):
        return str(self.adjMatrix)

#                 0
#                /  \
#               /    \
#              /      \
#             1        2
#              \      / \
#               \    /   \
#                \  /     \
#                 3        4




    
g=Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,3)
g.addEdge(0,2)
# g.bfs()



#               0                       2
#             /   \                    / \
#            /     \                  /   \
#           1       3                4     5
#                                   / \
#                                  /   \
#                                 7     6
#                                         \
#                                          \
#                                           8

a=Graph(9)
a.addEdge(0,1)
a.addEdge(0,3)
a.addEdge(2,4)
a.addEdge(2,5)
a.addEdge(4,6)
a.addEdge(4,7)
a.addEdge(6,8)
a.bfs()
# a.dfs()








# g.dfs()
# g.bfs()
# print(g)
    


## According to DFS we will explore depth untill end exploring and than come back and 
## Keep the note of visited vertex so that we need not to go to that node again