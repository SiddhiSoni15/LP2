
#################################################################################################

# Problem Statement:

''' Implement a solution for a Constraint Satisfaction Problem using Branch and Bound &
Backtracking for n-queens problem or a graph coloring problem. '''

#################################################################################################

#<------------------------------- Input and Board Printing ------------------------------------>#

N = int(input("\nEnter number of Queens : "))

# Initialize the board with 0 (Empty cells)
board = []
for i in range(N):
    row = [0] * N  # Create a row with all 0s (empty cells)
    board.append(row)

# Print the Original Board
print("\nOriginal Board is : \n")
for i in range(N):
    for j in range(N):
        print(".", end=" ")
    print()


#<-------------------------------- Back-Tracking Approach ------------------------------------->#

def print_solution(board):
    """Print the board with Queens placed by Back-Tracking Approach."""
    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")  # Print Queen (Q)
            else:
                print(".", end=" ")  # Print Empty Space (.)
        print()
    print()

#-------------------------------------------------------------------------------

def is_safe(board, row, column):

    """Check if it is safe to place a queen at (row, column)."""

    # Check the Left-Side of the same Row
    for i in range(column):
        if(board[row][i] == 1):
            return False

    # Check the Upper-Left Diagonal
    i = row
    j = column
    while(i >= 0 and j >= 0):
        if(board[i][j] == 1):
            return False
        i -= 1
        j -= 1

    # Check the Lower-Left Diagonal
    i = row
    j = column
    while(i < N and j >= 0):
        if(board[i][j] == 1):
            return False
        i += 1
        j -= 1

    # When the position (row, column) is safe to place a Queen (Q)
    return True

#-------------------------------------------------------------------------------

def solution_by_backTracking(board, column):

    """Solve the N-Queens problem using backtracking."""

    if (column >= N):
        print_solution(board)
        return True
    result = False
    for i in range(N):
        if is_safe(board, i, column):
            board[i][column] = 1  # Place Queen
            result = solution_by_backTracking(board, column + 1) or result
            board[i][column] = 0  # Backtrack
    return result

#-------------------------------------------------------------------------------

# Printing all the Back-Tracking Solutions

print("\nBack-Tracking Solutions : \n")
found = solution_by_backTracking(board, 0)
if not found:
    print(f"No solution found for {N} Queens.")


#<------------------------------- Branch and Bound Approach ----------------------------------->#

def print_solution_bnb(board):
    """Print the board with Queens placed by Branch and Bound Approach."""
    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")  # Print Queen (Q)
            else:
                print(".", end=" ")  # Print Empty Space (.)
        print()
    print()

#-------------------------------------------------------------------------------

def solve_branch_and_bound(col, slash_code, backslash_code, row_lookup, slash_lookup, backslash_lookup, board):
    """Solve using Branch and Bound method."""
    if col >= N:
        print_solution_bnb(board)
        return True

    result = False
    for i in range(N):
        sc = slash_code[i][col]
        bsc = backslash_code[i][col]
        if not row_lookup[i] and not slash_lookup[sc] and not backslash_lookup[bsc]:
            board[i][col] = 1
            row_lookup[i] = True
            slash_lookup[sc] = True
            backslash_lookup[bsc] = True
            result = solve_branch_and_bound(col + 1, slash_code, backslash_code, row_lookup, slash_lookup, backslash_lookup, board) or result
            board[i][col] = 0
            row_lookup[i] = False
            slash_lookup[sc] = False
            backslash_lookup[bsc] = False

    return result

#-------------------------------------------------------------------------------

def solve_n_queens_branch_and_bound():
    """Initialize and solve using Branch and Bound."""
    board = [[0] * N for _ in range(N)]
    slash_code = [[0] * N for _ in range(N)]
    backslash_code = [[0] * N for _ in range(N)]

    # Initialize diagonal codes
    for r in range(N):
        for c in range(N):
            slash_code[r][c] = r + c
            backslash_code[r][c] = r - c + (N - 1)

    row_lookup = [False] * N
    slash_lookup = [False] * (2 * N - 1)
    backslash_lookup = [False] * (2 * N - 1)

    return solve_branch_and_bound(0, slash_code, backslash_code, row_lookup, slash_lookup, backslash_lookup, board)

#-------------------------------------------------------------------------------

# Printing all the Branch and Bound Solutions

print("\nBranch and Bound Solutions : \n")
found_bnb = solve_n_queens_branch_and_bound()
if not found_bnb:
    print(f"No solution found for {N} Queens.")

print("\nThank You! (-_-)\n")

#################################################################################################