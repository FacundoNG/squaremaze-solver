from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__isRunning = False
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width,height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        #self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()

    def close(self):
        self.__isRunning = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)