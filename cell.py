# CELL.PY
from graphics import Line, Point  # import graphics

# Takes line & points -- cell size
# has access to window win so it can draw itself
class Cell: 
    def __init__(self, win):
        self.__win = win  # window input for drawing
        # booleans for if cell has certain walls
        # default ALL walls true, unless specified as False
        self.has_left_wall = True  
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # point coordinates for drawing each wall
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None

    # draw cells using topleft & bottom coordinates of cell
    def draw(self, x1, y1, x2, y2):
        # Set coordinates per input
        self.__x1 = x1  # left
        self.__x2 = x2  # right
        self.__y1 = y1  # top
        self.__y2 = y2  # bottom
        # Left wall check
        if self.has_left_wall:
            # points
            p1 = Point(self.__x1, self.__y1)  # top left
            p2 = Point(self.__x1, self.__y2)  # bottom left
            line = Line(p1, p2)  # line between points
            self.__win.draw_line(line, "green")  # draw wall, set green
        # Right wall check
        if self.has_right_wall:
            # points
            p1 = Point(self.__x2, self.__y1)  # top right
            p2 = Point(self.__x2, self.__y2)  # bottom right
            line = Line(p1, p2)  # line between points
            self.__win.draw_line(line, "red")  # draw wall, set red
        # Top wall check
        if self.has_top_wall:
            # points
            p1 = Point(self.__x1, self.__y1)  # top left
            p2 = Point(self.__x2, self.__y1)  # top tight
            line = Line(p1, p2)  # line between points
            self.__win.draw_line(line, "blue")  # draw wall, set blue
        # Bottom wall check
        if self.has_bottom_wall:
            # points
            p1 = Point(self.__x1, self.__y2)  # bottom left
            p2 = Point(self.__x2, self.__y2)  # bottom tight
            line = Line(p1, p2)  # line between points
            self.__win.draw_line(line, "purple")  # draw wall, set purple