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



    