class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.visited = False

    def draw(self, fill_color="black"):
        if self.has_left_wall:
            left = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left, fill_color)
        else:
            left = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left, "#d9d9d9")

        if self.has_right_wall:
            right = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right, fill_color)
        else:
            right = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right, "#d9d9d9")

        if self.has_top_wall:
            top = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top, fill_color)
        else:
            top = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top, "#d9d9d9")

        if self.has_bottom_wall:
            bottom = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom, fill_color)
        else:
            bottom = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        x_center = self._x1 + abs(self._x2 - self._x1)/2
        y_center = self._y1 + abs(self._y1 - self._y2)/2
        x2_center = to_cell._x1 + abs(to_cell._x2 - to_cell._x1)//2
        y2_center = to_cell._y1 + abs(to_cell._y1 - to_cell._y2)//2

        line = Line(Point(x_center, y_center), Point(x2_center, y2_center))
        self._win.draw_line(line, line_color)

    def draw_solve(self):
        line_color = "green"        
        x_center = self._x1 + abs(self._x2 - self._x1)/2
        y_center = self._y1 + abs(self._y1 - self._y2)/2
        y2_center = y_center + abs(self._y1 - self._y2)
        line = Line(Point(x_center, y_center), Point(x_center, y2_center))
        self._win.draw_line(line, line_color)