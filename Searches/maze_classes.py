import sys
from typing import Union

from constants import SEARCH_METHOD_FRONTIERS
from search_classes import Node


class Maze():

    def __init__(
        self, 
        file_path: str=None,
        height: int=None,
        width: int=None
    ):
        self.file_path = file_path
        self.height = height
        self.width = width
        self.maze_walls = []
        self.start = None
        self.goal = None
        self.explored_nodes = set()
        self.states_explored = 0
        self.solution = None

    def get_maze_context_from_file(self):
        try:
            with open(self.file_path, "r") as f:
                file_contents = f.read()
        
            # The maze needs to have a start and end point
            if file_contents.count("A") != 1:
                raise Exception("Maze must have exactly one start point")
            if file_contents.count("B") != 1:
                raise Exception("Maze must have exactly one goal")

            # Gather width and height
            line_context = file_contents.splitlines()
            self.height = len(line_context)
            self.width = max(len(line) for line in line_context)

            # Figure out walls, paths, goals, etc.
            for i in range(self.height):
                row = []
                
                for j in range(self.width):
                    try:
                        current_context = line_context[i][j]

                        # Python version < 3.10
                        # We can also consider a hash map containing key/value
                        # pairs of case: method_to_handle_appropriate_action()

                        # if current_context == "A":
                        #     self.start = (i, j)
                        #     row.append(0)
                        # elif current_context == "B":
                        #     self.goal = (i, j)
                        #     row.append(0)
                        # elif current_context == " ":
                        #     row.append(0)

                        # Python version >= 3.10
                        match current_context:
                            case "A":
                                self.start = (i, j)
                                row.append(0)
                            case "B":
                                self.goal = (i, j)
                                row.append(0)
                            case " ":
                                row.append(0)
                            case _:
                                row.append(1)
                    except IndexError as ie:
                        row.append(0)                
                self.maze_walls.append(row)        
        except FileNotFoundError as fnfe:
            print(f"{e.__traceback__.tb_lineno}")
            raise Exception(f"Exception occurred while reading file: {fnfe}")
        except Exception as e:
            print(f"{e.__traceback__.tb_lineno}")
            raise Exception(f"Exception occurred while getting maze context: {e}")


    def create_maze(self):
        if not self.file_path:
            raise Exception("Maze must be given a file path")
        
        self.get_maze_context_from_file()
        
        
    
    def generate_possible_actions_from(self, state) -> Union[str, tuple]:
        possible_actions = []
        current_row, current_col = state

        action_candidates = [
            ("up", (current_row - 1, current_col)),
            ("down", (current_row + 1, current_col)),
            ("left", (current_row, current_col - 1)),
            ("right", (current_row, current_col + 1))
        ]

        for action, (row, col) in action_candidates:
            try:
                if not self.maze_walls[row][col]:
                    possible_actions.append((action, (row, col)))
            except IndexError:
                continue
        
        return possible_actions
    
    def solve_maze(self, search_type: str = None):
        try: 
            start = Node(state=self.start)
            search_frontier = SEARCH_METHOD_FRONTIERS.get(search_type, "bfs")
            search_frontier.add(start)
            solving_maze = True

            while solving_maze:
                if search_frontier.is_empty():
                    raise Exception("Solution not found")
                
                current_node = search_frontier.remove_node()
                self.states_explored += 1

                if current_node.state == self.goal:
                    actions_taken = []
                    cells = []

                    while current_node.parent:
                        actions_taken.append(current_node.action)
                        cells.append(current_node.state)
                        current_node = current_node.parent
                    
                    # Re-order for visualization
                    actions_taken.reverse()
                    cells.reverse()
                    self.solution = (actions_taken, cells)
                    return
                
                # Current node was not the goal, continue search
                self.explored_nodes.add(current_node.state)
                
                actions = self.generate_possible_actions_from(current_node.state)
                print(f"Possible actions forund for node state {str(current_node.state)}: {actions}")
                for action, state in actions:
                    if not search_frontier.contains_state(state) and state not in self.explored_nodes:
                        child_node = Node(state=state, parent=current_node, action=action)
                        search_frontier.add(child_node)
        except Exception as e:
            print(f"{e.__traceback__.tb_lineno}")
            raise e

    def print_maze(self):
        solution = self.solution[1] if self.solution else None
        if solution:
            print(f"Solution steps: {self.solution[0]}")
            print(f"Solution cells: {self.solution[1]}")
        print("--------")
        for i, row in enumerate(self.maze_walls):
            row_string = ""
            for j, col in enumerate(row):
                # Print walls 
                if col:
                    row_string += "#"
                # Print start/goal
                elif (i, j) == (self.start or self.goal):
                    row_string += 'A' * ((i, j) == self.start)

                # Print solution pathing
                elif (solution and (i, j) in solution):
                    row_string += "*"
                # Print available paths
                else:
                    row_string += " "
            print(row_string)
        print("--------")
