
''' Implement A star Algorithm for any game search problem. '''

# Define the Node structure
class Node:
    def __init__(self, x, y, cost, heuristic, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent

    def f(self):
        return self.cost + self.heuristic

# Heuristic Function : Manhattan Distance Formula
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm
def a_star(grid, start, goal):
    open_list = []
    closed_set = []

    start_node = Node(start[0], start[1], 0, heuristic(start, goal))
    open_list.append(start_node)

    while open_list:
        current = open_list[0]
        for node in open_list:
            if node.f() < current.f():
                current = node

        open_list.remove(current)
        closed_set.append((current.x, current.y))

        if (current.x, current.y) == goal:
            return reconstruct_path(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current.x + dx, current.y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 1 or (nx, ny) in closed_set:
                    continue

                g_cost = current.cost + 1
                h_cost = heuristic((nx, ny), goal)
                neighbor = Node(nx, ny, g_cost, h_cost, current)

                skip = False
                for node in open_list:
                    if (node.x, node.y) == (nx, ny) and node.f() <= neighbor.f():
                        skip = True
                        break

                if not skip:
                    open_list.append(neighbor)

    return None

# Reconstruct path
def reconstruct_path(node):
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]

# Function to print the grid with or without a path
def print_grid(grid, path=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if path and (i, j) in path:
                print("P", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

# Driver code
def driver():
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    print("\nNotation Reference:\n\n    1] P shows the shortest path.\n    2] # are the obstacles.\n    3] . are the open spaces.")
    print("\nOriginal Grid:\n")
    print_grid(grid)

    rows = len(grid)
    cols = len(grid[0])

    # Input start and goal
    print("\nEnter Start Position (row and column, e.g., 0 0) : ")
    sx, sy = map(int, input().split())
    print("\nEnter Goal Position (row and column, e.g., 4 4) : ")
    gx, gy = map(int, input().split())

    if not (0 <= sx < rows and 0 <= sy < cols and 0 <= gx < rows and 0 <= gy < cols):
        print("\n Invalid input: Start or goal is out of grid bounds.")
        return
    if grid[sx][sy] == 1 or grid[gx][gy] == 1:
        print("\n Invalid input: Start or goal is on an obstacle.")
        return

    start = (sx, sy)
    goal = (gx, gy)

    path = a_star(grid, start, goal)
    if path:
        print("\nA* Path from Start", start, "to Goal", goal, ": \n\n",path)
        print("\nGrid with Path : \n")
        print_grid(grid, path)
        print("\n")
    else:
        print("\nNo path found from", start, "to", goal, "\n")

# Run
if __name__ == "__main__":
    driver()

#################################################################################################
# A Algorithm* combines both g(n) (cost from the start to the current node) and h(n) (estimated cost to the goal) for its evaluation function f(n) = g(n) + h(n).

# Steps:

# Choose a starting node and a goal.

# Evaluate each node by combining the path cost and the heuristic estimate to the goal.

# Use a priority queue to always process the node with the lowest f(n) value.

# The A algorithm* is widely used for pathfinding and graph traversal in AI due to its optimality and completeness when using an admissible heuristic. A* combines the concepts of both BFS and Greedy Best-First Search:

# f(n) = g(n) + h(n):

# g(n): The actual cost to reach the node n from the start node.

# h(n): The heuristic estimated cost from node n to the goal.

# f(n): The total estimated cost from the start to the goal through node n.

# This algorithm is used in AI for problems like pathfinding in a maze or game, where both cost and heuristic are important factors.

# Algorithm:

# Add the start node to the open list.

# While the open list is not empty, select the node with the lowest f(n).

# Expand the node, updating its neighbors with the new path cost and heuristic.

# Add the neighbors to the open list if they aren’t already visited.

# Repeat until the goal is reached.

# python
# Copy code
# def a_star_algorithm(start, goal, graph, heuristic):
#     open_list = []
#     closed_list = set()
#     open_list.append((start, 0 + heuristic(start, goal)))

#     while open_list:
#         current_node, current_cost = open_list.pop(0)

#         if current_node == goal:
#             return current_cost  # Path found

#         closed_list.add(current_node)
#         for neighbor in graph[current_node]:
#             if neighbor not in closed_list:
#                 cost = current_cost + 1  # Assuming uniform cost
#                 open_list.append((neighbor, cost + heuristic(neighbor, goal)))
#     return None  # No path found
# Explanation: In a maze, A* will find the optimal path by considering both the cost so far and the estimated cost to reach the goal.
