# CMPUT 366 - Search & Planning in AI: Pathfinding Algorithms

## Assignment Overview
This repository contains an implementation of two fundamental pathfinding algorithms: Dijkstra's Algorithm and A* Search, developed for the University of Alberta's CMPUT 366 course (Winter 2025).

## Where to finf the algorithm implmentation 
"AstarDijkstra\starter\search\algorithms.py"

## Implemented Algorithms

### 1. Dijkstra's Algorithm
- Finds the shortest path in a grid-based environment
- Supports movement in four cardinal directions (cost: 1.0) and four diagonal directions (cost: 1.5)
- Returns:
  - Optimal solution path
  - Solution cost
  - Number of nodes expanded

### 2. A* Search Algorithm
- Implements pathfinding using the Octile distance heuristic
- Heuristic formula: 
  ```
  h(s) = 1.5 * min(Δx, Δy) + |Δx - Δy|
  ```
- Returns similar outputs to Dijkstra's algorithm
- Uses an admissible and consistent heuristic

## Experimental Analysis
The implementation includes experiments that generate two key visualizations:
1. `nodes_expanded.png`: Compares node expansions between Dijkstra and A*
2. `running_time.png`: Compares computational time between Dijkstra and A*

## Additional Experiments
The assignment explores:
- Impact of heuristic scaling (multiplying heuristic by 2)
- Effect of not updating node costs during search

## Implementation Logic
### Dijkstra's Algorithm
High-Level Strategy
Initialization:
Create an empty list to track nodes to explore (Open List)
Create an empty dictionary to track explored nodes (Closed List)
Start at the initial state with a cost of 0
Mark the initial state's parent as None (for path reconstruction)

Exploration Process:
Always explore the node with the lowest cumulative cost first
For each explored node, generate its neighboring states (successors)
For each successor:
If the successor hasn't been explored before, add it to the Open List
If a shorter path to an already explored node is found, update its cost and parent

Termination:
Stop when the goal state is reached
Return the path, total cost, and number of nodes explored
If no path is found, return None and -1 for cost

Key Characteristics
Explores nodes based purely on accumulated cost
Guarantees finding the shortest path
Does not use any additional heuristic information

### A* Search
High-Level Strategy
Initialization:
Similar to Dijkstra's, but with an added heuristic estimation
Use Octile distance as the heuristic (combines diagonal and cardinal moves)
Calculate initial state's cost as: actual cost + heuristic to goal

Exploration Process:
Explore nodes based on combined actual cost and estimated distance to goal
Heuristic helps guide search more directly towards the goal

For each successor:
Calculate its total cost: actual path cost + heuristic estimate
If a cheaper path is found, update the node's cost and parent

Termination:
Same as Dijkstra's, but with cost calculation including heuristic
Returns path, total cost, and nodes explored

Key Characteristics
Uses Octile distance heuristic to estimate remaining distance
More efficient than Dijkstra's for many pathfinding scenarios
Guaranteed to find the shortest path if heuristic is admissible

Main Differences
Dijkstra's uses only actual path cost
A* incorporates a heuristic to estimate remaining distance
A* typically explores fewer nodes due to more intelligent exploration

## Requirements
- Python 3
- Libraries specified in `requirements.txt`

## How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```
   python3 main.py
   ```

## Course Information
- **Course**: CMPUT 366 - Search & Planning in AI
- **Semester**: Winter 2025
- **Assignment**: Pathfinding Algorithms
- **Due Date**: February 4

