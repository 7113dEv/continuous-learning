from time import sleep
from maze_classes import Maze
from constants import SEARCH_METHOD_FRONTIERS

try:
    for search in SEARCH_METHOD_FRONTIERS.keys():
        print(f"Building maze object for the {search} demo...")
        maze = Maze(file_path="./maze2.txt")
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

"""
OUTPUT for maze1.txt:

Building maze object for the <search_type_string> demo...
Creating maze...
Solving maze...
Possible actions forund for node state (4, 0): [('up', (3, 0))]
Possible actions forund for node state (3, 0): [('down', (4, 0)), ('right', (3, 1))]
Possible actions forund for node state (3, 1): [('left', (3, 0)), ('right', (3, 2))]
Possible actions forund for node state (3, 2): [('left', (3, 1)), ('right', (3, 3))]
Possible actions forund for node state (3, 3): [('left', (3, 2)), ('right', (3, 4))]
Possible actions forund for node state (3, 4): [('up', (2, 4)), ('left', (3, 3))]
Possible actions forund for node state (2, 4): [('up', (1, 4)), ('down', (3, 4))]
Possible actions forund for node state (1, 4): [('down', (2, 4)), ('right', (1, 5))]
Possible actions forund for node state (1, 5): [('up', (0, 5)), ('left', (1, 4))]
Solved! Printing out maze...
Solution steps: ['up', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'up']
Solution cells: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 5), (0, 5)]
--------
#####*#
####**#
####*##
*****##
A######
--------
"""
"""
OUTPUT of maze2.txt:
Building maze object for the breadth-first search demo...
Creating maze...
Solving maze...
Possible actions forund for node state (4, 11): [('down', (5, 11))]
Possible actions forund for node state (5, 11): [('up', (4, 11)), ('down', (6, 11)), ('left', (5, 10))]
Possible actions forund for node state (6, 11): [('up', (5, 11)), ('right', (6, 12))]
Possible actions forund for node state (5, 10): [('left', (5, 9)), ('right', (5, 11))]
Possible actions forund for node state (6, 12): [('left', (6, 11)), ('right', (6, 13))]
Possible actions forund for node state (5, 9): [('down', (6, 9)), ('left', (5, 8)), ('right', (5, 10))]
Possible actions forund for node state (6, 13): [('down', (7, 13)), ('left', (6, 12)), ('right', (6, 14))]
Possible actions forund for node state (6, 9): [('up', (5, 9)), ('down', (7, 9))]
Possible actions forund for node state (5, 8): [('left', (5, 7)), ('right', (5, 9))]
Possible actions forund for node state (7, 13): [('up', (6, 13))]
Possible actions forund for node state (6, 14): [('up', (5, 14)), ('left', (6, 13))]
Possible actions forund for node state (7, 9): [('up', (6, 9))]
Possible actions forund for node state (5, 7): [('left', (5, 6)), ('right', (5, 8))]
Possible actions forund for node state (5, 14): [('up', (4, 14)), ('down', (6, 14))]
Possible actions forund for node state (5, 6): [('left', (5, 5)), ('right', (5, 7))]
Possible actions forund for node state (4, 14): [('down', (5, 14)), ('left', (4, 13))]
Possible actions forund for node state (5, 5): [('down', (6, 5)), ('left', (5, 4)), ('right', (5, 6))]
Possible actions forund for node state (4, 13): [('up', (3, 13)), ('right', (4, 14))]
Possible actions forund for node state (6, 5): [('up', (5, 5)), ('down', (7, 5))]
Possible actions forund for node state (5, 4): [('left', (5, 3)), ('right', (5, 5))]
Possible actions forund for node state (3, 13): [('up', (2, 13)), ('down', (4, 13))]
Possible actions forund for node state (7, 5): [('up', (6, 5))]
Possible actions forund for node state (5, 3): [('left', (5, 2)), ('right', (5, 4))]
Possible actions forund for node state (2, 13): [('down', (3, 13)), ('right', (2, 14))]
Possible actions forund for node state (5, 2): [('left', (5, 1)), ('right', (5, 3))]
Possible actions forund for node state (2, 14): [('left', (2, 13)), ('right', (2, 15))]
Possible actions forund for node state (5, 1): [('down', (6, 1)), ('left', (5, 0)), ('right', (5, 2))]
Possible actions forund for node state (2, 15): [('left', (2, 14)), ('right', (2, 16))]
Possible actions forund for node state (6, 1): [('up', (5, 1)), ('down', (7, 1))]
Possible actions forund for node state (5, 0): [('right', (5, 1))]
Possible actions forund for node state (2, 16): [('left', (2, 15)), ('right', (2, 17))]
Possible actions forund for node state (7, 1): [('up', (6, 1))]
Possible actions forund for node state (2, 17): [('down', (3, 17)), ('left', (2, 16))]
Possible actions forund for node state (3, 17): [('up', (2, 17)), ('down', (4, 17))]
Possible actions forund for node state (4, 17): [('up', (3, 17)), ('down', (5, 17))]
Possible actions forund for node state (5, 17): [('up', (4, 17)), ('down', (6, 17))]
Possible actions forund for node state (6, 17): [('up', (5, 17)), ('down', (7, 17))]
Possible actions forund for node state (7, 17): [('up', (6, 17)), ('right', (7, 18))]
Possible actions forund for node state (7, 18): [('left', (7, 17)), ('right', (7, 19))]
Possible actions forund for node state (7, 19): [('up', (6, 19)), ('left', (7, 18))]
Possible actions forund for node state (6, 19): [('up', (5, 19)), ('down', (7, 19))]
Possible actions forund for node state (5, 19): [('up', (4, 19)), ('down', (6, 19))]
Possible actions forund for node state (4, 19): [('up', (3, 19)), ('down', (5, 19))]
Possible actions forund for node state (3, 19): [('up', (2, 19)), ('down', (4, 19))]
Possible actions forund for node state (2, 19): [('up', (1, 19)), ('down', (3, 19))]
Possible actions forund for node state (1, 19): [('up', (0, 19)), ('down', (2, 19))]
Possible actions forund for node state (0, 19): [('up', (-1, 19)), ('down', (1, 19)), ('left', (0, 18))]
Possible actions forund for node state (-1, 19): [('up', (-2, 19)), ('down', (0, 19)), ('left', (-1, 18))]
Possible actions forund for node state (0, 18): [('up', (-1, 18)), ('left', (0, 17)), ('right', (0, 19))]
Possible actions forund for node state (-2, 19): [('up', (-3, 19)), ('down', (-1, 19))]
Possible actions forund for node state (-1, 18): [('down', (0, 18)), ('left', (-1, 17)), ('right', (-1, 19))]
Possible actions forund for node state (0, 17): [('up', (-1, 17)), ('left', (0, 16)), ('right', (0, 18))]
Possible actions forund for node state (-3, 19): [('up', (-4, 19)), ('down', (-2, 19))]
Possible actions forund for node state (-1, 17): [('up', (-2, 17)), ('down', (0, 17)), ('right', (-1, 18))]
Possible actions forund for node state (0, 16): [('left', (0, 15)), ('right', (0, 17))]
Possible actions forund for node state (-4, 19): [('up', (-5, 19)), ('down', (-3, 19))]
Possible actions forund for node state (-2, 17): [('up', (-3, 17)), ('down', (-1, 17))]
Possible actions forund for node state (0, 15): [('left', (0, 14)), ('right', (0, 16))]
Possible actions forund for node state (-5, 19): [('up', (-6, 19)), ('down', (-4, 19))]
Possible actions forund for node state (-3, 17): [('up', (-4, 17)), ('down', (-2, 17))]
Possible actions forund for node state (0, 14): [('left', (0, 13)), ('right', (0, 15))]
Possible actions forund for node state (-6, 19): [('up', (-7, 19)), ('down', (-5, 19))]
Possible actions forund for node state (-4, 17): [('up', (-5, 17)), ('down', (-3, 17))]
Possible actions forund for node state (0, 13): [('up', (-1, 13)), ('left', (0, 12)), ('right', (0, 14))]
Possible actions forund for node state (-7, 19): [('up', (-8, 19)), ('down', (-6, 19))]
Possible actions forund for node state (-5, 17): [('up', (-6, 17)), ('down', (-4, 17))]
Possible actions forund for node state (-1, 13): [('up', (-2, 13)), ('down', (0, 13))]
Possible actions forund for node state (0, 12): [('left', (0, 11)), ('right', (0, 13))]
Possible actions forund for node state (-8, 19): [('down', (-7, 19)), ('left', (-8, 18))]
Possible actions forund for node state (-6, 17): [('down', (-5, 17)), ('left', (-6, 16))]
Possible actions forund for node state (-2, 13): [('down', (-1, 13)), ('left', (-2, 12)), ('right', (-2, 14))]
Possible actions forund for node state (0, 11): [('down', (1, 11)), ('right', (0, 12))]
Possible actions forund for node state (-8, 18): [('left', (-8, 17)), ('right', (-8, 19))]
Possible actions forund for node state (-6, 16): [('left', (-6, 15)), ('right', (-6, 17))]
Possible actions forund for node state (-2, 12): [('left', (-2, 11)), ('right', (-2, 13))]
Possible actions forund for node state (-2, 14): [('up', (-3, 14)), ('left', (-2, 13))]
Possible actions forund for node state (1, 11): [('up', (0, 11)), ('down', (2, 11))]
Possible actions forund for node state (-8, 17): [('left', (-8, 16)), ('right', (-8, 18))]
Possible actions forund for node state (-6, 15): [('left', (-6, 14)), ('right', (-6, 16))]
Possible actions forund for node state (-2, 11): [('up', (-3, 11)), ('right', (-2, 12))]
Possible actions forund for node state (-3, 14): [('up', (-4, 14)), ('down', (-2, 14))]
Possible actions forund for node state (2, 11): [('up', (1, 11)), ('left', (2, 10))]
Possible actions forund for node state (-8, 16): [('left', (-8, 15)), ('right', (-8, 17))]
Possible actions forund for node state (-6, 14): [('left', (-6, 13)), ('right', (-6, 15))]
Possible actions forund for node state (-3, 11): [('up', (-4, 11)), ('down', (-2, 11)), ('left', (-3, 10))]
Possible actions forund for node state (-4, 14): [('down', (-3, 14)), ('left', (-4, 13))]
Possible actions forund for node state (2, 10): [('down', (3, 10)), ('right', (2, 11))]
Possible actions forund for node state (-8, 15): [('left', (-8, 14)), ('right', (-8, 16))]
Possible actions forund for node state (-6, 13): [('down', (-5, 13)), ('right', (-6, 14))]
Possible actions forund for node state (-4, 11): [('down', (-3, 11))]
Possible actions forund for node state (-3, 10): [('left', (-3, 9)), ('right', (-3, 11))]
Possible actions forund for node state (-4, 13): [('up', (-5, 13)), ('right', (-4, 14))]
Possible actions forund for node state (3, 10): [('up', (2, 10)), ('left', (3, 9))]
Possible actions forund for node state (-8, 14): [('left', (-8, 13)), ('right', (-8, 15))]
Possible actions forund for node state (-5, 13): [('up', (-6, 13)), ('down', (-4, 13))]
Possible actions forund for node state (-3, 9): [('down', (-2, 9)), ('left', (-3, 8)), ('right', (-3, 10))]
Possible actions forund for node state (3, 9): [('left', (3, 8)), ('right', (3, 10))]
Possible actions forund for node state (-8, 13): [('left', (-8, 12)), ('right', (-8, 14))]
Possible actions forund for node state (-2, 9): [('up', (-3, 9)), ('down', (-1, 9))]
Possible actions forund for node state (-3, 8): [('left', (-3, 7)), ('right', (-3, 9))]
Possible actions forund for node state (3, 8): [('up', (2, 8)), ('right', (3, 9))]
Possible actions forund for node state (-8, 12): [('left', (-8, 11)), ('right', (-8, 13))]
Possible actions forund for node state (-1, 9): [('up', (-2, 9))]
Possible actions forund for node state (-3, 7): [('left', (-3, 6)), ('right', (-3, 8))]
Possible actions forund for node state (2, 8): [('down', (3, 8)), ('left', (2, 7))]
Possible actions forund for node state (-8, 11): [('down', (-7, 11)), ('right', (-8, 12))]
Possible actions forund for node state (-3, 6): [('left', (-3, 5)), ('right', (-3, 7))]
Possible actions forund for node state (2, 7): [('left', (2, 6)), ('right', (2, 8))]
Possible actions forund for node state (-7, 11): [('up', (-8, 11)), ('down', (-6, 11))]
Possible actions forund for node state (-3, 5): [('down', (-2, 5)), ('left', (-3, 4)), ('right', (-3, 6))]
Possible actions forund for node state (2, 6): [('left', (2, 5)), ('right', (2, 7))]
Possible actions forund for node state (-6, 11): [('up', (-7, 11)), ('left', (-6, 10))]
Possible actions forund for node state (-2, 5): [('up', (-3, 5)), ('down', (-1, 5))]
Possible actions forund for node state (-3, 4): [('left', (-3, 3)), ('right', (-3, 5))]
Possible actions forund for node state (2, 5): [('left', (2, 4)), ('right', (2, 6))]
Possible actions forund for node state (-6, 10): [('down', (-5, 10)), ('right', (-6, 11))]
Possible actions forund for node state (-1, 5): [('up', (-2, 5))]
Possible actions forund for node state (-3, 3): [('left', (-3, 2)), ('right', (-3, 4))]
Possible actions forund for node state (2, 4): [('left', (2, 3)), ('right', (2, 5))]
Possible actions forund for node state (-5, 10): [('up', (-6, 10)), ('left', (-5, 9))]
Possible actions forund for node state (-3, 2): [('left', (-3, 1)), ('right', (-3, 3))]
Possible actions forund for node state (2, 3): [('down', (3, 3)), ('right', (2, 4))]
Possible actions forund for node state (-5, 9): [('left', (-5, 8)), ('right', (-5, 10))]
Possible actions forund for node state (-3, 1): [('down', (-2, 1)), ('left', (-3, 0)), ('right', (-3, 2))]
Possible actions forund for node state (3, 3): [('up', (2, 3)), ('left', (3, 2))]
Possible actions forund for node state (-5, 8): [('up', (-6, 8)), ('right', (-5, 9))]
Possible actions forund for node state (-2, 1): [('up', (-3, 1)), ('down', (-1, 1))]
Possible actions forund for node state (-3, 0): [('right', (-3, 1))]
Possible actions forund for node state (3, 2): [('left', (3, 1)), ('right', (3, 3))]
Possible actions forund for node state (-6, 8): [('down', (-5, 8)), ('left', (-6, 7))]
Possible actions forund for node state (-1, 1): [('up', (-2, 1))]
Possible actions forund for node state (3, 1): [('left', (3, 0)), ('right', (3, 2))]
Possible actions forund for node state (-6, 7): [('left', (-6, 6)), ('right', (-6, 8))]
Solved! Printing out maze...
Solution steps: ['down', 'down', 'right', 'right', 'right', 'up', 'up', 'left', 'up', 'up', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'right', 'right', 'up', 'up', 'up', 'up', 
'up', 'up', 'up', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'down', 'down', 'left', 'down', 'left', 'left', 'up', 'left', 'left', 'left', 'left', 'left', 'down', 'left', 'left', 'left']   
Solution cells: [(5, 11), (6, 11), (6, 12), (6, 13), (6, 14), (5, 14), (4, 14), (4, 13), (3, 13), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (3, 17), (4, 17), (5, 17), (6, 17), (7, 17), (7, 18), (7, 19), (6, 
19), (5, 19), (4, 19), (3, 19), (2, 19), (1, 19), (0, 19), (0, 18), (0, 17), (0, 16), (0, 15), (0, 14), (0, 13), (0, 12), (0, 11), (1, 11), (2, 11), (2, 10), (3, 10), (3, 9), (3, 8), (2, 8), (2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0)]
--------
###########*********#
###########*#######*#
###******#**#*****#*#
****####***##*###*#*#
###########A#**##*#*#
           *##*##*#*#
# ### ### #****##*#*#
# ### ### ### ###***#
--------
"""