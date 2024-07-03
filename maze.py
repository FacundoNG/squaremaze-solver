from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            self.seed = random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for ix in range(self.num_cols):
            self._cells.append([])
            xPos = self.x1 + self.cell_size_x*ix
            for iy in range(self.num_rows):
                yPos = self.y1 + self.cell_size_y*iy
                cell = Cell(self.win, xPos, yPos, xPos + self.cell_size_x, yPos + self.cell_size_y)
                self._cells[ix].insert(iy, cell)
                self._draw_cells(ix,iy)

    def _draw_cells(self, i ,j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        time.sleep(0.02)
        self.win.redraw()

    def _break_entrance_and_exit(self):
        last_col = self.num_cols - 1
        last_row = self.num_rows - 1
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0,0)
        self._cells[last_col][last_row].has_bottom_wall = False
        self._draw_cells(last_col, last_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))

            if len(to_visit) == 0:
                self._draw_cells(i, j)
                return


            dir = random.randrange(len(to_visit))
            next_cell = to_visit[dir]
            # remove walls from cell and it's adjacent
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        # end cell
        if i == (self.num_cols - 1) and j == (self.num_rows - 1):
            self._cells[i][j].draw_solve()
            return True
        else:
            # move right
            if i + 1 < self.num_cols and not self._cells[i+1][j].visited and not self._cells[i+1][j].has_left_wall:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1,j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+1][j], True)

            # move down
            if j + 1 < self.num_rows and not self._cells[i][j+1].visited and not self._cells[i][j+1].has_top_wall:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i,j+1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j+1], True)

            # move left
            if i - 1 >= 0 and not self._cells[i-1][j].visited and not self._cells[i-1][j].has_right_wall:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i-1,j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i-1][j], True)

            # move up
            if j - 1 >= 0 and not self._cells[i][j-1].visited and not self._cells[i][j-1].has_bottom_wall:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i,j-1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1], True)

            # no valid moves
            return False