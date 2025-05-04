# SEARCH CONCEPTS

Agent:
    Entity that percieves its environment and acts upon that environment

State:
    A configuration of the agent and its environment

Initial State:
    State the agent begins at

Actions:
    Choices that can be made in a state
    - ACTIONS(s) returns the set of actions that can be executed in state (s)

Transition Model:
    A description of what state results from performing any applicable action in any state
    - RESULT(s, a) returns the state resulting from performing action (a) in state (s)

State Space:
    The set of all states reachable from the inital state by any sequence of actions

Goal Test:
    Way to determine whether a given state is a goal state

Path Cost:
    Numerical cost associated with a given path

Search Problems:
    Inital state
    Actions
    Transition Model
    Goal Test
    Path Cost Function

Optimal Soultion:
    A solution that has the lowest path cost among all solutions

Node:
    A data structure that keeps track of
    - A state
    - A parent (node that generated this node)
    - An action (action applied to parent to get node)
    - A path cost (from initial state to node)

APPROACH

- Start with a frontier tha contains the inital state
- Repeat:
  - If the frontier is empty, then no solution
  - Remove a node from the frontier
  - If node contains goal state, return the solution
  - Expand node, and resulting nodes to the frontier
    - "Expand" == Look at all of the neighbors of that node; what possible actions can I take based on the state of the current node, and what other nodes can I get to from there?
    - Add all nodes found and add them to the frontier

## DEPTH-FIRST SEARCH

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

## BREADTH-FIRST SEARCH

Breadth-first Search
    - Search algo that alwasys expands the shallowest node in the frontier

Queue
    - First-in first-out data type
