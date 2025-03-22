# MAIN.PY
from graphics import Window, Point, Line  # import the graphics classes
from cell import Cell  # import the cell class



# our main loop function
def main():
    # Create window first
    win = Window(800, 600)  # create a window

    # Draw a few cells to test
    # x1, y1, x2, y2
    cell1 = Cell(win)
    cell1.has_top_wall = False
    cell1.has_bottom_wall = False
    cell1.draw(50,50,100,100)

    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.has_bottom_wall = False
    cell2.draw(100,50,150,150)

    cell3 = Cell(win)
    cell3.has_right_wall = False
    cell3.has_bottom_wall = False
    cell3.draw(50,100,100,150)

    cell4 = Cell(win)
    cell4.has_left_wall = False
    cell4.draw(100,100,150,150)
    
    # Wait to close
    win.wait_for_close()  # close it on call of this method


# Need this to run!
if __name__ == "__main__":
    main()
