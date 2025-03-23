# MAIN.PY
from graphics import Window, Point, Line  # import the graphics classes
from maze import Maze  # import the maze class




# our main loop function
def main():
    # Create window first
    win = Window(800, 600)  # create a window

    # Maze parameters
    x1 = 50
    y1 = 50
    num_rows = 10
    num_cols = 15
    cell_size_x = 40
    cell_size_y = 40

    # Create Maze
    maze = Maze(x1,
                y1,
                num_rows,
                num_cols,
                cell_size_x,
                cell_size_y,
                win,
                10)  # Fixed Seed

    # Wait to close
    win.wait_for_close()  # close it on call of this method


# Need this to run!
if __name__ == "__main__":
    main()
