import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget 
from PyQt5.QtCore import Qt, QTimer 
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

def astar(maze, start, end, open_list=None, closed_list=None): 
    if open_list is None: 
        open_list = [] 
    if closed_list is None: 
        closed_list = []

    if len(open_list) == 0:  # start a new search
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0
        open_list.append(start_node)
    else:
        start_node = open_list[0]  # continue from last moved state
        end_node = Node(None, end)

    if len(open_list) > 0:
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
            return path[::-1], current_node.g, current_node, open_list, closed_list  # Return path, cost, end_node, and lists

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue
            
            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            cost = 14 if abs(child.position[0] - current_node.position[0]) + abs(child.position[1] - current_node.position[1]) == 2 else 10
            child.g = current_node.g + cost
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g >= open_node.g:
                    break
            else:
                open_list.append(child)

    return [], float('inf'), None, open_list, closed_list 

class MainWindow(QMainWindow): 
    def __init__(self, *args, **kwargs): 
        super(MainWindow, self).__init__(*args, **kwargs) 
        self.table = QTableWidget(10, 10, self) 
        self.find_path_button = QPushButton('Step') 
        self.reset_button = QPushButton('Reset') 
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.table) 
        self.layout.addWidget(self.find_path_button) 
        self.layout.addWidget(self.reset_button) 
        self.setCentralWidget(QWidget(self)) 
        self.centralWidget().setLayout(self.layout) 
        self.start = None 
        self.end = None 
        self.maze = np.zeros((10, 10)) 
        self.open_list = [] 
        self.closed_list = [] 
        self.path_found = False 
        self.timer = QTimer(self) 
        # self.timer.setInterval(500) # set time interval to make it faster or slower
        self.timer.timeout.connect(self.step_astar)

        for i in range(10):
            for j in range(10):
                item = QTableWidgetItem()
                item.setBackground(QColor('white'))
                self.table.setItem(i, j, item)

        self.table.cellClicked.connect(self.on_click)
        self.find_path_button.clicked.connect(self.start_astar)  # connect to star a_star
        self.reset_button.clicked.connect(self.reset_grid)

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
            if (row, column) != self.start and (row, column) != self.end:
                self.maze[row][column] = 1 if self.maze[row][column] == 0 else 0  #  obstacle
                self.table.setItem(row, column, QTableWidgetItem())
                self.table.item(row, column).setBackground(QColor('black') if self.maze[row][column] == 1 else 'white')

    def start_astar(self):
        if self.start is not None and self.end is not None:
            self.find_path_button.setEnabled(False)  # disable  button during search
            self.step_astar()  # start the search process

    def step_astar(self):
        if not self.path_found:
            self.path, cost, end_node, self.open_list, self.closed_list = astar(
                self.maze, self.start, self.end, self.open_list, self.closed_list
            )
            if self.path:
                self.path_found = True
                self.end_node = end_node  # store end_node as an attribute
            self.update_grid()

    def update_grid(self):
        for i in range(10):
            for j in range(10):
                item = self.table.item(i, j)
                if item is None:
                    item = QTableWidgetItem()
                    self.table.setItem(i, j, item)

                if (i, j) == self.start:
                    item.setBackground(QColor('green'))
                elif (i, j) == self.end:
                    item.setBackground(QColor('red'))
                elif self.maze[i][j] == 1:
                    item.setBackground(QColor('black'))
                else:
                    item.setBackground(QColor('white'))

        for node in self.open_list:
            item = self.table.item(node.position[0], node.position[1])
            item.setBackground(QColor('lightblue'))
            item.setText(f"g:{node.g}\nh:{node.h}\nf:{node.f}")

        for node in self.closed_list:
            item = self.table.item(node.position[0], node.position[1])
            item.setBackground(QColor('lightgray'))
            item.setText(f"g:{node.g}\nh:{node.h}\nf:{node.f}")

        if self.path_found:
            # access end_node from the class attribute
            current = self.end_node  
            for step in self.path:
                item = self.table.item(step[0], step[1])
                item.setBackground(QColor('purple'))
                item.setText(str(current.g))  # display 'g' cost on the path
                current = current.parent
            self.timer.stop()
            self.find_path_button.setEnabled(True)  # renable the button
        else:
            self.timer.start()

    def reset_grid(self):
        self.start = None
        self.end = None
        self.maze = np.zeros((10, 10))
        self.open_list = []
        self.closed_list = []
        self.path_found = False
        self.find_path_button.setEnabled(True)
        self.timer.stop()

        for i in range(10):
            for j in range(10):
                item = self.table.item(i, j)
                if item is None:
                    item = QTableWidgetItem()
                    self.table.setItem(i, j, item)
                item.setBackground(QColor('white'))
                item.setText('')  # clear text to make it more better

app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec_()
