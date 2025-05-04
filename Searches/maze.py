from time import sleep
from maze_classes import Maze
from constants import SEARCH_METHOD_FRONTIERS

try:
    for search in SEARCH_METHOD_FRONTIERS.keys():
        print(f"Building maze object for the {search} demo...")
        maze = Maze(file_path="maze1.txt")
        sleep(2)

        print("Creating maze...")
        maze.create_maze()
        sleep(1)

        print("Solving maze...")
        maze.solve_maze(search_type=search)

        if maze.solution:
            print("Solved! Printing out maze...")
            sleep(2)
            maze.print_maze()
except Exception as e:
    print(f"Exception occurred running main file: {e}")