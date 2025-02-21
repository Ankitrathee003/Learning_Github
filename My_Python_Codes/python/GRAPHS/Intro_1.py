# Vertices are connected by edges 
# It is not necessary to have connections in all vertices of graph
# Connection between Vertices is called edge
# Graph is commenly used on Social Media plateforms
# Degree of vertex is the no. of edges passing through it
# having path between A and B means we can reach from A to B by using inter- connected Edges 
# If we can reach to any vertex from any vertex than it is called connected Graph
# If in case a Graph have the different connected components internally but not connected to other subgraph watch below example

#  ---------------------
# |                    |
# |    a-b-c           |
# |                    |  ## here all three subgraphs are connected internally but not connected to each other so these 3 are connected components
# |         d-e        |
# |                    |
# |                    |
# | m-n-o-p            |
# |                    |
# ----------------------

# Tree is always a connected graph
# For n vertices to have connnected graph we have n-1 edges
# For maximum no. of edgs each vertex is connected to other vertex so total no. of edges are (n-1)+(n-2)+(n-3)+(n-4)------+1===N(N-1)/2  to traverse all O(n^2)