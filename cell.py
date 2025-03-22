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

    # draw lines in centre of 1 cell to another
    # if undo False, must be red, otherwise it's gray
    # uses x/y of 2 cells to determine drawing of 2 cells
    def draw_move(self, to_cell, undo=False):
        # Self cell, called cell 1
        half_length_cell_1 = abs(self.__x2 - self.__x1) // 2  # assuming square, & abs to keep positive
        centre_x_cell_1 = self.__x1 + half_length_cell_1  # centre x coord of cell 1 (self)
        centre_y_cell_1 = self.__y1 + half_length_cell_1  # centre y coord of cell 1 (self)
        # to_cell , called cell 2
        half_length_cell_2 = abs(to_cell.__x2 - to_cell.__x1) // 2  # assuming square, & abs to keep positive
        centre_x_cell_2 = to_cell.__x1 + half_length_cell_2  # centre x coord of cell 2 (to cell)
        centre_y_cell_2 = to_cell.__y1 + half_length_cell_2  # centre y coord of cell 2 (to cell)

        # determine draw_move colour (undo = red, not_undo = grey)
        fill_colour = "red"  # default colour if False
        if undo:  # if undo is True
            fill_colour = "gray"  # override as gray

        # now set the line geometry
        centre_cell_1 = Point(centre_x_cell_1, centre_y_cell_1)  # cell 1 centre point (self)
        centre_cell_2 = Point(centre_x_cell_2, centre_y_cell_2)  # cell 2 centre point (to_cell)
        line = Line(centre_cell_1, centre_cell_2)  # draw line between points

        # then draw it
        self.__win.draw_line(line, fill_colour)  # draw line with colour)