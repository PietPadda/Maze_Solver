# MAIN.PY
from graphics import Window  # import the graphics classes
from maze import Maze  # import the maze class
import sys  # for increasing recursion depth limit (slightly!)


# our main loop function
def main():
    # Create window first
    win = Window(800, 600)  # create a window
    sys.setrecursionlimit(10000)  # increase from default 1000 by x10

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
    
    # Call our solver!
    print("Maze solver has started!")
    is_solvable = maze._solve()
    if is_solvable:  # if it returns True
        print("The maze has been solved!")
    else:
        print("The maze couldn't be solved!")

    # Wait to close
    win.wait_for_close()  # close it on call of this method


# Need this to run!
if __name__ == "__main__":
    main()
