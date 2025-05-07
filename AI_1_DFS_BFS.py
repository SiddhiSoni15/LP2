# Tree Node
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

# Recursive DFS
def dfs_recursive(node, result):
    if node is None:
        return
    result.append(node.key)
    for child in node.children:
        dfs_recursive(child, result)

# Non-Recursive DFS
def dfs_non_recursive(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.key)
        for child in reversed(node.children):
            stack.append(child)
    return result

# Recursive BFS
def bfs_recursive(queue, result):
    if not queue:
        return
    next_queue = []
    for node in queue:
        result.append(node.key)
        next_queue.extend(node.children)
    bfs_recursive(next_queue, result)

# Non-Recursive BFS
def bfs_non_recursive(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.key)
        queue.extend(node.children)
    return result

# Build Tree from User Input
def build_tree():
    nodes = {}

    n = int(input("Enter total number of nodes: "))
    for _ in range(n):
        parts = input("Enter node and its children (e.g. 1:2 3 4): ").split(":")
        parent_key = int(parts[0].strip())
        child_keys = list(map(int, parts[1].strip().split())) if len(parts) > 1 else []

        if parent_key not in nodes:
            nodes[parent_key] = Node(parent_key)
        parent_node = nodes[parent_key]

        for ck in child_keys:
            if ck not in nodes:
                nodes[ck] = Node(ck)
            parent_node.children.append(nodes[ck])

    root_key = int(input("Enter root node key: "))
    return nodes[root_key] if root_key in nodes else None

# Driver-Code
def driver():
    print("\n--- Build Tree ---")
    root = build_tree()

    dfs_result = []
    dfs_recursive(root, dfs_result)
    print("\nRecursive DFS Traversal:          ", dfs_result)

    print("\nNon-Recursive DFS Traversal:      ", dfs_non_recursive(root))

    bfs_result = []
    bfs_recursive([root], bfs_result)
    print("\nRecursive BFS Traversal:          ", bfs_result)

    print("\nNon-Recursive BFS Traversal:      ", bfs_non_recursive(root), "\n")

# Call to Driver Function
if __name__ == "__main__":
    driver()


# DFS (Depth First Search) explores as deep as possible before backtracking. It is typically used for solving puzzles, pathfinding, and topological sorting.

# BFS (Breadth First Search) explores all neighbors level by level. It’s often used in shortest path algorithms, such as for unweighted graphs.

# These algorithms have different uses and trade-offs, such as memory usage (DFS uses less memory in some cases, while BFS might require more due to the queue for levels).

# 2. Time and Space Complexities in Terms of Branching Factor and Solution Depth
# Time Complexity: Both DFS and BFS usually have a time complexity of O(V + E), where V is the number of vertices and E is the number of edges. The branching factor and solution depth do not significantly alter this unless you’re in a specific search space.

# DFS can go deeper into the solution space, so in a tree structure, the time complexity could also depend on the depth of the solution space.

# BFS explores each level at a time. So, the time complexity can grow faster if the branching factor is large, but BFS is guaranteed to find the shortest path in an unweighted graph.

# Space Complexity:

# DFS uses O(d) space, where d is the depth of the tree (or graph), as it only stores the current path.

# BFS uses O(b^d) space, where b is the branching factor, and d is the depth of the solution. This makes BFS less memory-efficient for wide trees.

# 3. Algorithm Working
# DFS Implementation (Recursive)
# python
# Copy code
# def DFS(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start, end=' ')
    
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             DFS(graph, neighbor, visited)
# Explanation: This is a recursive depth-first search for an undirected graph. It uses a set to track visited nodes and explores all vertices in depth before backtracking.

# BFS Implementation (Queue-based)
# python
# Copy code
# from collections import deque

# def BFS(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)
    
#     while queue:
#         vertex = queue.popleft()
#         print(vertex, end=' ')
        
#         for neighbor in graph[vertex]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
# Explanation: This is a queue-based breadth-first search. BFS explores nodes level by level, visiting neighbors before going deeper.
# DFS:

# Exploration: It explores as deeply as possible along each branch before backtracking. This can result in inefficient exploration if the search space is large or has deep solutions, but it can also be useful when looking for a specific solution in deep search trees.

# Memory: DFS requires O(d) memory where d is the maximum depth, which is typically better than BFS in memory usage, especially for deep solutions.

# Use Case in AI: DFS is used in game tree search for problems like puzzles where deeper levels of the tree are more important than the breadth of possible actions. It's also used in constraint satisfaction problems when you need to try every possible path.

# BFS:

# Exploration: BFS explores all nodes at the present depth level before moving on to nodes at the next level. This makes BFS useful when the goal is to find the shortest path in an unweighted graph.

# Memory: BFS uses O(b^d) memory, where b is the branching factor and d is the depth of the solution. This makes BFS less memory-efficient compared to DFS, especially in large branching spaces.

# Use Case in AI: BFS is often used in shortest pathfinding, such as finding the optimal solution in unweighted problems like maze-solving or pathfinding in grids.

# 2. Time and Space Complexities in Terms of Branching Factor and Solution Depth (AI)
# In AI, the performance of search algorithms like DFS and BFS can be analyzed based on their branching factor (b) and solution depth (d).

# DFS:

# Time Complexity: O(b^d), where b is the branching factor and d is the depth of the solution. The algorithm might explore all nodes in the worst case.

# Space Complexity: O(d), because it only needs to store the current path (depth) in memory.

# BFS:

# Time Complexity: O(b^d), where b is the branching factor and d is the depth of the solution. BFS explores all nodes at a given depth level before moving to the next.

# Space Complexity: O(b^d), because BFS needs to store all nodes at a particular depth level in memory, which can grow exponentially with the branching factor.

# The difference comes from the fact that DFS explores deeper into the tree, while BFS explores all branches at the current level first.
