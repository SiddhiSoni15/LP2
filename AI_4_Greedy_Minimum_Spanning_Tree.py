

''' Implement Greedy Search Algorithm for Minimum Spanning Tree (MST). '''

# Class to represent an Edge in the Undirected Graph
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

#<------------------------------------------------------------------------------

# Function to find the root of a set using path compression
def find_parent(parent, node):
    if (parent[node] != node):
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

#<------------------------------------------------------------------------------

# Function to join two sets using union by rank
def union(parent, rank, u, v):
    root_u = find_parent(parent, u)
    root_v = find_parent(parent, v)

    if (root_u != root_v):
        if (rank[root_u] < rank[root_v]):
            parent[root_u] = root_v
        elif (rank[root_u] > rank[root_v]):
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

#<------------------------------------------------------------------------------

# Kruskal's Algorithm to find the Minimum Spanning Tree (MST)

def kruskal_mst(vertices, edges):
    # Sort edges based on weight
    edges.sort(key=lambda edge: edge.weight)

    parent = []
    for i in range(vertices):
        parent.append(i)

    rank = [0] * vertices
    mst = []

    print("\n Selected Edges in MST : \n")

    for edge in edges:
        u, v = edge.u, edge.v

        if find_parent(parent, u) != find_parent(parent, v):
            union(parent, rank, u, v)
            mst.append(edge)
            print(f"    Edge ({u} - {v}) with weight {edge.weight}")

        if len(mst) == vertices - 1:
            break

    total_cost = sum(edge.weight for edge in mst)
    print("\n Total weight of MST:", total_cost)
    print("\n Thank You! (-_-)\n")

#<------------------------------------------------------------------------------

# Driver Code
def driver():
    print("\n <--- Minimum Spanning Tree (MST) using the Kruskal's Algorithm --->\n")

    print("\n Main Graph Details : ")
    vertices = int(input("\n Enter number of Vertices : "))
    e = int(input("\n Enter number of Edges : "))

    edges = []
    print("\n Enter each Edge in the format : u v weight (eg., 0 1 7  is the edge (0,1) with Weight 7)")
    print("\n Note : Vertex numbering should be from 0 to", vertices - 1,".")
    for i in range(e):
        u, v, w = map(int, input(f"\n    Edge {i + 1} : ").split())
        edges.append(Edge(u, v, w))

    kruskal_mst(vertices, edges)

#<------------------------------------------------------------------------------

# Run the program
if __name__ == "__main__":
    driver()

#################################################################################################

# Sample Graph :-

# Vertices = 7

# Edges = 11

# Edge 1: 0 1 7
# Edge 2: 0 3 5
# Edge 3: 1 2 8
# Edge 4: 1 3 9
# Edge 5: 1 4 7
# Edge 6: 2 4 5
# Edge 7: 3 4 15
# Edge 8: 3 5 6
# Edge 9: 4 5 8
# Edge 10: 4 6 9
# Edge 11: 5 6 11

#################################################################################################

# Prim’s Algorithm or Kruskal’s Algorithm are typical greedy solutions for MST.

# Prim’s Algorithm grows the MST by adding the minimum-weight edge to the tree that connects a new vertex.

# Prim's Algorithm is a greedy algorithm for finding the MST. It starts with any arbitrary vertex and grows the MST by adding the edge with the smallest weight that connects a vertex in the MST to a vertex outside the MST.

# python
# Copy code
# def prim_mst(graph):
#     visited = set()
#     min_edges = [(0, 0)]  # Start with an arbitrary vertex
#     while min_edges:
#         weight, vertex = min_edges.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             for neighbor, edge_weight in graph[vertex]:
#                 if neighbor not in visited:
#                     min_edges.append((edge_weight, neighbor))
#     return visited
# Explanation: This is a classical greedy algorithm that minimizes the total edge weight as the MST grows.
# Explanation: This algorithm starts with a single node and adds the smallest possible edge to include other vertices, ensuring no cycles.
