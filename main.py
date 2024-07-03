from window import Window
from maze import Maze

window = Window(800, 600)
rows = 12
columns = 16
cell_width = 48
cell_height = 48
maze = Maze(10, 10, rows, columns, cell_width, cell_height, window)
maze.solve()
window.wait_for_close()