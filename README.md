# A\* Pathfinding Visualization

This is a Python application that visualizes the A\* pathfinding algorithm using PyQt5.

## Requirements

- Python 3
- PyQt5
- numpy

## Installation

1. Clone this repository:
   git clone https://github.com/yourusername/yourrepository.git

2. Navigate to the directory:
   cd yourrepository

3. Create a virtual environment:
   python3 -m venv env

4. Activate the virtual environment:
   source env/bin/activate

5. Install the required packages:
   pip install -r requirements.txt

## Usage

Run the application with:
python new.py

A window will open with a 10x10 grid. Click on cells to set the start point (green), end point (red), and obstacles (black). Press the "Find Path" button to find and display the shortest path from the start to the end point. The path will be highlighted in blue.

## License

This project is licensed under the terms of the MIT license.

## Activate the environment

source myenv/bin/activate
deactivate

source env/bin/activate
deactivate

[Medium Article Link](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjY3NGRiYmE4ZmFlZTY5YWNhZTFiYzFiZTE5MDQ1MzY3OGY0NzI4MDMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDk1NjQ2Njg4NTA4ODcxNjM3NDgiLCJlbWFpbCI6IjFyYWh1bGNoYW5kcmExQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3MTc5MzI3MDUsIm5hbWUiOiJSYWh1bCBDaGFuZHJhIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0paU2UzQzNQU0dUY0t4UFZIZkpvRWxwOWJ4NEFIVzlNcDRnM0pZejk3UTRyWTg0QW9KMlE9czk2LWMiLCJnaXZlbl9uYW1lIjoiUmFodWwgQ2hhbmRyYSIsImlhdCI6MTcxNzkzMzAwNSwiZXhwIjoxNzE3OTM2NjA1LCJqdGkiOiJhM2RlYzQ2Y2VjOThmYjhiMmI1ODA5M2Q3NmRhMzZmMGJjZjhlMTk0In0.TvbYG1q6uloNphQeiMbovenHdAIw6MqNjcnMNABmu7sMj10BKuskmI1f5uEoMQAmw29k8zCrQpckJbB44sJB0VliXpiwX_4ZWxf00MY1CmIPKkDloMg0hjIfsfksA1UDo_9rYApPEgonYq8r7OxeNTROJlt7DYEYRuOkdE9yu2vmRez8OIAzqwSW5uuHGp_qJULaCsvP4IF9cwEyazZe5KXW-zVz91xMS_vBFuasGWmhvSHA-fTIled8av9z-Q9K4WGoFaSgl3Cv1jMxJtv2frXhOZurLeVjBs4Yh3wntP1YYatrI-ZsMt-F9wDiDpzKFbzRNaoW6089ILj6C4GixQ)


# Information:

This code is a PyQt5-based GUI application that visualizes the A* search algorithm on a grid. The A* algorithm is used to find the shortest path between two points in a graph, and it's commonly used in pathfinding and graph traversal.

Here's an overview of the key components of the code:

1. `Node` class: This class represents a node in the grid. Each node has a parent (the node from which it was reached), a position (its coordinates in the grid), and g, h, and f values which are used by the A* algorithm. The g value is the cost from the start node to the current node, the h value is the heuristic estimate of the cost from the current node to the end node, and the f value is the sum of g and h.

2. `astar` function: This function implements the A* algorithm. It takes a maze (grid), start position, end position, and optionally open and closed lists. The open list contains nodes that need to be evaluated, and the closed list contains nodes that have already been evaluated. The function returns the shortest path from the start to the end, the cost of the path, the end node, and the final open and closed lists.

3. `MainWindow` class: This class creates the main window of the application. It includes a table to represent the grid, buttons to start the search and reset the grid, and a timer to animate the search process. It also includes methods to handle user interactions (clicking on cells and buttons) and update the grid.

4. `on_click` method: This method is called when a cell in the table is clicked. It sets the start and end positions and toggles obstacles in the grid.

5. `start_astar` and `step_astar` methods: These methods start and step through the A* search process, respectively. They call the `astar` function and update the grid after each step.

6. `update_grid` method: This method updates the colors and texts of the cells in the table based on the current state of the search process.

7. `reset_grid` method: This method resets the grid and all variables to their initial state.

8. The last four lines create a QApplication, create and show the main window, and start the application's event loop.

This code provides a nice visualization of the A* algorithm and can be a great learning tool. You can see how the algorithm explores different paths, updates the g, h, and f values of the nodes, and eventually finds the shortest path.


---


Sure, here's a detailed explanation of the code:

1. **Import necessary modules**: The script starts by importing necessary modules. PyQt5 is used for creating the GUI, numpy is used for handling the grid (maze), and heapq is used for maintaining the open list as a priority queue.

2. **Node class**: This class represents a node in the grid. Each node has a parent (the node from which it was reached), a position (its coordinates in the grid), and g, h, and f values which are used by the A* algorithm. The g value is the cost from the start node to the current node, the h value is the heuristic estimate of the cost from the current node to the end node, and the f value is the sum of g and h.

3. **generate_children function**: This function generates the children of a given node. It checks all eight possible movements (up, down, left, right, and the four diagonals), and for each movement, it creates a new node if the movement leads to a valid position that is not an obstacle.

4. **astar function**: This function implements the A* search algorithm. It takes a maze (grid), start position, end position, and optionally open and closed lists. The open list contains nodes that need to be evaluated, and the closed list contains nodes that have already been evaluated. The function returns the shortest path from the start to the end, the cost of the path, the end node, and the final open and closed lists.

5. **MainWindow class**: This class creates the main window of the application. It includes a table to represent the grid, buttons to start the search and reset the grid, and a timer to animate the search process. It also includes methods to handle user interactions (clicking on cells and buttons) and update the grid.

6. **on_click method**: This method is called when a cell in the table is clicked. It sets the start and end positions and toggles obstacles in the grid.

7. **start_astar method**: This method is called when the "Start" button is clicked. It disables the "Start" button and enables the "Next" button.

8. **step_astar method**: This method is called when the "Next" button is clicked. It performs one step of the A* algorithm and updates the grid.

9. **update_grid method**: This method updates the colors and texts of the cells in the table based on the current state of the search.

10. **reset_grid method**: This method resets the grid and all variables to their initial state.

11. **Main script**: The last four lines create a QApplication, create and show the MainWindow, and start the application's event loop.

The key part of this code is the `astar` function, which implements the A* search algorithm. The algorithm works by maintaining a list of "open" nodes (nodes that have been discovered but not yet evaluated) and a list of "closed" nodes (nodes that have been evaluated). At each step, it chooses the node with the lowest f value from the open list, evaluates it (checks if it's the end node and generates its children), and moves it to the closed list. This process continues until the end node is found or all nodes have been evaluated.

The GUI part of the code provides a visual representation of the grid and the search process. It allows you to set the start and end positions, place obstacles, and watch as the algorithm finds the shortest path from the start to the end. The "Next" button allows you to step through the algorithm one step at a time.