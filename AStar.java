import java.util.*;

public class AStar {

    static int[][] grid = {
            { 0, 0, 0, 0, 0 },
            { 0, 1, 1, 1, 0 },
            { 0, 0, 0, 1, 0 },
            { 1, 1, 0, 1, 0 },
            { 0, 0, 0, 0, 0 }
    };

    static int[][] directions = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } }; // Right, Down, Left, Up
    static int[][] cost = new int[5][5]; // Store the shortest path cost
    static int[][] parentX = new int[5][5]; // Track path X
    static int[][] parentY = new int[5][5]; // Track path Y

    public static void main(String[] args) {
        System.out.println("Input Grid:");
        displayGrid();

        for (int[] row : cost)
            Arrays.fill(row, Integer.MAX_VALUE); // Set all costs to max
        findPath(0, 0, 4, 4);
    }

    static void findPath(int startX, int startY, int goalX, int goalY) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2])); // {x, y, fCost}
        pq.add(new int[] { startX, startY, 0 });
        cost[startX][startY] = 0;

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int x = current[0], y = current[1];

            if (x == goalX && y == goalY) {
                printPath(goalX, goalY);
                return;
            }

            for (int[] dir : directions) {
                int newX = x + dir[0], newY = y + dir[1];

                if (isValid(newX, newY)) {
                    int newCost = cost[x][y] + 1;
                    if (newCost < cost[newX][newY]) {
                        cost[newX][newY] = newCost;
                        pq.add(new int[] { newX, newY, newCost + heuristic(newX, newY, goalX, goalY) });
                        parentX[newX][newY] = x;
                        parentY[newX][newY] = y;
                    }
                }
            }
        }

        System.out.println("No path found.");
    }

    static int heuristic(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2); // Manhattan Distance
    }

    static boolean isValid(int x, int y) {
        return x >= 0 && y >= 0 && x < 5 && y < 5 && grid[x][y] == 0;
    }

    /*
     * static void printPath(int x, int y) {
     * List<int[]> path = new ArrayList<>();
     * while (x != 0 || y != 0) {
     * path.add(new int[] { x, y });
     * int tempX = parentX[x][y];
     * int tempY = parentY[x][y];
     * x = tempX;
     * y = tempY;
     * }
     * path.add(new int[] { 0, 0 });
     * Collections.reverse(path);
     * System.out.println("Path found:");
     * for (int[] step : path) {
     * System.out.println("(" + step[0] + ", " + step[1] + ")");
     * }
     * }
     */

    static void printPath(int x, int y) {
        List<int[]> path = new ArrayList<>();
        while (x != 0 || y != 0) {
            path.add(new int[] { x, y });
            int tempX = parentX[x][y];
            int tempY = parentY[x][y];
            x = tempX;
            y = tempY;
        }
        path.add(new int[] { 0, 0 });
        Collections.reverse(path);

        System.out.println("Path found:");
        for (int[] step : path) {
            System.out.println("(" + step[0] + ", " + step[1] + ")");
        }

        // Create a copy of the grid to mark the path
        String[][] resultGrid = new String[5][5];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                resultGrid[i][j] = Integer.toString(grid[i][j]);
            }
        }

        // Mark the path with 'x'
        for (int[] step : path) {
            int px = step[0], py = step[1];
            resultGrid[px][py] = "x";
        }

        System.out.println("\nGrid with path marked (x = path):");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(resultGrid[i][j] + " ");
            }
            System.out.println();
        }
    }

    static void displayGrid() {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();

    }
}
