Depth-first Search
    - Search algo that always expands the deepest node in the frontier
    
Stack:
    - Last-in first-out data type

REVISED APPROACH
 - Start with a frontier that contains the initial state
 - Start with an empty explored set
 - Repeat:
    - If the frontier is empty, then no solution
    - Remove a node from the frontier
    - If node contains goal state, return the solution
    - Add the node to the explored set
    - Expand node, and resulting nodes to the frontier if they aren't already in the frontier or the explored set
    
