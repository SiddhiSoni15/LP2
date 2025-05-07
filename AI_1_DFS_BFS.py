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
