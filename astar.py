import tkinter as tk
from queue import PriorityQueue


# Create a Tkinter window
root = tk.Tk()
root.title("A* Path Finding Algorithm")

# Set window size
WIDTH = 800
HEIGHT = 800
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Node class to represent each cell in the grid
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = "white"
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == "red"

    def is_open(self):
        return self.color == "green"

    def is_barrier(self):
        return self.color == "black"

    def is_start(self):
        return self.color == "orange"

    def is_end(self):
        return self.color == "turquoise"

    def reset(self):
        self.color = "white"

    def make_start(self):
        self.color = "orange"

    def make_closed(self):
        self.color = "red"

    def make_open(self):
        self.color = "green"

    def make_barrier(self):
        self.color = "black"

    def make_end(self):
        self.color = "turquoise"

    def make_path(self):
        self.color = "purple"

    def draw(self, win):
        win.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.width, fill=self.color)

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.row > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

# Heuristic function for A* algorithm
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Function to reconstruct path after finding end node
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

# A* algorithm implementation
def a_star_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        # This part needs to be replaced with Tkinter event handling
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

# Function to create a 2D list representing the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

# Function to draw grid lines on the window
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        win.create_line(0, i * gap, width, i * gap)
        for j in range(rows):
            win.create_line(j * gap, 0, j * gap, width)

# Function to draw everything on the window
def draw(win, grid, rows, width):
    win.delete("all")  # Clear the canvas

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    win.update()  # Update the canvas

# Function to get clicked position on grid
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

# Main function
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    # Create Clear Grid button
    clear_button = tk.Button(win, text="Clear Grid", command=lambda: clear_grid(grid, win, ROWS, width))
    clear_button.pack()

    # Initialize cost
    cost = 0
    # Create Cost label
    cost_var = tk.StringVar()
    cost_var.set("Cost: " + str(cost))
    cost_label = tk.Label(win, textvariable=cost_var)
    cost_label.pack()

    run = True
    while run:
        draw(win, grid, ROWS, width)
        # This part needs to be replaced with Tkinter event handling
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False

        #     if pygame.mouse.get_pressed()[0]: # LEFT
        #         pos = pygame.mouse.get_pos()
        #         row, col = get_clicked_pos(pos, ROWS, width)
        #         node = grid[row][col]
        #         if not start and node != end:
        #             start = node
        #             start.make_start()

        #         elif not end and node != start:
        #             end = node
        #             end.make_end()

        #         elif node != end and node != start:
        #             node.make_barrier()

        #     elif pygame.mouse.get_pressed()[2]: # RIGHT
        #         pos = pygame.mouse.get_pos()
        #         row, col = get_clicked_pos(pos, ROWS, width)
        #         node = grid[row][col]
        #         node.reset()
        #         if node == start:
        #             start = None
        #         elif node == end:
        #             end = None

        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE and start and end:
        #             for row in grid:
        #                 for node in row:
        #                     node.update_neighbors(grid)

        #             path_found = a_star_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    
        #             # Update cost
        #             if path_found:
        #                 cost += calculate_path_cost(came_from, start, end)  # You need to implement calculate_path_cost
        #                 cost_var.set("Cost: " + str(cost))

        #         if event.key == pygame.K_c:
        #             start = None
        #             end = None
        #             grid = make_grid(ROWS, width)
        #             cost = 0
        #             cost_var.set("Cost: " + str(cost))

    # pygame.quit()  # This needs to be replaced with Tkinter quit

main(canvas, WIDTH)

def clear_grid(grid, win, rows, width):
    grid = make_grid(rows, width)
    draw(win, grid, rows, width)

def on_click(event):
    pos = event.x, event.y
    row, col = get_clicked_pos(pos, ROWS, width)
    node = grid[row][col]
    # rest of your code...

canvas.bind("<Button-1>", on_click)  # Bind left mouse button click

def on_key_press(event):
    if event.char == ' ':  # Space key
        for row in grid:
            for node in row:
                node.update_neighbors(grid)

        path_found = a_star_algorithm(lambda: draw(canvas, grid, ROWS, WIDTH), grid, start, end)
        
        # Update cost
        if path_found:
            cost += calculate_path_cost(came_from, start, end)  # You need to implement calculate_path_cost
            cost_var.set("Cost: " + str(cost))

    elif event.char == 'c':  # 'c' key
        start = None
        end = None
        grid = make_grid(ROWS, WIDTH)
        cost = 0
        cost_var.set("Cost: " + str(cost))

root.bind("<Key>", on_key_press)  # Bind key press

def calculate_path_cost(came_from, start, end):
    current = end
    cost = 0
    while current in came_from:
        cost += 1  # Assuming each step costs 1
        current = came_from[current]
    return cost