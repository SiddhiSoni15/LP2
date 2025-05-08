from collections import deque, defaultdict

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

# Display Tree Structure using / and \
def display_tree(node, prefix=""):
    if node is None:
        return
    print(f"{prefix}{node.key}")
    
    if node.children:
        # Display the first child with `/`
        for i, child in enumerate(node.children):
            if i == 0:
                display_tree(child, prefix + " / ")
            else:
                display_tree(child, prefix + " \\ ")

# Print tree structure (in the format you wanted)
def print_tree_structure(root):
    # Build a map of node and their children using BFS
    tree_map = defaultdict(list)
    visited = {}
    queue = deque([root])
    visited[root.key] = True
    
    while queue:
        current = queue.popleft()
        for child in current.children:
            if child.key not in visited:
                visited[child.key] = True
                queue.append(child)
                tree_map[current.key].append(child.key)

    #print("\nTree Structure:\n")
    print("    " + root.key)
    
    # For level 1 children (first level)
    level1 = tree_map.get(root.key)

    if level1 and len(level1) == 2:
        print("   / \\")
        print("  " + level1[0] + "   " + level1[1])

        # For level 2 children
        left_children = tree_map.get(level1[0])
        right_children = tree_map.get(level1[1])

        if left_children and len(left_children) == 2 and right_children and len(right_children) == 2:
            print(" / \\ / \\")
            print(left_children[0] + "  " + left_children[1] + " " + right_children[0] + "  " + right_children[1])

# Build Tree from User Input
def build_tree():
    nodes = {}

    n = int(input("Enter total number of nodes: "))
    for _ in range(n):
        parts = input("Enter node and its children (e.g. A:B C D): ").split(":")
        parent_key = parts[0].strip()
        child_keys = list(map(str, parts[1].strip().split())) if len(parts) > 1 else []

        if parent_key not in nodes:
            nodes[parent_key] = Node(parent_key)
        parent_node = nodes[parent_key]

        for ck in child_keys:
            if ck not in nodes:
                nodes[ck] = Node(ck)
            parent_node.children.append(nodes[ck])

    root_key = input("Enter root node key: ").strip()
    return nodes[root_key] if root_key in nodes else None

# Driver-Code
def driver():
    print("\n--- Build Tree ---")
    root = build_tree()

    print("\nTree Structure:")
    print_tree_structure(root)  # Display the tree structure

    dfs_result = []
    dfs_recursive(root, dfs_result)
    print("\nRecursive DFS Traversal:          ", dfs_result)

    print("\nNon-Recursive BFS Traversal:      ", bfs_non_recursive(root), "\n")

# Call to Driver Function
if __name__ == "__main__":
    driver()
