# MAIN.PY
from graphics import Window, Point, Line  # import the graphics classes


# our main loop function
def main():
    # Create window first
    win = Window(800, 600)  # create a window

    # Draw a few lines to test
    # Points this
    p1 = Point(100, 100)
    p2 = Point(300, 300)
    p3 = Point(700, 400)
    p4 = Point(100, 600)

    # Then lines
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p1)
    line4 = Line(p2, p4)
    line5 = Line(p3, p4)
    line6 = Line(p1, p4)

    # Now draw the lines
    win.draw_line(line1, "green")  # set green
    win.draw_line(line2, "red")  # set red
    win.draw_line(line3)  # leave as default black
    win.draw_line(line4, "orange")  # set orange
    win.draw_line(line5, "purple")  # set purple
    win.draw_line(line6, "blue")  # set blue
    
    # Wait to close
    win.wait_for_close()  # close it on call of this method


# Need this to run!
if __name__ == "__main__":
    main()
