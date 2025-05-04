class Node():
    def __init__(self, state: tuple, parent: tuple = None, action=None, cost=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state) -> bool:
        return any(node.state == state for node in self.frontier)
    
    def is_empty(self) -> bool:
        return bool(not self.frontier)
    
    def remove_node(self):
        raise NotImplementedError
    

class DFSFrontier(StackFrontier):
    def remove_node(self):
        if self.is_empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        

class BFSFrontier(StackFrontier):
    def remove_node(self):
        if self.is_empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        