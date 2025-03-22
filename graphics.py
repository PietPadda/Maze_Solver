# GRAPHICS.PY
from tkinter import Tk, BOTH, Canvas  # import tkinter

# Takes width & height -- window size
# make all private to keep internal
class Window: 
    def __init__(self, width, height): 
        self.__root = Tk()   # create a root widget data member
        self.__root.title("Maze Solver")  # root widget title property
        # canvas ~ sheet of paper:
        # parent window, background colour, canvas size
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)  # create a Canvas widget
        # pack ~ how canvas will appear in window: 
        # fill=BOTH = expand both x&y if window resized, expand=1 = take up all extra space if window grows
        self.__canvas.pack(fill=BOTH, expand=1)  # pack canvas to make it ready to be drawn
        self.__running = False  # initialise window running flag
        # protocl ~ do something when clicked
        # "WM_DELETE_WINDOW" = X button, self.close = action performed on button press
        self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Link close() action to "X" button


    # Redraw all visuals in the window by updating the root widget
    def redraw(self):
        # idletasks() - process all tasks in the Tkinter event queue
        self.__root.update_idletasks()  # Handle pending tasks for rendering
        # update() - forces immediate process of events, else graphics wont appear
        self.__root.update()  # Refresh the display

    # Sets running flag true and keeps redrawing until False
    def wait_for_close(self):
        self.__running = True  # set window running flag true
        while self.__running:  # while it remains draw
            self.redraw()  # keep drawing
        print("Window closed...")  # once False, print to console

    # closes the window by setting flag False
    def close(self):
        self.__running = False  # set window running flag false


    # Draw a line in the window
    # takes a Line instance and fill colour (str)
    # set default colour as black
    def draw_line(self, line, fill_colour="black"):
        # Pass our canvas and the fill color to the line's draw method
        line.draw(self.__canvas, fill_colour)  # call draw on the line instance


# Generate points w x & y coords
# x=0 left of screen, y=0 top of screen
class Point: 
    def __init__(self, x, y): 
        self.x = x  # point x coord
        self.y = y  # point y coord


# Generate line of 2 input points
class Line: 
    def __init__(self, point1, point2): 
        self.point1 = point1  # point1 of line
        self.point2 = point2  # point2 of line

    
    # method to draw colour using canvas and colour (str)
    def draw(self, canvas, fill_colour):
        # Get coordinates of each point
        p1_x = self.point1.x  # point1 x coord
        p1_y = self.point1.y  # point1 y coord
        p2_x = self.point2.x  # point2 x coord
        p2_y = self.point2.y  # point2 y coord
        # Use Canvas's create_line() method:
        # x&y coords of each point, fill colour, line width
        canvas.create_line(p1_x, p1_y, p2_x, p2_y, fill=fill_colour, width=2)