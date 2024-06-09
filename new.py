import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import numpy as np

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)

    return []  # Return an empty list if no path was found

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.table = QTableWidget(10, 10, self)
        self.find_path_button = QPushButton('Find Path')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.find_path_button)
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.layout)

        self.start = None
        self.end = None
        self.maze = np.zeros((10, 10))

        # Set all cells to white
        for i in range(10):
            for j in range(10):
                item = QTableWidgetItem()
                item.setBackground(QColor('white'))
                self.table.setItem(i, j, item)

        self.table.cellClicked.connect(self.on_click)
        self.find_path_button.clicked.connect(self.find_path)

    def on_click(self, row, column):
        if self.start is None:
            self.start = (row, column)
            self.table.setItem(row, column, QTableWidgetItem())
            self.table.item(row, column).setBackground(QColor('green'))
        elif self.end is None:
            self.end = (row, column)
            self.table.setItem(row, column, QTableWidgetItem())
            self.table.item(row, column).setBackground(QColor('red'))
        else:
            self.maze[row][column] = 1
            self.table.setItem(row, column, QTableWidgetItem())
            self.table.item(row, column).setBackground(QColor('black'))

    def find_path(self):
        print("Finding path...")
        path = astar(self.maze, self.start, self.end)
        print(f"Path found: {path}")
        if path:
            for step in path:
                print(f"Coloring cell {step}...")
                item = self.table.item(step[0], step[1])
                if item is None:  # If no item exists for this cell yet
                    item = QTableWidgetItem()  # Create a new item
                    self.table.setItem(step[0], step[1], item)  # Set the new item for this cell
                item.setBackground(QColor('purple'))  # Color the item
    print("Done.")
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
